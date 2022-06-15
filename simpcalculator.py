# Simple CLI Calculator
print("welcome to simple CLI Calculator")

is_running = True

while is_running:
    # processing Calculations...
    print("Starting Calculator Process")
    user_operation = input("What operation would you like to perform?/npick any of ['+','-','*','/] : ")

    # Get user numbers
    try: # Try to get user number, if they're valid integers/floats, continue
        no1 = float(input("First number: "))
        no2 = float(input("Second number: "))

    except: # we get error when running it
        print("Failed, invalid number...")
        continue


    if user_operation == "+":
        # perform addition
        print(no1 + no2) 

    elif user_operation == "-":
        # perform subtraction
        print(no1 - no2)

    elif user_operation == "*":
        # perform multipliation
        print(no1 * no2)
    
    elif user_operation == "/":
        # perform devision
        print(no1 / no2)

    else:
        # Invalid operation
        print("Invalid operation entered, try again...")

    choice = input("Would you to run another calculation. [y,n]")
    if choice == "y":
        pass

    if choice == "n":
        is_running = False
        # This is the same thing as a braek
# Ctrl + C to exit any pyyhon proram ...