import pytest
from builders.posgre_orm_builder import PostgreOrmBuilder
from conftest import postgre_orm_client

from postgre_client.orm_client import PostgreOrmClient
from models.model import Student


class TestOrmPostgre:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, postgre_orm_client):
        self.postgre: PostgreOrmClient = postgre_orm_client
        self.builder: PostgreOrmBuilder = PostgreOrmBuilder(client=self.postgre)

    @pytest.mark.skip()
    def test(self):

        students = []
        for _ in range(10):
            students.append(self.builder.add_student())

        query_students = self.postgre.session.query(Student)

        for a, b in zip(students, query_students):
            assert a == b
