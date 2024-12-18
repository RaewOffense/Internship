number = int(input("Enter Number:"))
square_number = int(number**1/2)
count =0

for i in range(1,square_number):
    if(number%i ==0):
        count +=1
if count == 1:
    print("Prime Number")
else:
    print("Not Prime Number")
