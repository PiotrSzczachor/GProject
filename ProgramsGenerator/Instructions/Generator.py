import random
import string
import sys

from ForLoop import ForLoop
from IfStatement import IfStatement
from Assignment import Assignment
from Input import Input
from Print import Print
from VarDeclaration import VarDeclaration
from Program import Program
from Empty import Empty

sys.setrecursionlimit(10000)


counter = 0


def generateRandomProgram(program, depth, i=0, is_nested_=False):
    global counter
    counter = i
    instructions = ["for", "if", "assignment", "input", "print", "declaration", "empty"]
    variables_values = ["var", "val"]
    comparators = ["<", "<=", ">", ">=", "==", "!="]
    types = ["lancuch", "calkowita", "zmiennoprzecinkowa"]
    boolea_values = ["prawda", "falsz"]
    nested = [True, False]
    break_while = [True, False, False, False, False, False, False, False, False, False] # Probability 1/10

    while counter < depth:
        if is_nested_:
            random_break = break_while[random.randint(0, len(break_while)-1)]
            if random_break:
                counter = 0
                break
        instruction = instructions[random.randint(0, len(instructions) - 1)]
        # switch case
        if instruction == "for":
            start = random.randint(0, 10000)
            end = random.randint(start + 1, start + 10000)
            increment = random.randint(0, 1000)
            iterator_name = random.choice(string.ascii_letters)
            loop = ForLoop(iterator_name, start, end, increment, program)
            is_nested = nested[random.randint(0, len(nested) - 1)]
            if is_nested and counter < depth:
                counter += 1
                if counter != depth:
                    loop = generateRandomProgram(loop, depth, counter, True)
                is_nested_ = False
            program.add_instruction(loop)
        if instruction == "if":
            value = variables_values[random.randint(0, len(variables_values) - 1)]
            comparator = comparators[random.randint(0, len(comparators) - 1)]
            if_statement = None
            if value == "val":
                val1 = random.uniform(0, 1000)
                val2 = random.uniform(0, 1000)
                if_statement = IfStatement(val1, comparator, val2, program)
            else:
                var1 = random.choice(string.ascii_letters)
                var2 = random.choice(string.ascii_letters)
                if_statement = IfStatement(var1, comparator, var2, program)
            is_nested = nested[random.randint(0, len(variables_values) - 1)]
            if is_nested and counter < depth:
                counter += 1
                if counter != depth:
                    if_statement = generateRandomProgram(if_statement, depth, counter, True)
                is_nested_ = False
            program.add_instruction(if_statement)
        if instruction == "assignment":
            var = random.choice(string.ascii_letters)
            val = random.uniform(0, 1000)
            program.add_instruction(Assignment(var, val, program))
        if instruction == "input":
            var = random.choice(string.ascii_letters)
            program.add_instruction(Input(var, program))
        if instruction == "print":
            value = variables_values[random.randint(0, len(variables_values) - 1)]
            if value == "val":
                val = random.uniform(0, 1000)
                program.add_instruction(Print(val, program))
            else:
                var = random.choice(string.ascii_letters)
                program.add_instruction(Print(var, program))
        if instruction == "declaration":
            type_ = types[random.randint(0, len(types) - 1)]
            var = random.choice(string.ascii_letters)
            val = None
            if type_ == "logiczna":
                val = boolea_values[random.randint(0, len(boolea_values) - 1)]
            if type_ == "calkowita":
                val = random.randint(0, 1000)
            if type_ == "zmiennoprzecinkowa":
                val = random.uniform(0, 1000)
            program.add_instruction(VarDeclaration(type_, var, val, program))
        if instruction == "empty":
            program.add_instruction(Empty(program))
    return program


def programs_crossing(P1, P2):
    P1_element = get_program_element(P1)
    P2_element = get_program_element(P2)
    P1_element_index = P1_element.parent.instructions.index(P1_element)
    P2_element_index = P2_element.parent.instructions.index(P2_element)
    P1_element.parent.instructions[P1_element_index] = P2_element
    P2_element.parent.instructions[P2_element_index] = P1_element


def get_program_element(element):
    nested = [True, False]
    if isinstance(element, Program):
        element = element.instructions[random.randint(0, len(element.instructions) - 1)]
    if isinstance(element, ForLoop) or isinstance(element, IfStatement):
        if len(element.instructions) != 0:
            is_nested = nested[random.randint(0, 1)]
        else:
            is_nested = False
        if is_nested:
            element = get_program_element(element)
        else:
            if len(element.instructions) != 0:
                element = element.instructions[random.randint(0, len(element.instructions) - 1)]
    return element


def program_mutation(P, max_depth):
    # Getting random program element
    element = get_program_element(P)
    print(element)
    # Getting random instruction
    random_instructions = generateRandomProgram(Program(), max_depth)
    random_instruction = random_instructions.instructions[random.randint(0, len(random_instructions.instructions) - 1)]
    print(random_instruction)
    element_index = element.parent.instructions.index(element)
    element.parent.instructions[element_index] = random_instruction


P1 = generateRandomProgram(Program(), 2)
P2 = generateRandomProgram(Program(), 2)
print(P1)
print("\n\n\n")
print(P2)
print("\n\n\n")
programs_crossing(P1, P2)
print("After crossing")
print(P1)
print("\n\n\n")
print(P2)
