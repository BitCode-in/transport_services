# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_template/engine.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os


class Ui_widget(object):
    def setupUi(self, widget):
        self.tempwidget = widget
        widget.setObjectName("widget")
        widget.resize(705, 528)
        self.label = QtWidgets.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(12, 12, 110, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit_5 = QtWidgets.QLineEdit(widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(204, 136, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(204, 74, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_3 = QtWidgets.QLabel(widget)
        self.label_3.setGeometry(QtCore.QRect(12, 74, 184, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(widget)
        self.label_5.setGeometry(QtCore.QRect(12, 136, 63, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(widget)
        self.label_4.setGeometry(QtCore.QRect(12, 105, 112, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(widget)
        self.lineEdit.setGeometry(QtCore.QRect(204, 12, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(204, 43, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(204, 105, 471, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(12, 43, 43, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setGeometry(QtCore.QRect(490, 470, 201, 32))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background: rgb(0, 255, 127);\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    border-radius: 5px;  /* Установите радиус закругления, например, 10px */\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(widget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 180, 681, 221))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.scrollArea.setFont(font)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet("QScrollArea{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 679, 219))
        self.scrollAreaWidgetContents_2.setAutoFillBackground(True)
        self.scrollAreaWidgetContents_2.setStyleSheet("")
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_2.addWidget(self.label_6)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_2.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background: rgb(0, 255, 127);\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    border-radius: 5px;  /* Установите радиус закругления, например, 10px */\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_3.setMinimumSize(QtCore.QSize(20, 20))
        self.pushButton_3.setMaximumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background: rgb(255, 119, 121);\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    border-radius: 5px;  /* Установите радиус закругления, например, 10px */\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 20))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.widget_2.setFont(font)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_26 = QtWidgets.QLabel(self.widget_2)
        self.label_26.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_5.addWidget(self.label_26)
        self.label_27 = QtWidgets.QLabel(self.widget_2)
        self.label_27.setMinimumSize(QtCore.QSize(0, 0))
        self.label_27.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_27.setFont(font)
        self.label_27.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_5.addWidget(self.label_27)
        self.label_28 = QtWidgets.QLabel(self.widget_2)
        self.label_28.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_28.setFont(font)
        self.label_28.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_5.addWidget(self.label_28)
        self.label_29 = QtWidgets.QLabel(self.widget_2)
        self.label_29.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_29.setObjectName("label_29")
        self.horizontalLayout_5.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.widget_2)
        self.label_30.setMinimumSize(QtCore.QSize(180, 0))
        self.label_30.setMaximumSize(QtCore.QSize(180, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_5.addWidget(self.label_30)
        self.label_10 = QtWidgets.QLabel(self.widget_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout.addLayout(self.verticalLayout_3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.widget_3 = QtWidgets.QWidget(widget)
        self.widget_3.setGeometry(QtCore.QRect(10, 410, 681, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.widget_3.setFont(font)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout.addWidget(self.lineEdit_6)
        spacerItem2 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_4.setMinimumSize(QtCore.QSize(25, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background: rgba(255, 255, 255, 0);\n"
"}")
        self.pushButton_4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{os.getcwd()}/res/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.label_8 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout.addWidget(self.lineEdit_7)
        spacerItem5 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_5.setMinimumSize(QtCore.QSize(25, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background: rgba(255, 255, 255, 0);\n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.label_9 = QtWidgets.QLabel(widget)
        self.label_9.setGeometry(QtCore.QRect(10, 452, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_9.setFont(font)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(f"{os.getcwd()}/res/logo.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Зерновой трейдер"))
        self.label.setText(_translate("widget", "Номер договора:"))
        self.label_3.setText(_translate("widget", "Перевозимая культура"))
        self.label_5.setText(_translate("widget", "Маршрут:"))
        self.label_4.setText(_translate("widget", "Стоимость услуг:"))
        self.label_2.setText(_translate("widget", "Город:"))
        self.pushButton.setText(_translate("widget", "Сформировать договор"))
        self.label_6.setText(_translate("widget", "Авто"))
        self.pushButton_2.setText(_translate("widget", "+"))
        self.pushButton_3.setText(_translate("widget", "-"))
        self.label_26.setText(_translate("widget", "№"))
        self.label_27.setText(_translate("widget", "Марка:"))
        self.label_28.setText(_translate("widget", "№ Тягача"))
        self.label_29.setText(_translate("widget", "№ Прицепа"))
        self.label_30.setText(_translate("widget", "ФИО водителя"))
        self.label_10.setText(_translate("widget", "Паспортные данные"))
        self.label_7.setText(_translate("widget", "Исполнитель:"))
        self.label_8.setText(_translate("widget", "Заказчик:"))
