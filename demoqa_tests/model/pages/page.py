__author__ = 'miserylab'

from selene import command
from selene.support.shared import browser

from demoqa_tests.model.controls import dropdown
from demoqa_tests.model.controls.checkbox import hobby_select
from demoqa_tests.model.controls.datepicker import DatePicker
from demoqa_tests.model.controls.tags_input import TagsInput
from demoqa_tests.utils.path import data


class StudentRegistrationForm:

    def __init__(self):
        self.date_of_birth = DatePicker(browser.element('#dateOfBirthInput'))
        self.submit_button = browser.element('#submit')

    def set_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def set_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def set_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def set_gender(self, value):
        gender = ''
        if value == 'Male':
            gender = '[for=gender-radio-1]'
        elif value == 'Female':
            gender = '[for=gender-radio-2]'
        elif value == 'Other':
            gender = '[for=gender-radio-2]'
        browser.element(gender).click()
        return self

    def set_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def set_date_of_birth(self, year, month, day):
        self.date_of_birth.select(year, month, day)
        return self

    def set_subjects(self, *values):
        for value in values:
            TagsInput(browser.element('#subjectsInput')).add_by_tab_autocomplete(value)
        return self

    def set_hobbies(self, *values):
        for value in values:
            hobby_select(value)
        return self

    def upload_picture(self, image):
        browser.element('#uploadPicture').send_keys(data(image))
        return self

    def set_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def set_state(self, state):
        dropdown.select(browser.element('#state').perform(command.js.scroll_into_view), option=state)
        return self

    def set_city(self, city):
        dropdown.autocomplete(browser.element('#city'), option=city)
        return self

    def submit(self):
        self.submit_button.perform(command.js.click)
