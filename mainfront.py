#Новое
import sys, engine
from docxtpl import DocxTemplate
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from datetime import date


class App(QMainWindow, engine.Ui_widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('res/icon.png'))
        self.pushButton.clicked.connect(self.word_create)
        self.order_tab_sector()

    def order_tab_sector(self):
        self.tempwidget.setTabOrder(self.lineEdit, self.lineEdit_2)
        self.tempwidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        self.tempwidget.setTabOrder(self.lineEdit_3, self.lineEdit_4)
        self.tempwidget.setTabOrder(self.lineEdit_4, self.lineEdit_5)
        self.tempwidget.setTabOrder(self.lineEdit_5, self.lineEdit_6)
        self.tempwidget.setTabOrder(self.lineEdit_6, self.lineEdit_7)
        self.tempwidget.setTabOrder(self.lineEdit_7, self.lineEdit_8)
        self.tempwidget.setTabOrder(self.lineEdit_8, self.lineEdit_9)
        self.tempwidget.setTabOrder(self.lineEdit_9, self.lineEdit_10)
        self.tempwidget.setTabOrder(self.lineEdit_10, self.lineEdit_11)
        self.tempwidget.setTabOrder(self.lineEdit_11, self.lineEdit_12)
        self.tempwidget.setTabOrder(self.lineEdit_12, self.lineEdit_13)
        self.tempwidget.setTabOrder(self.lineEdit_13, self.lineEdit_18)
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
        context = {'number': self.lineEdit.text(),
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


