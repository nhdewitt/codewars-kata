{-
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []


https://www.codewars.com/kata/5899dc03bc95b1bf1b0000ad/train/haskell
-}

module Kata (invert) where

invert :: [Integer] -> [Integer]
invert xs = [-x | x <- xs]