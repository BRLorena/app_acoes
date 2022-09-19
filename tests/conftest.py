import os

DATABASE_URL = 'sqlite:///testedb.sqlite'
os.environ['DATABASE_URL'] = DATABASE_URL
os.environ['TEST_DATABASE'] = 'true'

from typing import Generator

import pytest
from app.cria_tabelas import config_banco
from app.main import app
from fastapi.testclient import TestClient


# config. de requisitos P/ o test
@pytest.fixture(scope='function')
def client() -> Generator:
  config_banco(DATABASE_URL)
  with TestClient(app) as c:
    yield c
