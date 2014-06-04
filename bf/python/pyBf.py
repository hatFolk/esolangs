### An interpreter for BF
"""
Here's the Character Chart:
    > | Increment data pointer to next cell right
    < | Incremente data pointer to next cell left
    + | Increment by one the byte at that data pointer.
    - | Decrement by one the byte at the data pointer
    . | Output byte at data pointer
    , | accept one byte of input, storing its value in the byte at the data pointer
    [ | if the byte at the data pointer is zero, then instead of movving the instruction pointer
        forward to the next command, jump it forward to the command after the matching ] command
    ] | If the byte at the data pointer is not zero, then instead of moving the instruction pointer
        forward to the next c ommand, jump it back to the command after the matching ] command.

    Their equivalences in C:
    Begin | char array[Really. Really big]; char *ptr = array;
    >     | ++ptr; // Move ptr forward
    <     | --ptr; // Move ptr backwards
    +     | ++*ptr; // Add one to the value at pointer
    -     | --*ptr; // Take one from value at pointer;
    .     | putchar(*ptr); // Display value at pointer
    ,     | *ptr = getchar(); // Get a value and give it to pointer.
    [     | while(*ptr) { // While pointer is not null or 0, loop. Else, jump to ]
    ]     | } // if *ptr is not null or 0, go back to [. Else go to next line.
"""
import sys

def openFile(filename):
    with open(filename, "rU") as x:# If unopenable, allow to crash
        return x.read()

def isZero(x):
    return x == 0

def inc(ind, ptr, ptrInd, state):
    ptr[ptrInd] += 1
    return iterate(ind, ptr, ptrInd, state)

def dec(ind, ptr, ptrInd, state):
    ptr[ptrInd] -= 1
    return iterate(ind, ptr, ptrInd, state)

def fwd(ind, ptr, ptrInd, state):
    ptrInd += 1
    if ptrInd > len(ptr)-1:
        ptr.append(0)
    return iterate(ind, ptr, ptrInd, state)

def bwd(ind, ptr, ptrInd, state):
    ptrInd -= 1
    if ptrInd < 0:
        raise IndexError()
    return iterate(ind, ptr, ptrInd, state)

def prt(ind, ptr, ptrInd, state):
    print(chr(ptr[ptrInd]), end = '')
    return iterate(ind, ptr, ptrInd, state)

def getChar(ind, ptr, ptrInd, state):
    ptr[ptrInd] = ord(input("")[0])
    return iterate(ind, ptr, ptrInd, state)

def inLoop(ind, ptr, ptrInd, state):
    notZero = not isZero(ptr[ptrInd])
    notContained = ind not in state
    if notZero and notContained:
        state.append(ind)
    return iterate(ind, ptr, ptrInd, state)

def outLoop(ind, ptr, ptrInd, state):
    notZero = not isZero(ptr[ptrInd])
    return iterate(state[-1], ptr, ptrInd, state) if notZero else iterate(ind, ptr, ptrInd, state[:-1])

def iterate(ind, ptr, ptrInd, state):
    return ind+1, ptr, ptrInd, state

def execute(ind, ptr, ptrInd, state, char):
    options = {"+":inc,
            "-":dec,
            ">":fwd,
            "<":bwd,
            ".":prt,
            ",":getChar,
            "[":inLoop,
            "]":outLoop}
    return options.get(char, iterate)(ind, ptr, ptrInd, state)

def parse(text):
    i, ptr, ptrInd, state = 0, [0], 0, []
    while i < len(text):
        i, ptr, ptrInd, state = execute(i, ptr, ptrInd, state, text[i])

def main(files):
    [i for i in map(lambda x: parse(openFile(x)), files)]

if __name__=="__main__": main(sys.argv[1:])
