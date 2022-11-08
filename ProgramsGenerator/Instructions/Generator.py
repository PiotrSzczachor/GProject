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

def createProgram(program, depth, i):
    instructions = ["for", "if", "assignment"]
    variables_values = ["var", "val"]
    comparators = ["<", "<=", ">", ">=", "==", "!="]
    types = ["lancuch", "calkowita", "zmiennoprzecinkowa"]
    boolea_values = ["prawda", "falsz"]
    nested = [True, False]

    while i <= depth:
        instruction = instructions[random.randint(0, len(instructions)-1)]
        #switch case
        if instruction == "for":
            start = random.randint(-10000, 10000)
            end = random.randint(start+1, start+10000)
            increment = random.randint(-1000, 1000)
            iterator_name = random.choice(string.ascii_letters)
            loop = ForLoop(iterator_name, start, end, increment)
            is_nested = nested[random.randint(0, len(variables_values)-1)]
            if is_nested:
                i += 1
                if i != depth:
                    return createProgram(loop, depth, i)
            program.add_instruction(loop)
        if instruction == "if":
            value = variables_values[random.randint(0, len(variables_values)-1)]
            comparator = comparators[random.randint(0, len(comparators)-1)]
            if value == "val":
                val1 = random.uniform(-1000, 1000)
                val2 = random.uniform(-1000, 1000)
                if_statement = IfStatement(val1, comparator, val2)
                program.add_instruction(if_statement)
            else:
                var1 = random.choice(string.ascii_letters)
                var2 = random.choice(string.ascii_letters)
                if_statement = IfStatement(var1, comparator, var2)
                program.add_instruction(if_statement)
        if instruction == "assignment":
            var = random.choice(string.ascii_letters)
            val = random.uniform(-1000, 1000)
            program.add_instruction(Assignment(var, val))
        if instruction == "input":
            var = random.choice(string.ascii_letters)
            program.add_instruction(Input(var))
        if instruction == "print":
            value = variables_values[random.randint(0, len(variables_values)-1)]
            if value == "val":
                val = random.uniform(-1000, 1000)
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
                val = random.randint(-1000, 1000)
            if type_ == "zmiennoprzecinkowa":
                val = random.uniform(-1000, 1000)
            program.add_instruction(VarDeclaration(type_, var, val))
        if instruction == "empty":
            program.add_instruction(Empty())
        print(program)
    return program


print(createProgram(Program(), 10, 0))
