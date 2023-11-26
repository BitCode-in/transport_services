import sys
import customers # таблица с заказчиками
import executor_add # маленькие окна Исполнитель
import customers_add # маленькие окна Зазазчик
import executor # таблица с исполнителями
import engine # основное окно
import mainback

from docxtpl import DocxTemplate
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from datetime import date

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

class App(QMainWindow, engine.Ui_widget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setting_init()
		self.order_tab_sector()
		self.generate_constraction()
		self.db = mainback.DB()

	def open_executor(self):
		self.list_executor = {}
		self.list_executor_widget = {}
		self.executor = QMainWindow()
		self.executorui = executor.Ui_Form()
		self.executorui.setupUi(self.executor)
		self.executor.setWindowIcon(QtGui.QIcon('res/icon.png'))
		self.executor.setWindowTitle('Исполнители')
		self.executor.show()
		self.executorui.pushButton_2.clicked.connect(self.open_executor_add)
		for i in self.db.view_executor():
			self.list_executor[i[0]] = i
			self.list_executor_widget[i[0]] = TablePrint(str(i[0]), str(i[1]), str(i[2]), str(i[3]))
			self.executorui.verticalLayout_3.addWidget(self.list_executor_widget[i[0]])

#Обновление
	def open_customers(self):
		self.list_customers = {}
		self.list_customers_widget = {}
		self.customers = QMainWindow()
		self.customersui = customers.Ui_Form()
		self.customersui.setupUi(self.customers)
		self.customers.setWindowIcon(QtGui.QIcon('res/icon.png'))
		self.customers.setWindowTitle('Заказчики')
		self.customers.show()
		self.customersui.pushButton_2.clicked.connect(self.open_customers_add)

	def open_executor_add(self):
		self.executor_add = QMainWindow()
		self.executor_addui = executor_add.Ui_Form()
		self.executor_addui.setupUi(self.executor_add)
		self.executor_add.setWindowIcon(QtGui.QIcon('res/icon.png'))
		self.executor_add.setWindowTitle('Добавить исполнителя')
		self.executor_add.show()

	def open_customers_add(self):
		self.customers_add = QMainWindow()
		self.customers_addui = customers_add.Ui_Form()
		self.customers_addui.setupUi(self.customers_add)
		self.customers_add.setWindowIcon(QtGui.QIcon('res/icon.png'))
		self.customers_add.setWindowTitle('Добавить заказчика')
		self.customers_add.show()

	def add_auto(self):
		temp_genauto = GenAuto(settext=str(len(self.list_auto)+1))
		self.list_auto.append(temp_genauto)
		self.verticalLayout_3.addWidget(temp_genauto)

	def del_auto(self):
		if len(self.list_auto) > 1:
			self.verticalLayout_3.removeWidget(self.list_auto[-1])
			self.list_auto.pop(-1)

	def generate_constraction(self):
		self.list_auto = []
		temp_genauto = GenAuto(settext='1')
		self.list_auto.append(temp_genauto)
		self.verticalLayout_3.addWidget(temp_genauto)

	def setting_init(self):
		self.setWindowIcon(QtGui.QIcon('res/icon.png'))
		self.pushButton.clicked.connect(self.word_create)
		self.pushButton_2.clicked.connect(self.add_auto)
		self.pushButton_3.clicked.connect(self.del_auto)
		self.pushButton_4.clicked.connect(self.open_executor)
		self.pushButton_5.clicked.connect(self.open_customers)
		self.font = QtGui.QFont()
		self.font.setFamily("Arial")

		

	def order_tab_sector(self):
		pass
		# self.tempwidget.setTabOrder(self.lineEdit, self.lineEdit_2)
		# self.tempwidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
		# self.tempwidget.setTabOrder(self.lineEdit_3, self.lineEdit_4)
		# self.tempwidget.setTabOrder(self.lineEdit_4, self.lineEdit_5)
		# self.tempwidget.setTabOrder(self.lineEdit_5, self.lineEdit_18)
		# self.tempwidget.setTabOrder(self.lineEdit_18, self.lineEdit_19)
		# self.tempwidget.setTabOrder(self.lineEdit_19, self.lineEdit_20)
		# self.tempwidget.setTabOrder(self.lineEdit_20, self.lineEdit_21)
		# self.tempwidget.setTabOrder(self.lineEdit_21, self.lineEdit_22)
		# self.tempwidget.setTabOrder(self.lineEdit_22, self.pushButton)

# вставка в ворд
	def word_create(self):

		dict_month = {'01': 'января',
					  '02': 'февраля',
					  '03': 'марта',
					  '04': 'апреля',
					  '05': 'мая',
					  '06': 'июня',
					  '07': 'июля',
					  '08': 'августа',
					  '09': 'сентября',
					  '10': 'октября',
					  '11': 'ноября',
					  '12': 'декабря'
					  }

		year = date.today().year
		month = date.today().month
		day = date.today().day

		full_year = str(day) + ' ' + dict_month[f'{month}'] + ' ' + str(year) + ' г.'

		name_save = QFileDialog.getExistingDirectory()


		if self.lineEdit_10.text() == "":
			a = " "
			b = " "
			c = " "
			d = " "

		else:
			a = self.lineEdit_10.text()
			b = self.lineEdit_11.text()
			c = self.lineEdit_12.text()
			d = self.lineEdit_13.text()

		year = date.today()
		doc = DocxTemplate("agreement.docx")
		context = {'number': '№' + ' ' + self.lineEdit.text(),
				   'city': self.lineEdit_2.text(),
				   'year': full_year,
				   'organization': self.lineEdit_3.text(),
				   'price': self.lineEdit_4.text(),
				   'route': self.lineEdit_5.text(),

				   'mark1':self.lineEdit_6.text(),
				   'num_t1': self.lineEdit_7.text(),
				   'num_p1': self.lineEdit_8.text(),
				   'fio_v1': self.lineEdit_9.text(),

				   'mark2': a,
				   'num_t2': b,
				   'num_p2': c,
				   'fio_v2': d,

				   'inn': self.lineEdit_18.text(),
				   'address': self.lineEdit_19.text(),
				   'pc': self.lineEdit_20.text(),
				   'bik': self.lineEdit_21.text(),
				   'fio': self.lineEdit_22.text()}

		doc.render(context)
		doc.save(f'{name_save}/Договор № {self.lineEdit.text()}.docx')

		msBox= QMessageBox()
		msBox.setText('Договор сформирован.')
		msBox.exec()

		self.clear_text()

	def clear_text(self):

		self.lineEdit.clear()
		self.lineEdit_2.clear()
		self.lineEdit_3.clear()
		self.lineEdit_4.clear()
		self.lineEdit_5.clear()
		self.lineEdit_6.clear()
		self.lineEdit_7.clear()
		self.lineEdit_8.clear()
		self.lineEdit_9.clear()
		self.lineEdit_10.clear()
		self.lineEdit_11.clear()
		self.lineEdit_12.clear()
		self.lineEdit_13.clear()
		self.lineEdit_18.clear()
		self.lineEdit_19.clear()
		self.lineEdit_20.clear()
		self.lineEdit_21.clear()
		self.lineEdit_22.clear()



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	ex.show()
	sys.exit(app.exec())


