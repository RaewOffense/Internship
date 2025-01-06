import csv

class Ice_Cream:
    def __init__(self):
        self.list_of_IceCream = {
            "1": ["Vanilla", 100],
            "2": ["Chocolate", 120],
            "3": ["Mango", 50],
            "4": ["Strawberry", 200],
            "5": ["Sugar-Free Vanilla", 150]
        }
        self.totalCones = 200
        self.buyItems = []
        self.totalPrice = 0

        with open("ice_cream_menu.csv", "w", newline="") as iceCreamMenu:
            menu_writer = csv.writer(iceCreamMenu)
            menu_writer.writerow(["Key", "Flavor", "Price"])
            for key, [flavor, price] in self.list_of_IceCream.items():
                menu_writer.writerow([key, flavor, price])

    
    # save buy item in this bill.csv file
    def bill(self):
        with open("bill.csv","w") as billFile:
            bill_writer = csv.writer(billFile)
            bill_writer.writerow(["Flavor", "Price", "Total"])

            for item in self.buyItems:
                bill_writer.writerow(item)
            bill_writer.writerow(["Grand Total", "", "", self.totalPrice])
    
    #show the Ice Cream items 
    def show_List_of_IceCream(self):
        print("*"*15,"Ice Cream List","*"*15)
        with open("ice_cream_menu.csv","r") as iceCreamMenu:
            reader = csv.reader(iceCreamMenu)
            for row in reader:
                key, flavor,price =row
                print(f"{key} : {flavor} - Rs.{price}")
        print("*"*50)

    def display_bill(self):
        print("\n*************** Your Bill ***************")
        print(f"{'Flavor':<20} {'Quantity':<10} {'Price':<10} {'Total':<10}")
        print("-" * 50)
        for flavor, qty, price, total in self.buyItems:
            print(f"{flavor:<20} {qty:<10} Rs.{price:<10} Rs.{total:<10}")
        print("-" * 50)
        print(f"{'Grand Total':<20} {'':<10} {'':<10} Rs.{self.totalPrice:<10}")
        print("*****************************************\n")

    def buy_IceCream(self):
        while True:
            if self.totalCones == 0:
                print("\n Sorry,We are out of Stock!")
                self.bill() 
                self.display_bill()
                break

            print("\n Welcome to Ice Cream Shop!!!\n")
            self.show_List_of_IceCream()
            choice  =  input("Which Flavor of Ice Cream Do You Want to Buy (or type 'exit' to leave)?:")
            
            if choice.lower() == 'exit':
                print("\n Thank You for Visiting! You have a great day!!!")
                self.bill() 
                self.display_bill()
                break
            if choice in self.list_of_IceCream:
                flavor,price = self.list_of_IceCream[choice]

                if self.totalCones > 0:
                    while True:
                        try:
                            no_of_IceCream = int(input(f"\nHow many {flavor} flavor of Ice Cream Do You Want To Buy? :"))
                            if no_of_IceCream <=0:
                                print("\n Please enter valid quantity!")
                                continue
                            if no_of_IceCream > self.totalCones:
                                print(f"\n Only {self.totalCones} cones are available in the stocks.")
                                continue
                            break
                        except ValueError:
                            print("\n Please enter valid number.")

                    total = no_of_IceCream * price
                    self.totalPrice += total
                    remainingCones = self.totalCones - no_of_IceCream
                    self.buyItems.append([flavor, no_of_IceCream, price, total])
                    print(f"Remaining cones in stock: {remainingCones}\n")

                buy_more = input("Do You want to buy more Ice Cream (Yes/No):")
                if buy_more.lower() =="no":
                    print("\nThank you for visiting! You have a great day!")
                    self.bill() 
                    self.display_bill() 
                    break
            else:
                print("\nInvalid choice! Please select a valid option.")



iceCream = Ice_Cream()
iceCream.buy_IceCream()
