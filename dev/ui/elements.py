from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

class GenAuto(QtWidgets.QWidget):
	def __init__(self, settext):
		super().__init__()
		self.setMinimumSize(QtCore.QSize(0, 20))
		self.setMaximumSize(QtCore.QSize(16777215, 20))
		font = QtGui.QFont()
		font.setFamily("Arial")
		self.setFont(font)
		self.setObjectName("widget")
		self.verticalLayout = QtWidgets.QVBoxLayout(self)
		self.verticalLayout.setContentsMargins(0, 0, 0, 0)
		self.verticalLayout.setSpacing(0)
		self.verticalLayout.setObjectName("verticalLayout")
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setSpacing(5)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label_1 = QtWidgets.QLabel(self)
		self.label_1.setMinimumSize(QtCore.QSize(30, 0))
		self.label_1.setMaximumSize(QtCore.QSize(30, 16777215))
		self.label_1.setFont(font)
		self.label_1.setObjectName("label_1")
		self.label_1.setText(settext)
		self.horizontalLayout.addWidget(self.label_1)
		self.lineEdit_1 = QtWidgets.QLineEdit(self)
		self.lineEdit_1.setFont(font)
		self.lineEdit_1.setObjectName("lineEdit_1")
		self.lineEdit_1.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
		self.horizontalLayout.addWidget(self.lineEdit_1)
		self.lineEdit_2 = QtWidgets.QLineEdit(self)
		self.lineEdit_2.setFont(font)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
		self.horizontalLayout.addWidget(self.lineEdit_2)
		self.lineEdit_3 = QtWidgets.QLineEdit(self)
		self.lineEdit_3.setFont(font)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
		self.horizontalLayout.addWidget(self.lineEdit_3)
		self.lineEdit_4 = QtWidgets.QLineEdit(self)
		self.lineEdit_4.setMinimumSize(QtCore.QSize(250, 0))
		self.lineEdit_4.setFont(font)
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"    border-radius: 5px;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"}")
		self.horizontalLayout.addWidget(self.lineEdit_4)
		self.verticalLayout.addLayout(self.horizontalLayout)

