from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators import BasePageLocators

RETRY = 3

class BasePage(object):

    locators = BasePageLocators()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(expected_conditions.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        try:
            element = self.find(locator)
            element.click()
        except StaleElementReferenceException:
            pass

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def write(self, locatorInput, keys):
        try:
            element = self.find(locatorInput)
            element.send_keys(keys)
        except StaleElementReferenceException:
            pass
    
    


