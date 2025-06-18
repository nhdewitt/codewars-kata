/*
Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.

Your function also receives a third argument, a string, with the name of the fighter that attacks first.

Example:
  declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew") => "Lew"
  
  Lew attacks Harry; Harry now has 3 health.
  Harry attacks Lew; Lew now has 6 health.
  Lew attacks Harry; Harry now has 1 health.
  Harry attacks Lew; Lew now has 2 health.
  Lew attacks Harry: Harry now has -1 health and is dead. Lew wins.
type Fighter struct {
    Name            string
    Health          int
    DamagePerAttack int
}

https://www.codewars.com/kata/577bd8d4ae2807c64b00045b/train/go
*/

package kata

import (
  "strings"
  "fmt"
)

func StillAlive(f Fighter) bool {
  return f.Health > 0
}

func DeclareWinner(fighter1 Fighter, fighter2 Fighter, firstAttacker string) string {
  var sb strings.Builder
  if firstAttacker != fighter1.Name {
    fighter1, fighter2 = fighter2, fighter1
  }
  for {
    fighter2.Health -= fighter1.DamagePerAttack
    fmt.Fprintf(&sb, "%s attacks %s; %s now has ", fighter1.Name, fighter2.Name, fighter2.Name)
    if !StillAlive(fighter2) {
      fmt.Fprintf(&sb, "%d health and is dead. %s wins.", fighter2.Health, fighter2.Name)
      fmt.Println(sb.String())
      sb.Reset()
      break
    } else {
      fmt.Fprintf(&sb, "%d health.", fighter2.Health)
      fmt.Println(sb.String())
      sb.Reset()
    }
    fighter1, fighter2 = fighter2, fighter1
  }
  return fighter1.Name
}