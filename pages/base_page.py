from selenium.webdriver import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _load(self, url: str):
        self._driver.get(url)

    def _wait_until_element_is_visible(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        wait = WebDriverWait(self._driver, timeout)
        return wait.until(ec.visibility_of_element_located(locator))

    def _wait_until_element_is_present(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        wait = WebDriverWait(self._driver, timeout)
        return wait.until(ec.presence_of_element_located(locator))

    def _find_element(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        return self._wait_until_element_is_visible(locator, timeout)

    def _click(self, locator: tuple[str, str], timeout: int = 10):
        self._find_element(locator, timeout).click()

    def _type(self, locator: tuple[str, str], text: str, timeout: int = 10):
        self._find_element(locator, timeout).send_keys(text)

    def _delete_and_type(self, locator: tuple[str, str], text: str, timeout: int = 10):
        self._find_element(locator, timeout).send_keys(Keys.BACKSPACE, Keys.BACKSPACE, text)

    def _get_attribute(self, locator: tuple[str, str], attribute_name: str, timeout: int = 10) -> str:
        return self._find_element(locator, timeout).get_attribute(attribute_name)

    def _is_checkbox_selected(self, locator: tuple[str, str], timeout: int = 10) -> bool:
        return self._wait_until_element_is_present(locator, timeout).is_selected()
