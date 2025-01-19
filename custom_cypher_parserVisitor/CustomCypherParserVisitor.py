from io import StringIO

from antlr4 import Token, ParserRuleContext
from antlr4.Token import CommonToken
from antlr4.tree.Tree import TerminalNodeImpl, TerminalNode

from antlr4_cypher import CypherParser, CypherParserVisitor


def build_token_node(text=None, type: int=None):
    try:
        if text and not type:
            type = CypherParser.literalNames.index(f"'{text}'")
        elif not text and type:
            text = CypherParser.literalNames[type][1:-1]
        elif text and type:
            if text != CypherParser.literalNames[type]:
                raise MappingError(f"{text} is not a valid token")
        else:
            raise Exception("text and type cannot be both empty")
    except ValueError:
        raise MappingError(f"{text} is not a valid token")
    except KeyError:
        raise MappingError(f"{type} is not a valid type")
    except:
        raise MappingError("text and type error")
    token = CommonToken(type=type)
    token.text = text
    return TerminalNodeImpl(token)


NODE_LT = build_token_node(type=CypherParser.LT)
NODE_SUB = build_token_node(type=CypherParser.SUB)
NODE_GT = build_token_node(type=CypherParser.GT)


def get_cypher_query_from_tree(tree: ParserRuleContext):
    """由语法树生成Cypher语句"""
    tokens = extract_tokens_from_tree(tree)
    with StringIO() as buf:
        # print("tokens:")
        for t in tokens:
            # print(t)
            if t.type == Token.EOF:
                break
            buf.write(t.text)
        return buf.getvalue()

def extract_tokens_from_tree(tree: ParserRuleContext):
    """用于提取语法树中的 tokens"""
    if tree is None:
        return []
    tokens = []
    for child in tree.getChildren():
        if isinstance(child, TerminalNodeImpl):  # 如果是叶子节点
            tokens.append(child.getSymbol())     # 获取 token
        else:
            # 递归访问子节点
            tokens.extend(extract_tokens_from_tree(child))
    return tokens


class MappingError(Exception):
    """自定义异常类，用于捕获不支持的映射操作。"""
    def __init__(self, message: str):
        super().__init__(message)


class CustomCypherParserVisitor(CypherParserVisitor):
    def __init__(self, mapping: dict):
        super().__init__()
        self.mapping = mapping

    def visitRelationshipPattern(self, ctx: CypherParser.RelationshipPatternContext):
        """
        访问关系模式节点，动态替换关系。
        """
        def get_direction(ctx: CypherParser.RelationshipPatternContext) -> str:
            for child in ctx.getChildren():
                if not isinstance(child, TerminalNode):
                    continue
                if child.symbol.type == CypherParser.LT:
                    return '<'
                elif child.symbol.type == CypherParser.GT:
                    return '>'
                else:
                    continue
            return ''

        # tokens = extract_tokens_from_tree(ctx)
        # for t in tokens:
        #     print(t)
        relation_detail = ctx.relationDetail()
        if relation_detail:
            # print("relationship_detail: ", relation_detail.getText())
            relationship_types = relation_detail.relationshipTypes()
            if relationship_types:
                # for name_context in relationship_types.name():
                ## 目前只支持对一个关系类型的情况进行映射，// 后续可以支持对多个关系类型的映射。
                name_contexts = relationship_types.name()
                if len(name_contexts) == 1:
                    # print("name_context: ", name_context.getText())
                    name_context = name_contexts[0]
                    original_type = name_context.getText()
                    if original_type in self.mapping:
                        mapping_config:dict = self.mapping[original_type]
                        # print("mapping_config: ", mapping_config)
                        target_rules = mapping_config.get("target", {})
                        if target_rules:
                            name_context.symbol().children[0].symbol.text = target_rules['type']
                            if target_rules.get("direction", "") == "reverse":
                                # print("direction: ", getDirection(ctx))
                                direction = get_direction(ctx)
                                if direction == '<':
                                    ctx.children = [NODE_SUB, relation_detail ,NODE_SUB, NODE_GT]
                                elif direction == '>' or direction == '':
                                    ctx.children = [NODE_LT, NODE_SUB, relation_detail ,NODE_SUB]

                            # tokens = extract_tokens_from_tree(ctx)
                            # for t in tokens:
                            #     print(t)
                else:
                    pass
        # return self.visitChildren(ctx)
        return None


