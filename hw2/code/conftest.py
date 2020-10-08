import pytest
from _pytest.fixtures import FixtureRequest
from selenium.webdriver import ChromeOptions
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    selenoid = request.config.getoption('--selenoid')
    return {'url': url, 'selenoid' : selenoid, 'download_dir': '/tmp'}


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com')
    parser.addoption('--selenoid', default=None)


@pytest.fixture(scope='function')
def driver(config):
    driver = None

    if config['selenoid'] is not None:
        
        selenoid_url = 'http://' + config['selenoid'] + '/wd/hub'
        options = ChromeOptions()
        driver = webdriver.Remote(command_executor=selenoid_url, options=options, desired_capabilities=DesiredCapabilities().CHROME)

    else:  

        options = ChromeOptions()
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options, desired_capabilities=DesiredCapabilities().CHROME)
    
    driver.maximize_window()
    driver.get(config['url'])
    yield driver
    driver.quit()
