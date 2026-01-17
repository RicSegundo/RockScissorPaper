from definitions import Replies as R
import engine

opponent_name: str = input(f"> {R.opponent}\n")

engine.game_engine(opponent=opponent_name)
