__author__ = 'miserylab'

import pytest
from selene import have, command, browser
import conftest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene.support.shared import browser
from selene import Browser
from demoqa_tests.model.pages.modal_dialog import ModalDialog
from demoqa_tests.model.pages.page import StudentRegistrationForm

class ApplicationManager:
    def __init__(self):
        self.form = StudentRegistrationForm()
        self.results = ModalDialog()

    def given_student_registration_form_opened(self, browser_):
        # options = Options()
        # selenoid_capabilities = {
        #     "browserName": "chrome",
        #     "browserVersion": "100.0",
        #     "selenoid:options": {
        #         "enableVNC": True,
        #         "enableVideo": True
        #     }
        # }
        # options.capabilities.update(selenoid_capabilities)
        # driver = webdriver.Remote(
        #     command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        #     options=options)
        # browser.config.driver = driver

        browser.config.driver = browser_.driver

        browser.open('https://demoqa.com/automation-practice-form')
        (
            browser.all('[id^=google_ads][id$=container__],[id$=Advertisement]')
            .with_(timeout=10)
            .should(have.size_greater_than_or_equal(3))
            .perform(command.js.remove)
        )
        return self


app = ApplicationManager()
