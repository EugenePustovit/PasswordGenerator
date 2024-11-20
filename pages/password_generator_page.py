import time

from jinja2.idtracking import symbols_for_node
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from pages.base_page import BasePage


class PasswordGeneratorPage(BasePage):

    _url = 'https://www.security.org/password-generator/'

    __password_locator = By.ID, 'password'
    __generate_password_button_locator = By.XPATH, '//button[@title="Generate password"]'
    __password_length_locator = By.ID, 'passwordLength'
    __password_length_range_locator = By.ID, 'passwordLengthRange'
    __option_lowercase_checkbox_locator = By.ID, 'option-lowercase'
    __option_uppercase_checkbox_locator = By.ID, 'option-uppercase'
    __option_numbers_checkbox_locator = By.ID, 'option-numbers'
    __option_symbols_checkbox_locator = By.ID, 'option-symbols'
    __set_option_lowercase_checkbox_locator = By.XPATH, '//label[@for="option-lowercase"]'
    __set_option_uppercase_checkbox_locator = By.XPATH, '//label[@for="option-uppercase"]'
    __set_option_numbers_checkbox_locator = By.XPATH, '//label[@for="option-numbers"]'
    __set_option_symbols_checkbox_locator = By.XPATH, '//label[@for="option-symbols"]'
    __copy_password_button_locator = By.XPATH, '//button[@title="Copy Password"]'


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def load(self):
        self._load(self._url)

    @property
    def password(self) -> str:
        return self._get_attribute(self.__password_locator, 'value')

    @property
    def password_length(self) -> str:
        return self._get_attribute(self.__password_length_range_locator, 'value')

    @password_length.setter
    def password_length(self, length: str):
        self._delete_and_type(self.__password_length_locator, length)

    @property
    def lowercase_enabled(self) -> bool:
        return self._is_checkbox_selected(self.__option_lowercase_checkbox_locator)

    @lowercase_enabled.setter
    def lowercase_enabled(self, value: bool):
        if self.lowercase_enabled != value:
            self._click(self.__set_option_lowercase_checkbox_locator)

    @property
    def uppercase_enabled(self) -> bool:
        return self._is_checkbox_selected(self.__option_uppercase_checkbox_locator)

    @uppercase_enabled.setter
    def uppercase_enabled(self, value: bool):
        if self.uppercase_enabled != value:
            self._click(self.__set_option_uppercase_checkbox_locator)

    @property
    def numbers_enabled(self) -> bool:
        return self._is_checkbox_selected(self.__option_numbers_checkbox_locator)

    @numbers_enabled.setter
    def numbers_enabled(self, value: bool):
        if self.numbers_enabled != value:
            self._click(self.__set_option_numbers_checkbox_locator)

    @property
    def symbols_enabled(self) -> bool:
        return self._is_checkbox_selected(self.__option_symbols_checkbox_locator)

    @symbols_enabled.setter
    def symbols_enabled(self, value: bool):
        if self.symbols_enabled != value:
            self._click(self.__set_option_symbols_checkbox_locator)

    @property
    def password_options(self) -> dict:
        return {
            'Lowercase': self.lowercase_enabled,
            'Uppercase': self.uppercase_enabled,
            'Numbers': self.numbers_enabled,
            'Symbols': self.symbols_enabled
        }

    def generate_password(self):
        self._click(self.__generate_password_button_locator)

    def enable_options(self,
                       lowercase :bool = False,
                       uppercase :bool = False,
                       numbers : bool = False,
                       symbols : bool = False):

        self.symbols_enabled = symbols
        self.numbers_enabled = numbers
        self.uppercase_enabled = uppercase
        self.lowercase_enabled = lowercase

    def copy_password(self):
        self._click(self.__copy_password_button_locator)

    def is_text_present(self, text: str) -> bool:
        return self._wait_until_text_is_present(self.__copy_password_button_locator, text)



