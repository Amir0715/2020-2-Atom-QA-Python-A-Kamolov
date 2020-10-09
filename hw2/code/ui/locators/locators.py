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
    BUTTON_CAMPAIGNS_LOCATOR = (By.XPATH, '//a[@href="/dashboard"]')
    BUTTON_AUDIENCE_LOCATOR = (By.XPATH, '//a[@href="/segments"]')
    BUTTON_BALANCE_LOCATOR = (By.XPATH, '//a[@href="/billing" and @target="_self"]')
    BUTTON_STATISTICS_LOCATOR = (By.XPATH, '//a[@href="/statistics"]')
    BUTTON_PRO_LOCATOR = (By.XPATH, '//a[@href="/pro"]')
    BUTTON_PROFILE_LOCATOR = (By.XPATH, '//a[@href="/profile"]')
    BUTTON_TOOLS_LOCATOR = (By.XPATH, '//a[@href="/tools"]')
    BUTTON_HELP_LOCATOR = (By.XPATH, '//a[@href="//target.my.com/help/advertisers/ru"]')
    DIV_INSTROCTION_LOCATOR = (By.XPATH, '//div[@class="instruction-module-title-zPmY3V"]')


class ProPageLocators(BasePageLocators):
    pass


class CampaignPageLocators(CabinetPageLocators):
    CAMPAIGN_TRAFIC_LOCATOR = (By.XPATH, '//div[contains(@class, "_traffic")]')
    INPUT_URL_ADS_LOCATOR = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[3]/div[1]/div/div[1]/div/div/input')
    INPUT_NAME_CAMPAIGN_LOCATOR = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[2]/div/div[9]/div/div[2]/div/div[2]/input')
    FORMAT_BANER_LOCATOR = (By.XPATH, '//div[@id="patterns_4"]')
    BUTTON_FOOTER_CREATE_CAMPAIGN_LOCATOR = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div[3]/div[1]/div[1]/button')
    BUTTON_GO_TO_CREATE_CAMPAIGN_LOCATOR = (By.XPATH, '/html/body/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[1]/div[1]/div/div')
    INPUT_UPLOAD_IMAGE_LOCATOR = (By.XPATH, '//input[@type="file" and @data-test="image_240x400"]')
    BUTTON_SAVE_ADS_LOCATOR = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[4]/div[6]/div/div[4]/div/div[3]/div[1]/div')
    INPUT_CLEAR_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "input__clear")]')

class AudiencePageLocators(CabinetPageLocators):
    CHECK_BOX_LOCATOR = (By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div/div/div[1]/input')
    HREF_CREATE_SEGMENT_LOCATOR = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    BUTTON_CREATE_SEGMENT_LOCATOR = (By.XPATH, '//button[@class="button button_submit"]')
    BUTTON_ADD_SEGMENT_LOCATOR = (By.XPATH,'/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[5]/div[1]/button/div')
    # BUTTON_CREATE_SEGMENT_LOCATOR = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[3]/div/div[4]/button/div')
    BUTTON_DELETE_SEGMENT_LOCATOR = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[6]/div/div[1]/div[1]/div/div/div/div[2]/div/div/div[6]/span')
    BUTTON_ACCEPT_DELETING_SEGMENT_LOCATOR = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div[2]/div[2]/button[1]/div')
    INPUT_NAME_SEGMENT_LOCATOR = (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/input')
    # TEST_SEGMENT_LOCATOR = (By.XPATH, '//a[@title="Test segment"]')
    DIV_APPS_AND_GAMES_LOCATOR = (By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[2]/div/div[2]/div[1]/div[8]')


    INPUT_SEARCH_SEGMENT_LOCATOR = (By.XPATH, '//input[@type="text"]')
    CHECKBOX_ALL_SELECT_LOCATOR = (By.XPATH, '//input[@type="checkbox"][1]')
    BUTTON_ACTIONS_LOCATOR = (By.XPATH, '//div[1][@data-test="select"]')
    BUTTON_REMOVE_SELECTER_LOCATOR = (By.XPATH, '//li[@data-test="remove"]')