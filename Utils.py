
from typing import Dict

score_board = {}

def update_score(user_name: str, score: int) -> Dict[str, int]:
    score_board[user_name] = score
    return score_board
