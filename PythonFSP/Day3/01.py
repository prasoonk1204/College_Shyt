# Error Handling

try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    quotient = num1 / num2
    print(f"So {num1} / {num2} = {quotient}...")
except ValueError as ve:
    print("Please provide Interger values only...")
    print("Error message:", ve)
    print("Error Type:", type(ve))
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
finally: 
    print("FINALLY block is executing")
    print("It executes always...")

print("End of the program...")