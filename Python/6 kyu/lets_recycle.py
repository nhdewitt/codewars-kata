"""
Task
You will be given a list of objects. Each object has type, material, and possibly secondMaterial. The existing materials are: paper, glass, organic, and plastic.

Your job is to sort these objects across the 4 recycling bins according to their material (and secondMaterial if it's present), by listing the type's of objects that should go into those bins.

Notes
The bins should come in the same order as the materials listed above
All bins should be listed in the output, even if some of them are empty
If an object is made of two materials, its type should be listed in both of the respective bins
The order of the type's in each bin should be the same as the order of their respective objects was in the input list
Contrary to the example below, the output in Python should be a tuple of 4 lists instead of a 2-dimensional list
Example
input = [
  {"type": "rotten apples", "material": "organic"},
  {"type": "out of date yogurt", "material": "organic", "secondMaterial": "plastic"},
  {"type": "wine bottle", "material": "glass", "secondMaterial": "paper"},
  {"type": "amazon box", "material": "paper"},
  {"type": "beer bottle", "material": "glass", "secondMaterial": "paper"}
]

output = [
  ["wine bottle", "amazon box", "beer bottle"],
  ["wine bottle", "beer bottle"],
  ["rotten apples", "out of date yogurt"],
  ["out of date yogurt"]
]

https://www.codewars.com/kata/5b6db1acb118141f6b000060/train/python
"""

def recycle(a):
    paper, glass, organic, plastic = [], [], [], []                     # outputs for each material
    recycling_bins = {                                                  # map each material from dictionary to the previous lists
        "paper": paper,
        "glass": glass,
        "organic": organic,
        "plastic": plastic
    }
    
    for el in a:
        i = el["type"]                                                  # type = item to be added
        for m in (el.get("material"), el.get("secondMaterial")):        # add to the first list (material) and, if present, the second list
            if m in recycling_bins:
                recycling_bins[m].append(i)
    
    return (paper, glass, organic, plastic)                             # return as tuple of lists