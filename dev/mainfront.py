import sys, mainback
from ui import customers # таблица с заказчиками
from ui import executor_add # маленькие окна Исполнитель
from ui import customers_add # маленькие окна Зазазчик
from ui import executor # таблица с исполнителями
from ui import engine # основное окно
from ui.elements import GenAuto, TablePrint, CustomPushBtn

from docxtpl import DocxTemplate
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from datetime import date



class App(QMainWindow, engine.Ui_widget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setting_init()
		self.order_tab_sector()
		self.generate_constraction()

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
		self.lineEdit_6.setReadOnly(True)
		self.lineEdit_7.setReadOnly(True)
		self.font = QtGui.QFont()
		self.font.setFamily("Arial")
		self.executor_now = None
		self.customer_now = None
		self.db = mainback.DB()

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

	def take_executor(self, id):
		executor_temp = self.db.search_executor_id(id)
		self.executor_now = executor_temp[0]
		self.lineEdit_6.setText(f"{executor_temp[0][1]} | ИНН:{executor_temp[0][4]}")
		self.executor.close()
		print(self.executor_now)

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
																self.update_table_executor(),self.executor_add.close())
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
			self.executorui.tableWidget.setItem(a, 3, QtWidgets.QTableWidgetItem(str(i[4])))
			self.executorui.tableWidget.setCellWidget(a, 4, CustomPushBtn(self.take_executor, i[0]))

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
		for i in self.list_auto:
			print(i.lineEdit_1.text())

	def del_auto(self):
		if len(self.list_auto) > 1:
			self.verticalLayout_3.removeWidget(self.list_auto[-1])
			self.list_auto.pop(-1)



		

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


