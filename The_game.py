import random
secret = random.randint(1,100)

# Initialise variables
counter = 1
guessed_number = int(input("Guess a number between 1 ~ 100 \n"))

# Was the number guessed too high or too low?
while guessed_number != secret:

    if guessed_number > secret :
        print("\nYour guess is too high.")
        counter += 1
        guessed_number = int(input("Please try again! \n"))
    else:
        print("\nYour guess is too low.")
        counter += 1
        guessed_number = int(input("Please try again! \n"))

# Congrets the user when they guessed the correct number
if guessed_number == secret :
        print(f"\nWoo hoo! You guessed it right! \nIt only took you {counter} attempts!")

