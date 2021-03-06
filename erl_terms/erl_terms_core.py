import re
from parsimonious.grammar import Grammar
import parsimonious.exceptions
from functools import reduce

class ParseError(Exception):
    pass

def readint(text):
    if "#" in text:
        (a, b) = text.split("#", 2)
        return int(b, int(a))
    else:
        return int(text)

def transform(ast):
    if ast.expr_name == "number":
        return [float(ast.text)] if "." in ast.text else [readint(ast.text)]
    elif ast.expr_name == "char_number":
        return [chr(readint(ast.text))]
    elif ast.expr_name == "boolean":
        return [ast.text=="true"]
    elif ast.expr_name == "string":
        return [ast.text[1:-1].replace(r'\"', '"').replace(r'\\\\', '\\\\')]
    elif ast.expr_name == "atom":
        return [ast.text]
    else:
        lis = reduce(lambda a, x: a + transform(x), ast.children, [])
        if ast.expr_name == "list":
            return [lis]
        elif ast.expr_name == "map":
            return [dict(lis)]
        elif ast.expr_name in ["tuple", "keyvalue"]:
            return [tuple(lis)]
        if ast.expr_name == "binary":
            return ["".join(lis)]
        return lis


def lex(text):
    grammar = Grammar("""\
    entry = (term _ "." _)* _
    term = boolean / atom / list / tuple / map / string / binary / number
    atom = ~"[a-z][0-9a-zA-Z_]*" / ("'" ~"[^']*" "'")
    _ = ~"\s*" (~"%[^\\r\\n]*\s*")*
    list = ( _ "[" _ term (_ "," _ term)* _ "]" ) / ( _ "[" _ "]")
    tuple = ( _ "{" _ term (_ "," _ term)* _ "}" ) / ( _ "{" _ "}")
    map   = ( _ "#{" _ keyvalue (_ "," _ keyvalue)* _ "}" ) / ( _ "#{" _ "}")
    keyvalue = term _ "=>" _ term _
    string = '"' ~r'(\\\\.|[^"])*' '"'
    binary = ( "<<" _ binary_part ( _ "," _ binary_part)* _ ">>") / ("<<" _ ">>")
    binary_part = string / char_number
    char_number = ~"[0-9]+"
    boolean = "true" / "false"
    number = ~"\-?[0-9]+\#[0-9a-zA-Z]+" / ~"\-?[0-9]+(\.[0-9]+)?((e|E)(\-|\+)?[0-9]+)?"
    """)
    try:
        return grammar.parse(text)
    except parsimonious.exceptions.ParseError as e:
        raise ParseError(e)


def decode(text):
    return transform(lex(text))
