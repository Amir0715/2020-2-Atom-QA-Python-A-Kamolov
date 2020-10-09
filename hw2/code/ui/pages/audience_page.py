from cabinet_page import CabinetPage
from locators import AudiencePageLocators
from selenium.webdriver.common.by import By

class AudiencePage(CabinetPage):
    locators = AudiencePageLocators()


    # //span[@class="icon-cross"] 
    # //div[@data-test="id-100378 row-100378"]

    def create_segment(self,name):
        if self.check_locator_to_clickcable(self.locators.HREF_CREATE_SEGMENT_LOCATOR):
            self.click(self.locators.HREF_CREATE_SEGMENT_LOCATOR)
        elif self.check_locator_to_clickcable(self.locators.BUTTON_CREATE_SEGMENT_LOCATOR):
            self.click(self.locators.BUTTON_CREATE_SEGMENT_LOCATOR)
            self.click(self.locators.DIV_APPS_AND_GAMES_LOCATOR)
        else:
            pass 
            # FIXME: кидать исключение если не был найден ни один локатор для создания сегмента
        
        self.click(self.locators.CHECK_BOX_LOCATOR)
        self.click(self.locators.BUTTON_ADD_SEGMENT_LOCATOR)
        self.write(self.locators.INPUT_NAME_SEGMENT_LOCATOR, name)
        self.click(self.locators.BUTTON_CREATE_SEGMENT_LOCATOR)
    
    def delete_segment(self, name):
        self.click(self.locators.BUTTON_AUDIENCE_LOCATOR)
        self.write(self.locators.INPUT_SEARCH_SEGMENT_LOCATOR, name)
        li = '//li[@title="'+name+'"]'
        LI_SEGMENT_SEARCH_LOCATOR = (By.XPATH, li)
        self.click(LI_SEGMENT_SEARCH_LOCATOR)
        self.remove_all()
    
    
    def remove_all(self):
        if self.check_locator_to_clickcable(self.locators.BUTTON_ACTIONS_LOCATOR):
            self.click(self.locators.CHECKBOX_ALL_SELECT_LOCATOR)
            self.click(self.locators.BUTTON_ACTIONS_LOCATOR)
            self.click(self.locators.BUTTON_REMOVE_SELECTER_LOCATOR)
        return

    def cheack_segment(self, name):
        pass
