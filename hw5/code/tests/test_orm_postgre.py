import pytest
from code.builders.posgre_orm_builder import PostgreOrmBuilder
from code.conftest import postgre_orm_client
from code.postgre_client.orm_client import PostgreOrmClient
from code.models.models import *

@pytest.mark.skip()
class TestOrmPostgre:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, postgre_orm_client):
        self.postgre: PostgreOrmClient = postgre_orm_client
        self.builder: PostgreOrmBuilder = PostgreOrmBuilder(client=self.postgre)

    def test(self):

        # Добавляем 10 записей в табилцу 'prepods'
        for _ in range(10):
            self.builder.add_prepod()

        # Далее приводится несколько примеров работы с данными через ORM.
        # Допустим мы хотим обновить имя первого препода. Найденм его:
        first_prepod = self.postgre.session.query(Prepod).first()
        # Обновим его имя
        first_prepod.name = 'Владимир'
        # Запишем обновленные данные в базу
        self.postgre.session.add(first_prepod)
        self.postgre.session.commit()

        # Более того, алхимия умеет довольно удобно фильтровать записи через объекты моделей.
        # Вот так можно получить все записи из таблицы prepods и отфильтровать их по id
        # (перенос строки \n добавлен просто для удобства чтения):
        prepod_with_id_5 = self.postgre.session.query(Prepod).filter_by(id=5).first()
        print('\nID=5 prepod: ' + str(prepod_with_id_5))

        # Аналогично можно получить список всех записей через модель:
        all_prepods = self.postgre.session.query(Prepod).all()
        all_prepods_as_string = ' '.join(str(prepod) for prepod in all_prepods)
        print('All prepods: ' + all_prepods_as_string)

        # А если привести к строке объект, возвращаемый методом query (или filter_by, то можно будет посмотреть
        # текст запроса, который алхимия сформирует, основываясь на переданной модели:
        all_prepods_query = str(self.postgre.session.query(Prepod))
        all_prepods_filter_by_name_query = str(self.postgre.session.query(Prepod).filter_by(name='Владимир'))
        print(f'All prepods query: "{all_prepods_query}"')
        print(f'All prepods filter by name query: "{all_prepods_filter_by_name_query}"')

    
    def test_students_delete(self):
        """Тест показывает, как с помощью  ORM можно удалять записи из базы """
        # Создаем 10 записей в базе через ORM
        self.builder.add_students(count=10)

        # Удаляем запись с id=5
        res = self.postgre.session.query(Student).filter_by(id=5)
        res.delete()
        self.postgre.session.commit()

        # Удаляем все оставшиеся записи
        # self.postgre.session.query(Student).delete()
        # self.postgre.session.commit()
