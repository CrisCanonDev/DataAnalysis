#String handling
# Methods for strings. Strings are inmmutable in python
# String methods works with return value

s="text One"

# 1.String classifications (Returns truth values)
s.isalnum() # True if all characters are letters or digits
s.isalpha() #True if all characters are letters
s.isdigit() #True if all characters are digits
s.islower() #True if contains letters, and all are lowercase
s.isupper() #True if contains letters, and all are uppercase
s.isspace() #True if all characters are whitespace
s.istitle() #True if uppercase in the beginning of word, elsewhere lowercase
