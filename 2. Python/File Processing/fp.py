# File open with open function -> Return file object of type file

# # r: Read only mode, file must exist
# # w: Write-only mode, create, overwrite an existing file
# # a: Write-only mode, appends to the end
# # r+: read/write mode, file must exist
# # w+: read/write mode, creates, overwrite an existing file
# # a+: read/write mode, append to end


# # t text mode
# # b binary mode (Contents are not interpretated in any way)
# #     read and wirte methods handle bytes
# #     byte = 8 bits (range 0-255)
    
    
#FILE OBJECT methods
read(size)  
write(String)
readline() 
readlines() 
writelines()
flush()# make sure if changes made to a file are written to disk immediately