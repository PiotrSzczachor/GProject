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

def generateRandomProgram(program, depth, i = 0):
    instructions = ["for", "if", "assignment", "input", "print", "declaration", "empty"]
    variables_values = ["var", "val"]
    comparators = ["<", "<=", ">", ">=", "==", "!="]
    types = ["lancuch", "calkowita", "zmiennoprzecinkowa"]
    boolea_values = ["prawda", "falsz"]
    nested = [True, False]

    while i < depth:
        instruction = instructions[random.randint(0, len(instructions)-1)]
        #switch case
        if instruction == "for":
            start = random.randint(0, 10000)
            end = random.randint(start+1, start+10000)
            increment = random.randint(0, 1000)
            iterator_name = random.choice(string.ascii_letters)
            loop = ForLoop(iterator_name, start, end, increment)
            is_nested = nested[random.randint(0, len(nested)-1)]
            if is_nested and i < depth:
                i += 1
                if i != depth:
                    loop = generateRandomProgram(loop, depth, i)
            program.add_instruction(loop)
        if instruction == "if":
            value = variables_values[random.randint(0, len(variables_values)-1)]
            comparator = comparators[random.randint(0, len(comparators)-1)]
            if_statement = None
            if value == "val":
                val1 = random.uniform(0, 1000)
                val2 = random.uniform(0, 1000)
                if_statement = IfStatement(val1, comparator, val2)
            else:
                var1 = random.choice(string.ascii_letters)
                var2 = random.choice(string.ascii_letters)
                if_statement = IfStatement(var1, comparator, var2)
            is_nested = nested[random.randint(0, len(variables_values)-1)]
            if is_nested and i < depth:
                i += 1
                if i != depth:
                    if_statement = generateRandomProgram(if_statement, depth, i)
            program.add_instruction(if_statement)
        if instruction == "assignment":
            var = random.choice(string.ascii_letters)
            val = random.uniform(0, 1000)
            program.add_instruction(Assignment(var, val))
        if instruction == "input":
            var = random.choice(string.ascii_letters)
            program.add_instruction(Input(var))
        if instruction == "print":
            value = variables_values[random.randint(0, len(variables_values)-1)]
            if value == "val":
                val = random.uniform(0, 1000)
                program.add_instruction(Print(val))
            else:
                var = random.choice(string.ascii_letters)
                program.add_instruction(Print(var))
        if instruction == "declaration":
            type_ = types[random.randint(0, len(types)-1)]
            var = random.choice(string.ascii_letters)
            val = None
            if type_ == "logiczna":
                val = boolea_values[random.randint(0, len(boolea_values)-1)]
            if type_ == "calkowita":
                val = random.randint(0, 1000)
            if type_ == "zmiennoprzecinkowa":
                val = random.uniform(0, 1000)
            program.add_instruction(VarDeclaration(type_, var, val))
        if instruction == "empty":
            program.add_instruction(Empty())
    return program


def programs_crossing(P1, P2):
    pass


def get_program_element(element):
    nested = [True, False]
    if isinstance(element, Program):
        element = element.instructions[random.randint(0, len(element.instructions)-1)]
    if isinstance(element, ForLoop) or isinstance(element, IfStatement):
        if len(element.instructions) != 0:
            is_nested = nested[random.randint(0, 1)]
        else:
            is_nested = False
        if is_nested:
            element = get_program_element(element)
        else:
            if len(element.instructions) != 0:
                element = element.instructions[random.randint(0, len(element.instructions)-1)]
    return element


def program_mutation(P, max_depth):
    index = random.randint(0, len(P.instructions)-1)
    nested = [True, False]
    element = P.instructions[index]
    tmp = None
    if isinstance(element, Assignment):
        is_nested = nested[random.randint(0, len(nested) - 1)]
        if is_nested:
            tmp = generateRandomProgram(Program(), max_depth)
        else:
            new_value = random.randint(-1000, 1000)
            element.value = new_value
    if isinstance(element, Empty):
        tmp = generateRandomProgram(Program(), max_depth)
    if isinstance(element, Input):
        is_nested = nested[random.randint(0, len(nested) - 1)]
        if is_nested:
            tmp = generateRandomProgram(Program(), max_depth)
        else:
            element.variable = random.choice(string.ascii_letters)
    if isinstance(element, Print):
        is_nested = nested[random.randint(0, len(nested) - 1)]
        if is_nested:
            tmp = generateRandomProgram(Program(), max_depth)
    if isinstance(element, VarDeclaration):
        tmp = generateRandomProgram(Program(), max_depth)
    element.instructions.clear()
    element = generateRandomProgram(element, max_depth, 0)
    return P


P = generateRandomProgram(Program(), 3)
print(P)
print("\n\n\n\n")
print(get_program_element(P))
