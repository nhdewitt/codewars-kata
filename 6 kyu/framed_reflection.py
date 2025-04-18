"""
100th Kata
You are given a message (text) that you choose to read in a mirror (weirdo). Return what you would see, complete with the mirror frame. Example:

'Hello World'

would give:


Words in your solution should be left-aligned.

https://www.codewars.com/kata/581331293788bc1702001fa6/train/python
"""

def mirror(text):
    splt = text.split()                                                             # words separated by newline, split on ()
    border = len(sorted(splt, key=len)[-1]) + 4                                     # border is the length of the longest substring (sort splt on length, grab [-1]) + 4
    output = ['*' * border]
    for i in range(len(splt)):
        output.append(f"* {splt[i][::-1]}{' ' * (border - 3 - len(splt[i]))}*")     # for each word, append "* " + reversed word + "[border length - 3 ("* " and "*") - length of the word]"
    output.append(f"{'*' * border}")
    
    return "\n".join(output)                                                         # output as a string