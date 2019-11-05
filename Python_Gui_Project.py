# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Python_Gui_Project.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1874, 1079)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tests_btn = QtWidgets.QPushButton(self.centralwidget)
        self.tests_btn.setGeometry(QtCore.QRect(100, 40, 151, 71))
        self.tests_btn.setObjectName("tests_btn")
        self.run_btn = QtWidgets.QPushButton(self.centralwidget)
        self.run_btn.setGeometry(QtCore.QRect(280, 40, 151, 71))
        self.run_btn.setObjectName("run_btn")
        self.logs_btn = QtWidgets.QPushButton(self.centralwidget)
        self.logs_btn.setGeometry(QtCore.QRect(450, 40, 151, 71))
        self.logs_btn.setObjectName("logs_btn")
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setGeometry(QtCore.QRect(630, 40, 161, 71))
        self.stop_btn.setFlat(False)
        self.stop_btn.setObjectName("stop_btn")
        self.selectall_btn = QtWidgets.QPushButton(self.centralwidget)
        self.selectall_btn.setGeometry(QtCore.QRect(80, 760, 181, 51))
        self.selectall_btn.setObjectName("selectall_btn")
        self.deselectall_btn = QtWidgets.QPushButton(self.centralwidget)
        self.deselectall_btn.setGeometry(QtCore.QRect(80, 850, 181, 51))
        self.deselectall_btn.setObjectName("deselectall_btn")
        self.log_list = QtWidgets.QTreeWidget(self.centralwidget)
        self.log_list.setGeometry(QtCore.QRect(20, 140, 291, 591))
        self.log_list.setObjectName("log_list")
        self.log_list.headerItem().setText(0, "1")
        self.text_box = QtWidgets.QTextEdit(self.centralwidget)
        self.text_box.setGeometry(QtCore.QRect(333, 143, 1531, 981))
        self.text_box.setObjectName("text_box")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1874, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tests_btn.setText(_translate("MainWindow", "Tests"))
        self.run_btn.setText(_translate("MainWindow", "Run"))
        self.logs_btn.setText(_translate("MainWindow", "Logs"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.selectall_btn.setText(_translate("MainWindow", "Select All"))
        self.deselectall_btn.setText(_translate("MainWindow", "Deselect All"))
