from ply import lex
from ply import yacc

reserved = {
    'dla': 'FOR',
    'calkowita': 'INT',
    'lancuch': 'STRING',
    'logiczna': 'BOOL',
    'zmiennoprzecinkowa': 'FLOAT',
    'jezeli': 'IF',
    'inaczej': 'ELSE',
    'prawda': 'TRUE',
    'falsz': 'FALSE',
    'wyswietl': 'PRINT',
    'wprowadz': 'INPUT'
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