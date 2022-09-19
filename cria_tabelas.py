import sqlalchemy
from sqlalchemy import engine

from config import DATABASE_URL, metadata
from models.papel import Papel


def config_banco(database = DATABASE_URL):
  engine = sqlalchemy.create_engine(database)
  metadata.drop_all(engine)
  metadata.create_all(engine)

if __name__ == '__main__':
  config_banco()
