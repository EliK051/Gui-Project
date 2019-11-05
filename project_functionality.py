import os
import datetime
import sys
from pathlib import Path
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QFileInfo, QUrl
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTreeWidgetItem, QTreeWidget
from subprocess import Popen, PIPE, call

from PyQt5.uic.properties import QtGui

from Python_Gui_Project import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.run_btn.clicked.connect(self.run_selected)
        self.ui.tests_btn.clicked.connect(self.get_and_create_list)
        # QtWidgets.QTreeWidget.setHeaderLabel('tree')
        self.ui.log_list.header().hide()
        # self.ui.logs_btn.clicked.connect(self.on_pushButton_clicked)
        self.ui.logs_btn.setEnabled(False)
        self.ui.deselectall_btn.setEnabled(False)
        self.ui.selectall_btn.setEnabled(False)
        self.ui.stop_btn.setEnabled(False)


    def run_selected(self):
        # checked = dict()
        checked_boxes = list()
        root = self.ui.log_list.invisibleRootItem()
        node_count = root.childCount()

        for i in range(node_count):
            signal = root.child(i)
            if signal.checkState(0) == QtCore.Qt.Checked:
                checked_boxes.append(signal.text(0))

            # checked[signal.text(0)] = checked_boxes
        print(checked_boxes)
        self.execute_test(checked_boxes)



    def present_log(self,current):
        current_date=datetime.datetime.now()
        current_time=(current_date.strftime("%H-%M"))
        # print(current_time)
        current_date=str(current_date)
        current_date=current_date.split(" ")
        # print(current_date[0])
        print(f'{current}\\{current_date[0]}\\results-{current_time}')
        # \\results - {current_time}
        file = QtCore.QFile(f'C:\\Users\\Elik\\Desktop\\seleniumProject\\log\\{current}\\{current_date[0]}.log')
        if not file.open(QtCore.QIODevice.ReadOnly):
            QtGui.QMessageBox.information(None, 'info', file.errorString())
        stream = QtCore.QTextStream(file)
        self.ui.text_box.append(stream.readAll())

    def execute_test(self,tests):
        # print(tests)
        for current_test in tests:
            # print(current_test)
            call(f'node {current_test}',cwd='C:\\Users\\Elik\Desktop\\seleniumProject', shell='true')
            self.present_log(current_test.split(".")[0])

    def get_and_create_list(self):
        files = QFileDialog.getOpenFileNames(self, ("Open test"), "C:\\Users\Elik\Desktop\seleniumProject", ("Js Files (*.js)"))[0]

        if files:
            print(files)

            for file in files:
                print(file)
                filename = Path(file).name
                QtWidgets.QTreeWidgetItem(self.ui.log_list, [filename]).setCheckState(0, Qt.Unchecked)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
