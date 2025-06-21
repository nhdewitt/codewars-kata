/*
Introduction
You might know the popular app "Tinder", which can be used to find nice people, which fit to you. The core functionality of it is to show you profiles of people and you can decide to either swipe left to dismiss the chance to get to know the person or to swipe right, if the profile sounds promising.

In this kata we want to build something similar to find programmer profiles, which fit to us :)

Task
You are given one person's profile and two callbacks: one to swipe to the left and another one to swipe to the right. If the person mentions your favorite programming language in their bio, then you want to give your friendship a chance and swipe to the right. Otherwise you swipe to the left.

Note: Your favorite programming language is assumed to be the one, you're solving this kata in. So if you're solving this kata in Javascript, you should look out for JavaScript in the profile text. See the examples matching and non-matching profiles.

Profile Structure
Each profile has the following fields:

name (string)
age (int)
bio (string)
Examples
Swipe Right
profile := Profile{
    Name: "Julia Green",
    Age: 24,
    Bio: "From Chile. Sushi lover 🍣 Learning Go on codewars.com. Always be yourself. Unless you can be a unicorn, then always be a unicorn 🦄",
}

RateProfile(profile, swipeLeft, swipeRight);
// should call swipeRight(), as Go is mentioned in the bio
Swipe Left
profile := Profile{
    Name: "Peter Parker",
    Age: 31,
    Bio: "Huge soccer fan ⚽️ Living in Dallas. Java = ❤️",
}

RateProfile(profile, swipeLeft, swipeRight);
// should call swipeLeft(), as Go is not mentioned in the bio

https://www.codewars.com/kata/62c68f0920d291001737fa22/train/go
*/

package kata

import "strings"

func RateProfile(profile Profile, swipeLeft func(), swipeRight func()) {
  if strings.Contains(profile.Bio, "Go") {
    swipeRight()
  } else {
    swipeLeft()
  }
}