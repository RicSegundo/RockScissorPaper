from definitions import Players as P, Replies as R, Weapons as W, print_slowly
import functions as F
from typing import List


def game_engine(opponent:str = P.opponent) -> None:
    #   Add initial variables, values and constants
    #   If no name is passed, the default is Henrique

    #   Get all possible weapons from the definitions file
    weapons:List = [weapon.name for weapon in W]

    instance:object = F.Game(opponent = opponent, weapons = weapons)
    
    player_final_score:int; opponent_final_score:int
    player_final_score, opponent_final_score = instance.play()

    print_slowly(f"{R.final} {P.player} {player_final_score} - {opponent_final_score} {opponent}")

