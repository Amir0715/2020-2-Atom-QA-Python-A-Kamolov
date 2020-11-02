import pytest
from postgre_client.orm_client import PostgreOrmClient
from postgre_client.client import PostgreClient


@pytest.fixture(scope="session")
def postgre_client():
    return PostgreClient(user='postgres', password='merkyri0715', db_name='test_python', port=3452)


@pytest.fixture(scope="session")
def postgre_orm_client():
    return PostgreOrmClient(user='postgres', password='merkyri0715', db_name='test_python_orm', port=3452)
