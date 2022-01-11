from typing import List, Tuple
import random
from definitions import Weapons as W, Players as P, Replies as R, print_slowly


class Game():
    """Runs a game of Rock, Scissors, Paper, Spock, Lizard
    
    Args:
        opponent (str): name of the opponent (optional)

    Returns:
        object: instance of a game of Rock, Scissors, Paper, Spock, Lizard
    """

    def __init__(self,
    opponent:str,
    player_score:int = 0,
    opponent_score:int = 0,
    game_on:bool = True,
    weapons:List = []
    ) -> None:
        self.player:str = P.player
        self.player_weapon:str = random.choice(weapons)
        self.opponent:str = opponent
        self.opponent_weapon:str = random.choice(weapons)
        self.player_score:int = player_score
        self.opponent_score:int = opponent_score
        self.game_on:bool = game_on
        self.weapons:List = weapons

    #   Main function of the game
    def play(self) -> Tuple[int, int]:
        while self.game_on == True:
            self.player_weapons()
            outcome = self.compute_outcome()
            self.compute_score(outcome)
            self.output_score()
            self.continuity()
            
        return self.player_score, self.opponent_score

    #   Choose players weapon and announce the "battle"
    def player_weapons(self) -> None:
        self.opponent_weapon = input(f"> {self.opponent}, {R.continuation} {', '.join(map(str.capitalize, self.weapons))}:\n").lower()
        self.check_validity()
        print_slowly(f"You have chosen {self.opponent_weapon.capitalize()} as the weapon to accompany you in battle!")
        self.player_weapon = random.choice(self.weapons)
        print_slowly(f"{self.player} chooses the mightiest of weapons, {self.player_weapon.capitalize()}!")

    #   Check if the chosen weapon is a valid weapon
    def check_validity(self) -> None:
        while self.opponent_weapon not in self.weapons:
            self.opponent_weapon = input(f"> {R.wrong_weapon}\n")

    #   Function to decide the outcome
    def compute_outcome(self) -> str:
        player_weapon = W[self.player_weapon].value
        opponent_weapon = W[self.opponent_weapon].value
        outcome = player_weapon > opponent_weapon
        print_slowly(f"{R[outcome].value}")
        return outcome

    #   Function to adjust score for Win, Tie and Loss
    def compute_score(self, outcome:str) -> None:
        if outcome == 'win':
            self.player_score += 1
        elif outcome == 'loss':
            self.opponent_score += 1

    #   Function to print_slowly current score
    def output_score(self) -> None:
        print_slowly(f"{R.current_score} {self.player}: {self.player_score} - {self.opponent_score} {self.opponent}")
    
    #   Check if the game continues
    def continuity(self) -> None:
        response = input(f"{R.status}\n").lower()
        while response not in ['yes', 'no']:
            response = input(f"{R.wrong_status}\n").lower()
        if response == 'no':
            self.game_on = False

