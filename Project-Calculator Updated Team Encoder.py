# Enhanced Simple Calculator Program in Python with Improved User Experience
#sonal
def add(a, b):
    """Calculate the summation of two numbers."""
    return a + b

#Sapna
def subtract(a, b):
    """Calculate the subtraction of two numbers."""
    return a - b

#Roshan
def divide(a, b):
    """Calculate the division of two numbers."""
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

#Sharvaree
def multiply(a, b):
    """Calculate the multiplication of two numbers."""
    return a * b

#Saima
def mod(a, b):
    """Calculate the remainder of two numbers."""
    if b != 0:
        return a % b
    else:
        return "Error: Division by zero is not allowed."

#Rakesh
def power(a, b):
    """Calculate the power of the first number raised to the second number."""
    return a ** b

def get_number(prompt):
    """Prompt the user to enter a number and validate the input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#sakshi 
def main():
    """Main function to take user input and perform the selected operation."""
    print("=" * 40)
    print(" " * 10 + "WELCOME TO CALCULATOR")
    print("=" * 40)
    
    while True:
        print("\nPlease choose an operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Divide")
        print("4. Multiply")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")
        
        choice = input("Enter your choice (1/2/3/4/5/6/7): ").strip()
        
        if choice in ['1', '2', '3', '4', '5', '6']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")
            
            if choice == '1':
                result = add(num1, num2)
                operation = "Addition"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = "Subtraction"
            elif choice == '3':
                result = divide(num1, num2)
                operation = "Division"
            elif choice == '4':
                result = multiply(num1, num2)
                operation = "Multiplication"
            elif choice == '5':
                result = mod(num1, num2)
                operation = "Modulus"
            elif choice == '6':
                result = power(num1, num2)
                operation = "Power"
            
            print(f"\n{operation} of {num1} and {num2} is: {result}")
        
        elif choice == '7':
            print("\nThank you for using the calculator. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid operation.")
            continue
        
        # Ask if the user wants to perform another operation
        again = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("\nThank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
