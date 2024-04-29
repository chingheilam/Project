"""
Project - Hangman Game
Lam Ching Hei

- This game comprises four key functions:
    - Printing the hangman image.

    - Checking if the user has guessed all the correct letters.

    - Managing the display of letters, tracking correct and incorrect guesses, the number of chances left,
      and the state of the hangman's figure.

    - Selecting a random word from a list of topics, allowing users to choose their preferred theme across
      three game modes.

- Additionally, the game includes four extra features for enhanced gameplay:
    - Unlimited replays: Users can play the game multiple times in one session, with new random elements introduced
      in each round.

    - Multiple difficulty levels: Players can choose from easy, medium, and hard modes to suit their skill level.

    - Enhanced visual presentation: Special attention is given to ensure the game’s output is aesthetically formatted,
      including the hangman image.

    - Robust user input validation: To maintain smooth gameplay, user inputs are carefully checked. If invalid data is
      entered, the input request is repeated until valid information is provided, preventing the game from ending
      prematurely due to incorrect inputs.
"""

import random

def hangman(body):
    """
    Prints the image of the hangman if the user enters an incorrect letter.
    The user only has 7 chances.
    Argument: body (list representing parts of the hangman's body)
    """
    hangman_parts = [
        "     _______________                   ",
        "     |/            |                     ",
        f"     |            {body[0]}             ",
        f"     |            {body[1]}{body[2]}{body[3]}",
        f"     |            {body[4]}            ",
        f"     |            {body[5]} {body[6]}     ",
        "     |                                   ",
        "     |                                   ",
        "     -------------------               \n"
    ]
    print('\n'.join(hangman_parts))


def check_completion(body):
    """
    Checks if the user has entered all the correct letters.
    Arguments: body (current state of word being guessed, with '_' for missing letters)
    Returns True to continue running the rest of the code.
    Returns False to indicate completion and prints the word of congratulations,
    the image of the Hangman alive, and the correct answer.
    """
    return "_" not in body

def hangman_game(word):
    """
    Stores the display letters, correct and wrong answers, calculates the chances left for the user,
    represents the hangman's body in the image, and instructs the user if they enter an incorrect letter or unexpected input.
    Argument: word (the word to be guessed in the game)
    """
    chances = 0
    correct_answer = set(word.upper())
    wrong_answer = set()
    display_letter = ["_" if x.isalpha() else x for x in word]
    hangman_body = ["(_)", "/", "|", "\\", "|", "/", "\\"]
    no_hangman_body = [" "] * 7

    while chances < 7:
        hangman(no_hangman_body)
        print(' '.join(display_letter))
        print("\nIncorrect letters:", ' '.join(wrong_answer))

        answer = input("Enter a letter: ").upper()

        if len(answer) != 1 or not answer.isalpha():
            print("Please enter one letter only! Try again!")
            continue

        if answer in wrong_answer or answer in display_letter:
            print(f"Already guessed the letter: {answer}, please try again!")
            continue

        if answer in correct_answer:
            for i, char in enumerate(word.upper()):
                if char == answer:
                    display_letter[i] = answer
            if check_completion(display_letter):
                print("""
                    Congratulations!
                    You've guessed the word correctly!
                    ____________
                                |/         |
                                |
                                |
                                |         (_)
                                |         \\|/
                                |          |
                                |         / \\
                                ---------------
                    """)
                print(" ".join(display_letter))
                break

        else:
            wrong_answer.add(answer)
            no_hangman_body[chances] = hangman_body[chances]
            chances += 1

            if chances == 7:
                hangman(hangman_body)
                print("""Game Over! 
                  _____                         ____                 
                 / ____|                       / __ \\
                | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
                | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
                | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |
                 \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                 \n The correct word was:""", word.upper())
                break

        print("\033[H\033[J")  # Clear the screen


