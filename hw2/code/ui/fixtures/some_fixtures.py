import pytest
from ui.pages.audience_page import AudiencePage
from ui.pages.base_page import BasePage
from ui.pages.campaign_page import CampaignPage
from ui.pages.cabinet_page import CabinetPage


@pytest.fixture
def base_page(driver):
    return BasePage(driver)
    
@pytest.fixture
def cabinet_page(driver):
    return CabinetPage(driver)

@pytest.fixture
def audience_page(driver):
    return AudiencePage(driver)

@pytest.fixture
def campaign_page(driver):
    return CampaignPage(driver)

@pytest.fixture
def auto_auth(driver):
    page = BasePage(driver)
    page.auth(page.EMAIL,page.PASSWORD)
    return CabinetPage(page.driver)