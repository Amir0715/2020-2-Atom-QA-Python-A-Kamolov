from base_page import BasePage
from locators import CabinetPageLocators
from main_page import MainPage

class CabinetPage(BasePage):
    locators = CabinetPageLocators()

    def __init__(self, driver):
        self = MainPage.auth(MainPage, MainPage.locators.BUTTON_AUTH_BODY_LOCATOR, 'kamolov.amir2000@yandex.ru', 'x4r-zbC-SYM-gj8')
    
        

