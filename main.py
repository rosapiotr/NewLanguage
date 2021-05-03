from antlr4 import *
import antlr4
from LangLexer import LangLexer
from LangListenerImpl import LangListenerImpl
from LangParser import LangParser
import sys

def main(input_file=None):
    if input_file is None:
        lexer = LangLexer(StdinStream())
    else:
        lexer = LangLexer(FileStream(input_file))
    
    stream = CommonTokenStream(lexer)
    parser = LangParser(stream)
    tree = parser.prog()
    for node in tree.children:
        if type(node) is antlr4.tree.Tree.ErrorNodeImpl:
            print(">>>No code generated<<<")
            return
        # print(type(node))
    # print(tree.toStringTree())
    printer = LangListenerImpl()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    if len(sys.argv) - 1 == 1:
        main(sys.argv[1])
    else:
        main()
