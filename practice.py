price = int(input())


if price > 50000:
    final_price = price * 0.8

elif 20000 <= price  <=50000:
    final_price = price * 0.9

else:
    final_price = price
    
    
    
print(int(final_price))        