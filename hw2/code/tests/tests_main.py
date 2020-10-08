from attr import s
import pytest
from cabinet_page import CabinetPage
from main_page import MainPage
from some_fixtures import base_page, main_page, cabinet_page
from base import BaseCase

EMAIL = 'kamolov.amir2000@yandex.ru'
PASSWORD = 'x4r-zbC-SYM-gj8'

class Test(BaseCase):
    
    @pytest.mark.skip
    def test_title(self):
        assert 'myTarget' in self.driver.title
    
    @pytest.mark.skip
    @pytest.mark.parametrize('BUTTON_LOCATOR' , ['BUTTON_AUTH_BODY_LOCATOR', 'BUTTON_AUTH_HEADER_LOCATOR'] )
    def test_button_auth(self,BUTTON_LOCATOR):
        locator = getattr(self.main_page.locators, BUTTON_LOCATOR)
        self.base_page.click(locator)
        assert "Вход в рекламный кабинет" in self.driver.page_source

    @pytest.mark.skip
    @pytest.mark.parametrize('BUTTON_LOCATOR', ['BUTTON_AUTH_BODY_LOCATOR', 'BUTTON_AUTH_HEADER_LOCATOR'])
    def test_auth_via_button(self, BUTTON_LOCATOR : str):
        locator = getattr(self.main_page.locators, BUTTON_LOCATOR)
        cabinete : CabinetPage = self.main_page.auth(locator, EMAIL, PASSWORD)
        cabinete.find(self.cabinet_page.locators.DIV_INSTROCTION_LOCATOR)
        assert EMAIL in self.driver.page_source
    
        