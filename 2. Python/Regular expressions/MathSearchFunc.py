import re

# Math.search > Allows to match any substring of a String
x = "back"
y = "a back"
z = "backbone"  
print(re.search(r'\bback\b', z)) #None
print(re.search(r'\bback\b', x)) #There is a match

xyz = "Doing stuff, going home, staying awake, sleeping later"
# re.search finds first occurence
# re.findall to find all occurences 

print( re.findall(r"\w+ing\b", xyz) )

#Find all integers from an string
print( re.findall(r"[+-]?\d+", "23 + -5 = 18") )

# re.findaiter() #Returns iterator whose item match an object

text= "She is going home and she has 4 cats"
print(re.sub(r"\b[sS]he\b", "he", text))
