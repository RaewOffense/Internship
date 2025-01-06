import csv

class IceCream:
    def __init__(self):
        self.list_of_IceCream = {
            "1": ["Vanilla",100],
            "2" : ["Chocolate",200],
            "3" : ["Strawberry",300]
        }

        self.totalCones = 100
        self.grandTotal = 0
        self.buyIceCream = []

        with open("menu.csv","w") as menu:
            writer = csv.writer(menu)
            writer.writerow(["Key","Flavor","Price"])

            for key,[flavor,price] in self.list_of_IceCream.items():
                writer.writerow([key,flavor,price])

    def display_menu(self):
        print("\n"+"*"*20 + "Menu List of Ice Cream" + "*" *20+"\n")

        with open("menu.csv","r") as menu:
            reader =csv.reader(menu)
            for row in reader:
                key, flavor, price =row
                print(f"{key} : {flavor} - Rs.{price}")
        print("\n"+"*"*60)
    
    def buy_iceCream(self):
        while True:
            print("\n"+"*"*20 + "Welcome To Ice Cream Shop!" + "*"*20) 
            self.display_menu()

            choice = input("Which flavor of Ice Cream Do You Want To Do Buy (or type 'exit' to leave)?:")
            if choice.lower() == 'exit':
                print("\n Thank You for Visiting! Have a Great Day! ")
                self.bill() 
                self.display_bill()
                break
            
            if choice in self.list_of_IceCream:
                flavor, price = self.list_of_IceCream[choice]

                if self.totalCones > 0:
                    while True:
                        no_of_IceCream = int(input(f"\nHow many {flavor} flavor of Ice Cream Do you Want to Buy?:"))
                        if no_of_IceCream > self.totalCones:
                            print(f"\n Only {self.totalCones} cones are available in the stock.")
                            continue
                        
                        if no_of_IceCream <= 0:
                            print(f"\n Please enter Valid Quantity.")
                            continue
                        break
                        
                    
                    total = no_of_IceCream * price
                    self.grandTotal +=total
                    self.totalCones -= no_of_IceCream
                    self.buyIceCream.append([flavor, no_of_IceCream,price,total])

                    print(f"\n Remaining cones is {self.totalCones}")


                    buy_more = input("\n Do you Want to buy more ice Cream (yes/no)? :")
                    if buy_more.lower() == 'no':
                        print("\n Thank You for Visiting! Have a Great Day! ")
                        self.bill() 
                        self.display_bill()
                        break

                    if self.totalCones == 0:
                        print("\n Sorry,We are out of Stock!")
                        self.bill() 
                        self.display_bill()
                        break

    def bill(self):
        with open("bill.csv","w") as bill:
            writer = csv.writer(bill)
            writer.writerow(["Flavor","Quantity", "Price","Total"])
            for item in self.buyIceCream:
                writer.writerow(item)
            writer.writerow(["Grand Total", "", "", self.grandTotal])
    
                
    def display_bill(self):
        print("\n*************** Your Bill ***************")
        print(f"{'Flavor':<20} {'Quantity':<10} {'Price':<10} {'Total':<10}")
        print("-" * 50)

        for flavor,qty, price, total in self.buyIceCream:
            print(f"{flavor:<20} {qty:<10} Rs.{price:<10} Rs.{total:<10}")
        print("-" * 50)
        print(f"{'Grand Total':<20} {'':<10} {'':<10} Rs.{self.grandTotal:<10}")
        print("\n"+"*"*50)

ice_cream = IceCream()
ice_cream.buy_iceCream()