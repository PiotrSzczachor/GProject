import random

from ply import lex
from ply import yacc
from ProgramsGenerator.Instructions.Generator import Generator
from ProgramsGenerator.Instructions.Program import Program
import numpy as np
import copy

reserved = {
    'program': 'PROGRAM',
    'dla': 'FOR',
    'calkowita': 'INT',
    'lancuch': 'STRING',
    'logiczna': 'BOOL',
    'zmiennoprzecinkowa': 'FLOAT',
    'jezeli': 'IF',
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

# -----------------------------------------------CREATING .PY FILE CONTENT----------------------------------------------
pythonCode = ""
elements = {}
num_of_tabs = 0
inClass = False


# -----------------------------------------------GRAMMAR----------------------------------------------------------------


def p_start_symbol(p):
    '''
    start_symbol : program
    '''
    p[0] = p[1]
    global pythonCode
    pythonCode = p[0]


def p_program(p):
    '''
    program : PROGRAM LEFT_BR_CURLY instructions RIGHT_BR_CURLY
            | empty
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[3]


def p_instructions(p):
    '''
    instructions : instruction
        | instruction instructions
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]


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
    global num_of_tabs
    tabs = ""
    for i in range(num_of_tabs):
        tabs += "    "
    if p[1] != "":
        p[0] = tabs + str(p[1])
    else:
        p[0] = p[1]


def p_for_loop(p):
    '''
    for_loop : for_loop_statement LEFT_BR_CURLY change_tab_number instructions RIGHT_BR_CURLY
    '''
    p[0] = p[1] + ":\n" + p[4] + "\n"
    global num_of_tabs
    num_of_tabs -= 1


def p_for_loop_statement(p):
    '''
    for_loop_statement : FOR LEFT_BR INT VAR EQUAL INT_NUMBER SEMICOLON VAR LESS INT_NUMBER SEMICOLON VAR EQUAL VAR PLUS number RIGHT_BR
    '''
    start_range = p[6]
    end_range = p[10]
    step = p[16]
    p[0] = "for " + p[4] + " in range(" + str(start_range) + ", " + str(end_range) + ", " + str(step) + ")"


def p_if_statement(p):
    '''
    if_statement : IF LEFT_BR comparisons RIGHT_BR LEFT_BR_CURLY change_tab_number instructions RIGHT_BR_CURLY
    '''
    p[0] = "if " + p[3] + ":\n" + str(p[7]) + "\n"
    global num_of_tabs
    num_of_tabs -= 1


