from builders.postgre_builder import PostgreBuilder
from faker import Faker

from models.model import *

from postgre_client.orm_client import PostgreOrmClient

fake = Faker(locale='ru_RU')


class PostgreOrmBuilder(object):
    def __init__(self, client: PostgreOrmClient):
        self.client = client
        self.engine = self.client.connection.engine

        self.create_CountsOfReq()
        self.create_TopTenSize()
        self.create_TopTenSizeWithServerError()
        self.create_TopTenCountWithUserError()
        self.create_Students()

    def create_CountsOfReq(self):
        if not self.engine.dialect.has_table(self.engine, 'CountsOfReq'):
            Base.metadata.tables['CountsOfReq'].create(self.engine)

    def create_TopTenSize(self):
        if not self.engine.dialect.has_table(self.engine, 'TopTenSize'):
            Base.metadata.tables['TopTenSize'].create(self.engine)

    def create_TopTenCountWithUserError(self):
        if not self.engine.dialect.has_table(self.engine, 'TopTenCountWithUserError'):
            Base.metadata.tables['TopTenCountWithUserError'].create(self.engine)

    def create_TopTenSizeWithServerError(self):
        if not self.engine.dialect.has_table(self.engine, 'TopTenSizeWithServerError'):
            Base.metadata.tables['TopTenSizeWithServerError'].create(self.engine)

    def create_Students(self):
        if not self.engine.dialect.has_table(self.engine, 'students'):
            Base.metadata.tables['students'].create(self.engine)

    def add_student(self, name=None):
        if name is None:
            name = fake.first_name()

        student = Student(
            name=name
        )

        self.client.session.add(student)
        self.client.session.commit()
        return student

    def add_CountOfReq(self, get, post, all):
        count = CountsOfReq(
            count_get_req=get,
            count_post_req=post,
            count_all_req=all
        )

        self.client.session.add(count)
        self.client.session.commit()
        return count

    def add_TopTenSize(self, req, code, size):
        topTen = TopTenSize(
            req=req,
            code=code,
            size=size
        )

        self.client.session.add(topTen)
        self.client.session.commit()
        return topTen

    def add_TopTenCountWithUserError(self, req, count):
        topTen = TopTenCountWithUserError(
            req=req,
            count=count
        )

        self.client.session.add(topTen)
        self.client.session.commit()
        return topTen

    def add_TopTenSizeWithServerError(self, req, code, size):
        topTen = TopTenSizeWithServerError(
            req=req,
            code=code,
            size=size
        )

        self.client.session.add(topTen)
        self.client.session.commit()
        return topTen
