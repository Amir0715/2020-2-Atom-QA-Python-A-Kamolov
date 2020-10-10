from base_page import BasePage
from locators import CabinetPageLocators


class CabinetPage(BasePage):
    locators = CabinetPageLocators()

    def go_to_audience(self):
        self.click(self.locators.BUTTON_AUDIENCE_LOCATOR)
        
    def go_to_campaigns(self):
        self.click(self.locators.BUTTON_CAMPAIGNS_LOCATOR)

    def check_auth(self):
        return self.check_locator_to_displayed(self.locators.BUTTON_CAMPAIGNS_LOCATOR)

