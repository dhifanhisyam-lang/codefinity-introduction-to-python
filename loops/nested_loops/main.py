produce = ["Tomatoes", "Lettuce"]
dairy   = ["Milk", "Cheese"]

groceries = [produce, dairy]

for section in groceries:      # goes through each sublist
    for item in section:       # goes through each element of that sublist
        print("Item name:", item)