# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ispoln.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IspolnWindow(object):
    def setupUi(self, IspolnWindow):
        IspolnWindow.setObjectName("IspolnWindow")
        IspolnWindow.resize(485, 445)
        self.centralwidget = QtWidgets.QWidget(IspolnWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 60, 431, 31))
        self.comboBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 190, 431, 31))
        self.lineEdit.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 240, 431, 31))
        self.pushButton.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 110, 431, 31))
        self.pushButton_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 351, 21))
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 431, 21))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(344, 320, 91, 61))
        self.pushButton_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        IspolnWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(IspolnWindow)
        self.statusbar.setObjectName("statusbar")
        IspolnWindow.setStatusBar(self.statusbar)

        self.retranslateUi(IspolnWindow)
        QtCore.QMetaObject.connectSlotsByName(IspolnWindow)

    def retranslateUi(self, IspolnWindow):
        _translate = QtCore.QCoreApplication.translate
        IspolnWindow.setWindowTitle(_translate("IspolnWindow", "Сбор-SN"))
        self.pushButton.setText(_translate("IspolnWindow", "Добавить"))
        self.pushButton_2.setText(_translate("IspolnWindow", "Удалить"))
        self.label.setText(_translate("IspolnWindow", "Выбрать исполнителя на удаление"))
        self.label_2.setText(_translate("IspolnWindow", "Введите Фамилию и инициалы для добавления"))
        self.pushButton_3.setText(_translate("IspolnWindow", "Назад"))

