# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customers_add.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(703, 304)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(490, 260, 201, 32))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background: rgb(0, 255, 127);\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    border-radius: 5px;  /* Установите радиус закругления, например, 10px */\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalWidget = QtWidgets.QWidget(Form)
        self.verticalWidget.setGeometry(QtCore.QRect(10, 10, 681, 241))
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalWidget)
        self.label.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.verticalWidget)
        self.label_2.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_5.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.verticalWidget)
        self.label_3.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_6.addWidget(self.lineEdit_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.verticalWidget)
        self.label_4.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_7.addWidget(self.lineEdit_4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.verticalWidget)
        self.label_5.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_8.addWidget(self.lineEdit_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.verticalWidget)
        self.label_7.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_10.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_10.addWidget(self.lineEdit_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.verticalWidget)
        self.label_6.setMinimumSize(QtCore.QSize(300, 0))
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalWidget)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_9.addWidget(self.lineEdit_6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Сохранить"))
        self.label.setText(_translate("Form", "Название организации"))
        self.label_2.setText(_translate("Form", "ФИО заказчика"))
        self.label_3.setText(_translate("Form", "Адрес"))
        self.label_4.setText(_translate("Form", "ИНН"))
        self.label_5.setText(_translate("Form", "Р/С"))
        self.label_7.setText(_translate("Form", "Название банка заказчика"))
        self.label_6.setText(_translate("Form", "БИК заказчика"))
