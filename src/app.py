from datetime import datetime

from aiohttp import web

from src.game import create_game_room, get_available_room


async def handler_game_start(request: web.Request) -> web.Response:
    body = await request.json()

    if 'user_id' not in body:
        return web.Response(status=422)

    room = get_available_room() or create_game_room(datetime.now(), body['user_id'])
    return web.json_response(data={
        'user_id': body['user_id'],
        'game_id': room['id']
    }, status=202)


def create_app():
    application = web.Application()
    application.add_routes([
        web.post('/game', handler_game_start)
    ])

    return application
