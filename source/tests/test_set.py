import pytest


class TestSet():

    def test_1(self, random_value):
        """Тест на метод add"""
        s = set()
        assert len(s) == 0
        s.add(random_value)
        assert len(s) == 1

    def test_2(self, random_value):
        """Тест на метод remove"""
        s = set()
        s.add(random_value)
        assert len(s) == 1
        s.remove(random_value)
        assert len(s) == 0

    def test_3(self):
        """Тест на разницу множеств"""
        s = {1, 2, 3, 4}
        a = {3, 4}
        assert {1, 2} == s.difference(a)

    def test_4(self):
        """Тест на пересечение множеств"""
        s = {1, 2, 3, 4}
        a = {3, 4}
        assert {3, 4} == s.intersection(a)

    @pytest.mark.parametrize('c', range(5))
    def test_5(self, c):
        """Тест на метод update"""
        s = set()
        assert len(s) == 0
        a = set()
        a.add(c)
        s.update(a)
        assert len(s) == 1
