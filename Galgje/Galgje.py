# Apollo (Roel Zondag)
# Functie om de woorden uit een txt bestand in te lezen, en op te slaan als dictionary
import random

#todo, spendeer 15 minuten met alle comments in het nederlands of in het engels te zetten ipv het wisselend te laten staan
#todo, spendeer 15 minuten met comments toevoegen aan functies die ze nog missen
#todo, spendeer 15 minuten met uitzoeken welke functionaliteit ik nog kan toevoegen aan dit onderdeel van p Nano

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
    # Todo; Add a functionality to have an easier/well formatted final check
    done = False
    while not done:
        uinput = input("Please enter any word to add it to the list of possibilities, or done when you are done making additions")
        if uinput == "done":
            print("Let us briefly go trough the list to check if you still wish to keep all current entries")
            done = True
        elif uinput:
            dict.update({uinput : 0})
        else:
            print("Invalid input, try again")

    file = open(bestaandsnaam, 'w+')
    for x in dict:
        print(x)
        confirmation = input("Do you wish to add/keep this word? Enter y/n to answer")
        if(confirmation == "y"):
            file.write(f'{x} \n')
            print("Word Updated successfully")
    print("List updated successfully")


voeg_woorden_toe("woorden.txt", lees_woorden("woorden.txt"))

#
def haal_woorden_weg(bestandsnaam):
    # Todo: check whether the function's current functionality is complete
    # Todo, write content to file after having gone trough all the options?\

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

def max_poginingen(moeilijkheidsgreaad):
    match moeilijkheidsgreaad:
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
    file = open("score.txt", "r+")
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
    # Todo: Add the functionality to calculate and log scores using the function defined above
    # Todo: Write out the core gameplayloop i wish this function to fulfil, in schrift/bavblok
    # Vraagt om de gewenste moeilijkheidsgraad
    moeilijkheidsgraad = input("What would you like the difficulty to be?: ")
    # Kiest een random word met de juiste moeilijkheidsgraad
    woord = kies_woord(int(moeilijkheidsgraad))

    gamecompletion = False
    geraden_letters = []

    while gamecompletion == False:
        huidige_staat_woord = toon_tussenstand(woord, geraden_letters)
        print(huidige_staat_woord)
        userGuess = input("Guess any letter")
        if userGuess in woord:
            geraden_letters.append(userGuess)
            huidige_staat_woord = toon_tussenstand(woord, geraden_letters)
            if "_" not in huidige_staat_woord:
                print("You have won!")
                gamecompletion = True
        elif type(userGuess) != type('d'):
            print("That's not a letter my dear fellow")
        else:
            print("ja rip")
    # Houdt pogingen bij
    # Logt resultaat van gebruiker in scorebestand
    pass
