import re, os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, 'src/listing.txt')

def file_listing():
    with open (file_path, "r") as f:
        for line in f:
            
            size = r"[0-9]{5}"
            sizeRe = re.search(size,line).group()
                      
            month = r"[A-Z]\w{2}"
            monthRe= re.search(month, line).group()
            
            dayHourMin = r"[0-9]{1,2}\s+[0-9]{1,2}:[0-9]{1,2}"
            dayHourMin = re.search(dayHourMin, line).group()
            dayHourSplit = dayHourMin.split()
            day = dayHourSplit[0]
            time = dayHourSplit[1]
            
            dayHourMinRE = re.findall(dayHourMin, line)
            print(dayHourMinRE)
            
            filename = r"\w*\.\w{3}"
            filenameRe = re.search(filename, line).group()
            
            
            return (int(sizeRe), str(monthRe), int(day), int(time.split(":")[0]), int(time.split(":")[1]), str(filenameRe))
    
print(file_listing())