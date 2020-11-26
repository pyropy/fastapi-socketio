from setuptools import setup
import os

VERSION = "0.0.4"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="fastapi-socketio",
    description="Easly integrate socket.io with your FastAPI app.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Srdjan Stankovic",
    author_email="stankovic.srdjo@gmail.com",
    url="https://github.com/pyropy/fastapi-socketio",
    project_urls={
        "Issues": "https://github.com/pyropy/fastapi-socketio/issues",
        "CI": "https://github.com/pyropy/fastapi-socketio/actions",
        "Changelog": "https://github.com/pyropy/fastapi-socketio/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["fastapi_socketio"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    tests_require=["fastapi-socketio[test]"],
)
