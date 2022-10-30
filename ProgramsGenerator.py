import sys
import numpy as np
from nltk import CFG
from nltk.parse.generate import generate
import random


def generateRandomProgram(depth):
    random_programs = []
    limit = 0
    while limit < 100:
        int1 = random.randint(-sys.maxsize, sys.maxsize)
        int2 = random.randint(-sys.maxsize, sys.maxsize)
        int3 = random.randint(-sys.maxsize, sys.maxsize)
        int4 = random.randint(-sys.maxsize, sys.maxsize)
        float1 = random.uniform(-sys.maxsize, sys.maxsize)
        grammar = CFG.fromstring(''' S -> PROGRAM
        PROGRAM -> "program" "{" INSTRUCTIONS "}"
        INSTRUCTIONS -> INSTRUCTION | INSTRUCTION INSTRUCTIONS
        INSTRUCTION -> FOR_LOOP | IF_STATEMENT | ASSIGNMENT | EMPTY | VAR_DECLARATION | PRINT | INPUT
        FOR_LOOP -> FOR_LOOP_STATEMENT "{" INSTRUCTIONS "}"
        FOR_LOOP_STATEMENT -> "dla" "(" "calkowita" "zmienna" "=" "''' + str(int1) + "\""''' ";" "zmienna" "<" "''' + str(
            int2) + "\""''' ";" "zmienna" "=" "zmienna" "+" "''' + str(int3) + "\""''' ")"
        IF_STATEMENT -> "jezeli" "(" COMPARISONS ")" "{" INSTRUCTIONS "}" | "jezeli" "(" COMPARISONS ")" "{" INSTRUCTIONS "}" ELSE_STATEMENT
        ELSE_STATEMENT -> "inaczej" "{" INSTRUCTIONS "}"
        COMPARISONS -> COMPARISON | COMPARISON CONJUNCTION COMPARISONS
        COMPARISON -> VALUE COMPARATOR VALUE
        COMPARATOR -> "<" | "<=" | ">" | ">=" | "==" | "!="
        OPERATOR -> "+" | "-" | "*" | "/"
        TYPE -> "calkowita" | "lancuch" | "logiczna" | "zmiennoprzecinkowa"
        CONJUNCTION -> "&&" | "||"
        NUMBER -> "''' + str(int4) + "\""''' | "''' + str(float1) + "\""'''
        BOOL_VALUE -> "prawda" | "falsz"
        VALUE -> NUMBER | "zmienna" | "tekst" | BOOL_VALUE | MATH_OPERATION
        MATH_OPERATION -> "zmienna" OPERATOR "zmienna" | "zmienna" OPERATOR NUMBER | NUMBER OPERATOR "zmienna" | NUMBER OPERATOR NUMBER
        ASSIGNMENT -> "zmienna" "=" VALUE ";" | "zmienna" "=" "zmienna" ";" 
        VAR_DECLARATION -> TYPE "zmienna" ";" | TYPE "zmienna" "=" VALUE ";" | TYPE "zmienna" "=" "zmienna" ";"
        PRINT -> "wyswietl" "(" OUT ")"
        OUT -> "tekst" | "zmienna" | NUMBER
        INPUT -> "wprowadz" "(" "zmienna" ")" ";"
        EMPTY -> ""
        ''')

        grammar.productions()
        counter = 0
        for prog in generate(grammar, depth=depth):
            if counter % 10 == 0:
                random_programs.append(prog)
            if counter == 10000:
                break
            counter += 1
        limit += 1
        print(random_programs)
    index = random.randint(0, len(random_programs))
    return random_programs[index]


prog1 = generateRandomProgram(60)
prog2 = generateRandomProgram(30)


def crossover(program1, program2):
    index1 = random.randint(0, len(program1))
    index2 = random.randint(0, len(program2))
    result = program1[0:index1] + program2[index2:len(program2)]
    return result


print(' '.join(crossover(prog1, prog2)))



