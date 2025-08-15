{-
The objective of Duck, duck, goose is to walk in a circle, tapping on each player's head until one is chosen.

Task:

Given a list of Players and a position (first position is 1), return the name of the chosen Player.

newtype Player = Player {name :: String} deriving (Show, Eq)
Example:

duckDuckGoose [a, b, c, d] 1 == name a
duckDuckGoose [a, b, c, d] 5 == name a
duckDuckGoose [a, b, c, d] 4 == name d
Random input limits:

6
≤
Players
≤
50
6≤Players≤50
5000
≤
Position
≤
50000
5000≤Position≤50000


https://www.codewars.com/kata/582e0e592029ea10530009ce/train/haskell
-}

module DuckDuckGoose where

import Preloaded (Player(name))
-- newtype Player = Player {name :: String} deriving (Show, Eq)

duckDuckGoose :: [Player] -> Int -> String
duckDuckGoose players goose = name (players !! idx)
  where
    n   = length players
    idx = (goose - 1) `mod` n