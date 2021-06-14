import pytest

from pages.login_page import LoginPage
from utils.xl_reader import Excel


class TestLogin:


    @pytest.fixture()
    def delete_cookies(self):
        yield
        self.driver.delete_all_cookies()


    def test_login_success(self, delete_cookies):
        assert LoginPage(self.driver).load().login("Admin", "admin123").wait_until_dashboard_load()


    @pytest.mark.parametrize("username, password, err_msg", Excel("LoginFail").get_data())
    def test_login_fail(self, username, password, err_msg):
        assert LoginPage(self.driver).load().login(username, password).get_err_msg() == err_msg
