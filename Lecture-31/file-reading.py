file_name = "Lecture-31/numbers.in"

with open(file_name,"r") as file: 
    contents = file.readlines() # return lines of a file as a list
    numbers = [] 
    for line in contents: 
        number = int(line.replace("\n",""))
        numbers.append(number)

    print(numbers)

# here you cannot access the file variable 