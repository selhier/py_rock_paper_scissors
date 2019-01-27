from datetime import datetime

GAMES = []


def generate_game_id(time: datetime) -> str:
    return time.strftime('%Y%m%d%H%M%S')

def create_game_room(time: datetime, owner: str):
    game_id = time.strftime('%Y%m%d%H%M%S')
    GAMES.append({
        'id': game_id,
        'owner': owner,
        'rival': None
    })
    return game_id

def get_available_room():
    for game in GAMES:
        if game['rival'] is None:
            return game
    return None
