from antlr4 import *
from antlr.ArithLexer import ArithLexer
from antlr.ArithListener import ArithListener
from antlr.ArithParser import ArithParser
from EvalVisitor import EvalVisitor
from antlr4.tree.Trees import Trees


def main():
    inputt = FileStream("test.txt")
    lexer = ArithLexer(inputt)
    tokens = CommonTokenStream(lexer)

    parser = ArithParser(tokens)

    tree = parser.prog() # begin parsing at prog rule
    # print(Trees.toStringTree(tree, None, parser))
    eval = EvalVisitor()
    # walker = ParseTreeWalker()
    # walker.walk(ShortToUnicodeString(), tree)
    # print()


if __name__ == '__main__':
    main()