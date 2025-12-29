def main():
    print('1 - Addition')
    print('2 - Subtraction')
    print('3 - Multiply')
    print('4 - Divide')
    print('5 - Power')

    try:
        option = int(input("Choose an operation: "))
    except ValueError:
        print("Invalid operation entered. Please enter a number between 1-5.")
        return

    if option in [1, 2, 3, 4, 5]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values only.")
            return

        try:
            if option == 1:
                result = num1 + num2
            elif option == 2:
                result = num1 - num2
            elif option == 3:
                result = num1 * num2
            elif option == 4:
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    return
                result = num1 / num2  
            elif option == 5:
                result = num1 ** num2 

            print("Result:", result)
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Invalid operation entered. Please choose a number between 1-5.")

while True:
    main()
    quit = input("Do you want to quit: ")

    if quit == 'yes':
        print("Bye!")
        break
