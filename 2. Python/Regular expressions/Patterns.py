#Patters -> Set of strings that save some commonality (Regular structure)
import re
# Regular expressions (RE) 

# . Matches any character
# [...] Matches any character contained within the brackets
# [^...] Matches any character not appearing after the hat (ˆ)
# ˆ Matches the start of the string
# $ Matches the end of the string
# * Matches zero or more previous RE
# + Matches one or more previous RE
# {m,n} Matches m to n occurences of previous RE
# ? Matches zero or one occurences of previous RE

Str = "Get ready"
print(re.match(r"Get (on|off|ready)", Str)) #Matches following strings: "Get on", "Get off", "Get ready"

    # () Create groupings inside a pattern: r"(ab)+" {"ab", "abab", "ababab" and so on}

#Backreference  \number : to the first capturing group, ensuring that the same word is repeated.


# `\d` same as `[0-9]`, matches a digit
# `\D` same as `[ˆ0-9]`, matches anything but a digit
# `\s` matches a whitespace character (space, newline, tab, ... )
# `\S` matches a nonwhitespace character
# `\w` same as `[a-zA-Z0-9_]`, matches one alphanumeric character
# `\W` matches one non-alphanumeric character


# Using the above notation we can now shorten our previous variable name example to r’[a-zA-Z_]\w*\Z’ same as r"[A-Za-z_][A-Za-z_0-9]*\Z"


# \A \Z Recognize beggining/end of string
# ^ $ Match after newline and before newline
# /b cheeck if there is more characters at the beggining/end of string



