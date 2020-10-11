from selenium.webdriver.common.by import By
from locators import AudiencePageLocators
from cabinet_page import CabinetPage

class CanNotCreateSegmentException(Exception):
    pass

class AudiencePage(CabinetPage):
    locators = AudiencePageLocators()


    def create_segment(self,name):
        if self.check_locator_to_displayed(self.locators.HREF_CREATE_SEGMENT_LOCATOR, 3, 3):
            self.click(self.locators.HREF_CREATE_SEGMENT_LOCATOR)
        elif self.check_locator_to_displayed(self.locators.BUTTON_CREATE_SEGMENT_LOCATOR, 3, 3):
            self.click(self.locators.BUTTON_CREATE_SEGMENT_LOCATOR)
            self.click(self.locators.DIV_APPS_AND_GAMES_LOCATOR)
        else:
            raise CanNotCreateSegmentException()

        
        self.click(self.locators.CHECK_BOX_LOCATOR)
        self.click(self.locators.BUTTON_ADD_SEGMENT_LOCATOR)
        self.write(self.locators.INPUT_NAME_SEGMENT_LOCATOR, name)
        self.click(self.locators.BUTTON_CREATE_SEGMENT_LOCATOR)
    

    def delete_segment(self, name):
        self.go_to_audience()
        self.write(self.locators.INPUT_SEARCH_SEGMENT_LOCATOR, name)
        li = '//li[@title="'+name+'"]'
        LI_SEGMENT_SEARCH_LOCATOR = (By.XPATH, li)
        self.click(LI_SEGMENT_SEARCH_LOCATOR)
        self.remove_all()
    
    
    def remove_all(self):
        if self.check_locator_to_displayed(self.locators.BUTTON_ACTIONS_LOCATOR, 3, 3):
            self.click(self.locators.CHECKBOX_ALL_SELECT_LOCATOR)
            self.click(self.locators.BUTTON_ACTIONS_LOCATOR)
            self.click(self.locators.BUTTON_REMOVE_SELECTER_LOCATOR)
        return


    def check_segment(self, name):
        xpath = '//a[@title="'+name+'"]'
        li = '//li[@title="'+name+'"]'
        TEST_SEGMENT_LOCATOR = (By.XPATH,xpath)
        LI_SEGMENT_SEARCH_LOCATOR = (By.XPATH, li)
        self.go_to_audience()
        self.write(self.locators.INPUT_SEARCH_SEGMENT_LOCATOR, name, True)
        if self.check_locator_to_displayed(LI_SEGMENT_SEARCH_LOCATOR, 5, 5):
            self.click(LI_SEGMENT_SEARCH_LOCATOR)
            if self.check_locator_to_displayed(TEST_SEGMENT_LOCATOR, 5, 5) :
                self.click(TEST_SEGMENT_LOCATOR)
                return True
        
        else:
            return False