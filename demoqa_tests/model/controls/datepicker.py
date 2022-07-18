__author__ = 'miserylab'

from selene.core import command
from selene.core.entity import Element
from selene.support.shared import browser


class DatePicker:
    def __init__(self, element: Element):
        self.element = element

    def select(self, year: int, month: int, day: int):
        self.element.click()
        browser.element('[class*="year-select"]').click().element(f'[value="{year}"]').click()
        browser.element('[class*="month-select"]').click().element(f'[value="{month - 1}"]').click()
        browser.element(f'[class*="datepicker__day--0{day}"]').click()

    def set_value(self, option: str):
        self.element.click()
        browser.execute_script(
            '''
                document.querySelector("#dateOfBirthInput")
                .value = ''
            ''')
        self.element.set_value(option).click()
