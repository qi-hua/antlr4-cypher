# antlr4-cypher

`antlr4-cypher` is a Python package that provides the Lexer and Parser for the Cypher query language, generated using [ANTLR](https://github.com/antlr/antlr4) with the command `java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -listener -visitor -o ./antlr4_cypher CypherLexer.g4 CypherParser.g4`. The project includes the necessary grammar, lexer, and parser files, as well as empty listener and visitor classes that serve as a reference for implementing custom logic.

## Installation

You can install the package using pip:

```bash
pip install antlr4-cypher
```

## Grammar Source

The grammar files (`CypherLexer.g4` and `CypherParser.g4`) are sourced from the [ANTLR grammars-v4 repository](https://github.com/antlr/grammars-v4/tree/master/cypher). These files define the syntax and structure of the Cypher query language.

## Usage

To use the lexer and parser in your project, you can import them as follows:

```python
from antlr4 import InputStream, CommonTokenStream
from antlr4_cypher import CypherLexer, CypherParser

# Example input
input_query = "MATCH (n) RETURN n"

# Create a lexer and parser
input_stream = InputStream(input_query)
lexer = CypherLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = CypherParser(token_stream)

# Parse the input
tree = parser.script()

# Use the tree for further processing
```

## Custom Listeners and Visitors

The package includes empty listener and visitor classes that you can extend to implement custom logic for traversing the parse tree. For example:

```python
from antlr4_cypher import CypherParserListener

class MyCypherListener(CypherParserListener):
    def enterMatchSt(self, ctx):
        print("Entering MATCH clause")

    def exitMatchSt(self, ctx):
        print("Exiting MATCH clause")


from antlr4_cypher import CypherParserVisitor

class CustomCypherParserVisitor(CypherParserVisitor):
    def __init__(self, mapping: dict):
        super().__init__()
        self.mapping = mapping

    def visit(self, tree):
        print("Visiting node:", tree.getText())
        return tree.accept(self)

    # Example of overriding a specific visit method
    def visitMatchSt(self, ctx):
        print("Processing MATCH clause with mapping:", self.mapping)
        return self.visitChildren(ctx)
```

---

This README provides a basic overview of the `antlr4-cypher` project. For more detailed information, please refer to the source code and the ANTLR documentation.