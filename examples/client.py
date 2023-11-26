import socketio

sio = socketio.Client()


@sio.event
def connect():
    print("Connected!")


@sio.on('test')
def on_message(data):
    print('Message Received! >> ', data)
    sio.emit('test', 'Hello world!')


sio.connect('http://127.0.0.1:8000')
sio.wait()
