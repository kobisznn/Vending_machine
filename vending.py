#Author: Kobi Okafor 
#Spire ID: 34435529
#Email: kokafor@umass.edu
class VendingMachine:
    def __init__(self):
        self.items={}
        self.coins=0
        self.sales=0
        self.sales_account=[]
    def list_items(self):
        if len(self.items)==0:
            print(f"No items in the vending machine")
        else:
            print("Available items:")
            for item_name in sorted(self.items):
                item_contents=self.items[item_name]
                cost=item_contents['price']
                num=item_contents['quantity']
                print(f"{item_name} (${cost}): {num} available")
    def add_item(self,name,price,quantity):
        if name in self.items: 
            self.items[name]['quantity'] += quantity
            self.items[name]['price'] = price
        else:
            self.items[name]= {"quantity": quantity,"price": price}
        print(f"{quantity} {name}(s) added to inventory")
    def insert_money(self,dollar_amount):
        if dollar_amount== 1 or dollar_amount==2 or dollar_amount==3:
            self.coins += dollar_amount
            print(f"Balance: {round(self.coins,3)}")
        else:
            print(f"Invalid amount")
    def purchase(self,snack):
        if snack not in self.items:
            print(f"Invalid item")
        elif self.items[snack]["quantity"] ==0:
            print(f"Sorry {snack} is out of stock")
        elif self.items[snack]['price'] > self.coins:
            print(f"Insufficient balance. Price of {snack} is {self.items[snack]['price']}")
        else:
            self.items[snack]["quantity"] -=1
            self.coins= round(self.coins-self.items[snack]['price'],2)
            self.sales = round(self.sales + self.items[snack]['price'],2)
            self.sales_account.append(snack)
            print(f"Purchased {snack}")
            print(f"Balance: {self.coins}")
    def display_change(self):
        if self.coins == 0:
            print(f"No change")
        else:
            print(f"Change: {self.coins}")
            self.coins=0
    def get_item_price(self,snack):
        if snack not in self.items:
            print(f"Invalid item")
        else:
            return self.items[snack]['price']
    def empty_inventory(self):
        self.items={}
        print(f"Inventory cleared")
    def get_total_sales(self):
        return self.sales
    def get_item_quantity(self,snack):
        if snack in self.items:
            return self.items[snack]["quantity"]
        else:
            print(f"Invalid item")
    def remove_item(self,snack):
        if snack not in self.items:
            print(f"Invalid item")
        else:
            del self.items[snack]
            print(f"{snack} removed from inventory")
    def stats(self,n):
        if len(self.sales_account) ==0:
            print("No sale history in the vending machine")
        else:
            i=1
            previously_sold={}
            while i<= n and i <= len(self.sales_account):
                if self.sales_account[-i] in previously_sold:
                    previously_sold[self.sales_account[-i]] += 1
                else:
                    previously_sold[self.sales_account[-i]]= 1
                i+=1

            previously_sold= dict(sorted(previously_sold.items()))
            print(f"Sale history for the most recent {n} purchase(s):")  
            
           

            for snack, count in previously_sold.items():
                price=self.get_item_price(snack)
                if self.items[snack]["price"] is not None:
                    print(f"{snack}: ${price*count} for {count} purchase(s)")
       


                

        










            


    