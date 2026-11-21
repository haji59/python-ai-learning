stock_Argon = 0
stock_lpg = 0
if stock_Argon > 0:
    print("Argon:", "Available")
else:
    print("Argon:","not Available")     
if stock_lpg > 0:
    print("lpg:","Available")    
else:
    print("lpg:", "not Available")    
if stock_Argon > 0 or stock_lpg > 0 :
    print("حداقل یکی موجود است")
else:
    print("هیچ گازی موجود نیست")        

