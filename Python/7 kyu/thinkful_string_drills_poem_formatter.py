"""
You have a collection of lovely poems. Unfortunately, they aren't formatted very well. They're all on one line, like this:

Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated.
What you want is to present each sentence on a new line, so that it looks like this:

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Write a function that takes a string (like the one line example) as an argument, returns a new string that is formatted across multiple lines, with each new sentence starting on a new line when you print it out.

Try to solve this challenge with the str.split() and the str.join() string methods.

Every sentence will end with a period, and every new sentence will have one space before the previous period. Be careful about trailing whitespace in your solution.

https://www.codewars.com/kata/585af8f645376cda59000200/train/python
"""

def format_poem(poem):
    return "\n".join(list(p.strip() + "." for p in poem.split(".") if p))   # split leaves leading whitespace and an empty element at the end
                                                                            # re-add the period, strip the whitespace, and ignore the empty element