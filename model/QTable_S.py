# coding: utf-8

from PyQt5 import QtGui
from PyQt5.QtGui import QStandardItem


class ModelQTableView(QtGui.QStandardItemModel):
    def __init__(self, parent=None):
        QtGui.QStandardItem.__init__(self, parent)

        # self.setHorizontalHeaderLabels(['id', 'Vertical', 'Bot', 'Status', 'Action', 'Info', 'Social'])

    # def update_table(self):
    #     return self.setHorizontalHeaderLabels(['id', 'Vertical', 'Bot', 'Status', 'Action', 'Info', 'Social'])
