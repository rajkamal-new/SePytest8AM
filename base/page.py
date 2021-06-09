from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from utils import get_

class Page:
    def __init__(self, driver):
        self.driver = driver

    def _find_element(self, locator):
        try:
            return self.driver.find_element(*locator)
        except NoSuchElementException:
            return self._wait_until_element_is_visible(locator)

    def _wait_until_element_is_visible(self, locator):
        wait = WebDriverWait(self.driver, 10)
        try:
            return wait.until(ec.visibility_of_element_located(locator))
        except TimeoutException as e:

            raise e

    def _wait_until_element_is_clickable(self, locator):
        wait = WebDriverWait(self.driver, 10)
        try:
            return wait.until(ec.element_to_be_clickable(locator))
        except TimeoutException as e:

            raise e

    def _click(self, locator):
        self._wait_until_element_is_clickable(locator).click()

    def _input_text(self, locator, text):
        self._find_element(locator).send_keys(text)

    def _get_text(self, locator):
        return self._find_element(locator).text

    def _load(self, url=get_("ENV", "url")):
        self.driver.get(url)
        return self

    def _wait_until_url_contains(self, text):
        wait = WebDriverWait(self.driver, 10)
        try:
            return wait.until(ec.url_contains(text))
        except TimeoutException as e:

            raise e

    def _wait_until_url_to_be(self, text):
        wait = WebDriverWait(self.driver, 10)
        try:
            return wait.until(ec.url_to_be(text))
        except TimeoutException as e:

            raise e
