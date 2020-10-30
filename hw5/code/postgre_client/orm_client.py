import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

class PostgreOrmClient(object):
    def __init__(self,user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = '127.0.0.1'
        self.port = 32768
        self.charset = 'utf8'

        self.connection = self.connect() 

        session = sessionmaker(bind=self.connection)
        self.session = session()

    def get_connection(self, db_created=False):
        engine = sqlalchemy.create_engine('postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}'.format(
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            db=self.db_name if db_created else 'postgres'
        ))
        conn = engine.connect()
        return conn

    def connect(self):
        connection = self.get_connection(db_created=False)
        
        connection.execute('commit')
        connection.execute('DROP DATABASE IF EXISTS TEST_PYTHON_ORM')
        connection.execute('commit')
        connection.execute('CREATE DATABASE TEST_PYTHON_ORM')
        connection.close()

        return self.get_connection(db_created=True)