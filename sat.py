#!/usr/bin/python3

import fileinput
import statistics
import sys

def parser():
    """
    Parser core.
    """
    #with open(filename, 'r') as dimacs_file:
    #    lines = dimacs_file.readlines()

    formula = []

    for line in fileinput.input():
        line = line.strip()
        if len(line) > 0 \
        and not line.startswith('c') \
        and not line.startswith('p'):
            formula.append([int(x) for x in line.split()[:-1]])

    return formula

def has_unit_clause(formula):
    """
    Returns a unit clause.
    Returns 0 (False) if there is no unit clause.
    """
    for i in formula:
        if len(i) == 1:
            return i[0]
    return 0

def has_empty_clause(formula):
    """
    Returns True if the formula has an empty clause.
    """
    for i in formula:
        if len(i) == 0:
            return True
    return False

def unit_propagation(formula):
    """
    Returns the formula after unit propagation.
    """
    litteral = has_unit_clause(formula)

    while litteral:
        formula = [[y for y in x if y != -1*litteral] \
            for x in formula if litteral not in x]
        litteral = has_unit_clause(formula)

    return formula

def choose_litteral(formula):
    """
    Returns the literal with the highest occurrence.
    """
    return statistics.mode([x for y in formula for x in y])

def solver(formula):
    """
    Solver core.
    """
    formula = unit_propagation(formula)

    if formula == []:
        return True
    if [] in formula:
        return False

    litteral = choose_litteral(formula)

    if solver(formula + [[litteral]]):
        return True
    return solver(formula + [[-1*litteral]])

if __name__ == '__main__':
    #try:
    cnf = parser()
    if solver(cnf):
        print("satisfiable")
    else:
        print("unsatisfiable")
    #except:
    #    print("Error: File not found.")
    #else:
    #    print("Error: File argugment is missing.")
