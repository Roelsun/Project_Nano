import random
# Initialize game loop
# Print game rules, number between 0 - 10, 3 guesses after which the computer will respond higher/lower, after wrong 3 attempts you fail
# Function to receive user input, and convert it to int to minimize repetition
def uInput():
    return int(input('What is your guess?: '))

# Generate a random number, using the random library, with the ranges based on the difficulty
def genereer_getal(difficulty):
    match difficulty:
        case "1":
            print("You have chosen the easy difficulty")
            print("Your number will be between 1 and 10")
            return random.randrange(1, 10)
        case "2":
            print("You have chosen the normal difficulty")
            print("Your number will be between 1 and 50")
            return random.randrange(1, 50)

        case "3":
            print("You have chosen the hard difficulty")
            print("Your number will be between 1 and 100")
            return random.randrange(1, 100)
# A function that uses a match statement to return the max attempts for any gjven difficulty
def max_pogingen(difficulty):
    match difficulty:
        case "1":
            return 5
        case "2":
            return 7
        case "3":
            return 10

# Calculate score based on the max attempts, the attempts left over multiplied by difficulty
def score(difficulty, pogingen):
    score = (max_pogingen(difficulty) - pogingen) * difficulty
    return score

# Generate an advice concerning the difficulty based on the achieved score
def advies_difficulty(score):
    if (score < 5):
        print("I would reccomend a lower difficulty next time")
    elif (score < 12):
        print("This is the correct difficulty for you")
    else:
        print("This is just too easy for you, try a harder difficulty")


## The function containing the main game loop,
def raad_het_nummer():
    # Ask for user input for their name and the desired difficulty
    name = input('Please enter your name: ')
    difficulty = input('Choose your difficulty (1=Easy, 2=Normal, 3=Difficult): ')
    # Generate the random number based on difficulty settings
    cnumber = genereer_getal(difficulty)

    # Set pogingen to the max attempts for the given difficulty, and print that info to the user
    pogingen = max_pogingen(difficulty)
    print("You have " + str(pogingen) + " attempts to guess the number")
    # Initialize a variable to keep track of whether the user has correctly guessed the number
    correctGuess = False
    # Initialize a while loop to continue receiving user input, checking it and printing the relevant output
    while pogingen > 0 and correctGuess != True:
        uGuess = int(uInput())
        # If the user input and the computer's guess are the same, print the win message and score.
        if uGuess == cnumber:
            print("You have won!")
            final_score = score(difficulty, pogingen)
            print("Your score is: " + str(final_score))
            advies_difficulty(int(final_score))
            correctGuess = True

        elif(abs(uGuess - cnumber) <= 2):
            print("Je bent dichtbij!")
            pogingen = pogingen - 1

        elif (uGuess > cnumber):
            pogingen = pogingen - 1
            print('Think Lower, You have ' + str(pogingen) + ' attempts left')

        elif (uGuess < cnumber):
            pogingen = pogingen - 1
            print('Think Higher, You have ' + str(pogingen) + ' attempts left')

    if (not correctGuess):
        print("Jammer, je hebt het niet kunnen raden, het juiste getal was " + str(cnumber))
        advies_difficulty(0)
    else:
        score(difficulty, pogingen)

# Calling the main game loop function
