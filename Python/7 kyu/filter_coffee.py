"""
You love coffee and want to know what beans you can afford to buy it.

The first argument to your search function will be a number which represents your budget.

The second argument will be an array of coffee bean prices.

Your 'search' function should return the stores that sell coffee within your budget.

The search function should return a string of prices for the coffees beans you can afford. The prices in this string are to be sorted in ascending order.

https://www.codewars.com/kata/56069d0c4af7f633910000d3/train/python
"""

def search(budget, prices):
    return ",".join(sorted([str(p) for p in prices if p <= budget], key=lambda x: float(x)))