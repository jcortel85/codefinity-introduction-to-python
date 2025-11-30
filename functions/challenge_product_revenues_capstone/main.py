# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

#define function that calculates revenues and store in new list "revenues"
def calculate_revenue(prices, quantities_sold):
    revenues = []
    for i in range(len(prices)):
        revenues.append(prices[i] * quantities_sold[i])
    #print(revenues)
    return revenues

#define function that sorts revenue_per_product list and print line for each product and revenue
def formatted_output(revenues):
    sorted_revenue_per_product = sorted(revenue_per_product, key = lambda item: item[0])
    #print(sorted_revenue_per_product)
    for name, rev in sorted_revenue_per_product:
        print(f"{name} has total revenue of ${rev}.")

#set "revenues" and call calculate_revenue to store output into revenues list
revenues = calculate_revenue(prices, quantities_sold)

#combine products and revenues into one list of tuples
revenue_per_product = list(zip(products, revenues))

#pass revenues list into formatted_output to print name and rev for each item
formatted_output(revenues)