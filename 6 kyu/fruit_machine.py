"""
Introduction
Slot machine (American English), informally fruit machine (British English), puggy (Scottish English slang), the slots (Canadian and American English), poker machine (or pokies in slang) (Australian English and New Zealand English) or simply slot (American English), is a casino gambling machine with three or more reels which spin when a button is pushed. Slot machines are also known as one-armed bandits because they were originally operated by one lever on the side of the machine as distinct from a button on the front panel, and because of their ability to leave the player in debt and impoverished. Many modern machines are still equipped with a legacy lever in addition to the button. (Source Wikipedia)

Task
You will be given three reels of different images and told at which index the reels stop. From this information your job is to return the score of the resulted reels.
Rules
1. There are always exactly three reels

2. Each reel has 10 different items.

3. The three reel inputs may be different.

4. The spin array represents the index of where the reels finish.

5. The three spin inputs may be different

6. Three of the same is worth more than two of the same

7. Two of the same plus one "Wild" is double the score.

8. No matching items returns 0.
Scoring
Item
Three of the same
Two of the same
Two of the same plus one Wild
Wild
100
10
N/A
Star
90
9
18
Bell
80
8
16
Shell
70
7
14
Seven
60
6
12
Cherry
50
5
10
Bar
40
4
8
King
30
3
6
Queen
20
2
4
Jack
10
1
2
 

Returns
Return an integer of the score.
Example
Initialise
reel1 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel2 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
reel3 = ["Wild","Star","Bell","Shell","Seven","Cherry","Bar","King","Queen","Jack"]
spin = [5,5,5]
result = fruit([reel1,reel2,reel3],spin)
Scoring
reel1[5] == "Cherry"
reel2[5] == "Cherry"
reel3[5] == "Cherry"

Cherry + Cherry + Cherry == 50
Return
result == 50
Good luck and enjoy!

https://www.codewars.com/kata/590adadea658017d90000039/train/python
"""

def fruit(reels, spins):
    values = {
        "Wild": 10,
        "Star": 9,
        "Bell": 8,
        "Shell": 7,
        "Seven": 6,
        "Cherry": 5,
        "Bar": 4,
        "King": 3,
        "Queen": 2,
        "Jack": 1
    }
    result = [reels[i][spins[i]] for i in range(3)]                                     # grab each spin result and put into a list
    if len(set(result)) == 1:                                                           # if set len=1, all three are the same, return value * 10
        return values[result[0]] * 10
    if len(set(result)) == 2:                                                           # if set len=2, two match, check for Wild
        if "Wild" in result and result.count("Wild") == 1:
            return values[sorted(result)[0]] * 2                                        # 1 wild, sorted, "Wild" will be at the end, grab [0] to get the matching pair, multiply by 2
        if "Wild" in result and result.count("Wild") == 2:
            return values["Wild"]                                                       # 2 wild, return Wild value
        return values[[item for item in set(result) if result.count(item) == 2][0]]     # no wild, find the matching pair and return the value
    return 0                                                                            # if set len=3, no match, return 0