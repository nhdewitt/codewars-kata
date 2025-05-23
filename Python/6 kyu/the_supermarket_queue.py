"""
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total time required for all the customers to check out!

input
customers: an array of positive integers representing the queue. Each integer represents a customer, and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.
output
The function should return an integer, the total time required.

Important
Please look at the examples and clarifications below, to ensure you understand the task correctly :)

Examples
queue_time([5,3,4], 1)
# should return 12
# because when n=1, the total time is just the sum of the times

queue_time([10,2,3,3], 2)
# should return 10
# because here n=2 and the 2nd, 3rd, and 4th people in the 
# queue finish before the 1st person has finished.

queue_time([2,3,10], 2)
# should return 12
Clarifications
There is only ONE queue serving many tills, and
The order of the queue NEVER changes, and
The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes free.
N.B. You should assume that all the test input will be valid, as specified above.

P.S. The situation in this kata can be likened to the more-computer-science-related idea of a thread pool, with relation to running multiple processes at the same time: https://en.wikipedia.org/wiki/Thread_pool

https://www.codewars.com/kata/57b06f90e298a7b53d000a86/train/python
"""

def queue_time(customers, n):
    if customers == []: return 0
    if len(customers) <= n: return max(customers)
    if n == 1: return sum(customers)
    decrement_list = lambda x, y: x - y
    result = []
    i = 0
    next_i = n                                                      # slice starting at [0:n] for the initial queue of n registers
    queue = customers[i:next_i]
    while next_i < len(customers):
        next_free = min(queue)
        result.append(next_free)                                    # shortest time will add to the overall total time
        queue = list(decrement_list(q, next_free) for q in queue)   # decrement the remaining queue times 
        queue = list(q for q in queue if q != 0)                    # remove all zeroes to free up the tills
        i, next_i = next_i, next_i + (n - len(queue))               # shift the slice to the next customers
        queue.extend(customers[i:next_i])
    result.append(max(queue))                                       # when all customers are using the tills, the final time will increase by the longest customer
    return sum(result)