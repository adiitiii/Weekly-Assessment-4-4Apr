from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)   # wait for elements

    # wait until element is clickable and then click
    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    # wait until element is visible, clear and type text
    def enter_text(self, locator, text):
        self.wait.until(EC.visibility_of_element_located(locator)).clear()
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    # get text from element
    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    # check element is visible
    def is_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))