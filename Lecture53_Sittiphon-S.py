def vatCal(totalPrice = int(input("Item Price ;" ))):
    result = totalPrice+(totalPrice*7/100)
    return result

print(vatCal())