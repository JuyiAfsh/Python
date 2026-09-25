# ATM Cash Dispenser
print("=== ATM CASH DISPENSER ===\n")

# Initialize note counters
total_500 = total_200 = total_100 = total_50 = total_20 = total_10 = total_5 = total_1 = 0
customers_served = 0
total_dispensed = 0

serving = True
while serving:
    # outer while -- one customer per loop
    name = input("Enter customer name: ")
    amount = int(input(f"Hello {name}! Enter withdrawal amount."))
    if amount <= 0:
        print("Invaid amount. Please enter a positive number.\n")
        continue

    print(f"\nDispensing R{amount} for {name}: ")

    # Initially, the entire withdrawel amount is still remaining
    remaining = amount

    # idx tells the program which denomination it is currently working with
    idx = 1
    while idx <= 8:
        if idx == 1: price = 500
        elif idx == 2: price = 200
        elif idx == 3: price = 100
        elif idx == 4: price = 50
        elif idx == 5: price = 20
        elif idx == 6: price = 10
        elif idx == 7: price = 5
        else: price = 1

        # tells us how many complete of that denomination fit into the
        count = remaining // price
        if count > 0:
            print(f" {count} x {price}-unit note(s) = {count * price}")

            # Subtract dispensed money from remaining amount and update total notes
            remaining -= count * price
            if price == 500:
                total_500 += count
            elif price == 200:
                total_200 += count
            elif price == 100:
                total_100 += count
            elif price == 50:
                total_50 += count
            elif price == 20:
                total_20 += count
            elif price == 10:
                total_10 += count
            elif price == 5:
                total_5 += count
            else:
                total_1 += count
        idx += 1

    customers_served += 1
    total_dispensed += amount
    print(f"Transaction complete, {name}!\n")
    again = input("Next customer? (yes/no)").strip().lower()
    if again != "yes":
        serving = False

print("\n=== Daily Denomination Report ===")
for slot in range(1, 9):
    # outer for -- one denomintaion per loop
    if slot == 1:
        price, total = 500, total_500
    elif slot == 2:
        price, total = 200, total_200
    elif slot == 3:
        price, total = 100, total_100
    elif slot == 4:
        price, total = 50, total_50
    elif slot == 5:
        price, total = 20, total_20
    elif slot == 6:
        price, total = 10, total_10
    elif slot == 7:
        price, total = 5, total_5
    else:
        price, total = 1, total_1

    if total > 0:
        print(f" {price}-unit notes dispensed : {total} ")

print(f"\nCustomers served : {customers_served}")
print(f"\nTotal dispensed : {total_dispensed} units")
print("ATM session closed. Goodbye!")
            

     