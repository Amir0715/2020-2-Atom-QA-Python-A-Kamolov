from code.api.target_client import TargetClient
from conftest import Settings, config
import pytest

class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config, request):
        self.config: Settings = config
        self.target_client: TargetClient = request.getfixturevalue('target_client')