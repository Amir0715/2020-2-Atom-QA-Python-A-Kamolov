import datetime
import time
import pytest
from selenium.webdriver.common.by import By

from some_fixtures import *
from base import BaseCase
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
        assert self.cabinet_page.check_auth()

    
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
        name = 'Test segment ' + datetime.datetime.today().strftime("%H:%M:%S:%f")
        xpath = '//a[@title="' + name + '"]'
        TEST_SEGMENT_LOCATOR = (By.XPATH, xpath)
        self.audience_page.create_segment(name)
        assert self.base_page.check_locator_to_displayed(TEST_SEGMENT_LOCATOR)
        self.audience_page.click(TEST_SEGMENT_LOCATOR)
        assert "Редактирование аудиторного сегмента" in self.driver.page_source

    # @pytest.mark.skip
    def test_delete_segment(self, auto_auth):
        self.cabinet_page : CabinetPage = auto_auth
        self.cabinet_page.go_to_audience()
        name = 'Test segment ' + datetime.datetime.today().strftime("%H:%M:%S:%f")
        xpath = '//a[@title="'+name+'"]'
        TEST_SEGMENT_LOCATOR = (By.XPATH,xpath)
        self.audience_page.create_segment(name)
        assert self.base_page.check_locator_to_displayed(TEST_SEGMENT_LOCATOR)
        self.audience_page.click(TEST_SEGMENT_LOCATOR)
        assert "Редактирование аудиторного сегмента" in self.driver.page_source

        self.audience_page.delete_segment(name)
        assert "С чего начать?" in self.driver.page_source

    
    def test_create_campaign(self, auto_auth):
        self.cabinet_page : CabinetPage = auto_auth
        self.cabinet_page.go_to_campaigns()

        name = 'Test campaign ' + datetime.datetime.today().strftime("%H:%M:%S:%f")

        self.campaign_page.create_campaign(name,self.base_page.path_to_file)
        assert self.campaign_page.check_campaign(name)

    def test_delete_campaign(self,auto_auth):
        self.cabinet_page : CabinetPage = auto_auth
        self.cabinet_page.go_to_campaigns()

        name = 'Test campaign ' + datetime.datetime.today().strftime("%H:%M:%S:%f")

        self.campaign_page.create_campaign(name,self.base_page.path_to_file)
        assert self.campaign_page.check_campaign(name)
        # TODO: COMPLITE
        
    