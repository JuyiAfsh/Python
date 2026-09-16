import keyword

# print all the Python keywords
print("The keywords in python are...\n")
print(keyword.kwlist)

print("\n ")

# Questions
name = input("enter your name: ")
goal = input("enter one thing you want to become or be better at: ")
month = int(input("enter the month you would like to reach this goal: "))

print()
print("===== PERSONAL GOAL DISPLAY =====")
print("Name: ", name)
print("Goal: ", goal)
print("Month: ", month)
print("=================================")

print("Good luck ", name , "! You can reach your goal!")