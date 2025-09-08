# Exception Handling

# try:
#     num1 = int(input("Enter first number:"))
#     num2 = int(input("Enter second number:"))
#     quotient = num1 / num2
#     print(f"So {num1} / {num2} = {quotient}...")
# except ValueError as ve:
#     print("Please provide Interger values only...")
#     print("Error message:", ve)
#     print("Error Type:", type(ve))
# except ZeroDivisionError as zde:
#     print("Division by ZERO is not allowed...")
#     print("Error message:", zde)
#     print("Error Type:", type(zde))
# except OverflowError as oe:
#     print("Input number is TOO BIG...")
#     print("Error message:", oe)
#     print("Error Type:", type(oe))
# except Exception as e:
#     print("Some other Exception has occurred...")
#     print("Error message:", e)
#     print("Error Type:", type(e))
# else:
#     print("ELSE block is executing")
#     print("Had a smooth execution...")
# finally: 
#     print("FINALLY block is executing")
#     print("It executes always...")

# print("End of the program...")



# User-defined Exception Handling

while(True):    # to allow multiple attempts
    try:
        num1 = int(input("Enter first number(-100 to +100):"))
        num2 = int(input("Enter second number(-100 to +100):"))
        if (num1 < -100 or num2 < -100):
            raise NameError("Below -100")
        if (num1 > 100 or num2 > 100):
            raise OverflowError("Above +100")
        quotient = num1 / num2
        print(f"So {num1} / {num2} = {quotient}...")
    except ValueError as ve:
        print("Please provide Interger values only...")
        print("Error message:", ve)
        print("Error Type:", type(ve))
    except NameError as ne:
        print("Out of bound inputes have been provided...")
        print("Error message:", ne)
        print("Error Type:", type(ne))
        if (str(ne) == "Below -100"): print("Input value < -100 !!!")
        if (str(ne) == "Above +100"): print("Input value > +100 !!!")
    except ZeroDivisionError as zde:
        print("Division by ZERO is not allowed...")
        print("Error message:", zde)
        print("Error Type:", type(zde))
    except OverflowError as oe:
        print("Input number is TOO BIG...")
        print("Error message:", oe)
        print("Error Type:", type(oe))
    except Exception as e:
        print("Some other Exception has occurred...")
        print("Error message:", e)
        print("Error Type:", type(e))
    else:
        print("ELSE block is executing")
        print("Had a smooth execution...")
        break     # to exit from the while loop after successful execution
    finally: 
        print("FINALLY block is executing")
        print("It executes always...")
    

print("End of the program...")