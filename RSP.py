import random

possibilities = ['Rock', 'Scissors', 'Paper']
Game = True
H_score = 0
R_score = 0

user_input = input("> Hi Henrique, let's play a game!\nPlease choose one among Rock, Scissors and Paper: ")

while Game == True:
    if user_input in possibilities:

        choice = random.choice(possibilities)
        print(f"Tio Ricardo chooses the mightiest of weapons, {choice}!")

        if choice == user_input:
            response = input(f"> Ahhh, what an unfortunate tie!\nWould you like to play again? (Yes/No)\nThe current score is Tio Ricardo: {R_score} - {H_score} Henrique\n")
            if response == 'No':
                Game = False
            else:
                user_input = input("> Please choose one among Rock, Scissors and Paper: ")

        else:
            if choice == 'Rock':
                if user_input == 'Paper':
                    H_score += 1
                    response = input(f"Alas, a lucky stroke! You have won this battle, but not the war!\nWould you like to play again? (Yes/No)\nThe current score is Tio Ricardo: {R_score} - {H_score} Henrique\n")
                    if response == 'No':
                        Game = False
                    else:
                        user_input = input("> Please choose one among Rock, Scissors and Paper: ")
                
                else:
                    R_score += 1
                    response = input(f"Truth has prevailed, and the strongest has won!\nWould you like to play again? (Yes/No)\nThe current score is Tio Ricardo: {R_score} - {H_score} Henrique\n")
                    if response == 'No':
                        Game = False
                    else:
                        user_input = input("> Please choose one among Rock, Scissors and Paper: ")
            
            if choice == 'Scissors':
                if user_input == 'Rock':
                    H_score += 1
                    response = input(f"Alas, a lucky stroke! You have won this battle, but not the war!\nWould you like to play again? (Yes/No)\nThe current score is Tio Ricardo: {R_score} - {H_score} Henrique\n")
                    if response == 'No':
                        Game = False
                    else:
                        user_input = input("> Please choose one among Rock, Scissors and Paper: ")
                
                else:
                    R_score += 1
                    response = input(f"Truth has prevailed, and the strongest has won!\nWould you like to play again? (Yes/No)\nThe current score is Tio Ricardo: {R_score} - {H_score} Henrique\n")
                    if response == 'No':
                        Game = False
                    else:
                        user_input = input("> Please choose one among Rock, Scissors and Paper: ")
            
            if choice == 'Paper':
                if user_input == 'Scissors':
                    H_score += 1
                    response = input(f"Alas, a lucky stroke! You have won this battle, but not the war!\nWould you like to play again? (Yes/No)\nThe current score is Tio Ricardo: {R_score} - {H_score} Henrique\n")
                    if response == 'No':
                        Game = False
                    else:
                        user_input = input("> Please choose one among Rock, Scissors and Paper: ")
                
                else:
                    R_score += 1
                    response = input(f"Truth has prevailed, and the strongest has won!\nWould you like to play again? (Yes/No)\nThe current score is Tio Ricardo: {R_score} - {H_score} Henrique\n")
                    if response == 'No':
                        Game = False
                    else:
                        user_input = input("> Please choose one among Rock, Scissors and Paper: ")

    else:
        user_input = input("> Are you sure about that choice?\nPlease select one among the possible 'weapons' listed above: ")

print(f"Well, it seems that this game has ended! The final score is: Tio Ricardo: {R_score} - {H_score} Henrique")

