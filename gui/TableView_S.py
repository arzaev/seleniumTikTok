# coding: utf-8

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QAbstractTableModel
from PyQt5.QtWidgets import QTableView, QHeaderView


class TableView(QTableView):
    def __init__(self, model, parent=None):
        QTableView.__init__(self, parent)
        # self.table_twitter = QtGui.QTableView()
        # self.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.setModel(model)
        self.setSelectionBehavior(self.SelectRows)
        self.setSelectionMode(self.ExtendedSelection)
        self.horizontalHeader().setStretchLastSection(True)
        self.setSortingEnabled(True)
        self.verticalHeader().hide()