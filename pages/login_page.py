from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):

    # locators for login page elements
    login_link = (By.LINK_TEXT, "Log in")
    email = (By.ID, "Email")
    password = (By.ID, "Password")
    login_button = (By.XPATH, "//input[@value='Log in']")

    def __init__(self, driver):
        super().__init__(driver)   # calling base class constructor

    def click_login(self):
        self.click(self.login_link)   # click login link

    def enter_email(self, email):
        self.enter_text(self.email, email)   # enter email

    def enter_password(self, password):
        self.enter_text(self.password, password)   # enter password

    def click_login_button(self):
        self.click(self.login_button)   # click login button