"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return 
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python
"""

def format_duration(seconds):
    if seconds == 0: return "now"
    
    YEAR = 365 * 24 * 3600
    DAY = 24 * 3600
    HOUR = 3600
    MIN = 60
    
    y, r = divmod(seconds, YEAR)
    d, r = divmod(r, DAY)
    h, r = divmod(r, HOUR)
    m, s = divmod(r, MIN)
    
    output = []                                                 # grammar checks
    if y > 0:
        output.append(f"{y} year{'s' if y > 1 else ''}")
    if d > 0:
        output.append(f"{d} day{'s' if d > 1 else ''}")
    if h > 0:
        output.append(f"{h} hour{'s' if h > 1 else ''}")
    if m > 0:
        output.append(f"{m} minute{'s' if m > 1 else ''}")
    if s > 0:
        output.append(f"{s} second{'s' if s > 1 else ''}")
    
    if len(output) == 1:                                        # comma checks, none needed if len <= 2, needed up to the last element if > 2 (and last element is separated by an and)
        return "".join(output)
    if len(output) == 2:
        return " and ".join(output)
    else:
        commas = ", ".join(output[:len(output)-1])
        return commas + " and " + output[-1]