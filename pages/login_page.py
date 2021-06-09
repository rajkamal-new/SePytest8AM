from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager

from base.page import Page
from utils import get_


class LoginPage(Page):

    def __init__(self, driver):
        super().__init__(driver)
        self.__title = By.ID, "logInPanelHeading"
        self.__username_tbox = By.ID, "txtUsername"
        self.__password_tbox = By.ID, "txtPassword"
        self.__login_btn = By.ID, "btnLogin"
        self.__forget_pass_link = By.CSS_SELECTOR, "#forgotPasswordLink>a"
        self.__err_msg_text = By.ID, "spanMessage"

    def load(self):
        return self._load()

    def get_title(self):
        return self._get_text(self.__title)

    def get_err_msg(self):
        return self._get_text(self.__err_msg_text)

    def input_username(self, username):
        self._input_text(self.__username_tbox, username)
        return self

    def input_password(self, password):
        self._input_text(self.__password_tbox, password)
        return self

    def click_login_btn(self):
        self._click(self.__login_btn)
        return self

    def click_forgot_pass(self):
        self._click(self.__forget_pass_link)

    def wait_until_dashboard_load(self):
        return self._wait_until_url_to_be(get_("SUB_URLS", "dashboard"))

    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_login_btn()
        return self



