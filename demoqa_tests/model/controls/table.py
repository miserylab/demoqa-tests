__author__ = 'miserylab'

from selene import have
from selene.core.entity import Element


class Table:
    def __init__(self, element: Element):
        self.element = element

    # def results(self, row_index: int, column_index: int, *values: str):
    #     for value in values:
    #         self.element.all('tr')[row_index].all('td')[column_index].should(have.text(value))
    #     return self

    def cell(self, row_index: int, colum_index: int):
        return self.element.all('tbody tr')[row_index].all('td')[colum_index]

