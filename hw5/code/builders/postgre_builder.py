from postgre_client.client import PostgreClient
from faker import Faker

fake = Faker(locale='ru_RU')

class PostgreBuilder(object):
    def __init__(self, client: PostgreClient) -> None:
        self.client = client
        self.id = 0;
        self.drop_students_table()
        self.create_students_table()

    def create_students_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS students(
	        id int NOT NULL,
  	        name varchar(20) NOT NULL,
  	        PRIMARY KEY(id)
        );
        """

        self.client.execute(query)

    def drop_students_table(self):
        query = """
            DROP TABLE IF EXISTS students;
        """

        return self.client.execute(query)

    def add_students(self, name=None):
        if name is None:
            name = fake.first_name()

        query = """
            INSERT INTO students(id,name) VALUES({},'{}');
        """.format(self.id, name)
        self.id +=1
        return self.client.execute(query)

    def get_students(self):
        query = """
            SELECT name FROM students;
        """

        return self.client.execute(query,fetch=True)