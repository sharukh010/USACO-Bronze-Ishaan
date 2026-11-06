file_name = "Lecture-31/greetings.out"

# write mode will delete existing data in the file and writes the data freshly 
# with open(file_name,"w") as file: 
#     name = input("Name: ")
#     greeting = f"Hi, {name}"
#     file.writelines([greeting])

with open(file_name,"a") as file: 
    name = input("Name: ")
    greeting = f"Hi, {name}"
    # file.write(greeting)
    print(greeting,file=file)
