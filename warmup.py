name = input("whats your name? ")
print("Hey " + name + "!")

guess = input("Guess a number 1-10: ")
guess = int(guess)

if guess == 7:
    print("You got it!")
else:
    print("Nope, try again next time.")