class TablePrint(QtWidgets.QWidget):
	def __init__(self, strlb_1, strlb_2, strlb_3, strlb_4):
		super().__init__()
		self.setStyleSheet("QWidget{\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    border-color: none rgb(122, 122, 122) rgb(122, 122, 122) rgb(122, 122, 122);\n"
"}")
		self.setObjectName("widget")
		self.horizontalLayout = QtWidgets.QHBoxLayout(self)
		self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout.setSpacing(0)
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.label_2 = QtWidgets.QLabel(self)
		self.label_2.setMinimumSize(QtCore.QSize(20, 0))
		self.label_2.setMaximumSize(QtCore.QSize(20, 16777215))
		self.label_2.setText(strlb_1)
		font = QtGui.QFont()
		font.setFamily("Montserrat")
		self.label_2.setFont(font)
		self.label_2.setStyleSheet("border-color: none rgb(122, 122, 122) none none;")
		self.label_2.setObjectName("label_2")
		self.horizontalLayout.addWidget(self.label_2)
		self.label_3 = QtWidgets.QLabel(self)
		self.label_3.setMinimumSize(QtCore.QSize(150, 0))
		self.label_3.setMaximumSize(QtCore.QSize(150, 16777215))
		self.label_3.setText(strlb_2)
		font = QtGui.QFont()
		font.setFamily("Montserrat")
		self.label_3.setFont(font)
		self.label_3.setStyleSheet("border-color: none rgb(122, 122, 122) none none;")
		self.label_3.setObjectName("label_3")
		self.horizontalLayout.addWidget(self.label_3)
		self.label_4 = QtWidgets.QLabel(self)
		self.label_4.setMinimumSize(QtCore.QSize(200, 0))
		self.label_4.setMaximumSize(QtCore.QSize(200, 16777215))
		self.label_4.setText(strlb_3)
		font = QtGui.QFont()
		font.setFamily("Montserrat")
		self.label_4.setFont(font)
		self.label_4.setStyleSheet("border-color: none rgb(122, 122, 122) none none;")
		self.label_4.setObjectName("label_4")
		self.horizontalLayout.addWidget(self.label_4)
		self.label_7 = QtWidgets.QLabel(self)
		self.label_7.setMinimumSize(QtCore.QSize(130, 0))
		self.label_7.setMaximumSize(QtCore.QSize(130, 16777215))
		self.label_7.setText(strlb_4)
		font = QtGui.QFont()
		font.setFamily("Montserrat")
		self.label_7.setFont(font)
		self.label_7.setStyleSheet("border-color: none rgb(122, 122, 122) none none;")
		self.label_7.setObjectName("label_7")
		self.horizontalLayout.addWidget(self.label_7)
		self.label_9 = QtWidgets.QLabel(self)
		self.label_9.setMinimumSize(QtCore.QSize(0, 21))
		self.label_9.setMaximumSize(QtCore.QSize(16777215, 18))
		self.label_9.setStyleSheet("border-color: none;")
		self.label_9.setText("")
		self.label_9.setObjectName("label_9")
		self.horizontalLayout.addWidget(self.label_9)
		self.pushButton_9 = QtWidgets.QPushButton(self)
		self.pushButton_9.setMinimumSize(QtCore.QSize(55, 18))
		self.pushButton_9.setMaximumSize(QtCore.QSize(16777215, 18))
		font = QtGui.QFont()
		font.setFamily("Montserrat")
		font.setPointSize(7)
		self.pushButton_9.setFont(font)
		self.pushButton_9.setStyleSheet("QPushButton {\n"
"    background: rgb(0, 255, 127);\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    border-radius: 5px;  /* Установите радиус закругления, например, 10px */\n"
"}")
		self.pushButton_9.setObjectName("pushButton_9")
		self.pushButton_9.setText('Выбрать')
		self.horizontalLayout.addWidget(self.pushButton_9)
		self.label_18 = QtWidgets.QLabel(self)
		self.label_18.setMinimumSize(QtCore.QSize(0, 0))
		self.label_18.setMaximumSize(QtCore.QSize(16777215, 16777215))
		self.label_18.setStyleSheet("border-color: none;")
		self.label_18.setText("")
		self.label_18.setObjectName("label_18")
		self.horizontalLayout.addWidget(self.label_18)
		self.pushButton_5 = QtWidgets.QPushButton(self)
		self.pushButton_5.setMinimumSize(QtCore.QSize(55, 18))
		self.pushButton_5.setMaximumSize(QtCore.QSize(16777215, 18))
		font = QtGui.QFont()
		font.setFamily("Montserrat")
		font.setPointSize(7)
		self.pushButton_5.setFont(font)
		self.pushButton_5.setStyleSheet("QPushButton {\n"
"    background: #FFB200;\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    border-radius: 5px;  /* Установите радиус закругления, например, 10px */\n"
"}")
		self.pushButton_5.setObjectName("pushButton_5")
		self.pushButton_5.setText('Изменить')
		self.horizontalLayout.addWidget(self.pushButton_5)
		self.label_5 = QtWidgets.QLabel(self)
		self.label_5.setMinimumSize(QtCore.QSize(0, 20))
		self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
		self.label_5.setStyleSheet("border-color: none;")
		self.label_5.setText("")
		self.label_5.setObjectName("label_5")
		self.horizontalLayout.addWidget(self.label_5)
		self.pushButton_6 = QtWidgets.QPushButton(self)
		self.pushButton_6.setMinimumSize(QtCore.QSize(18, 18))
		self.pushButton_6.setMaximumSize(QtCore.QSize(18, 18))
		font = QtGui.QFont()
		font.setFamily("Montserrat")
		self.pushButton_6.setFont(font)
		self.pushButton_6.setStyleSheet("QPushButton {\n"
"    background: rgb(255, 119, 121);\n"
"    border: 1px solid rgb(122, 122, 122);\n"
"    border-radius: 5px;  /* Установите радиус закругления, например, 10px */\n"
"}")
		self.pushButton_6.setObjectName("pushButton_6")
		self.pushButton_6.setText('-')
		self.horizontalLayout.addWidget(self.pushButton_6)
		self.label_10 = QtWidgets.QLabel(self)
		self.label_10.setStyleSheet("border-color: none;")
		self.label_10.setText("")
		self.label_10.setObjectName("label_10")
		self.horizontalLayout.addWidget(self.label_10)

class CustomPushBtn(QtWidgets.QPushButton):
	def __init__(self, func, id_i):
		super().__init__()
		self.setObjectName(u"Выбрать")
		self.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(122, 122, 122);\n"
"	background: #26DE81;\n"
"}")
		self.setText("Выбрать")
		self.id = id_i
		font = QtGui.QFont()
		font.setFamily("Montserrat")
		self.setFont(font)
		self.clicked.connect(lambda: func(self.id))