# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(551, 95)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 391, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 12, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(340, 50, 201, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background: rgb(0, 255, 127);\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    border-radius: 5px;  /* Установите радиус закругления, например, 10px */\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(10, 39, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("../res/logo.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 0, 21, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background: rgb(0, 255, 127);\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    border-radius: 5px;  /* Установите радиус закругления, например, 10px */\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Путь сохранения:"))
        self.pushButton.setText(_translate("Form", "Сохранить"))
        self.pushButton_2.setText(_translate("Form", "Сохранить"))
