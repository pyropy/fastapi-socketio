from typing import Union

import socketio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


class SocketManager(socketio.AsyncServer):
    """
    Integrates SocketIO with FastAPI app.
    Adds `sio` property to FastAPI object (app).

    Default mount location for SocketIO app is at `/ws`
    and defautl SocketIO path is `socket.io`.
    (e.g. full path: `ws://www.example.com/ws/socket.io/)

    SocketManager exposes basic underlying SocketIO functionality

    e.g. emit, on, send, call, etc.
    """

    def __init__(
            self,
            app: FastAPI,
            mount_location: str = "/ws",
            socketio_path: str = "socket.io",
            cors_allowed_origins: Union[str, list] = '*',
            async_mode: str = "asgi",
            **kwargs
    ) -> None:
        middleware = next((x for x in app.user_middleware if issubclass(x.cls, CORSMiddleware)), None)
        if middleware:
            cors_allowed_origins = middleware.options.get("allow_origins", "*")
        super().__init__(cors_allowed_origins=cors_allowed_origins, async_mode=async_mode, **kwargs)
        self._app = socketio.ASGIApp(
            socketio_server=self, socketio_path=socketio_path
        )

        app.mount(mount_location, self._app)
        app.add_route(f"/{socketio_path}/", route=self._app, methods=["GET", "POST"])
        app.add_websocket_route(f"/{socketio_path}/", self._app)
        app.sio = self

    def is_asyncio_based(self) -> bool:
        return True
