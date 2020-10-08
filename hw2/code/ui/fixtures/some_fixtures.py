from base_page import BasePage
from main_page import MainPage
from cabinet_page import CabinetPage
import pytest


@pytest.fixture
def base_page(driver):
    return BasePage(driver)
    
@pytest.fixture
def main_page(driver):
    return MainPage(driver)
    
@pytest.fixture
def cabinet_page(driver):
    return CabinetPage(driver)