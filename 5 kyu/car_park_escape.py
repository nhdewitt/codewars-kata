"""
Introduction
A multi-storey car park (also called a parking garage, parking structure, parking ramp, parkade, parking building, parking deck or indoor parking) is a building designed for car parking and where there are a number of floors or levels on which parking takes place. It is essentially an indoor, stacked car park. Parking structures may be heated if they are enclosed.

Design of parking structures can add considerable cost for planning new developments, and can be mandated by cities or states in new building parking requirements. Some cities such as London have abolished previously enacted minimum parking requirements (Source Wikipedia)

Task
Your task is to escape from the carpark using only the staircases provided to reach the exit. You may not jump over the edge of the levels (you’re not Superman!) and the exit is always on the far right of the ground floor.
Rules
1. You are passed the carpark data as an argument into the function.

2. Free carparking spaces are represented by a 0

3. Staircases are represented by a 1

4. Your parking place (start position) is represented by a 2 which could be on any floor.

5. The exit is always the far right element of the ground floor.

6. You must use the staircases to go down a level.

7. You will never start on a staircase.

8. The start level may be any level of the car park.

9. Each floor will have only one staircase apart from the ground floor which will not have any staircases.
Returns
Return an array of the quickest route out of the carpark

R1 = Move Right one parking space.

L1 = Move Left one parking space.

D1 = Move Down one level.
Example
Initialise
carpark = [[1, 0, 0, 0, 2],
           [0, 0, 0, 0, 0]]
Working Out
- You start in the most far right position on level 1
- You have to move Left 4 places to reach the staircase => "L4"
- You then go down one flight of stairs => "D1"
- To escape you have to move Right 4 places => "R4"
Result
result = ["L4", "D1", "R4"]
Good luck and enjoy!

https://www.codewars.com/kata/591eab1d192fe0435e000014/train/python
"""

def escape(carpark):
    if len(carpark) == 1 and carpark[0].index(2) == len(carpark[0]) - 1:
        return []
    sublist_idx = 0
    if carpark[0].count(2) == 0:
        for sublist in carpark:
            if 2 in sublist:
                break
            sublist_idx += 1
    if carpark[sublist_idx].count(1) == 1:
        first = carpark[sublist_idx].index(2) - carpark[sublist_idx].index(1)
    else:
        first = carpark[sublist_idx].index(2) - (len(carpark[sublist_idx]) - 1)
    exit = []
    if first > 0:
        exit.append(f"L{first}")
    else:
        exit.append(f"R{-first}")
    down = 0
    for i in range(sublist_idx + 1, len(carpark)):
        down += 1
        start = carpark[i - 1].index(1)
        if carpark[i].count(1) == 0:
            exit.append(f"D{down}")
            last = start - (len(carpark[i]) - 1)
            if last > 0:
                exit.append(f"L{last}")
            elif last < 0:
                exit.append(f"R{-last}")
            break
        if carpark[i].index(1) == start:
            continue
        else:
            exit.append(f"D{down}")
            down = 0
            level = start - carpark[i].index(1)
            if level > 0:
                exit.append(f"L{level}")
            else:
                exit.append(f"R{-level}")
    
    return exit