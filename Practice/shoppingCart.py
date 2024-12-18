itemDictionary = {
    "Laptop":"Rs. 100000",
    "Mobile":"Rs. 60000",
    "Watch": "Rs. 5000",
    "Earbud":"Rs. 1500",
}

addItems_in_Cart =[]
totalPrice =[]


#Display Dictionary items
def displayDictItem():
    print("======================Product Lists==========================")
    for key in itemDictionary:
        print(f"{key} : {itemDictionary[key]}")
   
#Item add in Cart
def itemAddInCart():
    while True:
        displayDictItem()
        choiceItem = input("Enter your choice:")
        if choiceItem == "0":
            break
        elif choiceItem =="Laptop":
            totalPrice.append(100000)
            addItems_in_Cart.append("Laptop")
        elif choiceItem == "Mobile":
            totalPrice.append(60000)
            addItems_in_Cart.append("Mobile")
        elif choiceItem == "Watch":
            totalPrice.append(5000)
            addItems_in_Cart.append("Watch")
        elif choiceItem == "Earbud":
            totalPrice.append(1500)
            addItems_in_Cart.append("Earbud")
        else:
            print("Invalid Entry")
        
#view cart Items
def viewCartItems():
    print(addItems_in_Cart)

#Remove item from Cart
def removeItem():
    item_remove = input("Which item want to remove?:")
    addItems_in_Cart.remove(item_remove)

#Display Total price
def itemTotalPrice():
    print(totalPrice)
    totalAmount=0
    for price in totalPrice:
        totalAmount =totalAmount+price
    print(totalAmount)

#main Menu
def mainMenu():
    while True:
        print('======================= Menu ==========================\n'\
            "1. Add items to Cart\n"\
            "2. View Cart Items\n"\
            "3. Remove Item From Cart\n"\
            "4. Display Total Price\n"\
            "5. Exit")

        menuChoice = input("Enter menu choice:")
        if menuChoice == "1":
            itemAddInCart()
        elif menuChoice == "2":
            viewCartItems()
        elif menuChoice =="3":
            print(addItems_in_Cart)
            removeItem()
        elif menuChoice == "4":
            itemTotalPrice()
        elif menuChoice == "5":
            print("Thank You, Visit Again!!!")
            break
        else:
            print("Invalid choice")
mainMenu()