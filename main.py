from ply import lex
from ply import yacc

reserved = {
    'program': 'PROGRAM',
    'dla': 'FOR',
    'calkowita': 'INT',
    'lancuch': 'STRING',
    'logiczna': 'BOOL',
    'zmiennoprzecinkowa': 'FLOAT',
    'jezeli': 'IF',
    'to': 'THEN',
    'inaczej': 'ELSE',
    'prawda': 'TRUE',
    'falsz': 'FALSE',
    'wyswietl': 'PRINT',
    'wprowadz': 'INPUT',
}

tokens = [
             'EQUAL_EQUAL',
             'PLUS',
             'MINUS',
             'MULTIPLY',
             'DIVIDE',
             'EQUAL',
             'LEFT_BR',
             'RIGHT_BR',
             'LEFT_BR_CURLY',
             'RIGHT_BR_CURLY',
             'LESS',
             'LESS_EQUAL',
             'GREATER',
             'GREATER_EQUAL',
             'NOT_EQUAL',
             'AND',
             'OR',
             'INT_NUMBER',
             'FLOAT_NUMBER',
             'VAR',
             'TEXT',
             'EMPTY_TEXT'
        ]


t_EQUAL_EQUAL = r'\=='
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\/'
t_EQUAL = r'\='
t_LEFT_BR = r'\('
t_RIGHT_BR = r'\)'
t_LEFT_BR_CURLY = r'\{'
t_RIGHT_BR_CURLY = r'\}'
t_LESS = r'\<'
t_LESS_EQUAL = r'\<='
t_GREATER = r'\>'
t_GREATER_EQUAL = r'\>='
t_NOT_EQUAL = r'\!='
t_AND = r'\&&'
t_OR = r'\|\|'

def t_FLOAT_NUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_INT_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_TEXT = r'"(.*?[^\\])"'
t_EMPTY_TEXT = r'""'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    global wasError
    wasError = True


lexer = lex.lex()
lexer.input('program{jezeli(2.3==3)to("")}')

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
