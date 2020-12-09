import psycopg2
from psycopg2.extras import DictCursor


class PostgreClient(object):

    def __init__(self, user, password, db_name, host='127.0.0.1', port=5432):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.host = host
        self.port = port
        self.charset = 'utf8'

        self.cursor = self.connect()

    def get_cursor(self, db_created=False):
        conn = psycopg2.connect(dbname=self.db_name if db_created else None,
                                user=self.user, password=self.password, host=self.host, port=self.port,
                                cursor_factory=DictCursor)
        conn.autocommit = True
        conn.set_client_encoding('UTF8')
        return conn.cursor()

    def connect(self):
        connection = self.get_cursor()

        connection.execute('commit')
        connection.execute("DROP DATABASE IF EXISTS {} ".format(self.db_name))
        connection.execute('commit')
        connection.execute('CREATE DATABASE {}'.format(self.db_name))
        connection.close()

        return self.get_cursor(True)

    def execute(self, query, fetch=False):
        self.cursor.execute(query)
        res = None
        if fetch:
            res = self.cursor.fetchall()
        return res
