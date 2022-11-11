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

def generateRandomProgram(program, depth, i):
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
            is_nested = nested[random.randint(0, len(variables_values)-1)]
            if is_nested and i < depth:
                i += 1
                if i != depth:
                    loop = generateRandomProgram(loop, depth, i)
            program.add_instruction(loop)
        if instruction == "if":
            value = variables_values[random.randint(0, len(variables_values)-1)]
            comparator = comparators[random.randint(0, len(comparators)-1)]
            if value == "val":
                val1 = random.uniform(0, 1000)
                val2 = random.uniform(0, 1000)
                if_statement = IfStatement(val1, comparator, val2)
                program.add_instruction(if_statement)
            else:
                var1 = random.choice(string.ascii_letters)
                var2 = random.choice(string.ascii_letters)
                if_statement = IfStatement(var1, comparator, var2)
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


def programsCrossing(P1, P2):
    firstProgramIndex = random.randint(0, len(P1.instructions))
    secondProgramIndex = random.randint(0, len(P2.instructions))
    firstProgramPart = P1.instructions[0:firstProgramIndex]
    secondProgramPart = P2.instructions[secondProgramIndex:len(P2.instructions)]
    resultProgram = Program()
    resultProgram.instructions = firstProgramPart + secondProgramPart
    return resultProgram


program1 = generateRandomProgram(Program(), 1, 0)
program2 = generateRandomProgram(Program(), 1, 0)
print(program1)
print(program2)
crossed = programsCrossing(program1, program2)
print(crossed)


