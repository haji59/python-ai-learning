
stocks = {
    "Argon": 10,
    "co2": 3,
    "oxygen": 5,
    "Nitrogen": 8
}

count = 0
for gas, stock in stocks.items():
    
    
    count += stock
    
print("تعداد سیلندر: ", count)    
print("تعداد ر: ", len(stocks)) 
average = count / len(stocks)
print("میانگین:", average)
