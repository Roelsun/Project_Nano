# Imports to allow access to the other modules/games
from Galgje import galgje as Galgje
from NumberGuessingGame import number_guessing_game as NumberGuessingGame


def main_menu():
    # Todo: Define initial print statements within a seprate "Introduction" to provide an overview of the relevant options
    # Todo: Define the initial match statement structure for the mainmenu
    # Todo: Add the function calls to the match statement below

    validchoice = False
    keuze = ""
    while validchoice == False:
        optionslist = ["1) Het Galgje Menu", "2) A rond of number Guessing", "3) Leaderboards", "4) Exit"]

        for x in optionslist:
            print(x)

        keuze = input("Please enter the number that is before your choice")
        try:
            keuze = int(keuze)
            if keuze in [1,2,3,4]:
                validchoice = True
        except ValueError:
            print("That input was invalid, please try again")

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
            pass
        case 4:
            pass


    print("test")
    """
        1) Galgje_Menu
		2) Een rondje NumberGuessing spelen
			1) Moeilijkheidsgraad
		3) Score's Inzien van Zowel Galgje als NumberGuessing
		4) Stoppen

    """

    uChoice = input("Please choose one of the listed options: ")
    match uChoice:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
    # etc
    pass


def introductie():
    print("Introductory tomfoolery")
    pass


def secundaire_galgje_menu():
    # todo: Define the initial list of options that need to be available
    # todo: Define the initial input statement to acess the user's choice
    # todo: Set up a match statement for the choices, initially with simple pass statements, function calls come later
    menuOpties = ["1) Speel een potje galgje", "2) Verander de moeilijkheid", "3) Verwijder een woord uit de woordenlijst", "4) Voeg woord toe aan de woordenlijst",
                  '5) Toon aantal woorden in woordenlijst', "6) Stop het process"]
    print("The following are the various options available related to hangman:")
    for x in menuOpties:
        print(f"{x}")
    Galgje.lees_woorden("woorden.txt")
    uChoice = input("Please enter the number that relates to your choice")
    """	1) Speel een sessie  
	    2) Kies moeilijkheid
		3) Verwijder een woord uit de woordenlijst
		4) Voeg woord toe aan de woordenlijst
		5) Toon aantal woorden in de woordenlijst
		6) Stoppen
	"""

    pass
secundaire_galgje_menu()