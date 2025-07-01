"""
When working with color values it can sometimes be useful to extract the individual red, green, and blue (RGB) component values for a color. Implement a function that meets these requirements:

Accepts a case-insensitive hexadecimal color string as its parameter (ex. "#FF9933" or "#ff9933")
Returns a Map<String, int> with the structure {r: 255, g: 153, b: 51} where r, g, and b range from 0 through 255
Note: your implementation does not need to support the shorthand form of hexadecimal notation (ie "#FFF")

Example
"#FF9933" --> {r: 255, g: 153, b: 51}

https://www.codewars.com/kata/5282b48bb70058e4c4000fa7/train/python
"""

def hex_string_to_RGB(hex_string): 
    hex_string = hex_string.lower()
    r, g, b = hex_string[1:3], hex_string[3:5], hex_string[5:]
    return {
        "r": int(r, 16),
        "g": int(g, 16),
        "b": int(b, 16),
    }