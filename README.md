# fastapi-socketio

[![PyPI](https://img.shields.io/pypi/v/fastapi-socketio.svg)](https://pypi.org/project/fastapi-socketio/)
[![Changelog](https://img.shields.io/github/v/release/pyropy/fastapi-socketio?label=changelog)](https://github.com/pyropy/fastapi-socketio/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/pyropy/fastapi-socketio/blob/main/LICENSE)

Easly integrate socket.io with your FastAPI app.

## Installation

Install this plugin using `pip`:

    $ pip install fastapi-socketio

## Usage

To add SocketIO support to FastAPI all you need to do is import `SocketManager` and pass it `FastAPI` object.

```python
# app.py
from fastapi import FastAPI
from fastapi_socketio import SocketManager

app = FastAPI()
socket_manager = SocketManager(app=app)
```


Now you can use SocketIO directly from your `FastAPI` app object.
```python
# socket_handlers.py
from .app import app

@app.sio.on('join')
async def handle_join(sid, *args, **kwargs):
    await app.sio.emit('lobby', 'User joined')

```

Or you can import `SocketManager` object that exposes most of the SocketIO functionality.

```python
# socket_handlers2.py
from .app import socket_manager as sm

@sm.on('leave')
async def handle_leave(sid, *args, **kwargs):
    await sm.emit('lobby', 'User left')

```

### Working with distributed applications

When working with distributed applications, it is often necessary to access the functionality of the Socket.IO from multiple processes. As a solution to the above problems, the Socket.IO server can be configured to connect to a message queue such as `Redis` or `RabbitMQ`, to communicate with other related Socket.IO servers or auxiliary workers.

Refer this link for more details https://python-socketio.readthedocs.io/en/latest/server.html#using-a-message-queue

```python
# app.py
import socketio

from fastapi import FastAPI
from fastapi_socketio import SocketManager

app = FastAPI()
redis_manager = socketio.AsyncRedisManager('redis://')

socket_manager = SocketManager(app=app, client_manager=redis_manager)
```

### Emitting from external process

```python
# emitter.py
import socketio

external_sio = socketio.RedisManager('redis://', write_only=True) # connect to the redis queue as an external process
external_sio.emit('my event', data={'foo': 'bar'}, room='my room') # emit an event
```
## Development

To contribute to this library, first checkout the code. Then create a new virtual environment:

    cd fastapi-socketio
    python -mvenv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and tests:

    pip install -e '.[test]'

To run the tests:

    pytest


## Run example

To run the examples simply run:

```bash
PYTHONPATH=. python examples/app.py
```

Before running example make sure you have all dependencies installed.

## Contributors

For list of contributors please reefer to CONTRIBUTORS.md file in this repository.