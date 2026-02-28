# Apollo (Roel Zondag)
# Functie om de woorden uit een txt bestand in te lezen, en op te slaan als dictionary
import random


# todo, spendeer 15 minuten met alle comments in het nederlands of in het engels te zetten ipv het wisselend te laten staan
# todo, spendeer 15 minuten met comments toevoegen aan functies die ze nog missen
# todo, spendeer 15 minuten met uitzoeken welke functionaliteit ik nog kan toevoegen aan dit onderdeel van p Nano
# Todo: Voeg input validation toe aan de input voor moeilijkheidsgraad
# Todo: Voeg input validation toe aan de input voor the user guess
# Todo: check whether the function "haal_woorden_weg" current functionality is complete



def lees_woorden(bestandsnaam):
    file = open(bestandsnaam, "r")

    woorden_dict = {}
    for line in file:
        # Removing the \n to avoid the extra characters changing the difficulty/the word itself.
        line = line.strip('\n')
        length = len(line)
        # Assigning the difficulty of each word based on the length
        if length <= 6:
            woorden_dict.update({line: 1})

        elif 6 < length < 11:
            woorden_dict.update({line: 2})

        else:
            woorden_dict.update({line: 3})

    return woorden_dict


# Schrijft de "Woorden dictionary" naar het bestand, en return niets
def sla_woorden_op(bestandsnaam, dict):
    file = open(bestandsnaam, "w")
    for x in dict:
        file.write(f'{x} \n')
    pass


def voeg_woorden_toe(bestaandsnaam, dict):
    # Basic function to write whatever words desired into the words file
    done = False
    while not done:
        uinput = input(
            "Please enter any word to add it to the list of possibilities, or done when you are done making additions: ")
        if uinput == "done":
            print("Let us briefly go trough the list to check if you still wish to keep all current entries")
            done = True
        elif uinput:
            dict.update({uinput: 0})
        else:
            print("Invalid input, try again")
    print("The current list of words is: ")
    for x in dict:
        print(f'{x}, Length of the word: {len(x)}')

    file = open(bestaandsnaam, 'w+')
    for x in dict:
        confirmation = input(f"Do you wish to add/keep this word?: {x} . Enter y/n to answer :")
        if (confirmation == "y"):
            file.write(f'{x} \n')
            print("Word Updated successfully")
    print("List updated successfully")

# voeg_woorden_toe("woorden.txt", lees_woorden("woorden.txt"))

def haal_woorden_weg(bestandsnaam):
    lst = lees_woorden('woorden.txt')
    newcontent = []
    with open(bestandsnaam) as f:
        for i, line in enumerate(f):
            line = line.strip('\n')
            print("{0}: {1}".format(i + 1, line))
            keuze = input("Would you like to keep this word, or remove it. Enter y to keep it, and n to remove it")
            validkeuze = False
            while validkeuze == False and i < len(lst):
                if keuze == 'y':
                    print("keep")
                    newcontent.append(f'{line} \n')
                    validkeuze = True
                elif keuze == "n":
                    print("Remove")
                    validkeuze = True
                else:
                    print("Unknown input, try again")
                    input(
                        f' Would you like to keep this word: "{line}", or remove it. Enter y to keep it, and n to remove it ')


def max_poginingen(moeilijkheidsgraad):
    match moeilijkheidsgraad:
        case 1:
            return 10
        case 2:
            return 8
        case 3:
            return 6


## Bereken de score adhv de volgende berekeningen: (aantal_levens_over * moeilijkheid)
def bereken_score(aantal_levens_over, moeilijkheid):
    score = aantal_levens_over * moeilijkheid
    return score


## Voegt de score, de naam en het gegokte woord toe aan het scorebestand
def voeg_score_toe(naam, woord, score):
    file = open("score.txt", "a+")
    newLine = "User: " + naam + " has gotten a score of: " + str(score) + " with the word: " + woord + " \n"
    file.write(newLine)


# Toont de gerade letters als volgt V _ _ R _ E E L D van het woord "voorbeeld"
# Returnt de string met gerade letters als bovenstaand voorbeeld
def toon_tussenstand(woord, geraden_letters):
    for x in woord:
        if x not in geraden_letters:
            woord = woord.replace(x, '_')
    return woord


## Returnt een random gekozen woord met meegegeven moeilijkheidsgraad
def kies_woord(moeilijkheidsgraad):
    woorden_dict = lees_woorden("woorden.txt")
    mogelijkheden = []
    for key in woorden_dict:
        if woorden_dict[key] == moeilijkheidsgraad:
            mogelijkheden.append(key)
    return random.choice(mogelijkheden)


## Main game loop
def speel_sessie():

    # Vraagt om de gewenste moeilijkheidsgraad
    moeilijkheidsgraad = input("What would you like the difficulty to be?: ")

    # Asks user for name, if the input is not equal to string it simply asks again
    naam = input("Please enter your name: ")
    while naam is not str:
        print("This is an invalid name, please try again")
        naam = input("Please enter your name")

    # Kiest een random woord met de juiste moeilijkheidsgraad
    woord = kies_woord(int(moeilijkheidsgraad))

    gamecompletion = False
    geraden_letters = []

    pogingen = max_poginingen(int(moeilijkheidsgraad))
    print(f'You have {pogingen} attempts to guess the word')
    # So long as the attempts dont run out, and the word isn't fully guessed:
    while gamecompletion == False:
        huidige_staat_woord = toon_tussenstand(woord, geraden_letters)
        print(huidige_staat_woord)
        userGuess = input("Guess any letter: ")
        # If the guessed letter is contained within the list of characters in the word
        if pogingen == 0:
            print("You have run out of guesses, feel free to try again, perhaps on a lower difficulty")
            break
        if userGuess in woord:
            geraden_letters.append(userGuess)
            huidige_staat_woord = toon_tussenstand(woord, geraden_letters)
            # If all Unknown letters have been guessed, the user has won and program exits out of the loop
            if "_" not in huidige_staat_woord:
                print("You have won!")
                voeg_score_toe(naam, woord, bereken_score(pogingen, moeilijkheidsgraad))
                gamecompletion = True
            # If the user enters a guess that isn't a string
        elif type(userGuess) != type('d'):
            print("That's not a letter my dear fellow")


            # If the users guess is not contained within the word
        else:
            print("ja rip")
            pogingen = pogingen - 1
            print(f'You have {pogingen} attempts left')
    # Houdt pogingen bij
    # Logt resultaat van gebruiker in scorebestand

