"""
It's a Pokemon battle! Your task is to calculate the damage that a particular move would do using the following formula (not the actual one from the game):

damage = 50 * (attack / defense) * effectiveness
Where:

attack = your attack power
defense = the opponent's defense
effectiveness = the effectiveness of the attack based on the matchup (see explanation below)
Effectiveness:

Attacks can be super effective, neutral, or not very effective depending on the matchup. For example, water would be super effective against fire, but not very effective against grass.

Super effective: 2x damage
Neutral: 1x damage
Not very effective: 0.5x damage
To prevent this kata from being tedious, you'll only be dealing with four types: fire, water, grass, and electric. Here is the effectiveness of each matchup:

fire > grass

fire < water

fire = electric

water < grass

water < electric

grass = electric

For this kata, any type against itself is not very effective. Also, assume that the relationships between different types are symmetric (if A is super effective against B, then B is not very effective against A).

The function you must implement takes in:

your type
the opponent's type
your attack power
the opponent's defense

https://www.codewars.com/kata/536e9a7973130a06eb000e9f/train/python
"""

def calculate_damage(your_type, opponent_type, attack, defense):
    damage_dict = {                                                         # 1 - super effective (2x)
        "fire": {"grass": 1, "water": -1, "electric": 0, "fire": -1},       # 0 - neutral (1x)
        "water": {"fire": 1, "grass": -1, "electric": -1, "water": -1},     #-1 - not very effective (0.5x)
        "grass": {"fire": -1, "water": 1, "electric": 0, "grass": -1},
        "electric": {"fire": 0, "water": 1, "grass": 0, "electric": -1},
    }
    
    mod_check = damage_dict[your_type][opponent_type]
    
    if mod_check == 1:
        modifier = 2.0
    elif mod_check == -1:
        modifier = 0.5
    else:
        modifier = 1.0
        
    return 50 * (attack / defense) * modifier