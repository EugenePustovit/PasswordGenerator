import pytest

from helper.password_config import PasswordConfig
from pages.password_generator_page import PasswordGeneratorPage


@pytest.mark.password_generator
class TestPasswordGenerator:

    __error_msg_pass_length = 'Wrong length of generated password'
    __error_msg_pass_options = 'Password does not match requested options'
    __error_msg_pass_was_not_generated = 'Password was not generated'
    __error_msg_enabled_options = 'Enabled options different from expected'
    __error_msg_wrong_pass_length_displayed = 'Wrong password length displayed on the page'

    @pytest.mark.test
    @pytest.mark.positive
    def test_default_password(self, driver):
        password_generator = PasswordGeneratorPage(driver)
        pass_cfg = PasswordConfig()

        password_generator.load()
        pass_cfg.password = password_generator.password
        pass_cfg.length = password_generator.password_length
        pass_cfg.options = password_generator.password_options

        assert pass_cfg.is_match_length(), self.__error_msg_pass_length
        assert pass_cfg.is_match_options(), self.__error_msg_pass_options

    @pytest.mark.positive
    def test_generate_password(self, driver):
        password_generator = PasswordGeneratorPage(driver)
        password_generator.load()
        password = password_generator.password

        password_generator.generate_password()
        new_pass_cfg = PasswordConfig()
        new_pass_cfg.password = password_generator.password
        new_pass_cfg.length = password_generator.password_length
        new_pass_cfg.options = password_generator.password_options

        assert password != new_pass_cfg.password, self.__error_msg_pass_was_not_generated
        assert new_pass_cfg.is_match_length(), self.__error_msg_pass_length
        assert new_pass_cfg.is_match_options(), self.__error_msg_pass_options

    @pytest.mark.positive
    @pytest.mark.parametrize('password_length', ['12', '32', '6'])
    def test_change_password_length(self, driver, password_length):
        password_generator = PasswordGeneratorPage(driver)
        password_generator.load()
        password = password_generator.password

        if password_length == '6':
            password_generator.password_length = str(int(password_length) + 4)

        password_generator.password_length = password_length
        new_pass_cfg = PasswordConfig()
        new_pass_cfg.password = password_generator.password
        new_pass_cfg.length = password_generator.password_length
        new_pass_cfg.options = password_generator.password_options

        assert password != new_pass_cfg.password, self.__error_msg_pass_was_not_generated
        assert len(new_pass_cfg.password) == int(password_length), self.__error_msg_pass_length
        assert new_pass_cfg.is_match_length(), self.__error_msg_wrong_pass_length_displayed
        assert new_pass_cfg.is_match_options(), self.__error_msg_pass_options

    @pytest.mark.positive
    @pytest.mark.parametrize('options', [(True, False, False, True),
                                         (False, False, True, True),
                                         (True, True, True, True),
                                         (False, True, True, False)])
    def test_enable_password_option(self, driver, options):
        password_generator = PasswordGeneratorPage(driver)
        password_generator.load()
        password = password_generator.password

        password_generator.enable_options(*options)

        new_pass_cfg = PasswordConfig()
        new_pass_cfg.password = password_generator.password
        new_pass_cfg.length = password_generator.password_length
        new_pass_cfg.options = password_generator.password_options

        assert password != new_pass_cfg.password, self.__error_msg_pass_was_not_generated
        assert tuple(new_pass_cfg.options.values()) == options, self.__error_msg_enabled_options
        assert new_pass_cfg.is_match_options(), self.__error_msg_pass_options
        assert new_pass_cfg.is_match_length(), self.__error_msg_pass_length

    @pytest.mark.negative
    @pytest.mark.parametrize('target_length, exp_length', [('33', '6'), ('5', '6')])
    def test_set_out_of_range_password_length(self, driver, target_length, exp_length):
        password_generator = PasswordGeneratorPage(driver)
        password_generator.load()

        password_generator.password_length = target_length

        new_pass_cfg = PasswordConfig()
        new_pass_cfg.password = password_generator.password
        new_pass_cfg.length = password_generator.password_length
        new_pass_cfg.options = password_generator.password_options

        assert new_pass_cfg.length == exp_length, self.__error_msg_pass_length
        assert new_pass_cfg.is_match_length(), self.__error_msg_pass_length
