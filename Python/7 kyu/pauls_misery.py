"""
Paul is an excellent coder and sits high on the CW leaderboard. He solves kata like a banshee but would also like to lead a normal life, with other activities. But he just can't stop solving all the kata!!

Given an array (x) you need to calculate the Paul Misery Score. The values are worth the following points:

kata = 5
Petes kata = 10
life = 0
eating = 1
The Misery Score is the total points gained from the array. Once you have the total, return as follows:

< 40 = 'Super happy!'
< 70 >= 40 = 'Happy!'
< 100 >= 70 = 'Sad!'
> 100 = 'Miserable!'

https://www.codewars.com/kata/57ee31c5e77282c24d000024/train/python
"""

def paul(x):
    misery = sum([5 if y == "kata" else 10 if y == "Petes kata" else 1 if y == "eating" else 0 for y in x])
    
    return "Super happy!" if misery < 40 else "Happy!" if misery < 70 else "Sad!" if misery < 100 else "Miserable!"    