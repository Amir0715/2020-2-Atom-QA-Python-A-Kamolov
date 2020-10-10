from conftest import config
import selenium
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import BasePageLocators

RETRY_COUNT = 10
TIMEOUT = 10
class BasePage(object):

    locators = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver
        self.EMAIL = 'kamolov.amir2000@yandex.ru'
        self.PASSWORD = 'x4r-zbC-SYM-gj8'
        self.path_to_file='/home/amir-kamolov/photo/cat.jpg'
        
        
    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(expected_conditions.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(expected_conditions.element_to_be_clickable(locator))
                element.click()
                return
            except StaleElementReferenceException:
                if i > RETRY_COUNT - 1 : 
                    raise
                

    def wait(self, timeout=None):
        if timeout is None:
            timeout = TIMEOUT
        return WebDriverWait(self.driver, timeout=timeout)

    def write(self, locatorInput, keys):
        element = self.find(locatorInput)
        element.clear()
        element.send_keys(keys)

    def auth(self,email,password,locator=locators.BUTTON_AUTH_HEADER_LOCATOR):
        self.click(locator)
        self.write(self.locators.INPUT_EMAIL_AUTH_LOCATOR, email)
        self.write(self.locators.INPUT_PASSWORD_AUTH_LOCATOR, password)
        self.click(self.locators.BUTTON_LOG_IN_LOCATOR)
    
    def check_locator_to_displayed(self, locator, timeout=None):
        try:
            if self.find(locator,timeout).is_displayed() :
                return True
        except TimeoutException:
            return False

    def check_locator_to_selected(self, locator, timeout=None):
        try:
            if self.find(locator,timeout).is_selected() :
                return True
        except TimeoutException:
            return False