def main():
    """
        Main function to choose a random word and play the game.
        Prompts the user to select a category and a difficulty level.
        """
    while True:
        print("""\
         _                                              ____________
        | |                                             |/         |  
        | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __   |         (_)
        | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \  |         \|/ 
        | | | | (_| | | | | (_| | | | | | | (_| | | | | |          |
        |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| |         / \\
                            __/ |                       ---------------
                           |___/                        """)
        print("""Rules of the Hangman Game:
        The objective of this game is to guess the word.
        After guessing a word, you are going to guess the
        next one until you guess all the correct letters
        of the word.""")
        print("""Let's begin the game!!!
>->->->-> HANGMAN GAME MENU <-<-<-<-<
Please enter 1: World Capitals 
Please enter 2: Fruits Name
Please enter 3: Cosmetics Brands
Please enter 4 to quit the game""")

        try:
            choice = int(input("Please enter your choice = "))

            if choice == 1:
                mode = int(input("1:Easy 2:Medium 3:Hard "))
                if mode == 1:
                    capitals_easy_mode = ["OTTAWA", "BEIJING", "PARIS", "ROME", "TOKYO", "MEXICO CITY", "SEOUL",
                                          "BANGKOK", "LONDON", "HAVANA", "PYONGYANG", "BERLIN", "ATHENS", "LISBON",
                                          "MOSCOW", "MADRID"]
                    hangman_game(random.choice(capitals_easy_mode))
                elif mode == 2:
                    capitals_medium_mode = ["BUENOS AIRES", "CANBERRA", "BRUSSELS", "BOGOTA", "PRAGUE", "COPENHAGEN",
                                            "CAIRO", "HELSINKI", "NEW DELHI", "JAKARTA", "TEHRAN", "BAGHDAD", "DUBLIN",
                                            "JERUSALEM", "NAIROBI", "AMSTERDAM", "OSLO", "MANILA", "WARSAW", "HANOI",
                                            "ISLAMABAD", "JAKARTA"]
                    hangman_game(random.choice(capitals_medium_mode))
                elif mode == 3:
                    capitals_hard_mode = ["ASUNCION", "CARACAS", "PORT MORESBY", "WELLINGTON", "ANKARA", "TUNIS",
                                          "MONTEVIDEO", "ABU DHABI", "RIYADH", "BUCHAREST", "VALLETTA", "KUALA LUMPUR",
                                          "ANTANANARIVO", "TRIPOLI", "RIGA", "RIGA", "NAIROBI", "PRISTINA",
                                          "TEHRAN", "BUDAPEST", "ADDIS ABABA", "QUITO", "SARAJEVO"]
                    hangman_game(random.choice(capitals_hard_mode))
                else:
                    print("3 modes only, please try again")
                    continue

            elif choice == 2:
                mode = int(input("1:Easy 2:Medium 3:Hard "))
                if mode == 1:
                    fruits_easy_mode = ["APPLE", "ORANGE", "BANANA", "COCONUT", "ORANGE", "PINEAPPLE", "MANGO", "LEMON",
                                        "WATERMELON", "AVOCADO", "BLUEBERRY", "CHERRY", "DRAGON FRUIT", "GRAPES",
                                        "PEACH", "PEAR", "STARFRUIT", "STRAWBERRY", "PASSION FRUIT",
                                        "KIWI", "PLUM", "DATES"]
                    hangman_game(random.choice(fruits_easy_mode))
                elif mode == 2:
                    fruits_medium_mode = ["PAPAYA", "GUAVA", "APRICOTS", "ALMOND", "BARBERRY", "BLACK CURRANT",
                                          "BLACKBERRY", "BREADFRUIT", "CASHEWS", "MULBERRY", "NUT", "OLIVE FRUIT",
                                          "POMEGRANATE", "POMELO", "MUSKMELON", "RED BANANA", "SUGAR CANE", "LOQUAT",
                                          "ELDERBERRY", "MONK FRUIT", "CLOUDBERRY", "PINEBERRY"]
                    hangman_game(random.choice(fruits_medium_mode))
                elif mode == 3:
                    fruits_hard_mode = ["CUSTARD APPLE", "GOOSEBERRY", "JACKFRUIT", "KUMQUAT", "LYCHEE", "RASPBERRY",
                                        "CRANBERRY", "DAMSON", "FEIJOA", "GOGI BERRY", "HONEY BERRY", "KIWANO",
                                        "MANGOSTEEN", "MIRACLE FRUIT", "NANCE", "SATSUMA", "MANDARIN"]
                    hangman_game(random.choice(fruits_hard_mode))
                else:
                    print("3 modes only, please try again")
                    continue

            elif choice == 3:
                mode = int(input("1:Easy 2:Medium 3:Hard "))
                if mode == 1:
                    cosmetics_easy_mode = ["LOREAL", "LANCOME", "SEPHORA", "MAC", "NEUTROGENA", "CLINIQUE",
                                           "MAYBELLINE","ESTEE LAUDER","CHANEL","CHRISTIAN DIOR", "NARS", "URBAN DECAY",
                                           "NYX", "MAKE UP FOR EVER", "BOBBI BROWN", "ARMANI", "CALVIN KLEIN",
                                           "YVES SAINT LAURENT", "NIVEA", "SHISEIDO", "DOVE", "GIVENCHY",
                                           "LAURA MERCIER", "TOM FORD", "LAMER"]
                    hangman_game(random.choice(cosmetics_easy_mode))
                elif mode == 2:
                    cosmetics_medium_mode = ["OLAY", "CLINIQUE", "GARNIER", "PANTENE", "CLARINS", "BENEFIT",
                                             "SCHWARZKOPF", "ELVIVE", "LOCCITANE", "NATURA", "LUX", "INNISFREE",
                                             "SUNSILK", "BIORE", "KOSE", "SULWHASOO", "AVON", "CHANDO", "COTA",
                                             "REJOICE", "COVERGIRL", "ELF", "COLOURPOP", "TOO FACED", "FENTY BEAUTY",
                                             "ELIZABETH ARDEN"]
                    hangman_game(random.choice(cosmetics_medium_mode))
                elif mode == 3:
                    cosmetics_hard_mode = ["ORIFLAME", "REVLON", "POLA", "SMASHBOX", "BARE MINERALS", "STILA", "BECCA",
                                           "MARC JACOBS", "KAT VON D", "HOURGLASS", "WET N WILD", "MAKEUP REVOLUTION",
                                           "LIME CRIME", "SUGARPILL", "BUTTER LONDON", "EOS"]
                    hangman_game(random.choice(cosmetics_hard_mode))
                else:
                    print("3 modes only, please try again")
                    continue

            elif choice == 4:
                print("Thank you for playing!Bye!"),
                break

            else:
                print()
                print("Sorry! We don't have this topic!!! Please try again.\n")
                continue

        except ValueError:
            print()
            print("Please follow the instruction! Only enter the number! Please try it again.\n")
            continue

if __name__=="__main__":
    main()


