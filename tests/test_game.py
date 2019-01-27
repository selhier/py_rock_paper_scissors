from datetime import datetime
from src.game import GAMES, generate_game_id, create_game_room, get_available_room


def test_game_id_correctly_generated():
    current_time = datetime.now()

    assert generate_game_id(current_time) == current_time.strftime('%Y%m%d%H%M%S')

def test_new_game_creation_returns_game_id(user_id):
    current_time = datetime.now()

    assert create_game_room(current_time, user_id) == current_time.strftime('%Y%m%d%H%M%S')

def test_new_game_is_persisted(user_id):
    current_time = datetime.now()
    create_game_room(current_time, user_id)

    game = GAMES[0]
    assert isinstance(game, dict)
    assert 'id' in game and game['id'] == current_time.strftime('%Y%m%d%H%M%S')
    assert 'owner' in game and game['owner'] == user_id
    assert 'rival' in game and game['rival'] is None

def test_new_game_is_waiting_for_next_player(user_id):
    current_time = datetime.now()
    create_game_room(current_time, user_id)

    game = get_available_room()
    assert game is not None
