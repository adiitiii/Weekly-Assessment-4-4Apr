from config.env import ConfigReader
from pages.login_page import LoginPage
from utils.loggers import get_logger


def test_valid_login(setup_and_teardown):
    driver = setup_and_teardown   # getting driver from fixture

    logger = get_logger()   # creating logger to track steps

    lp = LoginPage(driver)   # creating object of login page

    # reading data from config file
    config = ConfigReader.read_config()
    env = config['qa']

    BASE_URL = env['base_url']
    USERNAME = env['username']
    PASSWORD = env['password']

    logger.info("Opening website")

    driver.get(BASE_URL)   # open website

    # performing login steps
    logger.info("Clicking login link")
    lp.click_login()

    logger.info("Entering email")
    lp.enter_email(USERNAME)

    logger.info("Entering password")
    lp.enter_password(PASSWORD)

    logger.info("Clicking login button")
    lp.click_login_button()

    logger.info("Login steps completed")