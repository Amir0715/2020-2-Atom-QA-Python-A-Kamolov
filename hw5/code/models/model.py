from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.sqltypes import VARCHAR, String

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    __table_args = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(" \
               f"id='{self.id}'," \
               f"name='{self.name}'" \
               f")>"

class CountsOfReq(Base):
    __tablename__ = 'CountsOfReq'

    __table_args = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    count_get_req = Column(Integer, nullable=False)
    count_post_req = Column(Integer, nullable=False)
    count_all_req = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"<CountsOfReq(" \
               f"id='{self.id}'," \
               f"count_get_req='{self.count_get_req}'," \
               f"count_post_req='{self.count_post_req}'," \
               f"count_all_req='{self.count_all_req}'"   \
               f")>"


class TopTenSize(Base):
    __tablename__ = 'TopTenSize'
    __table_args = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    req = Column(VARCHAR, nullable=False)
    code = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<TopTenSize("\
               f"id='{self.id}',"\
               f"req='{self.req}',"\
               f"code='{self.code}',"\
               f"size='{self.size}'"  \
               f")>"

class TopTenCountWithUserError(Base):
    __tablename__ = 'TopTenCountWithUserError'
    __table_args = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    req = Column(VARCHAR, nullable=False)
    count = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"<TopTenCountWithUserError(" \
               f"id='{self.id}',"\
               f"req='{self.req}',"\
               f"count='{self.count}'"\
               f")>"

class TopTenSizeWithServerError(Base):
    __tablename__ = 'TopTenSizeWithServerError'
    __table_args = {'mysql_charset': 'utf8'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    req = Column(VARCHAR, nullable=False)
    code = Column(Integer, nullable=False)
    size = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"<TopTenSizeWithServerError(" \
               f"id='{self.id}',"\
               f"req='{self.req}',"\
               f"code='{self.code}',"\
               f"size='{self.size}'"\
               f")>"