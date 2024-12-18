#take user information
name = input("Enter your name:")
birth = int(input("Enter your birth year:"))
balance =0

#show membership options
print("1. Membership")
print("2. No Membership")
membership = input("You want to take membership card:")

if(membership =="1"):
    #show type of membership options
    print("You choose the Membership option")
    print("=============================Product menu============================")
    print("1. Gold - Rs.500")
    print("2. Silver - Rs.300")
    print("=======================================================================")

    chooseMembership = input("Choose which membership you want to take:")
# =========================== for gold membership ===========================================
    if(chooseMembership =='1'):
        print("You choose Gold.")
        balance += 500 
        #show product list
        print("=============================Product menu============================")
        print("1. Laptop - Rs. 160000")
        print("2. mobile - Rs.50000")
        print("====================================================================================")
        chooseProduct = input("which product you want to buy:")
        if(chooseProduct == '1'):
            print("You want to buy laptop.")
            balance = balance+160000
            actualBalance =balance-balance *0.3
            print(f"You have to Pay :{actualBalance}")
            depositeMoney = float(input("Enetr Money:"))
            if(depositeMoney<0):
                print("Invalid entry")
            elif(depositeMoney == 0 or depositeMoney <actualBalance):
                print("Insufficient Money")
            else:
                totalBalance = depositeMoney - actualBalance
                print("Congratulation you are successfully paid money.")
                print(f"Your return amount is {totalBalance}")
        elif(chooseProduct == '2'):
            print("You want to buy mobile.")
            balance = balance+50000
            actualBalance =balance - balance *0.3
            print(f"You have to Pay :{actualBalance}")
            depositeMoney = float(input("Enetr Money:"))
            if(depositeMoney<0):
                print("Invalid entry")
            elif(depositeMoney == 0 or depositeMoney <actualBalance):
                print("Insufficient Money")
            else:
                totalBalance = depositeMoney - actualBalance
                print("Congratulation you are successfully paid money.")
                print(f"Your return amount is {totalBalance}")
        else:
            print("Invalid choice.")
#====================================== for Silver Membership ===============================================
    elif(chooseMembership =='2'):
        balance += 300
        print("You choose Silver.")
        #show product list
        print("=============================Product menu============================")
        print("1. Laptop - Rs. 160000")
        print("2. mobile - Rs.50000")
        print("====================================================================================")
        chooseProduct = input("which product you want to buy:")
        if(chooseProduct == '1'):
            print("You choose Laptop.")
            balance = balance+160000
            if(birth == 0 or birth<0):
                print("Invalid birth year")
            # age >60 and age<16
            elif(2024-birth>=60 or 2024-birth<=16):
                actualBalance =balance - balance *0.25
                print(f"You have to Pay :{actualBalance}")
                depositeMoney = float(input("Enetr Money:"))
                if(depositeMoney<0):
                    print("Invalid entry")
                elif(depositeMoney == 0 or depositeMoney <actualBalance):
                    print("Insufficient Money")
                else:
                    totalBalance = depositeMoney - actualBalance
                    print("Congratulation you are successfully paid money.")
                    print(f"Your return amount is {totalBalance}")
            else:
                # age between 16 t0 60 
                actualBalance =balance - balance *0.15
                print(f"You have to Pay :{actualBalance}")
                depositeMoney = float(input("Enetr Money:"))
                if(depositeMoney<0):
                    print("Invalid entry")
                elif(depositeMoney == 0 or depositeMoney <actualBalance):
                    print("Insufficient Money")
                else:
                    totalBalance = depositeMoney - actualBalance
                    print("Congratulation you are successfully paid money.")
                    print(f"Your return amount is {totalBalance}")
        elif(chooseProduct =='2'):
            print("You choose Mobile.")
            balance = balance+50000

            if(birth == 0 or birth<0):
                print("Invalid birth year")
            # age >60 and age<16
            elif(2024-birth>=60 or 2024-birth<=16):
                actualBalance =balance - balance *0.25
                print(f"You have to Pay :{actualBalance}")
                depositeMoney = float(input("Enetr Money:"))
                if(depositeMoney<0):
                    print("Invalid entry")
                elif(depositeMoney == 0 or depositeMoney <actualBalance):
                    print("Insufficient Money")
                else:
                    totalBalance = depositeMoney - actualBalance
                    print("Congratulation you are successfully paid money.")
                    print(f"Your return amount is {totalBalance}")
            else:
                # age between 16 t0 60 
                actualBalance =balance - balance *0.15
                print(f"You have to Pay :{actualBalance}")
                depositeMoney = float(input("Enetr Money:"))
                if(depositeMoney<0):
                    print("Invalid entry")
                elif(depositeMoney == 0 or depositeMoney <actualBalance):
                    print("Insufficient Money")
                else:
                    totalBalance = depositeMoney - actualBalance
                    print("Congratulation you are successfully paid money.")
                    print(f"Your return amount is {totalBalance}")
        else:
            print("Invalid product choice.")
elif(membership == "2"):
# ======================== For normal User =====================================================
    print("You are not choose any membership")
 #show product list
    print("=============================Product menu============================")
    print("1. Laptop - Rs. 160000")
    print("2. mobile - Rs.50000")
    print("====================================================================================")
    chooseProduct = input("which product you want to buy:")
    if(chooseProduct == '1'):
        print("You want to buy laptop.")
        balance = balance+160000
        actualBalance =balance-balance *0.05
        print(f"You have to Pay :{actualBalance}")
        depositeMoney = float(input("Enetr Money:"))
        if(depositeMoney<0):
            print("Invalid entry")
        elif(depositeMoney == 0 or depositeMoney <actualBalance):
            print("Insufficient Money")
        else:
            totalBalance = depositeMoney - actualBalance
            print("Congratulation you are successfully paid money.")
            print(f"Your return amount is {totalBalance}")
    elif(chooseProduct == '2'):
            print("You want to buy mobile.")
            balance = balance+50000
            actualBalance =balance - balance *0.05
            print(f"You have to Pay :{actualBalance}")
            depositeMoney = float(input("Enetr Money:"))
            if(depositeMoney<0):
                print("Invalid entry")
            elif(depositeMoney == 0 or depositeMoney <actualBalance):
                print("Insufficient Money")
            else:
                totalBalance = depositeMoney - actualBalance
                print("Congratulation you are successfully paid money.")
                print(f"Your return amount is {totalBalance}")
    else:
        print("Invalid choice.")

else:
    print("Invalid entry!!")