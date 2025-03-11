def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose operation: ")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Division (/)")

choice = input("Enter choice (1/2/3): ")

if choice == '1':
    print(f"Result: {add(num1, num2)}")
elif choice == '2':
    print(f"Result: {subtract(num1, num2)}")
elif choice == '3':
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid choice! Please enter 1, 2, or 3.")
