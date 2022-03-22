from antlr4 import *
from antlr.basic2Parser import basic2Parser
from antlr.basic2Lexer import basic2Lexer
from listeners.data_generator import DataGenerator
from listeners.code_generator import GenCode

import sys


def main():
    parser = basic2Parser(CommonTokenStream(basic2Lexer(FileStream("input.txt"))))
    tree = parser.program()

    gencode = GenCode()
    dataGen = DataGenerator()

    walker = ParseTreeWalker()
    walker.walk(gencode, tree)
    walker.walk(dataGen, tree)


    with open('test.asm', "w") as writer:
        writer.write(gencode.r)
        writer.write(dataGen.r)

if __name__ == '__main__':
    main()