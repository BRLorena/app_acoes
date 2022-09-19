import sqlalchemy
from models.papel import Papel

from config.config import DATABASE_URL, metadata


def config_banco(database = DATABASE_URL):
  engine = sqlalchemy.create_engine(database)
  metadata.drop_all(engine)
  metadata.create_all(engine)

if __name__ == '__main__':
  config_banco()
