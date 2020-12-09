import pytest
from postgre_client.orm_client import PostgreOrmClient
from postgre_client.client import PostgreClient

PASSWORD=''
USERNAME='postgres'

@pytest.fixture(scope="session")
def postgre_client():
    return PostgreClient(user=USERNAME, password=PASSWORD, db_name='test_python')


@pytest.fixture(scope="session")
def postgre_orm_client():
    return PostgreOrmClient(user=USERNAME, password=PASSWORD, db_name='test_python_orm')
