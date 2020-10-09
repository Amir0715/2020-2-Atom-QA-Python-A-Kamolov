# from audience_page import AudiencePage
from base_page import BasePage
from locators import CabinetPageLocators


class CabinetPage(BasePage):
    locators = CabinetPageLocators()

    def go_to_audience(self):
        self.click(self.locators.BUTTON_AUDIENCE_LOCATOR)
        

    
        

