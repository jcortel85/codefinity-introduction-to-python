prices = [29.99, 45.50, 12.75, 38.20]
discounts = [.10,.20,.15,.05]

for price in range(len(prices)):
	prices[price] -= prices[price] * discounts[price]
	print(f"Updated price for item {price + 1}: ${prices[price]:.2f}" )
	