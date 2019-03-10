import pytest

from datetime import datetime
from src import game


def test_game_id_correctly_generated():
    current_time = datetime.now()

    assert game.generate_game_id(current_time) == current_time.strftime('%Y%m%d%H%M%S')

def test_new_game_creation_returns_game_room(owner_id):
    current_time = datetime.now()

    room = game.create_game_room(current_time, owner_id)
    assert isinstance(room, dict)

def test_new_game_is_persisted(owner_id):
    current_time = datetime.now()
    game.create_game_room(current_time, owner_id)

    room = game.GAMES[0]
    assert isinstance(room, dict)
    assert 'id' in room and room['id'] == current_time.strftime('%Y%m%d%H%M%S')
    assert 'owner' in room and room['owner'] == owner_id
    assert 'rival' in room and room['rival'] is None

def test_new_game_is_waiting_for_next_player(owner_id):
    current_time = datetime.now()
    game.create_game_room(current_time, owner_id)

    room = game.get_available_room()
    assert room is not None


def test_player_can_join_available_room(owner_id, rival_id):
    current_time = datetime.now()
    game.create_game_room(current_time, owner_id)

    room = game.get_available_room()

    try:
        assert not game.is_rival_in_room(room)
        game.join_game_room(room, rival_id)
        assert game.is_rival_in_room(room)
    except game.RoomFullError:
        pytest.fail("Game room is said to be full when it should not")

def test_player_can_not_join_full_room(owner_id, rival_id):
    current_time = datetime.now()
    game.create_game_room(current_time, owner_id)

    room = game.get_available_room()

    game.join_game_room(room, rival_id)
    with pytest.raises(game.RoomFullError):
        game.join_game_room(room, '9182631782')

def test_game_room_is_ready_to_play_after_players_joined(owner_id, rival_id):
    current_time = datetime.now()
    room = game.create_game_room(current_time, owner_id)
    game.join_game_room(room, rival_id)
    assert game.room_is_ready(room)
