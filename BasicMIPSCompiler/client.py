from antlr4 import *
from antlr.ericParser import ericParser
from antlr.ericLexer import ericLexer
from listeners.codegenerator import CodeGenerator

import sys


def main():
    lexer = ericLexer(FileStream("input.eric"))
    parser = ericParser(CommonTokenStream(lexer))
    tree = parser.program()

    gencode = CodeGenerator()
    walker = ParseTreeWalker()
    walker.walk(gencode, tree)


if __name__ == '__main__':
    main()