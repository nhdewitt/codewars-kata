"""

https://exercism.org/tracks/python/exercises/say

"""

NUMBERS = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    15: "fifteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred"
}

def say(number):
    output = []
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    if number < 100:
        output.append(tens(number))
    elif number < 1000:
        output.append(hundreds(number))
    elif number < 1000000:
        output.append(thousands(number))
    elif number < 1000000000:
        output.append(millions(number))
    elif number < 1000000000000:
        output.append(billions(number))

    return " ".join(output)

def tens(number):
    if number < 14 or number == 15 or number % 10 == 0:
        return NUMBERS[number]
    if number == 14 or number < 20:
        return f"{NUMBERS[number % 10]}teen"
    return f"{NUMBERS[(number // 10) * 10]}-{NUMBERS[number % 10]}"

def hundreds(number):
    if number < 100:
        return tens(number)
    hund_output = []
    hund, ten = number // 100, number % 100
    
    if ten == 0:
        pass
    else:
        hund_output.append(tens(ten))
        
    hund_output.append(f"{tens(hund)} hundred")
    return " ".join(hund_output[::-1])

def thousands(number):
    thou_output = []
    thou, hund = number // 1000, number % 1000

    if hund == 0:
        pass
    else:
        thou_output.append(hundreds(hund))
        
    if thou < 10:
        thou_output.append(f"{tens(thou)} thousand")
    else:
        thou_output.append(f"{hundreds(thou)} thousand")

    return " ".join(thou_output[::-1])

def millions(number):
    mill_output = []
    mill, thou = number // 1000000, number % 1000000

    if thou == 0:
        pass
    else:
        mill_output.append(thousands(thou))

    if mill < 10:
        mill_output.append(f"{tens(mill)} million")
    else:
        mill_output.append(f"{hundreds(mill)} million")

    return " ".join(mill_output[::-1])

def billions(number):
    bill_output = []
    bill, mill = number // 1000000000, number % 1000000000

    if mill == 0:
        pass
    else:
        bill_output.append(millions(mill))

    if bill < 10:
        bill_output.append(f"{tens(bill)} billion")
    else:
        bill_output.append(f"{hundreds(bill)} billion")

    return " ".join(bill_output[::-1])