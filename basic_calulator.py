

print("\nhey! Welcome to using this basic Calculator\n")

while True:
    def calculator(num1, num2):
        if operators == '+':
            return num1 + num2
        elif operators == '-':
            return num1 - num2
        elif operators == '*':
            return num1 * num2
        elif operators == '/':
            return num1 / num2
        elif operators != ['+', '-', '*', '/']:
            return print('\nUse a valid operator +, -, *, or /\n')
        

    num1 = int(input("Enter first number: \n\n"))
    operators = input("\nEnter the operator: \n\n")
    num2 = int(input("\nEnter the second number: \n\n"))
    

    result = calculator(num1, num2)
    print(f"\nResult = {result}")

    
    end_program = input("\n>>> Type 'End' to end the program or hit enter to continue: \n\n")  
      
    if end_program.lower() =='End'.lower(): 
        print('\nProgram Ended 👋\n')
        break


 