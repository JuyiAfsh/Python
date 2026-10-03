print("=== Grocery Billing Queue ===")

bread = 20
milk = 30
apple = 25
banana = 25
cabage = 15
carrot = 15

customers_served = 0
total_sales = 0
billing = True

while billing:
    name = input("Enter customer name: ")
    amount = int(input("Enter number of items: ")) 
    if amount <= 0:
        print("Invalid number. Please enter a positive number.\n")
        continue



