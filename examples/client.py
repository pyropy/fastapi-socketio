import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Connected!")

@sio.on('test')
def on_message(data):
    print('Message Received!')
    print(data)

sio.connect('http://127.0.0.1:8000/ws', socketio_path="/ws/socket.io", wait_timeout = 10)
sio.wait()
