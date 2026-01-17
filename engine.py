from definitions import Players as P, Replies as R, Weapons as W, print_slowly
import functions as F
from typing import List


def game_engine(opponent: str = str(P.opponent)) -> None:
    """Main game engine function
    
    Args:
        opponent (str): name of the opponent. Defaults to P.opponent value.
    """
    #   Get all possible weapons from the definitions file
    weapons: List[str] = [weapon.name for weapon in W]

    instance: F.Game = F.Game(opponent=opponent, weapons=weapons)
    
    player_final_score: int
    opponent_final_score: int
    player_final_score, opponent_final_score = instance.play()

    print_slowly(f"{R.final} {P.player} {player_final_score} - {opponent_final_score} {opponent}")

