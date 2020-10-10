import pytest
from _pytest.fixtures import FixtureRequest
from audience_page import AudiencePage
from base_page import BasePage
from campaign_page import CampaignPage
from cabinet_page import CabinetPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self,driver,config,request:FixtureRequest):
        self.driver = driver
        self.config = config
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.cabinet_page: CabinetPage = request.getfixturevalue('cabinet_page')
        self.audience_page : AudiencePage = request.getfixturevalue('audience_page')
        self.campaign_page : CampaignPage = request.getfixturevalue('campaign_page')