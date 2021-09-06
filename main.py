import sys
from model import QTable_S
from gui import TableView_S
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from gui import gui_template
from PyQt5.QtGui import QStandardItem
from scripts import action_start
import os


class MainForm(QWidget, gui_template.Ui_Form):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        """ table """
        self.model_table = QTable_S.ModelQTableView()
        self.QTable = TableView_S.TableView(self.model_table)
        self.verticalLayout.addWidget(self.QTable)
        self.model_table.setHorizontalHeaderLabels(['id', 'Email', 'Password', 'Proxy', 'Action', 'Info', 'Social'])
        self.add_data()

        """btn start"""
        self.btn_start.clicked.connect(self.start)

        """ add actions for comboBox here"""
        self.comboBox.addItems(['start', 'get main page', 'follow'])

        """ list with objects from table"""
        self.data_list = []

    def add_data(self):
        with open('data/accounts.txt', 'r') as f:
            accounts = f.readlines()
        with open('data/proxy.txt', 'r') as f:
            proxy = f.readlines()
        for i, acc in enumerate(accounts):
            self.model_table.setItem(i, 0, QStandardItem(str(i)))
            self.model_table.setItem(i, 1, QStandardItem(acc.split(':')[0]))
            self.model_table.setItem(i, 2, QStandardItem(acc.split(':')[1]))
            self.model_table.setItem(i, 3, QStandardItem(proxy[i]))

    def return_select_rows_and_action(self):
        action = self.comboBox.currentText()
        list_rows_id = []
        indexes = self.QTable.selectionModel().selectedRows()
        for index in sorted(indexes):
            row = str(index.row())
            list_rows_id.append(int(self.model_table.item(int(row), 0).text()))
        ret_data = (list_rows_id, action)
        return ret_data

    def start(self):
        bar = self.return_select_rows_and_action()
        id_list = bar[0]
        action = bar[1]
        if action == 'follow':
            parsing_file_path = QFileDialog.getOpenFileName(
                parent=self,
                caption='Select parsing file',
                directory=os.getcwd(),
            )[0]
            with open(parsing_file_path, 'r', encoding='utf-8') as f:
                parsing_file = f.read().split('\n')
            n = len(parsing_file) // len(id_list)
            list_of_lists_parsing = [parsing_file[i:i + n] for i in range(0, len(parsing_file), n)]
            for i in list_of_lists_parsing:
                print(i)
        count_parsing_list = 0
        for id in id_list:
            if action == 'start':
                email = self.model_table.item(id, 1).text()
                password = self.model_table.item(id, 2).text()
                proxy = self.model_table.item(id, 3).text()
                self.model_table.setItem(id, 5, QStandardItem('started'))
                data = action_start.Data(action, id, email, password, proxy)
                self.data_list.append({'id': id, 'data': data})
                action_start.thread_action(data)
            elif action == 'follow':
                for i in self.data_list:
                    if i['id'] == id:
                        i['data'].action = action
                        i['data'].parsing_list = list_of_lists_parsing[count_parsing_list]
                        count_parsing_list += 1
            else:
                for i in self.data_list:
                    if i['id'] == id:
                        i['data'].action = action


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainForm()
    w.setWindowTitle('StationTikTok')
    w.show()
    sys.exit(app.exec_())