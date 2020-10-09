from selenium.webdriver.common.by import By

class BasePageLocators(object):
    BUTTON_AUTH_HEADER_LOCATOR = (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div/div/div/div/div[2]/div/div[1]')
    BUTTON_AUTH_BODY_LOCATOR = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]')
    INPUT_EMAIL_AUTH_LOCATOR = (By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div/div[1]/input')
    INPUT_PASSWORD_AUTH_LOCATOR = (By.XPATH, '/html/body/div[2]/div/div[2]/div/form/div/div[2]/input')
    BUTTON_LOG_IN_LOCATOR = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[4]/div[1]')
    DIV_ERROR_LOG_IN_LOCATOR = (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[3]/div')
    DIV_INVALID_LOG_IN_LOCATOR = (By.XPATH, '//*[@id="login_form"]/div[1]/div/div[2]')

class CabinetPageLocators(BasePageLocators):
    BUTTON_COMPANY_LOCATOR = (By.XPATH, '//a[@href="/dashboard"]')
    BUTTON_AUDIENCE_LOCATOR = (By.XPATH, '//a[@href="/segments"]')
    BUTTON_BALANCE_LOCATOR = (By.XPATH, '//a[@href="/billing" and @target="_self"]')
    BUTTON_STATISTICS_LOCATOR = (By.XPATH, '//a[@href="/statistics"]')
    BUTTON_PRO_LOCATOR = (By.XPATH, '//a[@href="/pro"]')
    BUTTON_PROFILE_LOCATOR = (By.XPATH, '//a[@href="/profile"]')
    BUTTON_TOOLS_LOCATOR = (By.XPATH, '//a[@href="/tools"]')
    BUTTON_HELP_LOCATOR = (By.XPATH, '//a[@href="//target.my.com/help/advertisers/ru"]')
    DIV_INSTROCTION_LOCATOR = (By.XPATH, '//div[@class="instruction-module-title-zPmY3V"]')

class MainPageLocators(BasePageLocators):
    pass


class ProPageLocators(BasePageLocators):
    pass


class CampaignPageLocators(CabinetPageLocators):
    pass

class AudiencePageLocators(CabinetPageLocators):
    CHECK_BOX_LOCATOR = (By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/input')
    HREF_CREATE_SEGMENT_LOCATOR = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    BUTTON_ADD_SEGMENT_LOCATOR = (By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[5]/div[1]/button/div')
    BUTTON_CREATE_SEGMENT_LOCATOR = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[3]/div/div[4]/button/div')
    BUTTON_DELETE_SEGMENT_LOCATOR = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[6]/div/div[1]/div[1]/div/div/div/div[2]/div/div/div[6]/span')
    BUTTON_ACCEPT_DELETING_SEGMENT_LOCATOR = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div[2]/div[2]/button[1]/div')
    INPUT_NAME_SEGMENT_LOCATOR = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/input')
    TEST_SEGMENT_LOCATOR = (By.XPATH, '//a[@title="Test segment"]')