# STANDARD FILE OBJECTS

import sys
import random
i= random.randint(-10,10)

if i >=0:
    sys.stdout.write("Got a positive integer.\n")
else:
    sys.stdout.write("Got a negative     integer.\n")
    
sys.path #folders that python uses to look for imported modules.
sys.argv[0] #name of program
sys.argv[1] #commmand line parameters =="param1"
sys.argv[2] #"param2"

sys.exit #exit immediately of the program.
