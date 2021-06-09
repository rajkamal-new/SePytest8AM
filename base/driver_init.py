from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from utils import get_


def driver_init():
    browser = get_("ENV", "browser")
    global driver

    if browser == "chrome":
        driver = Chrome(ChromeDriverManager().install())


    driver.maximize_window()


    return driver

