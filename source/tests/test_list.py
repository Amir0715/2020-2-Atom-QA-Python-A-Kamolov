import pytest
import random


class TestList():

    def test_1(self, random_value):
        """Тест на метод append"""
        l = list()
        assert len(l) == 0
        l.append(random_value)
        assert len(l) == 1
        assert random_value in l

    def test_2(self, random_value):
        """Тест на метод remove"""
        l = list()
        l.append(random_value)
        assert len(l) == 1
        l.remove(random_value)
        assert len(l) == 0
        with pytest.raises(AssertionError):
            assert random_value in l

    def test_3(self, random_string):
        """Тест на метод clear"""
        l = list(random_string)
        assert len(l) > 0
        l.clear()
        assert len(l) == 0

    @pytest.mark.parametrize('c', range(0, 5))
    def test_4(self, c, random_value):
        """Тест на in"""
        l = list()
        l.append(c)
        assert c in l
        l.clear()
        with pytest.raises(AssertionError):
            assert c in l

    def test_5(self, random_string):
        """Тест на сложение списков"""
        l = list()
        assert len(l) == 0
        l = l + list(random_string)
        assert len(l) > 0
        assert random_string[random.randint(0, len(random_string)-1)] in l
