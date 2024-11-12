def math_chatbot():
    print("Hi! I am here to solve some basic mathematics problems. ")
    print("Here are your options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        # Ask the user for their choice of operation
        choice = input("Please select an option (1-4) or type 'exit' to quit: ").strip().lower()
        
        if choice == 'exit':
            print("Goodbye! Have a great day!")
            break
        
        # Check if the input is a valid choice
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice, please select a valid option.")
            continue
        
        # Ask for two numbers based on the user's choice
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue
        
        # Perform the chosen operation
        if choice == '1':  # Addition
            result = num1 + num2
            print(f"The result of {num1} + {num2} is {result}.")
        elif choice == '2':  # Subtraction
            result = num1 - num2
            print(f"The result of {num1} - {num2} is {result}.")
        elif choice == '3':  # Multiplication
            result = num1 * num2
            print(f"The result of {num1} * {num2} is {result}.")
        elif choice == '4':  # Division
            if num2 == 0:
                print("Error! Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is {result}.")
        
        # Ask if they want to perform another operation
        another_operation = input("Do you want to do another operation? (yes/no): ").strip().lower()
        if another_operation != 'yes':
            print("Goodbye! Hope I helped you with some math.")
            break

# Run the chatbot
math_chatbot()
