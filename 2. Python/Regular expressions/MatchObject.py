# MATCH OBJECT
import re
# re. search
#     match       uses match objects to describe found occurence
#     finditer


# () groups into RE 
mo = re.search(r'\d+ (\d+) \d+ (\d+)',
'first 123 45 67 890 last')
print(mo) #Printing match object
print(mo.group(1)) #Printing and item of the array of matches

if mo: #treated as boolean value
    print()#do something
    
found = bool(mo) #Match object converted as boolean value