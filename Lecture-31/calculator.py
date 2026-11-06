"""
you will have expressions in expression.in file 
ex: 
10 + 20 
2 ^ 3 
3 / 4 
operations: x , / , ^ , + , - 
write the result to result.out file 
ex: 
10 + 20 = 30 
2 ^ 3 = 8 
"""
def calculator(num1,op,num2): 
    match op: 
        case "+": 
            return num1 + num2 
        case "-": 
            return num1 - num2 
        case "x": 
            return num1 * num2 
        case "/": 
            if num2 == 0: 
                return "N/A"
            else: 
                return num1 / num2 
        case "^": 
            return num1 ** num2 
        
input_file_name = "Lecture-31/expression.in"
output_file_name = "Lecture-31/result.out"
output = [] 
with open(input_file_name,"r") as file: 
    # number op number \n 
    contents = file.readlines()
    for line in contents: 
        elements = line.split()
        # 0 -> num1 
        # 1 -> operator 
        # 2 -> num2 
        # 3 -> \n 
        num1 = float(elements[0])
        op = elements[1]
        num2 = float(elements[2])
        result = calculator(num1,op,num2)
        output.append(f"{num1} {op} {num2} = {result}\n")

with open(output_file_name,"w") as file: 
    file.writelines(output)
