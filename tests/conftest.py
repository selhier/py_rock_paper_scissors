import pytest

from src.app import create_app


@pytest.fixture
def application():
    return create_app()

@pytest.fixture
def user_id():
    return '20190127'
