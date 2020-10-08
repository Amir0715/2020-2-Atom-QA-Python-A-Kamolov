from base_page import BasePage
from locators import MainPageLocators




class MainPage(BasePage):
    locators = MainPageLocators()

    def auth(self,locator,email,password):
        self.click(locator)
        self.write(self.locators.INPUT_EMAIL_AUTH_LOCATOR, email)
        self.write(self.locators.INPUT_PASSWORD_AUTH_LOCATOR, password)
        self.click(self.locators.BUTTON_LOG_IN_LOCATOR)
        
        return CabinetPage(self.driver)

    