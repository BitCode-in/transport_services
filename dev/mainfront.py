import sys, mainback, os, pyperclip
from ui import customers # таблица с заказчиками
from ui import executor_add # маленькие окна Исполнитель
from ui import customers_add # маленькие окна Зазазчик
from ui import executor # таблица с исполнителями
from ui import engine # основное окно
from ui import setting
from ui.elements import GenAuto, TablePrint, CustomPushBtn

from docxtpl import DocxTemplate
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from datetime import date


class App(QMainWindow, engine.Ui_widget):

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setting_init()
		self.order_tab_sector()
		self.generate_constraction()
		self.data_customer = []
		self.data_executor = []

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
		self.pushButton_6.clicked.connect(self.open_settings)
		self.pushButton_7.clicked.connect(self.import_excel_to_auto)
		self.pushButton_8.clicked.connect(self.clear_text)
		self.lineEdit_6.setReadOnly(True)
		self.lineEdit_7.setReadOnly(True)
		self.font = QtGui.QFont()
		self.font.setFamily("Arial")
		self.executor_now = None
		self.customer_now = None
		self.db = mainback.DB()
		self.set_auto = None
		self.name_address = None
		self.check_correct_address(os.getcwd().replace('\\', "/"))

	def open_executor(self):
		self.list_executor = {}
		self.executor = QMainWindow()
		self.executorui = executor.Ui_Form()
		self.executorui.setupUi(self.executor)
		self.executor.setWindowIcon(QtGui.QIcon('res/icon.png'))
		self.executor.setWindowTitle('Исполнители')
		self.executor.show()
		self.executorui.pushButton.clicked.connect(self.open_executor_add)
		self.executorui.tableWidget.verticalHeader().setVisible(False)
		self.executorui.tableWidget.setColumnWidth(0, 41)
		self.executorui.tableWidget.setColumnWidth(1, 210)
		self.executorui.tableWidget.setColumnWidth(2, 210)
		self.executorui.tableWidget.setColumnWidth(3, 110)
		self.executorui.tableWidget.setColumnWidth(4, 98)
		self.executorui.tableWidget.horizontalScrollBar().setDisabled(True)
		self.update_table_executor()
		self.executorui.pushButton_3.clicked.connect(self.del_executor)
		self.executorui.pushButton_2.clicked.connect(self.open_executor_update)
		self.executorui.pushButton_4.clicked.connect(self.search_executor)

	def del_executor(self):
		num = self.executorui.tableWidget.currentRow()
		id = self.list_executor[num][0]
		self.db.delete_executor(int(id))
		self.update_table_executor()

	def del_customer(self):
		num = self.customersui.tableWidget.currentRow()
		id = self.list_customers[num][0]
		self.db.delete_customer(int(id))
		self.update_table_customers()

	def take_executor(self, id):
		executor_temp = self.db.search_executor_id(id)
		self.executor_now = executor_temp[0]
		self.lineEdit_6.setText(f"{executor_temp[0][1]} | ИНН:{executor_temp[0][4]}")
		self.executor.close()
		print(self.executor_now)
		self.data_executor = self.executor_now

	def take_customers(self, id):
		customer_temp = self.db.search_customer_id(id)
		self.customer_now = customer_temp[0]
		self.lineEdit_7.setText(f"{customer_temp[0][1]} | ИНН:{customer_temp[0][4]}")
		self.customers.close()
		print(self.customer_now)
		self.data_customer = self.customer_now

	def open_executor_add(self):
		self.executor_add = QMainWindow()
		self.executor_addui = executor_add.Ui_Form()
		self.executor_addui.setupUi(self.executor_add)
		self.executor_add.setWindowIcon(QtGui.QIcon('res/icon.png'))
		self.executor_add.setWindowTitle('Добавить исполнителя')
		self.executor_add.show()
		self.executor_addui.pushButton.clicked.connect(lambda: (self.db.insert_executor(self.executor_addui.lineEdit.text(),
																			   self.executor_addui.lineEdit_2.text(),
																			   self.executor_addui.lineEdit_3.text(),
																			   self.executor_addui.lineEdit_4.text(),
																			   self.executor_addui.lineEdit_5.text(),
																			   self.executor_addui.lineEdit_6.text()),
																self.update_table_executor(), self.executor_add.close())
													   )

	def open_executor_update(self):
		self.executor_add = QMainWindow()
		self.executor_addui = executor_add.Ui_Form()
		self.executor_addui.setupUi(self.executor_add)
		self.executor_add.setWindowIcon(QtGui.QIcon('res/icon.png'))
		self.executor_add.setWindowTitle('Изменить исполнителя')
		num = self.executorui.tableWidget.currentRow()
		id = self.list_executor[num][0]
		executor_temp = self.db.search_executor_id(id)
		self.executor_addui.lineEdit.setText(str(executor_temp[0][1]))
		self.executor_addui.lineEdit_2.setText(str(executor_temp[0][2]))
		self.executor_addui.lineEdit_3.setText(str(executor_temp[0][3]))
		self.executor_addui.lineEdit_4.setText(str(executor_temp[0][4]))
		self.executor_addui.lineEdit_5.setText(str(executor_temp[0][5]))
		self.executor_addui.lineEdit_6.setText(str(executor_temp[0][6]))

		self.executor_add.show()
		self.executor_addui.pushButton.clicked.connect(lambda: (self.db.update_executor(id,
																			   self.executor_addui.lineEdit.text(),
																			   self.executor_addui.lineEdit_2.text(),
																			   self.executor_addui.lineEdit_3.text(),
																			   self.executor_addui.lineEdit_4.text(),
																			   self.executor_addui.lineEdit_5.text(),
																			   self.executor_addui.lineEdit_6.text()),
																self.update_table_executor(),
																self.executor_add.close()))


	def update_table_executor(self):
		self.list_executor = []
		self.executorui.tableWidget.clearContents()
		self.executorui.tableWidget.setRowCount(0)
		for a, i in enumerate(self.db.view_executor()):
			self.executorui.tableWidget.insertRow(a)
			self.list_executor.append(i)
			self.executorui.tableWidget.setItem(a, 0, QtWidgets.QTableWidgetItem(str(a+1)))
			self.executorui.tableWidget.setItem(a, 1, QtWidgets.QTableWidgetItem(str(i[1])))
			self.executorui.tableWidget.setItem(a, 2, QtWidgets.QTableWidgetItem(str(i[2])))
			self.executorui.tableWidget.setItem(a, 3, QtWidgets.QTableWidgetItem(str(i[3])))
			self.executorui.tableWidget.setCellWidget(a, 4, CustomPushBtn(self.take_executor, i[0]))

	def search_executor(self):
		self.list_executor = []
		self.executorui.tableWidget.clearContents()
		self.executorui.tableWidget.setRowCount(0)
		for a, i in enumerate(self.db.search_executor(self.executorui.lineEdit.text())):
			self.executorui.tableWidget.insertRow(a)
			self.list_executor.append(i)
			self.executorui.tableWidget.setItem(a, 0, QtWidgets.QTableWidgetItem(str(a+1)))
			self.executorui.tableWidget.setItem(a, 1, QtWidgets.QTableWidgetItem(str(i[1])))
			self.executorui.tableWidget.setItem(a, 2, QtWidgets.QTableWidgetItem(str(i[2])))
			self.executorui.tableWidget.setItem(a, 3, QtWidgets.QTableWidgetItem(str(i[3])))
			self.executorui.tableWidget.setCellWidget(a, 4, CustomPushBtn(self.take_executor, i[0]))

	def search_customers(self):
		self.list_customers = []
		self.customersui.tableWidget.clearContents()
		self.customersui.tableWidget.setRowCount(0)
		for a, i in enumerate(self.db.search_customer(self.customersui.lineEdit.text())):
			self.customersui.tableWidget.insertRow(a)
			self.list_customers.append(i)
			self.customersui.tableWidget.setItem(a, 0, QtWidgets.QTableWidgetItem(str(a+1)))
			self.customersui.tableWidget.setItem(a, 1, QtWidgets.QTableWidgetItem(str(i[1])))
			self.customersui.tableWidget.setItem(a, 2, QtWidgets.QTableWidgetItem(str(i[2])))
			self.customersui.tableWidget.setItem(a, 3, QtWidgets.QTableWidgetItem(str(i[3])))
			self.customersui.tableWidget.setCellWidget(a, 4, CustomPushBtn(self.take_customers, i[0]))

	def open_customers(self):
		self.list_customers = {}
		self.list_customers_widget = {}
		self.customers = QMainWindow()
		self.customersui = customers.Ui_Form()
		self.customersui.setupUi(self.customers)
		self.customers.setWindowIcon(QtGui.QIcon('res/icon.png'))
		self.customers.setWindowTitle('Заказчики')
		self.customers.show()
		self.customersui.pushButton.clicked.connect(self.open_customers_add)
		self.customersui.tableWidget.verticalHeader().setVisible(False)
		self.customersui.tableWidget.setColumnWidth(0, 41)
		self.customersui.tableWidget.setColumnWidth(1, 210)
		self.customersui.tableWidget.setColumnWidth(2, 210)
		self.customersui.tableWidget.setColumnWidth(3, 110)
		self.customersui.tableWidget.setColumnWidth(4, 98)
		self.customersui.tableWidget.horizontalScrollBar().setDisabled(True)
		self.update_table_customers()
		self.customersui.pushButton_4.clicked.connect(self.search_customers)
		self.customersui.pushButton_3.clicked.connect(self.del_customer)
		self.customersui.pushButton_2.clicked.connect(self.open_customers_update)


	def open_customers_add(self):
		self.customers_add = QMainWindow()
		self.customers_addui = customers_add.Ui_Form()
		self.customers_addui.setupUi(self.customers_add)
		self.customers_add.setWindowIcon(QtGui.QIcon('res/icon.png'))
		self.customers_add.setWindowTitle('Добавить заказчика')
		self.customers_add.show()
		self.customers_addui.pushButton.clicked.connect(
			lambda: (self.db.insert_customer(self.customers_addui.lineEdit.text(),
											 self.customers_addui.lineEdit_8.text(),
											 self.customers_addui.lineEdit_2.text(),
											 self.customers_addui.lineEdit_3.text(),
											 self.customers_addui.lineEdit_4.text(),
											 self.customers_addui.lineEdit_5.text(),
											 self.customers_addui.lineEdit_7.text(),
											 self.customers_addui.lineEdit_6.text()),
					 self.update_table_customers(),
					 self.customers_add.close()))

	def open_customers_update(self):
		self.customers_add = QMainWindow()
		self.customers_addui = customers_add.Ui_Form()
		self.customers_addui.setupUi(self.customers_add)
		self.customers_add.setWindowIcon(QtGui.QIcon('res/icon.png'))
		self.customers_add.setWindowTitle('Изменить заказчика')
		num = self.customersui.tableWidget.currentRow()
		id = self.list_customers[num][0]
		customers_temp = self.db.search_customer_id(id)
		self.customers_addui.lineEdit.setText(str(customers_temp[0][1]))
		self.customers_addui.lineEdit_8.setText(str(customers_temp[0][2]))
		self.customers_addui.lineEdit_2.setText(str(customers_temp[0][3]))
		self.customers_addui.lineEdit_3.setText(str(customers_temp[0][4]))
		self.customers_addui.lineEdit_4.setText(str(customers_temp[0][5]))
		self.customers_addui.lineEdit_5.setText(str(customers_temp[0][6]))
		self.customers_addui.lineEdit_7.setText(str(customers_temp[0][7]))
		self.customers_addui.lineEdit_6.setText(str(customers_temp[0][8]))
		self.customers_add.show()
		self.customers_addui.pushButton.clicked.connect(
			lambda: (self.db.update_customer(id,
																						self.customers_addui.lineEdit.text(),
											 											self.customers_addui.lineEdit_8.text(),
																						self.customers_addui.lineEdit_2.text(),
																						self.customers_addui.lineEdit_3.text(),
																						self.customers_addui.lineEdit_4.text(),
																						self.customers_addui.lineEdit_5.text(),
																						self.customers_addui.lineEdit_7.text(),
																						self.customers_addui.lineEdit_6.text()),
																self.update_table_customers(),
																self.customers_add.close()))

	def update_table_customers(self):
		self.list_customers = []
		self.customersui.tableWidget.clearContents()
		self.customersui.tableWidget.setRowCount(0)
		for a, i in enumerate(self.db.view_customer()):
			self.customersui.tableWidget.insertRow(a)
			self.list_customers.append(i)
			self.customersui.tableWidget.setItem(a, 0, QtWidgets.QTableWidgetItem(str(a + 1)))
			self.customersui.tableWidget.setItem(a, 1, QtWidgets.QTableWidgetItem(str(i[1])))
			self.customersui.tableWidget.setItem(a, 2, QtWidgets.QTableWidgetItem(str(i[2])))
			self.customersui.tableWidget.setItem(a, 3, QtWidgets.QTableWidgetItem(str(i[3])))
			self.customersui.tableWidget.setCellWidget(a, 4, CustomPushBtn(self.take_customers, i[0]))

	def add_auto(self):
		temp_genauto = GenAuto(settext=str(len(self.list_auto)+1))
		self.list_auto.append(temp_genauto)
		self.verticalLayout_3.addWidget(temp_genauto)

	def data_auto(self):
		str_auto = ""
		for a, i in enumerate(self.list_auto):
			if i.lineEdit_5.text() == "":
				str_auto += "\t" + str(a+1) + ". " + i.lineEdit_1.text() + " | " + i.lineEdit_2.text() + " | " + i.lineEdit_3.text() + " | " + i.lineEdit_4.text() + " |\n"
			else:
				str_auto += "\t" + str(a+1) + ". " + i.lineEdit_1.text() + " | " + i.lineEdit_2.text() + " | " + i.lineEdit_3.text() + " | " + i.lineEdit_4.text() + " | " + i.lineEdit_5.text() + " |\n"

		self.set_auto = str_auto

	def del_auto(self):
		if len(self.list_auto) > 1:
			self.verticalLayout_3.removeWidget(self.list_auto[-1])
			self.list_auto.pop(-1)
		

	def order_tab_sector(self):
		self.tempwidget.setTabOrder(self.lineEdit, self.lineEdit_2)
		self.tempwidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
		self.tempwidget.setTabOrder(self.lineEdit_3, self.lineEdit_4)
		self.tempwidget.setTabOrder(self.lineEdit_4, self.lineEdit_5)
		self.tempwidget.setTabOrder(self.lineEdit_5, self.pushButton)

	def open_settings(self):
		self.setting = QMainWindow()
		self.settingui = setting.Ui_Form()
		self.settingui.setupUi(self.setting)
		self.setting.setWindowIcon(QtGui.QIcon('res/icon.png'))
		self.setting.setWindowTitle('Настройки')
		self.setting.show()
		self.settingui.lineEdit.setReadOnly(True)
		address = self.db.view_save_address()
		self.settingui.lineEdit.setText(str(address[0][1]))
		self.settingui.pushButton_2.clicked.connect(self.change_name_save)
		self.settingui.pushButton.clicked.connect(lambda: self.name_save())

	def change_name_save(self):
		self.settingui.lineEdit.setText(str(QFileDialog.getExistingDirectory()))

	def name_save(self):
		self.name_address = self.settingui.lineEdit.text()
		self.db.update_save_address(self.name_address)
		self.setting.close()

	def check_correct_address(self, str_path):
		address = self.db.view_save_address()
		try:
			self.name_address = address[0][1]
		except:
			self.db.insert_save_address(str_path)
			self.name_address = str_path
			


	def view_address(self):
		self.db.view_save_address()

		# print(self.db.view_save_address())
		# address_save = self.db.view_save_address()
		# print(address_save[0][0])
		# if self.db.view_save_address() != "":
		# 	self.settingui.lineEdit.setText(address_save[0])
		# else:
		# 	self.settingui.lineEdit.setText("Здесь будет путь для сохранения.")

	def import_excel_to_auto(self):
		try:
			clipboard_data = pyperclip.paste()
			df = []
			clipboard_data = clipboard_data.replace("\r", "").split('\n')[:-1]
			for i in clipboard_data:
				df.append(i.split('\t'))
			for i in df:
				print(i)
				temp_genauto = GenAuto(settext=str(len(self.list_auto) + 1))
				temp_genauto.lineEdit_1.setText(i[0])
				temp_genauto.lineEdit_2.setText(i[1])
				temp_genauto.lineEdit_3.setText(i[2])
				temp_genauto.lineEdit_4.setText(i[3])
				if self.list_auto[0].lineEdit_1.text() == "" and self.list_auto[0].lineEdit_2.text() == "" and self.list_auto[0].lineEdit_3.text() == "" and self.list_auto[0].lineEdit_4.text() == "":
					self.verticalLayout_3.removeWidget(self.list_auto[-1])
					self.list_auto.pop(-1)
				self.list_auto.append(temp_genauto)
				self.verticalLayout_3.addWidget(temp_genauto)
		except:
			msBox = QMessageBox()
			msBox.setText('Вам нужно выбрать 4 столбца!')
			msBox.setWindowTitle('Ошибка!')  # Замените 'Название окна' на ваше желаемое название
			msBox.setWindowIcon(QIcon('res/icon.png'))
			msBox.exec()

	def word_create(self):
		try:
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

			year = date.today()
			doc = DocxTemplate("./docx/agreement.docx")
			self.data_auto()
			context = {'number': '№' + ' ' + self.lineEdit.text(), # № договора
					   'city': self.lineEdit_2.text(), # город
					   'year': full_year, # дата
					   'price': self.lineEdit_4.text(), # цена
					   'culture' :self.lineEdit_3.text(),# культура
					   'route': self.lineEdit_5.text(), # маршрут

					   'auto':self.set_auto, # авто

					   'organization': self.data_executor[1], # исполнитель
					   'inn': self.data_executor[4], # инн исполнителя
					   'address': self.data_executor[3], # адрес исполнителя
					   'pc': self.data_executor[5], # рс исполнителя
					   'bik': self.data_executor[6],# бик исполнителя
					   'fio': self.data_executor[2],  # фио исполнителя

					   'customer': self.data_customer[1],  # заказчик
					   'job_title_customer': self.data_customer[2],
					   'inn_customer': self.data_customer[5],  # инн заказчика
					   'address_customer': self.data_customer[4],  # адрес заказчика
					   'pc_customer': self.data_customer[6],  # рс заказчика
					   'name_bank_customer': self.data_customer[7],# название банка заказчика
					   'bik_customer': self.data_customer[8],  # бик заказчика
					   'fio_customer': self.data_customer[3],  # фио заказчика
					   }

			doc.render(context)
			doc.save(f'{self.name_address}/Договор № {self.lineEdit.text()}.docx')

			msBox = QMessageBox()
			msBox.setText('Договор сформирован.')
			msBox.setWindowTitle('Уведомление!')  # Замените 'Название окна' на ваше желаемое название
			msBox.setWindowIcon(QIcon('res/icon.png'))
			msBox.exec()

		except:
			msBox = QMessageBox()
			msBox.setText('Заполните все поля!')
			msBox.setWindowTitle('Ошибка!')  # Замените 'Название окна' на ваше желаемое название
			msBox.setWindowIcon(QIcon('res/icon.png'))
			msBox.exec()

	def clear_text(self):

		self.lineEdit.clear()
		self.lineEdit_2.clear()
		self.lineEdit_3.clear()
		self.lineEdit_4.clear()
		self.lineEdit_5.clear()
		self.lineEdit_6.clear()
		self.lineEdit_7.clear()
		for i in self.list_auto.copy():
			self.verticalLayout_3.removeWidget(self.list_auto[-1])
			self.list_auto.pop(-1)
		self.generate_constraction()



if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = App()
	ex.show()
	sys.exit(app.exec())


