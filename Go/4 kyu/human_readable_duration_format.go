/*
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

https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/go
*/

package kata

import (
  "fmt"
  "strings"
)

const (
  year = 365 * 24 * 3600										// declare constants for the math below
  day = 24 * 3600
  hour = 3600
  min = 60
)

func DivMod(numerator, denominator int64) (int64, int64) {		// DivMod returns the quotient and remainder for an int64
  quotient := numerator / denominator
  remainder := numerator % denominator
  return quotient, remainder
}

func Pluralize(count int64, singular, plural string) string {	// return the singular or the plural based on the value count
  if count == 1 {
    return fmt.Sprintf("%d %s", count, singular)
  }
  return fmt.Sprintf("%d %s", count, plural)
}

func FormatDuration(seconds int64) string {						// work through the seconds, saving the remainder from each for the next calculation (last remainder is remaining seconds)
  y, r := DivMod(seconds, year)
  d, r := DivMod(r, day)
  h, r := DivMod(r, hour)
  m, s := DivMod(r, min)
  
  output := make([]string, 0, 5)								// max cap of 5 strings
  
  if y > 0 {
    output = append(output, Pluralize(y, "year", "years"))		// for each, append if it exists
  }
  if d > 0 {
    output = append(output, Pluralize(d, "day", "days"))
  }
  if h > 0 {
    output = append(output, Pluralize(h, "hour", "hours"))
  }
  if m > 0 {
    output = append(output, Pluralize(m, "minute", "minutes"))
  }
  if s > 0 {
    output = append(output, Pluralize(s, "second", "seconds"))
  }
  
  if len(output) == 1 {											// if there's only one element, we don't need to add anything
    return strings.Join(output, "")
  }
  if len(output) == 2 {											// if there are only two, there are no commas but just x and y
    return strings.Join(output, " and ")
  }
  commas := strings.Join(output[:len(output)-1], ", ")			// otherwise, take all but the last element and join with ", " then " and " and finally the last element
  return commas + " and " + output[len(output)-1]
}