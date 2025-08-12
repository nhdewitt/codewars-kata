{-
Task Overview
Given a non-negative integer b, write a function which returns an integer d such that the binary representation of b is the same as the decimal representation of d.

Examples:

n = 1 should return 1
n = 5 should return 101
n = 11 should return 1011


https://www.codewars.com/kata/59fca81a5712f9fa4700159a/train/haskell
-}

module Binary where

decToBin :: Integer -> String
decToBin 0 = "0"
decToBin 1 = "1"
decToBin n = decToBin (n `div` 2) ++ show (n `mod` 2)

toBinary :: Integer -> Integer
toBinary x = read (decToBin x) :: Integer