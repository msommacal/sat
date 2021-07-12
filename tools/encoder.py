#!/usr/bin/python3

string = input()

def encode(string):
    F = []
    for c in string.split("&"):
        C = []
        for l in c.split("|"):
            C.append(l.strip("() "))
        F.append(C)
    return F

def build_table(F):
    variable_table = dict()
    i = 1
    for clause in F:
        for litteral in clause:
            if litteral.startswith("~"):
                l = litteral[1:]
            else:
                l = litteral
            if not l in variable_table:
                variable_table.update({l:i})
                i += 1
    return variable_table

F = encode(string)
T = build_table(F)

for clause in F:
    for i in range(len(clause)):
        if clause[i].startswith("~"):
            clause[i] = "-"+str(T.get(clause[i][1:]))
        else:
            clause[i] = str(T.get(clause[i]))
    clause.append("0")
    print(" ".join(clause))
