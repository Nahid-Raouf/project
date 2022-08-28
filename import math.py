import math

def askForNumInput(textPrompt):
    # Devine local variable
    convertedNum = math.nan

    # Wait for valid numerical input 
    while True:
        num = input(textPrompt)
        try:
            # Try to typecast the input to a float
            float(num)
        except ValueError:
            # Catch the exception if it is not a number
            print("ERROR: Syn: Invalid Num")
        else:
            # Typecasting
            convertedNum = float(num)
            break
    return convertedNum

def abilitiesList():
    print("+...Addition")
    print("-...Subtraction")
    print("*...Multiplication")
    print("/...Division")
    print("^...Powers")
    print("sin...Sine")
    print("cos...Cosine")
    print("tan...Tangent")

    print("//////////////////////////////////////////////////////////////////////////")
    print("Type 'help' for a list of abilities")

while True:
        operator = input("What operation do you want to perform? ")

        num2 = askForNumInput("Second Number? ")
        # Catch x/0 error case
        if  operator == "/" and num2 == "0":
            print("ERROR: Math: Canot divide by 0!")
        else:
            break

if operator == "+":
    output = num1 + num2
    print("Your Answer: "+str(output))
elif operator == "-":
    output = num1 - num2
    print("Your Answer: "+str(output))
elif operator == "*":
    output = num1 * num2
    print("Your Answer: "+str(output))
elif operator == "/":
    output = num1 / num2
    print("Your Answer: "+str(output))
elif operator == "^":
    output = math.pow(num1,num2)
    print("Your Answer: "+str(output))
    elif operator == "sin":
    output = math.sin(num1)
    print("Your Answer: "+str(output))
elif operator == "cos":
    output = math.cos(num1)
    print("Your Answer: "+str(output))
elif operator == "tan":
    output = math.tan(num1)
    print("Your Answer: "+str(output))

else:
    print("we can not halp you")


