from typing import List, TypeVar, Dict
from datetime import datetime

Room = TypeVar('Room', bound=Dict)
GAMES: List[Room] = []


def generate_game_id(time: datetime) -> str:
    return time.strftime('%Y%m%d%H%M%S')

def create_game_room(time: datetime, owner: str) -> Room:
    room: Room = {
        'id': time.strftime('%Y%m%d%H%M%S'),
        'owner': owner,
        'rival': None
    }
    GAMES.append(room)
    return room

def get_available_room() -> Room:
    for game in GAMES:
        if game['rival'] is None:
            return game
    return None

def join_game_room(room: Room, rival_id: str):
    if is_rival_in_room(room):
        raise RoomFullError

    room['rival'] = rival_id

def is_rival_in_room(room: Room) -> bool:
    return room['rival'] is not None

def room_is_ready(room: Room):
    return room['owner'] is not None and room['rival'] is not None

class RoomFullError(Exception):
    ...
