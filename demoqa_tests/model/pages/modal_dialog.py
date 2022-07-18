__author__ = 'miserylab'

from selene import have
from selene.support.shared import browser

from demoqa_tests.model.controls.table import Table


class ModalDialog:

    def __init__(self):
        self.element = browser.element('.modal-content')
        self.table = Table(self.element.element('.table'))

    def should_have_row_with_exact_texts(self, row_index: int, column_index: int, *values: str):
        for values in values:
            self.element.all('tbody tr')[row_index].all('td')[column_index].should(have.text(values))
        return self