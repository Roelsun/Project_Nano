# Imports to allow access to the other modules/games
from Galgje import galgje as Galgje
from NumberGuessingGame import number_guessing_game as NumberGuessingGame


def validatie(keuzedict, uinput):
    try:
        if int(uinput) in keuzedict:
            return uinput
    except ValueError:
        pass

    while uinput not in keuzedict:
        try:
            print('==Err==')
            if int(uinput) in keuzedict:
                return uinput

        except ValueError:
            print("Dat is niet een nummer, probeer het nog een keer")
        for x in keuzedict.values():
            print(x)
        uinput = input("Please enter the number BEFORE your choice: ")


def main_menu():
    keuzedict = {1: "1) Het Galgje Menu", 2: "2) Een rondje number Guessing", 3: "3) Leaderboards", 4: "4) Exit"}

    for x in keuzedict.values():
        print(x)
    keuze = input("Please enter the number that is before your choice: ")
    keuze = validatie(keuzedict, keuze)

    match int(keuze):
        case 1:
            # GalgjeMenu
            secundaire_galgje_menu()
            pass
        case 2:
            # A round of Number Guessing -> raad_het_nummer vanuit "NumberGuessingGame"
            NumberGuessingGame.raad_het_nummer()
            pass
        case 3:
            # Leaderboards ->
            validchoice = False
            while validchoice == False:

                optionslist = ['Galgje scores', "Number_guessing_game Scores"]

                for x in optionslist:
                    print(x)

                keuze = input("Please enter the number that is before your choice: ")
                try:
                    keuze = int(keuze)
                    if keuze in [1, 2, 3, 4]:
                        validchoice = True
                except ValueError:
                    print("That input was invalid, please try again")

                match keuze:
                    case 1:
                        score_lijst = Galgje.lees_scores_in()
                        for x in score_lijst:
                            print(x)
                    case 2:
                        score_lijst = NumberGuessingGame.lees_scores_in()
                        for x in score_lijst:
                            print(x)
            pass
        case 4:
            exit()


def introductie():
    print("Introductory tomfoolery")
    pass


def secundaire_galgje_menu():
    keuzedict = {1: "1) Speel een potje galgje", 2: "2) Verwijder woorden uit de woordenlijst",
                 3: "3) Voeg woord toe aan de woordenlijst",
                 4: '4) Toon woorden in woordenlijst', 5: "5) Stop het process"}

    for x in keuzedict.values():
        print(x)
    keuze = input("Please enter the number that is before your choice: ")
    keuze = validatie(keuzedict, keuze)

    match int(keuze):
        case 1:
            # Speel een potje galgje
            Galgje.speel_sessie()

        case 2:
            # Verwijder een woord uit de woordenlijst
            Galgje.haal_woorden_weg()

        case 3:
            # Voeg woord toe aan woordenlijst
            Galgje.voeg_woorden_toe('../woorden.txt', Galgje.lees_woorden('../woorden.txt'))

        case 4:
            # Toont de volledige woordenlijst
            dict = Galgje.lees_woorden('../woorden.txt')
            for x in dict:
                print(x)
        case 5:
            # Stop het process
            exit()
    pass


def leaderboards():
    keuzedict = {1: "1) Galgje", 2: "2) Number Guessing Game", 3: "3) WIP", 4: "4) EXIT"}

    keuze = input("Please enter the number that is before your choice: ")
    keuze = validatie(keuzedict, keuze)

    returnlist = []
    match int(keuze):
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass

    for x in returnlist:
        print(x)


main_menu()
