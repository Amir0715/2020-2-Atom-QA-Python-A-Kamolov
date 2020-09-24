import pytest


class TestStr():

    def test_1(self, random_string):
        """Тест на сложение строк"""
        assert random_string + random_string

    def test_2(self, random_string):
        """Негативный тест на деление"""
        with pytest.raises(TypeError):
            assert random_string / random_string

    def test_3(self, random_string):
        """Негативный тест на вычитание строк"""
        with pytest.raises(TypeError):
            assert random_string - random_string

    def test_4(self, random_string, random_value):
        """Тест на умножение строки на целое число"""
        assert random_string * random_value

    def test_5(self, random_string):
        """Тест на реверс строки"""
        assert random_string[::-1] == ''.join(reversed(random_string))

    def test_6(self, random_string):
        """Тест на проверку in"""
        c = random_string[5]
        assert c in random_string

    @pytest.mark.parametrize('c', list('abcd'))
    def test_7(self, c, random_string):
        """Тест на проверку метода join"""
        assert random_string.join(c) == random_string + c
