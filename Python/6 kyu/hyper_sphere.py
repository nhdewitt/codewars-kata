"""
You will be given an array of cordinates and a radius. The function should return if the coordinates describe a point within the given radius of the origin.

In two dimensions the condition that any [x, y] coordinate lies in a given radius (= a circle) is:

x
2
+
y
2
≤
r
2
x 
2
 +y 
2
 ≤r 
2
 

This generalises to higher dimensions as follows:

x
2
+
y
2
+
z
2
+
.
.
.
≤
r
2
x 
2
 +y 
2
 +z 
2
 +...≤r 
2
 

Note: a point with no coordinates should return true, as in zero dimensions all points are the same point

https://www.codewars.com/kata/52de9bd621c71b919c000592/train/python
"""

def in_sphere(coords, radius):
    if not coords: return True
    return sum(list(c ** 2 for c in coords)) <= radius ** 2