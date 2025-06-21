"""
Task
Raj has got into a problem, he solved the triangle pattern but stuck in the codes of "inverse triangle". Help him with the codes and remember to get the output as per given in examples below.

Rules:
Take input as n which is always a natural number
Space between each digit
No space after the rows end
Examples
If n = 5, output should be:

 1 1 1 1 1
  2 2 2 2
   3 3 3
    4 4
     5             
If n = 9, output should be:

 1 1 1 1 1 1 1 1 1
  2 2 2 2 2 2 2 2
   3 3 3 3 3 3 3
    4 4 4 4 4 4
     5 5 5 5 5
      6 6 6 6
       7 7 7
        8 8
         9
If n = 16, output should be:

 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
  2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
   3 3 3 3 3 3 3 3 3 3 3 3 3 3
    4 4 4 4 4 4 4 4 4 4 4 4 4
     5 5 5 5 5 5 5 5 5 5 5 5
      6 6 6 6 6 6 6 6 6 6 6
       7 7 7 7 7 7 7 7 7 7
        8 8 8 8 8 8 8 8 8
         9 9 9 9 9 9 9 9
          0 0 0 0 0 0 0
           1 1 1 1 1 1
            2 2 2 2 2
             3 3 3 3
              4 4 4
               5 5
                6
                
                
https://www.codewars.com/kata/564f3d49a06556d27c000077/train/python              
"""

def pattern(n):
    res = []
    num = 1
    level_iter = n
    
    for i in range(n):
        res.append(f"{' ' * num}{' '.join([str(num % 10)] * level_iter)}")
        num += 1
        level_iter -= 1
    
    return "\n".join(res)