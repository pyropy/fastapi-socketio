from fastapi_socketio import example_function


def test_example_function():
    assert example_function() == 2
