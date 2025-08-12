module Pillars where

pillars :: Int -> Int -> Int -> Int
pillars n d w = if n <= 1
                  then 0
                  else (n - 1) * (d * 100) + (n - 2) * w