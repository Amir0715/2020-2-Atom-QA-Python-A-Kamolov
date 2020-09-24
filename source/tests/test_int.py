import pytest


class TestInt:

    def test_1(self, random_value):
        """Tест на умножение на ноль"""

        assert random_value * 0 == 0

    def test_2(self, random_value):
        """Тест на сравнения типов"""

        assert isinstance(random_value, int)

    def test_3(self, random_string):
        """Негативный тест на сравнение типов """

        with pytest.raises(AssertionError):
            assert isinstance(random_string, int)

    def test_4(self, random_value):
        """Негативный тест на деления на ноль"""

        with pytest.raises(ZeroDivisionError):
            assert random_value / 0

    @pytest.mark.parametrize('i', range(1, 5))
    def test_5(self, random_value, i):
        """Тест на деления двух целочисленных чисел"""

        assert isinstance(i//random_value, int)
        assert isinstance(i/random_value, float)

    def test_6(self, random_value, random_string):
        """Негативный тест на сложения целого числа и строки"""

        with pytest.raises(TypeError):
            assert random_value + random_string
    
    def test_7(self, random_value):
        """Тест на проверку деления с остатком (%)"""
        
        assert random_value % 10 == random_value - ( random_value // 10 ) * 10