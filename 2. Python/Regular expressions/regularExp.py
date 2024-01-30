#Regular expression
import re
# Seen previously

# If like to know whether  'Apple' 'apple', should call starswith method twice
s ="apple"
print(s.startswith("Apple")) #FALSE
print(s.startswith("apple")) #TRUE

# Regular expressions: Offers single solution
re.match(r"[aA]pple", s)
    # [] Special syntax of regular expression
    # [Aa] 
    # "pple" acts normally
    # r"[Aa]pple" is called pattern

re.match(r"[Aa]pple|[Bb]anana", str)
    # |  denotes as alternative
    
# Legal variable starts letter, underline character _hidden, L_33
# Expression to recognize legal variables name
re.match(r"[A-Za-z_][A-Za-z_0-9]*\Z", str)
    # A-Z range from A to Z
    # [A-Za-z_] First character of variable
    # [A-Za-z_0-9] Subsequent characters of variable
    # * allow any number of previous subpatterns
    #   - r"ba*" allows strings "b", "ba", "baa", "baaa" and so on
    # \Z denotes ends of string
    
    
# raw strings - r"ab*\Z" 
    # \n \t are not interpreted

    
    
    
    
    
    
    