from dataclasses import dataclass
from code.api.target_client import TargetClient
import pytest

@dataclass
class Settings:
    USERNAME: str = None
    PASSWORD: str = None

@pytest.fixture(scope='session')
def config() -> Settings:
    settings = Settings(
        USERNAME='kamolov.amir2000@yandex.ru', 
        PASSWORD='x4r-zbC-SYM-gj8'
        )

    return settings


@pytest.fixture(scope='function')
def target_client(config):
    return TargetClient(config.USERNAME, config.PASSWORD)