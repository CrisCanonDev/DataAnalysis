import re
# If pattern used in many functions calls > wise to precompile patterns for efficiency reasons

    # # compile(pattern, flags=0) > Returns RE object
    # flags -> Optional. Given inside patterns or as parameter    
    #     (?.) re.IGNORECASE makes lower and upper appears as equal
    #     (?m) re.MULTILINE makes ^ and $ match the beggining and end of each line.
    #     (?s) RE DOTALL makes character class .(dot) accept the newline character.
        # Elements on the left placed preferrably in the beggining
