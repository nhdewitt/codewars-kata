/*
Create a parser to interpret and execute the Deadfish language.

Deadfish operates on a single value in memory, which is initially set to 0.

It uses four single-character commands:

i: Increment the value
d: Decrement the value
s: Square the value
o: Output the value to a result array
All other instructions are no-ops and have no effect.

Examples
Program "iiisdoso" should return numbers [8, 64].
Program "iiisdosodddddiso" should return numbers [8, 64, 3600].

https://www.codewars.com/kata/51e0007c1f9378fa810002a9/train/go
*/

package kata

func Parse(data string) []int{
  memory := 0
  output := []int{}
  
  for _, r := range data {
    switch (r) {
      case 'i':
      memory++
      case 'd':
      memory--
      case 's':
      memory *= memory
      case 'o':
      output = append(output, memory)
      default:
      continue
    }
  }
  return output
}