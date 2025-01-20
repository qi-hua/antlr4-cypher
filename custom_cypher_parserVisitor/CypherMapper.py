import hashlib
import json
import pickle
import asyncio
from concurrent.futures import ProcessPoolExecutor

import xxhash
from aiocache import cached, Cache
from aiocache.serializers import NullSerializer

from antlr4.InputStream import InputStream
from antlr4.CommonTokenStream import CommonTokenStream

from antlr4_cypher import CypherParser, CypherLexer
from CustomCypherParserVisitor import CustomCypherParserVisitor, get_cypher_query_from_tree

executor = ProcessPoolExecutor(max_workers=10)


def key_from_args(func, *args, **kwargs):
    # 使用 pickle 序列化 args 和 kwargs
    args_data = pickle.dumps((args[1:], sorted(kwargs.items())))
    # 使用 xxhash 计算哈希值
    args_str = xxhash.xxh32(args_data).hexdigest()[:16]
    # 生成最终的键
    module_prefix = f"{func.__module__}:" if func.__module__ else ""
    return f"{module_prefix}{func.__name__}:{args_str}"


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
        ttl=300,
        cache=Cache.REDIS, key_builder=key_from_args,
        serializer = NullSerializer(),
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
