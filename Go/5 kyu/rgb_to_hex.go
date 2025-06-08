/*
The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"

https://www.codewars.com/kata/513e08acc600c94f01000001/train/go
*/

package kata

import "fmt"

func ValidateRGB(v *int) {
  if *v < 0 {
    *v = 0
  } else if *v > 255 {
    *v = 255
  }
}

func RGB(r, g, b int) string {
  ValidateRGB(&r)								// make sure each argument is > 0 and < 255
  ValidateRGB(&g)
  ValidateRGB(&b)
  
  return fmt.Sprintf("%02X%02X%02X", r, g, b)	// return as hex, padded with a zero
}