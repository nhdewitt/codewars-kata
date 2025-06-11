"""
Taking into consideration the 3.5 edition rules, your goal is to build a function that takes an ability score (worry not about validation: it is always going to be a non negative integer), will return:

attribute modifier, as indicated on the table of the above link;
maximum spell level for the spells you can cast (-1 for no spells at all) with that score;
the eventual extra spells you might get (as an array/list, with elements representing extra spells for 1st, 2nd,... spell level in order; empty array for no extra spells).
The result needs to be an object (associative array in PHP), as shown in the examples:

char_attribute(0) == {"modifier": 0, "maximum_spell_level": -1, "extra_spells": []}
char_attribute(1) == {"modifier": -5, "maximum_spell_level": -1, "extra_spells": []}
char_attribute(5) == {"modifier": -3, "maximum_spell_level": -1, "extra_spells": []}
char_attribute(10) == {"modifier": 0, "maximum_spell_level": 0, "extra_spells": []}
char_attribute(20) == {"modifier": +5, "maximum_spell_level": 9, "extra_spells": [2,1,1,1,1]}
Note: I didn't explain things in detail and just pointed out to the table on purpose, as my goal is also to train the pattern recognition skills of whoever is going to take this challenges, so do not complain about a summary description. Thanks :)

https://www.codewars.com/kata/596a690510ffee5c0b00006a/train/python
"""

def char_attribute(score):
    modifier = (score - 10) // 2 if score else 0
    if score - 10 > 9:
        max_spell_level = 9
    elif score - 10 < -1:
        max_spell_level = -1
    else:
        max_spell_level = score - 10
    extra_spells = []
    
    for spell_level in range(1, 10):
        if modifier >= spell_level:
            bonus = (modifier - spell_level + 4) // 4
            bonus = max(0, bonus)
            extra_spells.append(bonus)
        else:
            break
    
    return {
        "modifier": modifier,
        "maximum_spell_level": max_spell_level,
        "extra_spells": extra_spells,
    }