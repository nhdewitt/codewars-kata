"""
I merely walk the humble Michael Street.

Background
Well, you lost Michael.

You last saw him walking ahead of you on an infinitely forking road. Luckily, you don't need to think very hard about which road to take, for each fork leads only to two new roads, never more, never less. The issue is that it's much too foggy to see, and you can't tell whether a silhouette on the path is Michael or some other such terrible monster. Luckily, Michael lets off a very distinct, ghastly onion smell at all times, allowing you to use only your sense of smell to find him.

Task
You must traverse the given road to find Michael. Return a String representing the turns you took on the road before finding Michael. Right turns are denoted by the character 'R' and left turns by 'L'.

-> "RRRRLLLRLRL" // took the right path 4 times, then the left 3 times, then the right, left, right, left
-> "LLLLLLLLLLL" // just turned left like it's Nascar
The Road
The only argument passed to your code is a singular object, the Road. You can gather information about either of the next roads by using .sniffLeft() and .sniffRight() to retrieve the smells of the left and right roads respectively. Note that while you are on a road, you cannot access its scent, so you should gather scents before continuing down a path. Also, you can only sniff once per fork. After using a sniffing method, you cannot use another without an OverusedSnifferException being thrown. Of course, you can use your nose again once you move down one of the roads.

To go down a road, you must use its .traverseLeft() or .traverseRight() methods. This will change the road object to either its left or right subroad respectively.

The number of roads between you and Michael is at least 1 road.

Below is all that you need to know about the Road structure.

class Road:
    # L: Road     (private)
    # R: Road     (private)
    # scent: str  (private)

    sniff_left: Callable[[], str]       # returns scent of Road L
    sniff_right: Callable[[], str]      # returns scent of Road R
    
    traverse_left: Callable[[], None]   # changes this Road to Road L
    traverse_right: Callable[[], None]  # changes this Road to Road R
Hunting for Michael
You can find if a Road leads to Michael by using its scent. Michael is followed by a horrible, noxious odor: if the scent of a road reads "This one reeks." then you know that that is the road that you must go down. "Pleasant air." denotes that Michael is absolutely not down that road. If it reads "Michael!" then it is the road that Michael is currently on, meaning you only need one more turn to reach him. If you check one road while the other road has Michael, that road will read "I smell Michael on the other road!"

Final Notes
Road is a very unorthodox structure. You will have to be able to understand a new, usermade construct based off of its description; a useful skill in the programming world.
On any given road, one of the next roads will always carry Michael or his wretched stench; you don't need to worry about probability or taking chances.
The road is infinite. A single mistake will lead to you losing Michael forever, likely timing out your code.
You may create your own Road object, but it is not useful to do so.
See a detailed example of the problem in the sample test cases.
Other Michael katas will soon follow this first one, forming a Michael Series.

https://www.codewars.com/kata/67ff4d0d346ee84001e9cc60/train/python
"""

def solve_roads(road):
    output = ""                             # sniff, move L/R based on output unless Michael is found in which case append appropriate direction and return
    while True:
        sniff = road.sniff_left()
        if sniff == "This one reeks.":
            output += "L"
            road.traverse_left()
        elif sniff == "Pleasant air.":
            output += "R"
            road.traverse_right()
        elif sniff == "Michael!":
            output += "L"
            return output
        else:
            output += "R"
            return output