"""
Being a bald man myself, I know the feeling of needing to keep it clean shaven. Nothing worse that a stray hair waving in the wind.

You will be given a string(x). Clean shaved head is shown as "-" and stray hairs are shown as "/". Your task is to check the head for stray hairs and get rid of them.

You should return the original string, but with any stray hairs removed. Keep count ot them though, as there is a second element you need to return:

0 hairs --> "Clean!"
1 hair --> "Unicorn!"
2 hairs --> "Homer!"
3-5 hairs --> "Careless!"
>5 hairs --> "Hobo!"

So for this head: "------/------" you shoud return:

["-------------", "Unicorn"]

https://www.codewars.com/kata/57efab9acba9daa4d1000b30/train/python
"""

def bald(s):
    output = {
        0: "Clean!",
        1: "Unicorn!",
        2: "Homer!",
        3: "Careless!",
        4: "Careless!",
        5: "Careless!"
    }
    
    return [s.replace("/","-"), output.get(s.count("/"), "Hobo!")]