import pytest
import faker
from builders.postgre_builder import PostgreBuilder
from postgre_client.client import PostgreClient

from conftest import postgre_client


class TestPostgre:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, postgre_client):
        self.postgre: PostgreClient = postgre_client
        self.builder = PostgreBuilder(self.postgre)

    def test(self):
        name = 'Alex'
        self.builder.add_students(name)
        res = self.builder.get_students()
        assert name == res[0][0]