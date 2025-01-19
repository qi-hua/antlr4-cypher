import hashlib
import json
import asyncio
from concurrent.futures import ProcessPoolExecutor

from aiocache import cached, Cache
from aiocache.serializers import PickleSerializer

from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream

from antlr4_cypher import CypherParser, CypherLexer
from CustomCypherParserVisitor import CustomCypherParserVisitor, get_cypher_query_from_tree

executor = ProcessPoolExecutor(max_workers=10)


def key_from_args(func, *args, **kwargs):
    ordered_kwargs = sorted(kwargs.items())
    args_str = hashlib.md5(f'{args[1:]}{ordered_kwargs}'.encode("utf-8")).hexdigest()[:16]
    return f"{func.__module__ or ''}:{func.__name__}:{args_str}"


class CypherMapper:
    def __init__(self, mapping_file: str):
        self.mapping = self._load_mapping(mapping_file)
        self.visitor = CustomCypherParserVisitor(self.mapping)

    def _load_mapping(self, mapping_file: str) -> dict:
        """
        加载关系映射表。
        """
        with open(mapping_file, 'r') as f:
            return json.load(f)

    @cached(
        ttl=10,
        cache=Cache.REDIS, key_builder=key_from_args,
        serializer = PickleSerializer(),
        port = 6379,
        namespace = "main")
    async def map_query(self, cypher_query: str) -> str:
        loop = asyncio.get_event_loop()
        result = await loop.run_in_executor(executor, self.map_query_, cypher_query)
        return result

    def map_query_(self, cypher_query: str) -> str:
        """
        根据映射表修改Cypher语句。
        """
        parsed_query = self._parse_cypher(cypher_query)

        tree = parsed_query.script()
        self.visitor.visit(tree)

        # 生成修改后的Cypher语句
        return get_cypher_query_from_tree(tree)

    def _parse_cypher(self, cypher_query: str) -> CypherParser:
        """
        解析Cypher语句。
        """
        input_stream = InputStream(cypher_query)
        lexer = CypherLexer(input_stream)
        token_stream = CommonTokenStream(lexer)
        return CypherParser(token_stream)
