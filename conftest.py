import pytest
from app import JdpuPF

@pytest.fixture
def app():
    return JdpuPF()

@pytest.fixture
def test_client(app):
    return app.test_session()
