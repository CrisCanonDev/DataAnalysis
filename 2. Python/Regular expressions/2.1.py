import re
def integer_in_brackets(lst):
    matches = re.findall(r"\[ *([+-]?\d+) *\]", lst)
    return [int(match) for match in matches]
               
      
def main():
    input = "afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx"
    print(integer_in_brackets(input))
    
if __name__ == "__main__":
    main()