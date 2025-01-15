num = int(input("Num:"))
flag = False
if num ==0 or num ==1:
    print(f"{num} is not prime number")
elif num>1:
    for i in range(2,num):
        if(num%i) == 0:
            flag = True
            break
if flag:
    print("Not Prime")
else:
    print("Prime")


