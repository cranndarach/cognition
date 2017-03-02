-- A Haskell script for determining whether a number is prime, following
-- the discussion in class about modularity. Like the Python script, this
-- also divides the problem into smaller functions. Notice that the functional
-- style of Haskell allows for coding special cases directly without having
-- to use a separate function or if...elif statements. It also recognizes 0
-- as not being prime without hard-coding it. To do this in Python risks a
-- stack overflow.

biggestPossibleFactor :: Int -> Int
biggestPossibleFactor num = num `div` 2

evenlyDivides :: Int -> Int -> Bool
evenlyDivides a b
    | a `mod` b == 0 = True
    | otherwise      = False

isPrime :: Int -> Bool
isPrime 1 = False
isPrime 2 = True
isPrime x = checkFactors x 2

checkFactors :: Int -> Int -> Bool
checkFactors a b
    | evenlyDivides a b            = False
    | b >= biggestPossibleFactor a = True
    | otherwise                    = checkFactors a $ b + 1
