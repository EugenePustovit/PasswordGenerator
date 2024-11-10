import pytest
from selenium import webdriver


# @pytest.fixture(params=['Chrome', 'Firefox'])
@pytest.fixture
def driver(request):

    browser = request.config.getoption('--browser').capitalize()
    headless = request.config.getoption('--headless')

    # browser = request.param
    print(f'Creating {browser} driver')
    print(f'Headless mode { 'enabled' if headless else 'disabled' }')

    # my_driver = None
    match browser:
        case 'Chrome':
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument('--headless=new')

            my_driver = webdriver.Chrome(options=options)

        case 'Firefox':
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument('-headless')

            my_driver = webdriver.Firefox(options=options)

        case _:
            raise TypeError(f'Unknown browser {browser}. Available browsers for testing: Chrome, Firefox')

    yield my_driver

    print(f'Closing {browser} driver')
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        '--browser', action='store', default='Chrome', help='Web browser for test execution [ Chrome | Firefox ]'
    )
    parser.addoption(
        '--headless', action='store', default=False, help='Web browser headless mode [ True | False ]'
    )
