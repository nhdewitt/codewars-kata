"""
You are given a node that is the beginning of a linked list. This list contains a dangling piece and a loop. Your objective is to determine the length of the loop.

For example in the following picture the size of the dangling piece is 3 and the loop size is 12:


# Use the `next' attribute to get the following node
node.next
Notes:

do NOT mutate the nodes!
in some cases there may be only a loop, with no dangling piece
Thanks to shadchnev, I broke all of the methods from the Hash class.

Don't miss dmitry's article in the discussion after you pass the Kata !! 

https://www.codewars.com/kata/52a89c2ea8ddc5547a000863/train/python
"""

def loop_size(node):
    slow = node
    fast = node
    while True:
        if not (fast and fast.next):
            return None
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    fast = node
    while fast is not slow:
        fast = fast.next
        slow = slow.next
    count = 0
    seen = set()
    while fast not in seen:
        count += 1
        seen.add(fast)
        fast = fast.next
    return count