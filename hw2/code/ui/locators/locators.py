from selenium.webdriver.common.by import By

class BasePageLocators(object):
    BUTTON_AUTH_HEADER_LOCATOR = (By.XPATH, '//div[contains(text() , "Войти")]')
    BUTTON_AUTH_BODY_LOCATOR = (By.XPATH, '//div[contains(@class,"mainPage-module-description")]/div[contains(@class,"mainPage-module-button")]')
    INPUT_EMAIL_AUTH_LOCATOR = (By.XPATH, '//input[@name="email"]')
    INPUT_PASSWORD_AUTH_LOCATOR = (By.XPATH, '//input[@name="password"]')
    BUTTON_LOG_IN_LOCATOR = (By.XPATH, '//div[contains(@class,"authForm-module-button")]')
    DIV_ERROR_LOG_IN_LOCATOR = (By.XPATH, '//div[contains(@class,"notify-module-content")]')
    DIV_INVALID_LOG_IN_LOCATOR = (By.XPATH, '//*[@id="login_form"]/div/div[contains(@class,"formMsg")]')

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


class CampaignPageLocators(CabinetPageLocators):
    CAMPAIGN_TRAFIC_LOCATOR = (By.XPATH, '//div[contains(@class, "_traffic")]')
    INPUT_URL_ADS_LOCATOR = (By.XPATH, '//input[contains(@data-gtm-id,"ad_url_text")]')
    INPUT_NAME_CAMPAIGN_LOCATOR = (By.XPATH, '//div[contains(@class,"input_campaign-name")]//input')
    INPUT_CLEAR_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "input__clear")]')
    FORMAT_BANER_LOCATOR = (By.XPATH, '//div[@id="patterns_4"]')
    INPUT_UPLOAD_IMAGE_LOCATOR = (By.XPATH, '//input[@type="file" and @data-test="image_240x400"]')
    BUTTON_SAVE_ADS_LOCATOR = (By.XPATH, '//div[contains(@data-test,"submit_banner_button")]')
    BUTTON_FOOTER_CREATE_CAMPAIGN_LOCATOR = (By.XPATH, '//div[contains(@class, "footer")]/button')
    BUTTON_GO_TO_CREATE_CAMPAIGN_LOCATOR = (By.XPATH, '//div[contains(@class, "dashboard-module-createButtonWrap")]/div/div')
    INPUT_SEARCH_CAMPAIGN_LOCATOR = (By.XPATH, '//input[contains(@class,"searchInput")]')
    


class AudiencePageLocators(CabinetPageLocators):
    CHECK_BOX_LOCATOR = (By.XPATH,'//input[contains(@class, "adding-segments-source__checkbox")]')
    HREF_CREATE_SEGMENT_LOCATOR = (By.XPATH, '//a[@href="/segments/segments_list/new/"]')
    BUTTON_CREATE_SEGMENT_LOCATOR = (By.XPATH, '//button[@class="button button_submit"]')
    BUTTON_ADD_SEGMENT_LOCATOR = (By.XPATH,'//div[contains(@class, "adding-segments-modal__footer")]/div[1]/button/div') 
    BUTTON_DELETE_SEGMENT_LOCATOR = (By.XPATH, '//span[contains(@class,"icon-cross")]')
    BUTTON_ACCEPT_DELETING_SEGMENT_LOCATOR = (By.XPATH, '//button[contains(@class,"button_confirm-remove")]')
    INPUT_NAME_SEGMENT_LOCATOR = (By.XPATH, '//div[contains(@class,"input_create-segment-form")]//input')
    DIV_APPS_AND_GAMES_LOCATOR = (By.XPATH, '//div[contains(@class,"adding-segments-modal__block-left")]/div[8]')
    INPUT_SEARCH_SEGMENT_LOCATOR = (By.XPATH, '//input[@type="text"]')
    CHECKBOX_ALL_SELECT_LOCATOR = (By.XPATH, '//input[@type="checkbox"][1]')
    BUTTON_ACTIONS_LOCATOR = (By.XPATH, '//div[1][@data-test="select"]')
    BUTTON_REMOVE_SELECTER_LOCATOR = (By.XPATH, '//li[@data-test="remove"]')
    INPUT_EDIT_NAME_SEGMENT_LOCATOR = (By.XPATH, '//input[@maxlength="60"]')