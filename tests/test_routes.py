import json
import time

import pytest
from aiohttp import client, web


async def test_start_game_succeeds_when_passed_a_user_id(aiohttp_client, application, owner_id):
    client = await aiohttp_client(application)
    response: client.ClientResponse = await client.post('/game', json={
        'user_id': owner_id
    })

    assert response.status == 202

async def test_start_game_fails_without_user_id(aiohttp_client, application):
    client = await aiohttp_client(application)
    response: client.ClientResponse = await client.post('/game', json={})

    assert response.status == 422

async def test_start_game_responds_with_user_and_game_id(aiohttp_client, application, owner_id):
    client = await aiohttp_client(application)
    response: client.ClientResponse = await client.post('/game', json={
        'user_id': owner_id
    })
    body = await response.json()

    assert 'user_id' in body
    assert 'game_id' in body

async def test_start_game_user_id_matches_received(aiohttp_client, application, owner_id):
    client = await aiohttp_client(application)
    response: client.ClientResponse = await client.post('/game', json={
        'user_id': owner_id
    })
    body = await response.json()

    assert body['user_id'] == owner_id

async def test_start_game_game_id_generated(aiohttp_client, application, owner_id):
    client = await aiohttp_client(application)
    response: client.ClientResponse = await client.post('/game', json={
        'user_id': owner_id
    })
    body = await response.json()

    assert body['game_id'] is not None
    assert len(body['game_id']) == 14

async def test_start_game_matches_two_players(aiohttp_client, application, owner_id):
    client = await aiohttp_client(application)
    user1_response: client.ClientResponse = await client.post('/game', json={
        'user_id': owner_id
    })
    time.sleep(1)
    user2_response: client.ClientResponse = await client.post('/game', json={
        'user_id': '73728467'
    })
    body1 = await user1_response.json()
    body2 = await user2_response.json()

    assert body1['game_id'] == body2['game_id']

async def test_game_is_ready(aiohttp_client,application):
    ...
