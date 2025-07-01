"""
Complete the function/method so that it takes a PascalCase string and returns the string in snake_case notation. Lowercase characters can be numbers. If the method gets a number as input, it should return a string.

Examples
"TestController"  -->  "test_controller"
"MoviesAndBooks"  -->  "movies_and_books"
"App7Test"        -->  "app7_test"
1                 -->  "1"

https://www.codewars.com/kata/529b418d533b76924600085d/train/python
"""

def to_underscore(strng: str) -> str:
    if isinstance(strng, int):
        return str(strng)
    if not strng:
        return ""
    output = [strng[0].lower()]
    for i in range(1, len(strng)):
        if strng[i].isupper():
            output.append("_")
            output.append(strng[i].lower())
        else:
            output.append(strng[i])
    return "".join(output)