# Input a word or sentence
string = input("Please enter your own String : ")

string2 = ''

# Loop for printing in reverse
for b in string:
    string2 = b + string2


print("\nThe Originl String = ", string)
print("The Revrsed String = ", string2)