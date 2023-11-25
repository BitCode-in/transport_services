#Новый комент
import sys, engine
from docxtpl import DocxTemplate
from PyQt5 import QtCore, QtGui, QtWidgets, uic
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
		self.horizontalLayout.addWidget(self.lineEdit_1)
		self.lineEdit_2 = QtWidgets.QLineEdit(self)
		self.lineEdit_2.setFont(font)
		self.lineEdit_2.setObjectName("lineEdit_2")
		self.horizontalLayout.addWidget(self.lineEdit_2)
		self.lineEdit_3 = QtWidgets.QLineEdit(self)
		self.lineEdit_3.setFont(font)
		self.lineEdit_3.setObjectName("lineEdit_3")
		self.horizontalLayout.addWidget(self.lineEdit_3)
		self.lineEdit_4 = QtWidgets.QLineEdit(self)
		self.lineEdit_4.setMinimumSize(QtCore.QSize(250, 0))
		self.lineEdit_4.setFont(font)
		self.lineEdit_4.setObjectName("lineEdit_4")
		self.horizontalLayout.addWidget(self.lineEdit_4)
		self.verticalLayout.addLayout(self.horizontalLayout)

class App(QMainWindow, engine.Ui_widget):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.setting_init()
		self.order_tab_sector()
		self.generate_constraction()

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
		self.font = QtGui.QFont()
		self.font.setFamily("Arial")

		

	def order_tab_sector(self):
		self.tempwidget.setTabOrder(self.lineEdit, self.lineEdit_2)
		self.tempwidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
		self.tempwidget.setTabOrder(self.lineEdit_3, self.lineEdit_4)
		self.tempwidget.setTabOrder(self.lineEdit_4, self.lineEdit_5)
		self.tempwidget.setTabOrder(self.lineEdit_5, self.lineEdit_18)
		self.tempwidget.setTabOrder(self.lineEdit_18, self.lineEdit_19)
		self.tempwidget.setTabOrder(self.lineEdit_19, self.lineEdit_20)
		self.tempwidget.setTabOrder(self.lineEdit_20, self.lineEdit_21)
		self.tempwidget.setTabOrder(self.lineEdit_21, self.lineEdit_22)
		self.tempwidget.setTabOrder(self.lineEdit_22, self.pushButton)

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


