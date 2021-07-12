#!/usr/bin/python3

import sys

string = str(sys.stdin.read())

string = string.replace(" 0", "")
string = string.replace("-", "~")
string = string.replace(" ", " | ")

string = " & ".join(["("+x+")" for x in string.split("\n")])

print(string[:-5])
