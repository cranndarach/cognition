-- Function to relate counting numbers to integers to prove the viability of
-- integers as a countable infinity.

integerMap :: Int -> Int
-- integerMap n = (-1 * ((n `mod` 2) + 1)) * (n - (n `mod` 2)) `div` 2
integerMap n = (n - n `mod` 2) * (-1)^(n `mod` 2) `div` 2
