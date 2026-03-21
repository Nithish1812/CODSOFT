def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def main():
    print("--- CODSOFT Calculator ---")
    
    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            num2 = float(input("Enter second number: "))
            
            print("\nChoose Operation:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")
            print("5. Exit")
            
            choice = input("Enter choice (1/2/3/4/5): ")
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
            elif choice == '5':
                print("Exiting Calculator. Goodbye!")
                break
            else:
                print("Invalid Input! Please choose a number between 1-5.")
        
        except ValueError:
            print("Invalid Input! Please enter numeric values.")

if __name__ == "__main__":
    main()