def p_comparisons(p):
    '''
    comparisons : comparison
        | comparison conjunction comparisons
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[1] + p[2] + p[3]


def p_comparison(p):
    '''
    comparison : value comparator value
    '''
    p[0] = str(p[1]) + " " + p[2] + " " + str(p[3])


def p_comparator(p):
    '''
    comparator : LESS
        | LESS_EQUAL
        | GREATER
        | GREATER_EQUAL
        | EQUAL_EQUAL
        | NOT_EQUAL
    '''
    p[0] = p[1]


def p_operator(p):
    '''
    operator : PLUS
        | MINUS
        | MULTIPLY
        | DIVIDE
    '''
    p[0] = p[1]


def p_type(p):
    '''
    type : INT
        | STRING
        | BOOL
        | FLOAT
    '''
    p[0] = ""


def p_conjunction(p):
    '''
    conjunction : AND
        | OR
    '''
    p[0] = p[1]


def p_number(p):
    '''
    number : INT_NUMBER
        | FLOAT_NUMBER
    '''
    p[0] = p[1]


def p_bool_value(p):
    '''
    bool_value : TRUE
        | FALSE
    '''
    if p[1] == 'prawda':
        p[0] = '1'
    else:
        p[0] = '0'


def p_value(p):
    '''
    value : number
        | VAR
        | TEXT
        | bool_value
        | math_operation
    '''
    p[0] = p[1]


def p_math_operation(p):
    '''
    math_operation : VAR operator VAR
        | VAR operator number
        | number operator VAR
        | number operator number
    '''
    p[0] = str(p[1]) + " " + p[2] + " " + str(p[3])


def p_assignment(p):
    '''
    assignment : VAR EQUAL value SEMICOLON
               | VAR EQUAL VAR SEMICOLON
    '''
    p[0] = p[1] + p[2] + str(p[3]) + "\n"


def p_var_declaration(p):
    '''
    var_declaration : type VAR SEMICOLON
        | type VAR EQUAL value SEMICOLON
        | type VAR EQUAL VAR SEMICOLON
    '''
    if len(p) == 5:
        p[0] = p[1] + p[2] + " = 0\n"
    elif len(p) == 6:
        p[0] = str(p[2]) + " " + str(p[3]) + " " + str(p[4]) + "\n"


def p_print(p):
    '''
    print : PRINT LEFT_BR out RIGHT_BR SEMICOLON
    '''
    p[0] = "output += str(" + str(p[3]) + ") + '\\n'\n"


def p_out(p):
    '''
    out : TEXT
        | VAR
        | number
    '''
    p[0] = p[1]


def p_input(p):
    '''
    input : INPUT LEFT_BR VAR RIGHT_BR SEMICOLON
    '''
    global input_values
    global input_counter
    global input_count
    if input_values[input_counter] != "":
        p[0] = p[3] + " = " + input_values[input_counter] + "\n"
    else:
        p[0] = p[3] + " = 0" + "\n"
    if input_counter < len(input_values) - 1:
        input_counter += 1


def p_empty(p):
    '''
    empty :
    '''
    p[0] = "pass\n"


def p_change_tab_number(p):
    "change_tab_number : "
    global num_of_tabs
    num_of_tabs += 1


def translate_and_execute(alternative = False):
    global input_row_number
    if alternative:
        file_name = "alternativeIndividual.txt"
    else:
        file_name = "bestIndividual.txt"
    f = open(file_name, "r")
    code = f.read()
    f = open("input.txt", "r")
    global input_values
    global variables
    global input_counter
    global input_row_counter
    input_values = []
    input_values_rows = f.read().split("\n")
    input_row_number = len(input_values_rows)
    input_values = input_values_rows[input_row_counter].split(" ")
    if input_row_counter != input_row_number - 1:
        input_row_counter += 1
    else:
        input_row_counter = 0

    lexer.input(code)
    variables = []
    input_counter = 0
    for token in lexer:
        if token.type == "VAR":
            variables.append(token.value)

    variables = list(set(variables))
    var_declarations = ""
    for var in variables:
        var_declarations += var + " = 0\n"

    parser = yacc.yacc()
    parser.parse(code)
    write_to_file = "file = open('output.txt', 'w')\nfile.write(output)\nfile.close()"

    result = 'output = ""\n' + var_declarations + pythonCode + write_to_file

    exec(result)


def at_least_one_1(values):
    smallest_difference = np.inf
    for value in values:
        if value != "":
            if abs(float(value) - 1) < smallest_difference:
                smallest_difference = abs(float(value) - 1)
    return smallest_difference


def at_least_one_789(values):
    smallest_difference = np.inf
    for value in values:
        if value != "":
            if abs(float(value) - 7) < smallest_difference:
                smallest_difference = abs(float(value) - 7)
    return smallest_difference


def one_at_first_place(values):
    if len(values) > 0 and values[0] != "":
        return abs(10 - float(values[0]))
    else:
        return np.inf


def sum(values):
    global input_values
    input_sum = int(input_values[0]) + int(input_values[1])
    if len(values) != 2:
        return np.inf
    else:
        if values[0] != "":
            return abs(input_sum - float(values[0]))
        else:
            return np.inf


def sum_int_float(values):
    global input_values
    input_sum = int(input_values[0]) + float(input_values[1])
    if len(values) != 2:
        return np.inf
    else:
        if values[0] != "":
            return abs(input_sum - float(values[0]))
        else:
            return np.inf


def squared_sum(values):
    global input_values
    suma = 0
    for i in range(len(input_values)):
        suma += pow(int(input_values[i]), 2)
    if len(values) > 0 and values[0] != "":
        return abs(suma - float(values[0]))
    else:
        return np.inf


def print_smallest_int(values):
    global input_values
    min = np.inf
    for i in range(len(input_values)):
        if int(input_values[i]) < min:
            min = int(input_values[i])
    if len(values) > 0 and values[0] != "":
        if values[0].isdigit():
            return abs(min - int(values[0]))
        else:
            return np.inf
    else:
        return np.inf


def check_fitness():
    f = open("output.txt", "r")
    output_values = f.read().split('\n')
    fitness = one_at_first_place(output_values)
    return fitness


def run():
    global input_row_counter
    global input_row_number
    G = Generator()
    options = ["crossing", "mutation"]
    best_individual = G.generateRandomProgram(Program(), 3)
    G.save_program_to_file(best_individual, 'bestIndividual.txt')
    G.save_program_to_file(best_individual, 'currentIndividual.txt')
    translate_and_execute()
    best_fitness = check_fitness()
    while input_row_counter != 0:
        translate_and_execute()
        best_fitness += check_fitness()
    best_fitness /= input_row_number
    individual_number = 0
    print("Individual number: " + str(individual_number) + " Best Fintess: " + str(best_fitness))
    while best_fitness != 0:
        fitness_1 = 0
        fitness_2 = 0
        individual_number += 1
        if options[random.randint(0, 1)] == 'crossing':
            P = G.generateRandomProgram(Program(), 3)
            alternative_individual_1, alternative_individual_2 = G.programs_crossing(best_individual, P)
            G.save_program_to_file(alternative_individual_1, 'alternativeIndividual.txt')
            translate_and_execute(True)
            fitness_1 += check_fitness()
            while input_row_counter != 0:
                translate_and_execute(True)
                fitness_1 += check_fitness()
            fitness_1 /= input_row_number
            G.save_program_to_file(alternative_individual_2, 'alternativeIndividual.txt')
            translate_and_execute(True)
            fitness_2 += check_fitness()
            while input_row_counter != 0:
                translate_and_execute(True)
                fitness_2 += check_fitness()
            fitness_2 /= input_row_number
            if fitness_1 < fitness_2:
                alternative_individual = alternative_individual_1
            else:
                alternative_individual = alternative_individual_2
        else:
            alternative_individual = copy.deepcopy(best_individual)
            G.program_mutation(alternative_individual, 4)
        fitness = 0
        translate_and_execute(True)
        fitness += check_fitness()
        while input_row_counter != 0:
            translate_and_execute(True)
            fitness += check_fitness()
        fitness /= input_row_number
        if fitness < best_fitness:
            best_fitness = fitness
            best_individual = alternative_individual
            G.save_program_to_file(best_individual, "bestIndividual.txt")
        if best_fitness != 0:
            print("Individual number: " + str(individual_number) + " Best Fintess: " + str(best_fitness))
        else:
            print("Solution found in iteration number " + str(individual_number) + " ! Check it in bestIndividual file")


input_values = []
variables = []
input_counter = 0
input_row_counter = 0
input_row_number = 0
run()
#translate_and_execute()
