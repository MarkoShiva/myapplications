# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Tue Aug 27 15:55:46 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(275, 314)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.todoView = QtWidgets.QListView(self.centralwidget)
        self.todoView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.todoView.setObjectName("todoView")
        self.verticalLayout.addWidget(self.todoView)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.deleteButton = QtWidgets.QPushButton(self.widget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.completeButton = QtWidgets.QPushButton(self.widget)
        self.completeButton.setObjectName("completeButton")
        self.horizontalLayout.addWidget(self.completeButton)
        self.verticalLayout.addWidget(self.widget)
        self.todoEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.todoEdit.setObjectName("todoEdit")
        self.verticalLayout.addWidget(self.todoEdit)
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 275, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "Todo", None, -1))
        self.deleteButton.setText(QtWidgets.QApplication.translate("MainWindow", "Delete", None, -1))
        self.completeButton.setText(QtWidgets.QApplication.translate("MainWindow", "Complete", None, -1))
        self.addButton.setText(QtWidgets.QApplication.translate("MainWindow", "Add Todo", None, -1))

