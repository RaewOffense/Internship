number = int(input("Enter number:"))

for i in range(1,number+1):
    #Right-Aligned Triangle
    print(' ' *(number-i)+'*'*i)

    #Left-Aligned Triangle
    # print(i*'*')


for i in range(1,number+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()    

