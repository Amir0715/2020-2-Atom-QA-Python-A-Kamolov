import pytest
from code.builders.postgre_builder import PostgreBuilder
from code.postgre_client.client import PostgreClient
from code.conftest import postgre_client

class TestPostgre:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, postgre_client):
        self.postgre : PostgreClient = postgre_client
        self.builder = PostgreBuilder(self.postgre)
    
    @pytest.mark.skip(reason="no need")
    def test(self):
        # self.postgre.drop_test_table()
        # self.postgre.create_test_table()
        print(self.builder.drop_test_table())
        print(self.builder.create_test_table())
        # print(self.postgre.execute('SELECT * FROM students;'))
        
        