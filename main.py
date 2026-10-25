import ascii_art

# TODO: write out the other functions - +,-,*,/
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a/b
    except:
        print("Cannot divide by Zero.")
        return None


# TODO: Add these functions into a dictonary as the values and keys = "+", "-", "*", "/"

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

# TODO: Use the dictionary operations to perform the calcilations. Multiply 4*8 using the dictionary
# print((operations["*"])(4,9))


def calculator():
    print(ascii_art.LOGO)
    num1 = float(input("What is the first number?: "))
    should_accumulate = True
    while should_accumulate:
        print("Welcome To Calculaor()")
        print("Here is the Symbol...")
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an Operations: ")
        
        num2 = float(input("What is the second number?: "))

        # Accessing the dictionary
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculator.")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
            return 


calculator()

    
