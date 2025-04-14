"""
Unscramble the eggs.

The string given to your function has had an "egg" inserted directly after each consonant. You need to return the string before it became eggcoded.

Example
unscrambleEggs("Beggegeggineggneggeregg"); => "Beginner"
//             "B---eg---in---n---er---"
Kata is supposed to be for beginners to practice regular expressions, so commenting would be appreciated.

https://www.codewars.com/kata/55ea5650fe9247a2ea0000a7/train/python
"""

def unscramble_eggs(word):
    unscrambled = ""
    i = 0
    while i < len(word):
        unscrambled += word[i]
        if word[i].lower() in "aeiou" or word[i] == " ":
            if i == len(word) - 1:
                break
            i += 1
        else:
            i += 4
    return unscrambled