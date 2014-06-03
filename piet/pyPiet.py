# Piet interpreter
import sys

def openBin(filename):
    with open(filename, "rbU") as x:
        return x.read()


