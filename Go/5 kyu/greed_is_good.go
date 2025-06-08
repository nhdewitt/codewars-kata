/*
Greed is a dice game played with five six-sided dice. Your mission, should you choose to accept it, is to score a throw according to these rules. You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
Each of 5 dice can only be counted once in each roll. For example, a given "5" can only count as part of a triplet (contributing to the 500 points) or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)

https://www.codewars.com/kata/5270d0d18625160ada0000e4/train/go
 */

package kata

func Score(dice [5]int) int {
  dieCount := make(map[int]int)			// tabulate each die roll
  var score int
  for _, die := range dice {
    dieCount[die]++
  }
  switch {								// start with the highest possible score going down
  case dieCount[1] >= 3:
    score += 1000
    dieCount[1] -= 3					// need to adjust 1s and 5s as any remainder will be added at the end
  case dieCount[6] >= 3:				// can ignore the other counts
    score += 600
  case dieCount[5] >= 3:
    score += 500
    dieCount[5] -= 3
  case dieCount[4] >= 3:
    score += 400
  case dieCount[3] >= 3:
    score += 300
  case dieCount[2] >= 3:
    score += 200
  }
  score += dieCount[1] * 100
  score += dieCount[5] * 50
  return score
}