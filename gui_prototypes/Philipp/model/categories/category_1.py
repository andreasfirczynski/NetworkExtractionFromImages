# -*- coding: utf-8 -*-
from model.categories._category import *


class CatBody(Category):
    def __init__(self):
        self.name = 'EXAMPLE_CATEGORY_1'
        # we need Category to load its algorithms after self.name assignment
        Category.__init__(self)


if __name__ == '__main__':
    pass
