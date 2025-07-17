"""
Baby Shark Lyrics
baby shark

Create a function, as short as possible, that returns this lyrics.
Your code should be less than 300 characters. Watch out for the three points at the end of the song.

Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt!
Run away,…
Good Luck!

https://www.codewars.com/kata/5d076515e102162ac0dc514e/train/python
"""

def baby_shark_lyrics():
    o=""
    f="Baby Mommy Daddy Grandma Grandpa Let's go".split()
    for x in f[:5]:
        o+=(x+" shark,"+" doo"*6+"\n")*3+x+" shark!\n"
    o+=(f[5]+" "+f[6]+" hunt,"+" doo"*6+"\n")*3+f[5]+" "+f[6]+" hunt!\nRun away,…"
    return o