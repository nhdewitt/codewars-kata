"""
When no more interesting kata can be resolved, I just choose to create the new kata, to solve their own, to enjoy the process --myjinxin2015 said

Description:
Give you an array arr that contains some numbers(arr.length>=2), and give you a positive integer k. Find such two numbers m,n: m and n at least a difference of k, and their index is the most distant.

Returns their distance of index. If no such number found, return -1.

Some Examples
furthestDistance([8,7,1,9],5) === 2

The difference of 8 and 1, 1 and 9 is more than 5;
The index distance of (8,1) is 2;
The index distance of (1,9) is 1;
So 2 is the furthest distance of index.

furthestDistance([8,7,1,9],100) === -1
furthestDistance([1,2,3,4],1) === 3 (1 and 4)
furthestDistance([3,4,1,2],2) === 2 (3 and 1 or 4 and 2)

https://www.codewars.com/kata/581963edc929ba19e7000148/train/python
"""

def furthest_distance(arr, k):
    distance = 0
    for i in range(len(arr)):                       # starting at 0, iterate through remainder of list
        for j, _ in enumerate(arr[i+1:], i+1):      # enumerate to retain indices
            if abs(arr[i] - arr[j]) >= k:           # abs of difference between elements >= k then
                if abs(i - j) > distance:           # if this is larger than the largest distance so far
                    distance = abs(i - j)           # new distance is the distance between the two indices
    return distance if distance else -1             # if distance never changed, nothing is found, return -1