from datetime import datetime
from code.tests.base import BaseCase
import pytest


class TestTargetApi(BaseCase):
    
    @pytest.mark.API
    def test_create_segment(self):
        """
        Тест на создание сегмента и его проверка
        """
        name = 'Test segment ' + datetime.today().strftime("%H:%M:%S:%f")
        assert self.target_client.create_segment(name).status_code == 200
        assert self.target_client.check_segment(name)
    
    @pytest.mark.API
    def test_delete_segment(self):
        """
        Тест на удаление сегмента и его проверка
        """
        name = 'Test segment ' + datetime.today().strftime("%H:%M:%S:%f")
        assert self.target_client.create_segment(name).status_code == 200
        assert self.target_client.delete_segment(name).status_code == 204
        with pytest.raises(AssertionError) :
            assert self.target_client.check_segment(name)
