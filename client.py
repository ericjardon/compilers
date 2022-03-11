from antlr4 import *
from antlr.ericParser import ericParser
from antlr.ericLexer import ericLexer
from listeners.gencode import GenCode

import sys


def main():
    parser = ericParser(CommonTokenStream(ericLexer(FileStream("input.txt"))))
    tree = parser.program()

    gencode = GenCode()
    walker = ParseTreeWalker()
    walker.walk(gencode, tree)


if __name__ == '__main__':
    main()