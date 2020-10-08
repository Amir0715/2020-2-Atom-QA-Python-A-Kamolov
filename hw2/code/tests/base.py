from base_page import BasePage
from main_page import MainPage
from cabinet_page import CabinetPage
from _pytest.fixtures import FixtureRequest
import pytest


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self,driver,config,request:FixtureRequest):
        self.driver = driver
        self.config = config
        
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.cabinet_page: CabinetPage = request.getfixturevalue('cabinet_page')

    