import os

import databases
import sqlalchemy

# podemos config essas var em um ambiente virtual
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite')
#Banco de test, no geral como test se tiver como true o db é de test
TEST_DATABASE = os.getenv('TEST_DATABASE', 'false') in ('true', 'yes')

database = databases.Database(DATABASE_URL, force_rollback=TEST_DATABASE)
metadata = sqlalchemy.MetaData()
