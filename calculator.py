print('1 - Addition')
print('2 - Subtraction')
print('3 - Multiply')
print('4 - Divide')

option = int(input("Choose an operation: "))

if option in [1, 2, 3, 4]:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if option == 1:
        result = num1 + num2
    elif option == 2:
        result = num1 - num2
    elif option == 3:
        result = num1 * num2
    elif option == 4:
        result = num1 // num2  

    print("Result:", result)
else:
    print("Invalid operation entered.")