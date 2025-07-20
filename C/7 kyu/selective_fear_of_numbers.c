/*
I've got a crazy mental illness. I dislike numbers a lot. But it's a little complicated: The number I'm afraid of depends on which day of the week it is... This is a concrete description of my mental illness:

Monday --> 12

Tuesday --> numbers greater than 95

Wednesday --> 34

Thursday --> 0

Friday --> numbers divisible by 2

Saturday --> 56

Sunday --> 666 or -666

Write a function which takes a string (day of the week) and an integer (number to be tested) so it tells the doctor if I'm afraid or not. (return a boolean)

https://www.codewars.com/kata/55b1fd84a24ad00b32000075/train/c
*/

#include <stdbool.h>
#include <string.h>

enum days { 
  MONDAY,
  TUESDAY,
  WEDNESDAY,
  THURSDAY,
  FRIDAY,
  SATURDAY,
  SUNDAY,};

enum days check(const char *s) {
  if      (strcmp(s, "Monday")    == 0)     return MONDAY;
  else if (strcmp(s, "Tuesday")   == 0)     return TUESDAY;
  else if (strcmp(s, "Wednesday") == 0)     return WEDNESDAY;
  else if (strcmp(s, "Thursday")  == 0)     return THURSDAY;
  else if (strcmp(s, "Friday")    == 0)     return FRIDAY;
  else if (strcmp(s, "Saturday")  == 0)     return SATURDAY;
  else if (strcmp(s, "Sunday")    == 0)     return SUNDAY;
}

bool am_i_afraid(const char *day, int num)
{
  switch (check(day)) {
      case MONDAY:    return (num      ==  12) ? true : false;
      case TUESDAY:   return (num       >  95) ? true : false;
      case WEDNESDAY: return (num      ==  34) ? true : false;
      case THURSDAY:  return (num      ==   0) ? true : false;
      case FRIDAY:    return (num % 2  ==   0) ? true : false;
      case SATURDAY:  return (num      ==  56) ? true : false;
      case SUNDAY:    return (abs(num) == 666) ? true : false;
  }
}