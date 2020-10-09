from cabinet_page import CabinetPage
from locators import AudiencePageLocators

class AudiencePage(CabinetPage):
    locators = AudiencePageLocators()
    
    def create_segment(self,name):
        self.click(self.locators.HREF_CREATE_SEGMENT_LOCATOR)
        self.click(self.locators.CHECK_BOX_LOCATOR)
        self.click(self.locators.BUTTON_ADD_SEGMENT_LOCATOR)
        self.write(self.locators.INPUT_NAME_SEGMENT_LOCATOR,name)
        self.click(self.locators.BUTTON_CREATE_SEGMENT_LOCATOR)
    
    def delete_segment(self):
        self.click(self.locators.BUTTON_AUDIENCE_LOCATOR)
        self.click(self.locators.BUTTON_DELETE_SEGMENT_LOCATOR)
        self.click(self.locators.BUTTON_ACCEPT_DELETING_SEGMENT_LOCATOR)
    
