__author__ = 'miserylab'

from selene import have
from selene.core.entity import Element
from selene.support.shared import browser

class TagsInput:
    def __init__(self, element: Element):
        self.element = element

    def add_by_choosing(self, from_: str, /, *, option: str):
        self.element.type(from_)
        browser.all(
            '.subjects-auto-complete__option'
        ).element_by(have.text(option)).click()

    def add_by_tab_autocomplete(self, from_: str):
        self.element.type(from_).press_tab()
