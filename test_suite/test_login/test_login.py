import pytest

from pages.login_page import LoginPage


class TestLogin:

    @pytest.fixture()
    def delete_cookies(self):
        yield
        self.driver.delete_all_cookies()


    def test_login_success(self, delete_cookies):
        assert LoginPage(self.driver).load().login("Admin", "admin123").wait_until_dashboard_load()

    @pytest.mark.ft
    def test_login_fail_empty_username(self):
        assert LoginPage(self.driver).load().login("", "admin123").get_err_msg() == "Username cannot be empty"
