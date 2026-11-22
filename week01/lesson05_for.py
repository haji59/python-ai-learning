# Lesson 05: For Loop and Stock Management
gases = ["Argon", "LPG", "Oxygen", "Nitrogen", "CO2"]
stocks = [10, -3, 5, 8, 0]

for gas, stock in zip(gases, stocks):

    if stock == 0:
        print(gas, stock, "Out of Stock")

    elif stock >= 1 and stock < 5:
        print(gas, stock, "Low Stock")

    elif stock >= 5:
        print(gas, stock, "Available")

    else:
        print(gas, stock, "Negative Stock")

    # بررسی نیاز به سفارش
    if stock < 5:
        print(gas, "Order Required")
       