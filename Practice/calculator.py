#=============================Take user input number==========================================
number1 = int(input("Enter First number:"))
number2 = int(input("Enter Second number:"))

print("====================================== Menu List ===========================================")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

print("===========================================================================================")
choice = int(input("Enter choice:"))

if(choice ==1):
    addition = number1+number2
    print(f"Addition:{addition}")
elif(choice == 2):
    subtract = number2 -number1
    print(f"Subtraction: {subtract}")
elif(choice == 3):
    multiply = number1*number2
    print(f"Multiplication:{multiply}")
elif(choice == 4):
    divide = number1/number2
    print(f"Division:{divide}")
else:
    print("Invalid choice")