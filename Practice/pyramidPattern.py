number = int(input("Enter number:"))
for i in range(1,number+1):
    print(' '*(number-i)+'*'*(2*i-1))