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

program = Program()
instructions = ["for", "if", "assignment", "input", "print", "declaration", "empty"]
variables_values = ["var", "val"]
comparators = ["<", "<=", ">", ">=", "==", "!="]
assigned_variables = []
depth = input()
for i in depth:
    instruction = instructions[random.randint(0, len(instructions))]
    #switch case
    if instruction == "for":
        start = random.randint(-10000, 10000)
        end = random.randint(start, start+10000)
        increment = random.randint(0, end)
        iterator_name = random.choice(string.ascii_letters)
        program.add_instruction(ForLoop(iterator_name, start, end, increment))
    if instruction == "if":
        value = variables_values[random.randint(0, len(variables_values))]
        comparator = comparators[random.randint(0, len(comparators))]
        if value == "val":
            val1 = random.uniform(-1000, 1000)
            val2 = random.uniform(-1000, 1000)
            program.add_instruction(IfStatement(val1, comparator, val2))
