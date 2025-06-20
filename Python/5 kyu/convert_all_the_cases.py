"""
In this kata, you will make a function that converts between camelCase, snake_case, and kebab-case.

You must write a function that changes to a given case. It must be able to handle all three case types:

py> change_case("snakeCase", "snake")
"snake_case"
py> change_case("some-lisp-name", "camel")
"someLispName"
py> change_case("map_to_all", "kebab")
"map-to-all"
py> change_case("doHTMLRequest", "kebab")
"do-h-t-m-l-request"
py> change_case("invalid-inPut_bad", "kebab")
None
py> change_case("valid-input", "huh???")
None
py> change_case("", "camel")
""
Your function must deal with invalid input as shown, though it will only be passed strings. Furthermore, all valid identifiers will be lowercase except when necessary, in other words on word boundaries in camelCase.

(Any translations would be greatly appreciated!)

https://www.codewars.com/kata/59be8c08bf10a49a240000b1/train/python
"""

import re

class NamingConvention:
    def __init__(self, words: list):
        self.words = words
    
    def camel_case(self):
        return "".join([self.words[0].lower()] + [word.title() for word in self.words[1:]])
    
    def snake_case(self):
        return "_".join([word.lower() for word in self.words])
    
    def kebab_case(self):
        return "-".join([word.lower() for word in self.words])
    
    

def change_case(identifier, target_case):
    if ("-" in identifier and "_" in identifier) or (
        any(c.isupper() for c in identifier) and ("-" in identifier or "_" in identifier)):
        return None
    if identifier == "":
        return ""
    
    if "-" in identifier:
        words = identifier.split("-")
    elif "_" in identifier:
        words = identifier.split("_")
    else:
        words = re.findall(r'[a-z]+|[A-Z](?=[A-Z]|$)|[A-Z][a-z]*', identifier)
        
    nc = NamingConvention(words)
        
    match target_case:
        case "snake": return nc.snake_case()
        case "camel": return nc.camel_case()
        case "kebab": return nc.kebab_case()
        case _: return None