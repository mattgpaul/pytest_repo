import pytest


@pytest.fixture(scope='session')
def class_connection():
    connection = ...
    port = ...
    with connection.connect(port) as conn:
        yield conn