This project simulates a vending machine using Python. It allows users to add items, insert money, purchase items, and track sales. The vending machine handles various operations such as inventory management, money transactions, and sales statistics.

**Features**
List Items: Displays available items in the vending machine.

Add Item: Adds a specified quantity of an item to the inventory.

Insert Money: Accepts money in denominations of 1, 2, or 3 dollars.
Purchase: Allows the purchase of an item if it's in stock and the user has sufficient balance.
Display Change: Shows the remaining balance and resets it to zero.
Get Item Price: Retrieves the price of a specified item.
Empty Inventory: Clears all items from the inventory.
Get Total Sales: Displays the total sales amount.
Get Item Quantity: Retrieves the quantity of a specified item.
Remove Item: Removes a specified item from the inventory.
Sales Statistics: Shows the sales history for the most recent n purchases.

**EXAMPLE**

# Initialize the vending machine
vm = VendingMachine()

# Add items to the vending machine
vm.add_item("Soda", 1.5, 10)
vm.add_item("Chips", 1.0, 5)

# Insert money
vm.insert_money(2)

# Purchase an item
vm.purchase("Soda")

# Display remaining balance
vm.display_change()

# Get sales statistics
vm.stats(1)

