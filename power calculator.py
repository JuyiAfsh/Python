print("=== Power Calculator ===")
base = int(input("Enter base number: "))
exponent = int(input("Enter the power: "))
result = 1

for i in range(1, exponent+1):
    result = result * base
    print(f"Step {i}: Result = {result}")
print(f"\nAnswer: {base} to the power {exponent} = {result}")