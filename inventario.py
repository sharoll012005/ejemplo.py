
# Request product name
name = input("Product name: ").strip()

# Request price, repeat if invalid
price_input = input("Price: ")
try:
    price = float(price_input)
    if price <= 0:
        print("Price must be greater than 0.")
        price = float(input("Price: "))
except:
    print("Invalid price.")
    price = float(input("Price: "))

# Request quantity, repeat if invalid
quantity_input = input("Quantity: ")
try:
    quantity = int(quantity_input)
    if quantity <= 0:
        print("Quantity must be greater than 0.")
        quantity = int(input("Quantity: "))
except:
    print("Invalid quantity.")
    quantity = int(input("Quantity: "))

# Calculate total cost
total_cost = price * quantity

# Show results
print(f"Product: {name} | Price: {price} | Quantity: {quantity} | Total: {total_cost}")

# Program that asks for name, price and quantity, validates the last two,
# calculates price*quantity and displays a summary.