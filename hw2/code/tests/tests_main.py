from os import name
from audience_page import AudiencePage
import pytest
from base import BaseCase
from some_fixtures import *
from cabinet_page import CabinetPage


class Test(BaseCase):
    
    
    # @pytest.mark.skip
    @pytest.mark.parametrize('BUTTON_LOCATOR' , ['BUTTON_AUTH_BODY_LOCATOR', 'BUTTON_AUTH_HEADER_LOCATOR'] )
    def test_button_auth(self,BUTTON_LOCATOR : str):
        locator = getattr(self.base_page.locators, BUTTON_LOCATOR)
        self.base_page.click(locator)
        assert "Вход в рекламный кабинет" in self.driver.page_source


    # @pytest.mark.skip
    @pytest.mark.parametrize('BUTTON_LOCATOR', ['BUTTON_AUTH_BODY_LOCATOR', 'BUTTON_AUTH_HEADER_LOCATOR'])
    def test_positive_auth_via_button(self, BUTTON_LOCATOR : str):
        locator = getattr(self.base_page.locators, BUTTON_LOCATOR)
        self.base_page.auth(self.base_page.EMAIL, self.base_page.PASSWORD, locator)
        self.cabinet_page.find(self.cabinet_page.locators.DIV_INSTROCTION_LOCATOR)
        assert self.base_page.EMAIL in self.driver.page_source

    
    # @pytest.mark.skip
    @pytest.mark.parametrize('BUTTON_LOCATOR', ['BUTTON_AUTH_BODY_LOCATOR', 'BUTTON_AUTH_HEADER_LOCATOR'])
    def test_negetiv_auth_via_button_invalid_email(self, BUTTON_LOCATOR : str):
        """
            Негативный тест на авторизациб при неправильном вводе эл.почты или номера телефона 
        """
        locator = getattr(self.base_page.locators, BUTTON_LOCATOR)
        self.base_page.auth('dakdma', 'hdkadwioqdo', locator)
        self.cabinet_page.find(self.cabinet_page.locators.DIV_ERROR_LOG_IN_LOCATOR)
        assert 'Введите email или телефон' in self.driver.page_source


    # @pytest.mark.skip
    @pytest.mark.parametrize('BUTTON_LOCATOR', ['BUTTON_AUTH_BODY_LOCATOR', 'BUTTON_AUTH_HEADER_LOCATOR'])
    def test_negetiv_auth_via_button_invalid_password(self, BUTTON_LOCATOR : str):
        """
            Негативный тест на авторизациб при неправильном пароля
        """
        locator = getattr(self.base_page.locators, BUTTON_LOCATOR)
        self.base_page.auth(self.base_page.EMAIL, 'hdkadwioqdo', locator)
        self.base_page.find(self.base_page.locators.DIV_INVALID_LOG_IN_LOCATOR)
        assert 'Invalid login or password' in self.driver.page_source


    # @pytest.mark.skip
    def test_create_segment(self, auto_auth):
        self.cabinet_page : CabinetPage = auto_auth
        self.cabinet_page.go_to_audience()
        name = 'Test segment'
        self.audience_page.create_segment(name)
        self.audience_page.find(self.audience_page.locators.TEST_SEGMENT_LOCATOR).click()
        # assert name in self.driver.page_source
        assert "Редактирование аудиторного сегмента" in self.driver.page_source
        self.audience_page.delete_segment()

    # @pytest.mark.skip
    def test_delete_segment(self, auto_auth):
        self.cabinet_page : CabinetPage = auto_auth
        self.cabinet_page.go_to_audience()
        name = 'Test segment'
        self.audience_page.create_segment(name)
        self.audience_page.find(self.audience_page.locators.TEST_SEGMENT_LOCATOR).click()
        assert "Редактирование аудиторного сегмента" in self.driver.page_source
        self.audience_page.delete_segment()
        assert "С чего начать?"

        