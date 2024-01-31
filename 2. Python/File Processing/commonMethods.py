import os


script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'names.txt')

max_val=0 
with open(file_path, "r") as f: #Closes file automatically
    # for i in range(4):
    #     lin = f.readline()
    #     print(f"Line {i}: {lin}", end="")

    for line in f:
        if len(line) > max_val:
            max_val = len(line)
print(f"Longest file has {max_val}")

