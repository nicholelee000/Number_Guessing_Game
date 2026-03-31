import random
secret = random.randint(1,100)

# Initialise variables
counter = 1

def get_valid_guess (prompt):
    while True:
        try : 
            guessed_number = int(input(prompt + "\n"))

            if guessed_number <1 or guessed_number >100:
                print ("Please enter a number between 1 and 100.\n")

            else :
                return guessed_number
            
        except ValueError:
            print("Thats not a valid number.\n")


guessed_number = get_valid_guess("Guess a number between 1 and 100!")

# Was the number guessed too high or too low?
while guessed_number != secret:

    if guessed_number > secret :
        print("\nYour guess is too high.")

    else:
        print("\nYour guess is too low.")

    counter += 1
    guessed_number = get_valid_guess("Please try again! \n")

# Congrets the user when they guessed the correct number
if guessed_number == secret :
    print(f"\nWoo hoo! You guessed it right! \nIt only took you {counter} attempts! \n")

