n = int(input("Enter Number:"))
evenSum =0
oddSum =0
for i  in range(1,n+1):
    if(i%2 ==0):
        evenSum =evenSum + i
    else:
        oddSum = oddSum + i
        
print(f"Even number sum: {evenSum}")
print(f"Odd Number Sum: {oddSum}")