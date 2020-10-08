from base_page import BasePage
from locators import CabinetPageLocators

EMAIL = 'kamolov.amir2000@yandex.ru'
PASSWORD = 'x4r-zbC-SYM-gj8'


class CabinetPage(BasePage):
    locators = CabinetPageLocators()

    def __init__(self, driver):
        self.driver = driver
        
        # self.auth(self.locators.BUTTON_AUTH_BODY_LOCATOR, EMAIL, PASSWORD)
    
        

