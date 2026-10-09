secret = 48

guessing = True
while guessing:
    guess = int(input("Guess a number from 1 to 50: "))
    if guess == secret:
        print("Congratulatons! You guessed the right number!")
    elif guess <= 20:
        print("Ice cold! Try again")
    elif guess <= 30:
        print("Cold! Try again")
    elif guess <= 40:
        print("Warm! Try again")
    else:
        print("Hot! Almost there")
        

