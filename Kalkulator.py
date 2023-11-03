import math
from decimal import Decimal, getcontext
import sys
from mpmath import mp
sys.set_int_max_str_digits(0)                                                                                                                                        
getcontext().prec = 999999999
def main():
    mp.dps = 999999999
    while True:
        print("Options:")
        print("Enter 'add' for addition")
        print("Enter 'sub' for subtraction")
        print("Enter 'mul' for multiplication")
        print("Enter 'div' for division")
        print("Enter 'fact' for factorial")
        print("Enter 'exp' for exponentiation")
        print("Enter 'mod' for Mod Div")
        print("Enter 'sqrt' for ROOT")
        print("Enter 'quit' to end the program")
        user_input = input(": ")

        if user_input == "quit":
            break
        elif user_input in ("add", "sub", "mul", "mod", "div"):
            num1 = Decimal(input("Enter first number: "))
            num2 = Decimal(input("Enter second number: "))
            if user_input == "add":
                result = num1 + num2
            elif user_input == "sub":
                result = num1 - num2
            elif user_input == "mul":
                result = num1 * num2
            elif user_input == "div":
                result = num1 / num2
            elif user_input == "mod":
                result = num1 % num2
        elif user_input == "fact":
            num = int(input("Enter the number for factorial: "))
            result = math.factorial(num)
        elif user_input == "exp":
            base = input("Enter the base: ")
            exponent = input("Enter the exponent: ")
            base1 = Decimal(base)
            exponent2 = Decimal(exponent)
            result = base1 ** exponent2
        elif user_input == "sqrt":
            num = int(input("Enter the number for root: "))
            result = math.sqrt(num)
        else:
            print("Unknown input. Please enter a valid option.")
            continue
                           
        print("Result: " + mp.nstr(result))
        # Menulis hasil perhitungan ke dalam file
        with open("output.txt", "a") as file:
            file.write(f"User input: {user_input}, Result: {result}\n")


if __name__ == "__main__":
    main()
