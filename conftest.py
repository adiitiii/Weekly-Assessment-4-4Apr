import pytest
from selenium import webdriver
from config .env import ConfigReader

@pytest.fixture
def setup_and_teardown():
    # Read Config
    config = ConfigReader.read_config()
    env = config["qa"]          ## accessing the YAML file
    base_url = env["base_url"]

    # setup (Before test)

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(base_url)

    yield driver  # test runs here

    #Teardown began after here
    driver.quit()