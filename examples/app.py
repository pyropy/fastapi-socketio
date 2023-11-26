from fastapi import FastAPI
from fastapi_socketio import SocketManager

app = FastAPI()
sio = SocketManager(app=app)


@sio.event
async def connect(sid, *args, **kwargs):
    print(f"[{sid}] Connected!")
    await sio.emit('test', 'Hello world!')


@sio.on('test')
async def test(sid, data, **kwargs):
    print(f'[{sid}] Message Received! >> ', data)


if __name__ == '__main__':
    import logging
    import sys

    logging.basicConfig(level=logging.DEBUG,
                        stream=sys.stdout)

    import uvicorn

    uvicorn.run("app:app", host='0.0.0.0', port=8000)
