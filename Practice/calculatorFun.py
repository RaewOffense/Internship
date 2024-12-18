
def add(number1,number2):
    return number1+number2

def subtract(number1,number2):
    return number2-number1

def multiple(number1,number2):
    return number1*number2

def divide(number2,number1):
    return number1/number2

# take user input
number1 = int(input("Enter First Number:"))
number2 = int(input("Enter Second Number:"))

print("Please Select operation -\n"\
        "1. Addition\n"\
        "2.Subtraction\n"\
        "3. Multiplication\n"\
        "4. Division")
choice = int(input("Choose your operation(1,2,3,4):"))

if choice ==1:
    print("addition:",add(number1,number2))
elif choice ==2:
    print("Subtraction:",subtract(number1,number2))
elif choice == 3:
    print("Multiplication:",multiple(number1,number2))
elif choice == 4:
    print("Division:",divide(number1,number2))
else:
    print("Invalid Entry!!!")