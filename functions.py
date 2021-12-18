from definitions import Possibilities as Pb, Players as P, Replies as R
from typing import List
import random

class Game():
    """Runs a game of Rock, Scissors, Paper
    """

    def __init__(self,
    opponent:str,
    player_score:int = 0,
    opponent_score:int = 0,
    game:bool = True,
    weapons:List = []
    ) -> None:
        self.player:str = P.player
        self.player_weapon:str = random.choice(weapons)
        self.opponent:str = opponent
        self.opponent_weapon:str = random.choice(weapons)
        self.player_score:int = player_score
        self.opponent_score:int = opponent_score
        self.game:bool = game
        self.weapons:List = weapons

    #   Main function of the game
    def Play(self):
        while self.game == True:
            self.Weapons()
            outcome = self.Compute_outcome()
            self.Compute_score(outcome)
            self.Output_score()
            self.Continuity()
            
        return self.player_score, self.opponent_score

    #   Choose players weapon and announce the "battle"
    def Weapons(self):
        self.opponent_weapon = input(f"> {self.opponent}, {R.continuation} {', '.join(self.weapons)}: ")
        self.Check_validity()
        print(f"You have chosen {self.opponent_weapon} as the weapon to accompany you in battle!")
        self.player_weapon = random.choice(self.weapons)
        print(f"{self.player} chooses the mightiest of weapons, {self.player_weapon}!")

    #   Check if the chosen weapon is a valid weapon
    def Check_validity(self):
        while self.opponent_weapon not in self.weapons:
            self.opponent_weapon = input(f"> {R.wrong_weapon} ")

    #   Function to decide the outcome
    def Compute_outcome(self) -> str:
        result = ''.join([self.player_weapon, self.opponent_weapon])
        outcome = Pb[result].value
        print(f"{R[outcome].value}")
        return outcome

    #   Function to adjust score for Win, Tie and Loss
    def Compute_score(self, outcome:str) -> None:
        if outcome == 'win':
            self.player_score += 1
        elif outcome == 'loss':
            self.opponent_score += 1
        else:
            pass

    #   Function to print current score
    def Output_score(self) -> None:
        print(f"{R.current_score} {self.player}: {self.player_score} - {self.opponent_score} {self.opponent}")
    
    #   Check if the game continues
    def Continuity(self) -> None:
        response = input(f"{R.status}")
        if response == 'No':
            self.game = False

