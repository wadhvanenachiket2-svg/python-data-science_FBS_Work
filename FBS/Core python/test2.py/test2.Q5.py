#A man goes for shopping. He buys 5 products. Accept the price of all products and display
#the total bill after adding 18% GST
total = 0
for i in range(5):
    price = float(input(f"Enter the price of product {i+1}: "))
    total += price

gst = total * 0.18
total_bill = total + gst
print(f"Total bill after adding 18% GST: {total_bill}")