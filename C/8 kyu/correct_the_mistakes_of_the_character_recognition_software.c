/*
Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

S is misinterpreted as 5
O is misinterpreted as 0
I is misinterpreted as 1
The test cases contain numbers only by mistake.

https://www.codewars.com/kata/577bd026df78c19bca0002c0/train/c
*/

#include <string.h>

char *correct(char *string) {
  int length = strlen(string);
  
  for (int i = 0; i < length; i++) {
    switch (string[i]) {
    case '5':
        string[i] = 'S';
        break;
    case '0':
        string[i] = 'O';
        break;
    case '1':
        string[i] = 'I';
        break;
    }
  }
  return string;
}