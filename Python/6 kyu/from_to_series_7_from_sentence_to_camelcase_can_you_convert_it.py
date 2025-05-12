"""
Description:
Give you a sentence s. It contains some words and separated by spaces. Another arguments is n, its a number(1,2 or 3). You should convert s to camelCase n.

There are three kinds of camelCase:

camelCase 1: The first letter of each word should be capitalized. 
              Except for the first word.

Example: "Hello world"  -->  "helloWorld"

camelCase 2: The last letter of each word should be capitalized. 
              Except for the last word. 

Example: "Hello world"  -->  "hellOworld"

camelCase 3: The first and last letters of each word should be capitalized. 
              Except for the first and lasts letter of sentence. 

Example: "Hello world"  -->  "hellOWorld" 
You can assume that all of the input data is valid. That is: s always be a string; It contains at least two words; Each word contains only letters(a-zA-Z); Each word contains ar least three letters; n always be 1,2 or 3.

Examples
toCamelCase("hello world",1) === "helloWorld"
toCamelCase("hello world",2) === "hellOworld"
toCamelCase("hello world",3) === "hellOWorld"

toCamelCase("Hello world",1) === "helloWorld"

toCamelCase("Each number plus one",1) === "eachNumberPlusOne"
toCamelCase("Each number plus one",2) === "eacHnumbeRpluSone"
toCamelCase("Each number plus one",3) === "eacHNumbeRPluSOne"
Random tests may contains bug(I'm not sure), please test and feedback, thanks ;-)

https://www.codewars.com/kata/58097ae96037b88f57000105/train/python
"""

def to_camel_case(s, n):
    words = s.lower().split()                                                                             # normalize string to all lower, split by word
    output = []
    if n == 1:                                                                                            # standard camel case, 1st word already lowercase, add title() for each word after
        output.append(words[0])
        output.extend(list(word.title() for word in words[1:]))
    elif n == 2:
        output.extend(list(word[::-1].title()[::-1] for word in words[:-1]))                              # reverse the word, title() the word, reverse it back up to last word in sentence
        output.append(words[-1])                                                                          # append the last word (already all lowercase)
    elif n == 3:
        output.append(words[0][::-1].title()[::-1])                                                       # first word behaves like n==2
        output.extend(list(word[0].upper() + word[1:-1] + word[-1].upper() for word in words[1:-1]))      # capitalize the first and last letter, sandwich the rest of the word between
        output.append(words[-1].title())                                                                  # behaves like normal camel case
    return "".join(output)