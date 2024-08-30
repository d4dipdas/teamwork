# Simple Calculator Program in Python

def add(a, b):
    """Calculate the summation of two numbers."""
    return a + b

def subtract(a, b):
    """Calculate the subtraction of two numbers."""
    return a - b

def divide(a, b):
    """Calculate the division of two numbers."""
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero is not allowed."

def multiply(a, b):
    """Calculate the multiplication of two numbers."""
    return a * b

def mod(a, b):
    """Calculate the remainder of two numbers."""
    if b != 0:
        return a % b
    else:
        return "Error: Division by zero is not allowed."

def power(a, b):
    """Calculate the power of the first number raised to the second number."""
    return a ** b

def main():
    """Main function to take user input and perform the selected operation."""
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Divide")
    print("4. Multiply")
    print("5. Modulus")
    print("6. Power")
    
    choice = input("Enter choice (1/2/3/4/5/6): ")
    
    if choice in ['1', '2', '3', '4', '5', '6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"The result is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result is: {divide(num1, num2)}")
        elif choice == '4':
            print(f"The result is: {multiply(num1, num2)}")
        elif choice == '5':
            print(f"The result is: {mod(num1, num2)}")
        elif choice == '6':
            print(f"The result is: {power(num1, num2)}")
    else:
        print("Invalid input. Please select a valid operation.")

if __name__ == "__main__":
    main()
