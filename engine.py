from definitions import Players as P, Replies as R, Weapons as W
import functions as F


def game_engine(opponent:str = P.opponent):
    #   Add initial variables, values and constants
    #   If no name is passed, the default is Henrique

    #   Get all possible weapons from the definitions file
    weapons = [weapon.name for weapon in W]

    instance = F.Game(opponent = opponent, weapons = weapons)
    player_final_score, opponent_final_score = instance.Play()

    print(f"{R.final} {P.player} {player_final_score} - {opponent_final_score} {opponent}")

