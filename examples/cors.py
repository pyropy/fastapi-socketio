from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from fastapi_socketio import SocketManager

app = FastAPI()
# Adding the CORS middleware will overwrite SocketManager's CORS settings
# Make sure to add the CORS middleware before SocketManager
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
sio = SocketManager(app=app, cors_allowed_origins="*")


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("examples.cors:app", host='0.0.0.0', port=8000)
