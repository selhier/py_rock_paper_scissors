import pytest

from src.app import create_app
from src import game

@pytest.fixture
def application():
    return create_app()

@pytest.fixture
def owner_id():
    return '20190127'

@pytest.fixture
def rival_id():
    return '73728467'

@pytest.fixture(autouse=True)
def clear():
    game.GAMES = []
    yield
