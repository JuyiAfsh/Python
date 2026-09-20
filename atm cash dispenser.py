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
        if idx == 1: value = 500
        elif idx == 2: value = 200
        elif idx == 3: value = 100
        elif idx == 4: value = 50
        elif idx == 5: value = 20
        elif idx == 6: value = 10
        elif idx == 7: value = 5
        else: value = 1

        # tells us how many complete of that denomination fit into the
        count = remaining // value
        if count > 0:
            print(f" {count} x {value}-unit note(s) = {count * value}")

            # Subtract dispensed money from remaining amount and update total notes
            remaining -= count * value
            

     