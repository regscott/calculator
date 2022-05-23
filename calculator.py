type_of_operation =int(input("Which operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n"))
if type_of_operation > 0 and type_of_operation < 5:
    first_operand = int(input("First operator: ")) 
    second_operand = int(input("Second operator: "))
result = 0
if type_of_operation == 1:
    result = first_operand + second_operand   
elif type_of_operation == 2:
    result = first_operand - second_operand   
elif type_of_operation == 3:
    result = first_operand * second_operand   
elif type_of_operation == 4:
    result = first_operand / second_operand
if type_of_operation > 0 and type_of_operation < 5:
    print("Result: " + str(result))
else: 
    print("Invaild input")