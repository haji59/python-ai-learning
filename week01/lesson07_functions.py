def  check_gas_stock(gas_name, stock):
    if stock < 0:
        return "Invalid Stock"
    elif stock == 0:
        return "Out of Stock"
    elif stock < 5:
        return "Low Stock"
    else:
        return "Available"

try:
    gas_name = input("Enter gas name: ")

    if not gas_name:
        print("Gas name cannot be empty")

    else:
        stock = int(input("Enter stock: "))
        result = check_gas_stock(gas_name, stock)
        print(gas_name, ":", result)

except ValueError:
    print("Please enter a valid number")