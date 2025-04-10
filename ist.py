# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ist.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_IstWindow(object):
    def setupUi(self, IstWindow):
        IstWindow.setObjectName("IstWindow")
        IstWindow.resize(515, 660)
        self.centralwidget = QtWidgets.QWidget(IstWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 461, 31))
        self.lineEdit.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 211, 21))
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 130, 461, 31))
        self.lineEdit_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 211, 21))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 360, 461, 41))
        self.pushButton.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 420, 231, 21))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 460, 461, 31))
        self.comboBox.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 510, 461, 41))
        self.pushButton_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 261, 21))
        self.label_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 210, 461, 31))
        self.comboBox_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 570, 91, 61))
        self.pushButton_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 290, 461, 31))
        self.lineEdit_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 260, 471, 21))
        self.label_5.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        IstWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(IstWindow)
        self.statusbar.setObjectName("statusbar")
        IstWindow.setStatusBar(self.statusbar)

        self.retranslateUi(IstWindow)
        QtCore.QMetaObject.connectSlotsByName(IstWindow)

    def retranslateUi(self, IstWindow):
        _translate = QtCore.QCoreApplication.translate
        IstWindow.setWindowTitle(_translate("IstWindow", "Сбор-SN"))
        self.label.setText(_translate("IstWindow", "Введите код источника"))
        self.label_2.setText(_translate("IstWindow", "Введите URL-адрес"))
        self.pushButton.setText(_translate("IstWindow", "Добавить"))
        self.label_3.setText(_translate("IstWindow", "Выберите код источника"))
        self.pushButton_2.setText(_translate("IstWindow", "Удалить"))
        self.label_4.setText(_translate("IstWindow", "Выберите социальную сеть"))
        self.pushButton_3.setText(_translate("IstWindow", "Назад"))
        self.label_5.setText(_translate("IstWindow", "Введите ссылку на канал (группу) социальной сети"))

