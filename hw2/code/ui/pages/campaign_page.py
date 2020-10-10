from cabinet_page import CabinetPage
from locators import CampaignPageLocators
from selenium.webdriver.common.by import By

class CampaignPage(CabinetPage):
    locators = CampaignPageLocators()
    
    def create_campaign(self , name, file):
        self.click(self.locators.BUTTON_GO_TO_CREATE_CAMPAIGN_LOCATOR)
        self.click(self.locators.CAMPAIGN_TRAFIC_LOCATOR)
        self.write(self.locators.INPUT_URL_ADS_LOCATOR, 'https://target.my.com')
        self.click(self.locators.INPUT_CLEAR_BUTTON_LOCATOR)
        self.find(self.locators.INPUT_NAME_CAMPAIGN_LOCATOR).send_keys(name)
        
        self.click(self.locators.FORMAT_BANER_LOCATOR)
        self.find(self.locators.INPUT_UPLOAD_IMAGE_LOCATOR).send_keys(file)
        self.click(self.locators.BUTTON_SAVE_ADS_LOCATOR)
        self.click(self.locators.BUTTON_FOOTER_CREATE_CAMPAIGN_LOCATOR)

    def check_campaign(self, name):
        xpath = '//a[contains(@title,"' + name + '" )]/../label/input[@checked]'
        TOGGLE_CHECKED_CAMPAIGN_LOCATOR = (By.XPATH, xpath)
        return self.check_locator_to_selected(TOGGLE_CHECKED_CAMPAIGN_LOCATOR)
