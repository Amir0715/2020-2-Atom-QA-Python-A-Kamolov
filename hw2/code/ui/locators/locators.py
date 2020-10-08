from selenium.webdriver.common.by import By

class BasePageLocators(object):
    pass

class CabinetPageLocators(BasePageLocators):
    BUTTON_COMPANY_LOCATOR = (By.XPATH, '/html/body/div[1]/div/div[1]/div/div/div/div[2]/ul/li[1]/a')
    BUTTON_AUDIENCE_LOCATOR = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/ul/li[2]/a')
    BUTTON_BALANCE_LOCATOR = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/ul/li[2]/a')
    BUTTON_STATISTICS_LOCATOR = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/ul/li[4]/a')
    BUTTON_PRO_LOCATOR = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/ul/li[5]/a')
    BUTTON_PROFILE_LOCATOR = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/ul/li[6]/a')
    BUTTON_TOOLS_LOCATOR = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/ul/li[7]/a')
    BUTTON_HELP_LOCATOR = (By.XPATH, '/html/body/div[1]/div[1]/div/div/div/div[2]/ul/li[8]/a')
    DIV_INSTROCTION_LOCATOR = (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div')

class MainPageLocators(BasePageLocators):
    BUTTON_AUTH_HEADER_LOCATOR = (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]')
    BUTTON_AUTH_BODY_LOCATOR = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]')
    INPUT_EMAIL_AUTH_LOCATOR = (By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div/div[1]/input')
    INPUT_PASSWORD_AUTH_LOCATOR = (By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div/div[2]/input')
    BUTTON_LOG_IN_LOCATOR = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[4]/div[1]')


class ProPageLocators(BasePageLocators):
    pass


class CampaignPageLocators(CabinetPageLocators):
    pass

class AudiencePageLocators(CabinetPageLocators):
    pass