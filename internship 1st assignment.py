import sympy as sp
import random
import math

# Define basic arithmetic functions
def addition(a, b):
    return a + b

def multiplication(a, b):
    return a * b

def subtraction(a, b):
    return a - b

def modulus(a, b):
    return a % b

def division(a, b):
    return a / b

# Define calculus functions
def derivative():
    eq = input("Enter the equation (in terms of x): ")
    var = sp.symbols(input("Enter the variable to differentiate with respect to: ").strip())
    expr = sp.sympify(eq)
    diff_expr = sp.diff(expr, var)
    print("The derivative of the equation is:", diff_expr)

def integral():
    eq = input("Enter the equation (in terms of x): ")
    var = sp.symbols(input("Enter the variable to integrate with respect to: ").strip())
    expr = sp.sympify(eq)
    integral_expr = sp.integrate(expr, var)
    print("The indefinite integral of the equation is:", integral_expr)

# Dice rolling function
def roll_dice():
    return random.randint(1, 6)

# Start the game and calculator
print("\n\t\t\t\tWELCOME TO THE DICE GAME & CALCULATOR\n")
print("To earn calculation attempts, you must first play the dice game.\n")

total_attempts = 0

# Dice game loop
while True:
    play = input("Do you want to roll the dice? (yes to roll, anything else to quit): ").strip().lower()
    
    if play != "yes":
        print("Exiting the game. Goodbye!")
        break

    dice_value = roll_dice()
    total_attempts += dice_value
    print(f"You rolled a {dice_value}! You now have {total_attempts} calculation attempts.\n")

    # Calculation loop
    while total_attempts > 0:
        print("\n\t\t\t\tSIMPLE CALCULATOR\n")
        print("\t\tADDITION (enter add)")
        print("\t\tSUBTRACTION (enter sub)")
        print("\t\tMULTIPLICATION (enter mul)")
        print("\t\tDIVISION (enter div)")
        print("\t\tMODULUS (enter mu)")
        print("\t\tDERIVATIVE (enter der)")
        print("\t\tINTEGRAL (enter int)")
        print("\t\tQUIT (enter q)\n")
        
        enter = input("Enter The Operation: ").strip().lower()
        
        if enter == "q":
            print("Exiting the calculator. Goodbye!")
            break
        elif enter in ["add", "sub", "mul", "div", "mu"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if enter == "add":
                print("Your answer is =", addition(a, b))
            elif enter == "sub":
                print("Your answer is =", subtraction(a, b))
            elif enter == "mul":
                print("Your answer is =", multiplication(a, b))
            elif enter == "div":
                print("Your answer is =", division(a, b))
            elif enter == "mu":
                print("Your answer is =", modulus(a, b))
        elif enter == "der":
            derivative()
        elif enter == "int":
            integral()
        else:
            print("Invalid Operation Selected. Please try again.")
        
        total_attempts -= 1
        print(f"Remaining calculation attempts: {total_attempts}\n")
        
        if total_attempts == 0:
            print("You've used all your calculation attempts. Roll the dice to earn more!\n")
            break

