/*
Baby Shark Lyrics
baby shark

Create a function, as short as possible, that returns this lyrics.
Your code should be less than 300 characters. Watch out for the three points at the end of the song.

Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt!
Run away,…
Good Luck!

Haskell and Go: A trailing newline \n is expected in the result.

https://www.codewars.com/kata/5d076515e102162ac0dc514e/train/go
*/

package kata;import s"strings";func BabySharkLyrics()string{r:="";for _,v:=range s.Fields("Baby Mommy Daddy Grandma Grandpa"){r+=s.Repeat(v+" shark, "+s.Repeat("doo ",5)+"doo\n",3)+v+" shark!\n"};r+=s.Repeat("Let's go hunt, "+s.Repeat("doo ", 5)+"doo\n",3)+"Let's go hunt!\nRun away,…\n";return r}