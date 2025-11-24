# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started...")

for item in inventory:
	while inventory[item][0] < inventory[item][1]:
		inventory[item][0] += inventory[item][2]
		if inventory[item][0] > discount_threshold:
			inventory[item][3] = True
	print("Processing", item)
	#print(inventory[item])
print("Processing completed")
	