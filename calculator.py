while True:
    print('1 - Addition')
    print('2 - Subtraction')
    print('3 - Multiply')
    print('4 - Divide')
    print('5 - Exit')
    
    option = int(input("Choose an operation: "))
    
    if option == 5:
        print("Calculator exiting. Goodbye!")
        break  # Exit the loop and terminate the program
    
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
            if num2 == 0:
                print("Error: Cannot divide by zero.")
                continue  # Go back to operation selection
            result = num1 / num2

        print("Result:", result)
    else:
        print("Invalid operation entered.")
