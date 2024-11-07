'''13. Inventory Class for a Store
•	Create a class called Inventory with attributes:
o	items: A dictionary to store items and their quantities.
•	Write methods to:
o	Add items to the inventory with quantities.
o	Remove items from the inventory.
o	Display all items and their quantities.
•	Instantiate the Inventory class, add some items, remove an item, and list the remaining items.
'''
class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        print(f"Added {quantity} of {item_name}. New quantity: {self.items[item_name]}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"{item_name} removed from the inventory.")
        else:
            print(f"{item_name} not found in the inventory.")

    def display_items(self):
        if self.items:
            print("Inventory items and their quantities:")
            for item, quantity in self.items.items():
                print(f"{item}: {quantity}")
        else:
            print("The inventory is empty.")


inventory = Inventory()
inventory.add_item("Apples", 50)
inventory.add_item("Oranges", 30)
inventory.add_item("Apples", 20) 

inventory.display_items()

inventory.remove_item("Oranges") 
inventory.display_items()
