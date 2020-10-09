# from audience_page import AudiencePage
from base_page import BasePage
from locators import CabinetPageLocators


class CabinetPage(BasePage):
    locators = CabinetPageLocators()

    def go_to_audience(self):
        # self.find(self.locators.BUTTON_AUDIENCE_LOCATOR)
        self.click(self.locators.BUTTON_AUDIENCE_LOCATOR)
        
        
    def check_auth(self):
        return self.check_locator_to_clickcable(self.locators.BUTTON_CAMPAIGNS_LOCATOR)

