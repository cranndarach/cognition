applesAndOranges :: (String, String) -> Bool
applesAndOranges ("apples", _) = True
applesAndOranges (_, "oranges") = True
applesAndOranges _ = False
