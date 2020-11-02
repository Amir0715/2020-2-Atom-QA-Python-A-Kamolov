from postgre_client.client import PostgreClient


class PostgreBuilder(object):
    def __init__(self, client : PostgreClient) -> None:
        self.client = client

    def create_test_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS students(
	        id int NOT NULL,
  	        name varchar(20) NOT NULL,
  	        PRIMARY KEY(id)
        );
        """

        self.client.cursor.execute(query)

    def drop_test_table(self):
        query = """
            DROP TABLE IF EXISTS students;
        """

        return self.client.cursor.execute(query)