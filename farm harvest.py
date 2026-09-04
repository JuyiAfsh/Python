field1 = 100
field2 = 75
field3 = 140
field4 = 55
field5 = 180

# Calculate total and average harvest
total = field1 + field2 + field3 + field4 + field5
average = total / 5

print("Total harvest  :", total, "kg")
print("Average per field :", average, "kg")

#Price per kg is 15 rands - calculate total earnings
price_per_kg = 15
earnings = total * price_per_kg
print("Total earnings : R", earnings)
print()
# --- Floor Division (//) and Modulus (%) ---
# Pack the harvest into bags of 25 kg each
# Modulus Operator gives remainder
bags = total // 25
leftover = total % 25

print("Full bags packed :", bags)
print("Leftover grain :", leftover, "kg")
print()

# --- Comparison Operators (>, <, ==, >=) ---
# Compare this year's harvest with last year
last_year = 500
print("Better than last year? :", total > last_year)
print("Same as last year? :", total == last_year)
print()

# --- Assignment Operators (+=, -=) ---
# A bonus field adds 30 kg to the total
total += 30
print("After bonus crop :", total, "kg")

# Subtract 15kg saved as seeds for next season
total -= 15
print("After seed reserve :", total, "kg")

# Final bag count after all adjustments
bags = total // 25
print("Final bags packed :", bags)
