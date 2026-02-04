grocery_inventory = {"Milk": ("Dairy", 3.50, 8),
                    "Eggs": ("Dairy", 5.50, 30),
                    "Bread": ("Bakery", 2.99, 15)}
egg_price = grocery_inventory["Eggs"][1]
if egg_price > 5:
  print("Eggs are too expensive, reducing the price by $1")

grocery_inventory.update({"Tomatoes": ("Produce", 1.20, 30)})
print("Inventory after adding Tomatoes:", grocery_inventory)
milk_stock = grocery_inventory["Milk"][2]
if milk_stock < 10:
  print("Milk needs to be restocked. Increasing stock by 20 units")
    
  print("Updated inventory:", grocery_inventory)    
    