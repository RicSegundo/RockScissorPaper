import enum
import time
from typing import List


class Players(str, enum.Enum):
    """
    Contains the player's names
    """
    player      = 'Ricardo'
    opponent    = 'Henrique'


class Weapon():
    """Generates the objects for all possible weapons,
    with the __gt__ method allowing for the comparison

    Args:
        name (str): chosen weapon
        beats (list): list of weapons it beats
    """
    def __init__(self, name:str, beats:List = []):
        self.name = name
        self.beats = beats

    def __gt__(self, other:str) -> bool:
        if other.name in self.beats:
            return 'win'
        elif self.name == other.name:
            return 'tie'
        else:
            return 'loss'


## Implement unit tests for the game and functions

#   Define the Weapons objects
"""A Simple Way to Remember Who Wins
Scissors cuts paper. 
Paper covers rock.
Rock crushes lizard. 
Lizard poisons Spock. 
Spock smashes scissors. 
Scissors decapitates lizard.
Lizard eats paper. 
Paper disproves Spock.
Spock vaporizes rock. 
Rock crushes scissors.
"""
rock        = Weapon('rock', ['scissors', 'lizard'])
scissors    = Weapon('scissors', ['paper', 'lizard'])
paper       = Weapon('paper', ['rock', 'spock'])
spock       = Weapon('spock', ['scissors', 'rock'])
lizard      = Weapon('lizard', ['spock', 'paper'])


class Weapons(enum.Enum):
    """
    Contains all possible weapons to choose from
    """
    rock        = rock
    scissors    = scissors
    paper       = paper
    spock       = spock
    lizard      = lizard


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
    wrong_status    = "This choice doesn't exist warrior, you need to choose Yes or No !"
    final           = "Well, it seems that this game has ended!\nThe final score is"


#   define a printing function that slowly outputs the text
def print_slowly(text:str, line_break_delay:float = 1.5) -> None:
    print(text)
    time.sleep(line_break_delay)

