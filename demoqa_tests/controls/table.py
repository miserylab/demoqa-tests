__author__ = 'miserylab'

from selene.core.entity import Element


class Table:
    def __init__(self, element: Element):
        self.element = element

    def cell(self, row_index: int, colum_index: int):
        return self.element.all('tbody tr')[row_index].all('td')[colum_index]

