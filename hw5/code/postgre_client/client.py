import psycopg2
from psycopg2.extras import DictCursor

class PostgreClient(object):

    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = '127.0.0.1'
        self.port = 32768
        self.charset = 'utf8'

        self.cursor = self.connect()

    def get_cursor(self, db_created=False):
        conn = psycopg2.connect(dbname=self.db_name if db_created else None, 
        user=self.user, password=self.password,host=self.host, port=self.port, cursor_factory=DictCursor)
        conn.autocommit = True
        conn.set_client_encoding('UTF8')
        return conn.cursor()
    
    def connect(self):
        
        connection = self.get_cursor()

        connection.execute('DROP DATABASE IF EXISTS TEST')
        connection.execute('CREATE DATABASE TEST')

        connection.close()

        return self.get_cursor(True)

    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
        