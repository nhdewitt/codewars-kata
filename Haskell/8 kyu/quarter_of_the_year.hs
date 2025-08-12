module Kata (quarterOf) where

quarterOf :: Int -> Int
quarter = [1,1,1,2,2,2,3,3,3,4,4,4]
quarterOf month = quarter !! (month - 1)