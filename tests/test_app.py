import os
import pytest

from unittest.mock import patch
from server.app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@patch.dict(os.environ, {})
def test_index_env_vars_not_set(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Hello, World!<br><br>Here's my secret: not set" == resp.data.decode("utf-8")


@patch.dict(os.environ, {"APP_SECRET": "fakesecret", "APP_MESSAGE": "fakemessage"})
def test_index_env_vars_set(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert "fakemessage<br><br>Here's my secret: fakesecret" == resp.data.decode(
        "utf-8"
    )


@patch("logging.Logger.debug")
def test_log_some_info(mocked_logger, client):
    resp = client.get("/log-some-info")
    mocked_logger.assert_called_with("Some info")
    assert resp.status_code == 200
    assert "Logged 'Some info'" == resp.data.decode("utf-8")
