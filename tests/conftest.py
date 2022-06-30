__author__ = 'miserylab'

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selene.support.shared import browser
import pytest


@pytest.fixture(scope="session", autouse=True)
def set_web_driver():
    s = chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(service=Service(s))
    browser.set_driver(driver)


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.browser_name = 'chrome'
    browser.config.hold_browser_open = True
    browser.config.window_height = 1070
    browser.config.window_width = 1000

