from selenium.webdriver.common.by import By

from base.page import Page


class Header(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.__welcome_text = By.ID, "welcome"
        self.__about_link = By.ID, "aboutDisplayLink"
        self.__support_link = By.CSS_SELECTOR, "a[href$='support/index']"
        self.__logout_link = By.CSS_SELECTOR, "a[href$='logout']"

    def get_welcome_text(self):
        return self._get_text(self.__welcome_text)

    def logout(self):
        self._click(self.__welcome_text)
        self._click(self.__logout_link)
