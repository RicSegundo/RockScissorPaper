import enum
import time
from typing import List
from dataclasses import dataclass


class Players(str, enum.Enum):
    """
    Contains the player's names
    """
    player      = 'Ricardo'
    opponent    = 'Luís'
    
    def __str__(self) -> str:
        return self.value


@dataclass
class Weapon():
    """Generates the objects for all possible weapons,
    with the __gt__ method allowing for the comparison

    Args:
        name (str): chosen weapon
        beats (list): list of weapons it beats
    """
    name: str
    beats: List

    def __gt__(self, other: 'Weapon') -> str:
        if other.name in self.beats:
            return 'win'
        elif self.name == other.name:
            return 'tie'
        else:
            return 'loss'


## Implement unit tests for the game and functions
## Define return on every function

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
rock: object     = Weapon('rock', ['scissors', 'lizard'])
scissors: object = Weapon('scissors', ['paper', 'lizard'])
paper: object    = Weapon('paper', ['rock', 'spock'])
spock: object    = Weapon('spock', ['scissors', 'rock'])
lizard: object   = Weapon('lizard', ['spock', 'paper'])


class NoValue(enum.Enum):
    """
    Added to comply with the documentation when passing objects as values
    onto an enumerator:
    https://docs.python.org/3/library/enum.html#using-object
    """
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)

class Weapons(NoValue, enum.Enum):
    """
    Contains all possible weapons to choose from
    """
    rock        = rock
    scissors    = scissors
    paper       = paper
    spock       = spock
    lizard      = lizard
    
    def __str__(self) -> str:
        return self.name


class Replies(str, enum.Enum):
    """
    Contains the text of all the possible outcomes of the game
    plus the score and selection of continue/end game
    """
    opponent        = "Please state your name, Warrior"

    continuation    = "please choose one among"
    wrong_weapon    = "Are you sure about that choice?\nPlease select one among the possible 'weapons' listed above:"

    win             = "Truth has prevailed, and the strongest has won!"
    tie             = "Ah, what an unfortunate tie"
    loss            = "Alas, a lucky stroke! You have won this battle, but not the war!"

    current_score   = "The current score is"
    status          = "Would you like to play again? (Yes/No)"
    wrong_status    = "This choice doesn't exist warrior, you need to choose Yes or No !"
    final           = "Well, it seems that this game has ended!\nThe final score is"
    
    def __str__(self) -> str:
        return self.value


#   define a printing function that slowly outputs the text
def print_slowly(text: str, line_break_delay: float = 1.5) -> None:
    """Function to reduce the speed when multiple text blocks are printed
    Introduces a delay after printing each text

    Args:
        text (str): sentence to be printed
        line_break_delay (float, optional): Delay after printing the text. Defaults to 1.5 seconds.
    """
    print(text)
    time.sleep(line_break_delay)

