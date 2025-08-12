module GravityFlip (gravityFlip) where

import Data.List (sort)

gravityFlip :: Char -> [Int] -> [Int]
gravityFlip c a = if c == 'R' then sort a else reverse (sort a)