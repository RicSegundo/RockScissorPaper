import random

#   Add initial functions, for Win, Tie and Loss

def Win(player_score, opponent_score):
    player_score += 1
    response = input(f"Truth has prevailed, and the strongest has won!\nWould you like to play again? (Yes/No)\nThe current score is Tio Ricardo: {player_score} - {opponent_score} Henrique\n")
    if response == 'No':
        game = False
        user_input = None
    else:
        user_input = input("> Please choose one among Rock, Scissors and Paper: ")
        game = True
    return player_score, game, user_input


def Loss(player_score, opponent_score):
    opponent_score += 1
    response = input(f"Alas, a lucky stroke! You have won this battle, but not the war!\nWould you like to play again? (Yes/No)\nThe current score is Tio Ricardo: {player_score} - {opponent_score} Henrique\n")
    if response == 'No':
        game = False
        user_input = None
    else:
        user_input = input("> Please choose one among Rock, Scissors and Paper: ")
        game = True
    return opponent_score, game, user_input


def Tie(player_score, opponent_score):
    response = input(f"> Ahhh, what an unfortunate tie!\nWould you like to play again? (Yes/No)\nThe current score is Tio Ricardo: {player_score} - {opponent_score} Henrique\n")
    if response == 'No':
        game = False
        user_input = None
    else:
        user_input = input("> Please choose one among Rock, Scissors and Paper: ")
        game = True
    return game, user_input


#   Add initial variables, values and constants

possibilities = ['Rock', 'Scissors', 'Paper']
Game = True
H_score = 0
R_score = 0

#   Start game by getting the initial user_input

user_input = input("> Hi Henrique, let's play a game!\nPlease choose one among Rock, Scissors and Paper: ")

while Game == True:
    if user_input in possibilities:

        choice = random.choice(possibilities)
        print(f"Tio Ricardo chooses the mightiest of weapons, {choice}!")

        if choice == user_input:
            Game, user_input = Tie(R_score, H_score)

        elif (choice == 'Rock' and user_input == 'Paper') or (choice == 'Scissors' and user_input == 'Rock') or (choice == 'Paper' and user_input == 'Scissors'):
            H_score, Game, user_input = Loss(R_score, H_score)
        
        else:
            R_score, Game, user_input = Win(R_score, H_score)

    else:
        user_input = input("> Are you sure about that choice?\nPlease select one among the possible 'weapons' listed above: ")

print(f"Well, it seems that this game has ended! The final score is: Tio Ricardo: {R_score} - {H_score} Henrique")

