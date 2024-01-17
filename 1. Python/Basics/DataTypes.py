                #Variables and Data Types
a= "Some text"
print(type(a))

b="ä".encode("utf-8")     # Convert character(s) to a sequence of bytes
print(b)                  # Prints bytes in hexadecimal notation
print(list(b))            # Prints bytes in decimal notation

                #Creating Strings
print("Five\tFour\nThree\tTwo\n") # \t tabulator \n newLine

s="""A string 
spanning over
several lines"""  # String containing newlines
print(s)

a= "First"
b= "Second"
print(a+b)
print(" ".join([a,b,b,a]))

print("\n%i plus %i is equal to %i" % (1, 3, 4))     # Format syntax
print("{} plus {} is equal to {}".format(1, 3, 4)) # Format method
print(f"{1} plus {3} is equal to {4}")             # f-string