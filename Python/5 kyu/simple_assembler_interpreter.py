"""
This is the first part of this kata series. Second part is here.

We want to create a simple interpreter of assembler which will support the following instructions:

mov x y - copies y (either a constant value or the content of a register) into register x
inc x - increases the content of the register x by one
dec x - decreases the content of the register x by one
jnz x y - jumps to an instruction y steps away (positive means forward, negative means backward, y can be a register or a constant), but only if x (a constant or a register) is not zero
Register names are alphabetical (letters only). Constants are always integers (positive or negative).

Note: the jnz instruction moves relative to itself. For example, an offset of -1 would continue at the previous instruction, while an offset of 2 would skip over the next instruction.

The function will take an input list with the sequence of the program instructions and will execute them. The program ends when there are no more instructions to execute, then it returns a dictionary (a table in COBOL) with the contents of the registers.

Also, every inc/dec/jnz on a register will always be preceeded by a mov on the register first, so you don't need to worry about uninitialized registers.

Example
["mov a 5"; "inc a"; "dec a"; "dec a"; "jnz a -1"; "inc a"]

visualized:

mov a 5
inc a
dec a
dec a
jnz a -1
inc a
The above code will:

set register a to 5,
increase its value by 1,
decrease its value by 2,
then decrease its value until it is zero (jnz a -1 jumps to the previous instruction if a is not zero)
and then increase its value by 1, leaving register a at 1
So, the function should return:

{'a': 1}

https://www.codewars.com/kata/58e24788e24ddee28e000053/train/python
"""

def simple_assembler(program):
    register = {}
    i = 0
    while i < len(program):
        sp = program[i].split()                                                     # split into cmd, a, (b)
        cmd = sp[0]
        
        if cmd == "jnz":
            x, y = sp[1], sp[2]
            x = int(x) if x.lstrip('-').isdigit() else register[x]                  # if x is a digit, x = int(x) else grab dict value
            y = int(y) if y.lstrip('-').isdigit() else register[y]                  # same for y
            if x != 0:                                                              # if x is not 0, increment by y and restart the loop
                i += y                                                              # otherwise, i++ will happen as normal
                continue
        
        elif cmd == "mov":
            x, y = sp[1], sp[2]
            register[x] = int(y) if y.lstrip('-').isdigit() else register[y]        # set dict to either the value of register[y] or the number y
            
        elif cmd == "inc":
            x = sp[1]
            register[x] += 1
            
        elif cmd == "dec":
            x = sp[1]
            register[x] -= 1


        i += 1
    return register