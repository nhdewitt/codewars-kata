"""
It's important day today: the class has just had a math test. You will be given a list of marks. Complete the function that will:

Calculate the average mark of the whole class and round it to 3 decimal places.
Make a dictionary/hash with keys "h", "a", "l" to make clear how many high, average and low marks they got. High marks are 9 & 10, average marks are 7 & 8, and low marks are 1 to 6.
Return list [class_average, dictionary] if there are different type of marks, or [class_average, dictionary, "They did well"] if there are only high marks.
Examples
[10, 9, 9, 10, 9, 10, 9] ==> [9.429, {'h': 7, 'a': 0, 'l': 0}, 'They did well']

[5, 6, 4, 8, 9, 8, 9, 10, 10, 10] ==> [7.9, {'h': 5, 'a': 2, 'l': 3}]

https://www.codewars.com/kata/599db0a227ca9f294b0000c8/train/python
"""

def test(r):
    marks = {
        "h": 0,
        "a": 0,
        "l": 0
    }
    
    avg = 0
    for t in r:
        if t >= 9:
            marks["h"] += 1
        elif t >= 7:
            marks["a"] += 1
        else:
            marks["l"] += 1
        avg += t
    
    output = [round(avg / len(r), 3), marks]
    if marks["h"] == len(r):
        output.append("They did well")
    
    return output