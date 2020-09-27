import pytest


class TestDictionary():

    def test_1(self):
        """Тест метода update"""
        d = {a: a for a in range(4)}
        dc = {4: 4}
        d.update(dc)
        assert d == {a: a for a in range(5)}

    def test_2(self):
        """Тест метода remove"""
        d = {a: a for a in range(5)}
        assert len(d)
        d.clear()
        assert len(d) == 0

    def test_3(self):
        """Негативный тест на pop"""
        d = {a: a for a in range(1, 5)}
        assert len(d)
        with pytest.raises(KeyError):
            assert d.pop(0)

    def test_4(self):
        """Тест метода get"""
        d = {a: a for a in range(3)}
        assert 1 == d.get(1)
        with pytest.raises(AssertionError):
            assert d.get(6)

    @pytest.mark.parametrize('c', range(5))
    def test_5(self, c):
        """Тест in"""
        d = {a: a for a in range(5)}
        assert c in d
