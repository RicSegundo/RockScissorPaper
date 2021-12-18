import enum
from typing import NamedTuple


class Players(str, enum.Enum):
    """
    Contains the player's names
    """
    player = 'Ricardo'
    opponent = 'Henrique'


class Weapons(str, enum.Enum):
    """
    Contains all possible weapons to choose from
    These must be placed in order of "strength", meaning the
    first one defeats the second, etc.
    """
    Rock        = 'Rock'
    Scissors    = 'Scissors'
    Paper       = 'Paper'


# Define all possible name combinations that would represent a win, tie or loss
# This is useful if we want to extend the game to more weapons
# weapons = [weapon.name for weapon in Weapons]

# possible_outcomes = {}

# for ind, weapon in enumerate(weapons):
#     win_player = weapon + weapons[(ind+1) % len(weapons)]
#     possible_outcomes[win_player] = 'win'
#     tie_player = weapon + weapon
#     possible_outcomes[tie_player] = 'tie'
#     loss_player = weapon + weapons[ind-1]
#     possible_outcomes[loss_player] = 'loss'

# Possibilities = enum.Enum('Possibilities', possible_outcomes)


class Possibilities(str, enum.Enum):
    """
    Contains all the possible combination of "fights" and it's outcome
    """
    RockScissors        = 'win'
    ScissorsPaper       = 'win'
    PaperRock           = 'win'
    RockRock            = 'tie'
    ScissorsScissors    = 'tie'
    PaperPaper          = 'tie'
    ScissorsRock        = 'loss'
    PaperScissors       = 'loss'
    RockPaper           = 'loss'


class OutcomeGenerator(NamedTuple):
    outcome: str
    """
    Generates an action (Win, Tie, Lose) with the possible results
    Args:
        outcome (str): game result
    """


class Replies(str, enum.Enum):
    """
    Contains the text of all the possible outcomes of the game
    plus the score and selection of continue/end game
    """
    opponent        = "Please state your name, Warrior"

    continuation    = "please choose one among"
    wrong_weapon    = "Are you sure about that choice?\nPlease select one among the possible 'weapons' listed above:"

    win             = "Truth has prevailed, and the strongest has won!"
    tie             = "Ahhh, what an unfortunate tie"
    loss            = "Alas, a lucky stroke! You have won this battle, but not the war!"

    current_score   = "The current score is"
    status          = "Would you like to play again? (Yes/No)"
    final           = "Well, it seems that this game has ended!\nThe final score is"

