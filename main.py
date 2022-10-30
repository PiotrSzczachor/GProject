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
             'SEMICOLON',
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
             'ID'
        ] + list(reserved.values())


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
t_SEMICOLON = r'\;'
t_LESS = r'\<'
t_LESS_EQUAL = r'\<='
t_GREATER = r'\>'
t_GREATER_EQUAL = r'\>='
t_NOT_EQUAL = r'\!='
t_AND = r'\&&'
t_OR = r'\|\|'
t_ignore = ' '

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


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'VAR')  # Check for reserved words if not in reserved words than its VAR
    return t



def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


lexer = lex.lex()



def p_start_symbol(p):
    '''
    start_symbol : program
    '''
    p[0] = p[1]

def p_program(p):
    '''
    program : PROGRAM LEFT_BR_CURLY instructions RIGHT_BR_CURLY
            | empty
    '''
    if len(p) == 5:
        p[0] = str(p[1]) + str(p[2]) + str(p[3]) + str(p[4])
    else:
        p[0] = p[1]


def p_instructions(p):
    '''
    instructions : instruction
        | instruction instructions
    '''


def p_instruction(p):
    '''
    instruction : for_loop
        | if_statement
        | assignment
        | empty
        | var_declaration
        | print
        | input
    '''


def p_for_loop(p):
    '''
    for_loop : for_loop_statement LEFT_BR_CURLY instructions RIGHT_BR_CURLY
    '''


def p_for_loop_statement(p):
    '''
    for_loop_statement : FOR LEFT_BR INT VAR EQUAL INT_NUMBER SEMICOLON VAR LESS INT_NUMBER SEMICOLON VAR EQUAL VAR PLUS number RIGHT_BR
    | FOR LEFT_BR INT VAR EQUAL INT_NUMBER SEMICOLON VAR LESS INT_NUMBER SEMICOLON VAR EQUAL VAR MINUS number RIGHT_BR
    '''


def p_if_statement(p):
    '''
    if_statement : IF LEFT_BR comparisons RIGHT_BR LEFT_BR_CURLY instructions RIGHT_BR_CURLY
                 | IF LEFT_BR comparisons RIGHT_BR LEFT_BR_CURLY instructions RIGHT_BR_CURLY  else_statement
    '''


def p_else_statement(p):
    '''
    else_statement : ELSE LEFT_BR_CURLY instructions RIGHT_BR_CURLY
    '''


def p_comparisons(p):
    '''
    comparisons : comparison
        | comparison conjunction comparisons
    '''


def p_comparison(p):
    '''
    comparison : value comparator value
    '''


def p_comparator(p):
    '''
    comparator : LESS
        | LESS_EQUAL
        | GREATER
        | GREATER_EQUAL
        | EQUAL_EQUAL
        | NOT_EQUAL
    '''


def p_operator(p):
    '''
    operator : PLUS
        | MINUS
        | MULTIPLY
        | DIVIDE
    '''


def p_type(p):
    '''
    type : INT
        | STRING
        | BOOL
        | FLOAT
    '''


def p_conjunction(p):
    '''
    conjunction : AND
        | OR
    '''



def p_number(p):
    '''
    number : INT_NUMBER
        | FLOAT_NUMBER
    '''


def p_bool_value(p):
    '''
    bool_value : TRUE
        | FALSE
    '''


def p_value(p):
    '''
    value : number
        | VAR
        | TEXT
        | bool_value
        | math_operation
    '''


def p_math_operation(p):
    '''
    math_operation : VAR operator VAR
        | VAR operator number
        | number operator VAR
        | number operator number
    '''


def p_assignment(p):
    '''
    assignment : VAR EQUAL value SEMICOLON
               | VAR EQUAL VAR SEMICOLON
    '''


def p_var_declaration(p):
    '''
    var_declaration : type VAR SEMICOLON
        | type VAR EQUAL value SEMICOLON
        | type VAR EQUAL VAR SEMICOLON
    '''


def p_print(p):
    '''
    print : PRINT LEFT_BR out RIGHT_BR SEMICOLON
    '''


def p_out(p):
    '''
    out : TEXT
        | VAR
        | number
    '''


def p_input(p):
    '''
    input : INPUT LEFT_BR VAR RIGHT_BR SEMICOLON
    '''


def p_empty(p):
    '''
    empty :
    '''
    p[0] = ""


f = open("test.txt", "r")
code = f.read()
print(code)

parser = yacc.yacc()
print(parser.parse(code))
