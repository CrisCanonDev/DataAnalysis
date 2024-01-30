#3.Searching substrings (Get wanted substring as parameter, except "replace" method)

string  = "Text12.22"
string.count("2") #Counts the number of occurences of a substring
string.find("w") #Finds index of the first occurence of a substring, or -1
string.rfind(substr) #Finds index of the last occurence of a substring, or -1
string.index(substr) #Like find, except ValueError is raised if not found
string.rindex(substr) #Like rfind, except ValueError is raised if not found
string.startswith(substr) #Returns True if string starts with a given substring
string.endswith(substr) #Returns True if string ends with a given substring
string.replace(substr, replacement) #Returns a string where occurences of