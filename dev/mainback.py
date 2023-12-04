import sqlite3

class DB:
	def __init__(self):
		self.conn = sqlite3.connect('data.db')
		self.c = self.conn.cursor()

		# Таблица заказчики (Строки по порядку: айдишник,
		# название организации,
		# фио заказчика,
		# адрес,
		# ИНН,
		# Р/С,
		# название банка заказчика,
		# БИК заказчика)
		self.c.execute(
			""" CREATE TABLE IF NOT EXISTS customer ( 
			id_customer INTEGER PRIMARY KEY AUTOINCREMENT,
			organization TEXT,
			job_title_customer TEXT, 
			fio_customer TEXT,
			address_customer TEXT,
			inn_customer INTEGER,
			rc_customer TEXT,
			name_bank_customer TEXT,
			bik_customer INTEGER)
			""")
		self.conn.commit()

		# Таблица исполнители (Строки по порядку: айдишник,
		# название организации,
		# фио исполнителя,
		# адрес,
		# ИНН,
		# Р/С,
		# БИК заказчика)
		self.c.execute(
			""" CREATE TABLE IF NOT EXISTS executor ( 
			id_executor INTEGER PRIMARY KEY AUTOINCREMENT,
			organization TEXT, 
			fio_executor TEXT,
			address_executor TEXT,
			inn_executor INTEGER,
			rc_executor TEXT,
			bik_executor INTEGER)
			""")
		self.conn.commit()

		# Таблица водители (Строки по порядку: айдишник,
		# айди исполнителя,
		# марка авто,
		# номер тягача (формат ТЕКСТ, в номерах буквы есть),
		# номер прицепа (формат ТЕКСТ, в номерах буквы есть),
		# фио водителя)

		self.c.execute(
			""" CREATE TABLE IF NOT EXISTS auto ( 
			id_auto INTEGER PRIMARY KEY AUTOINCREMENT,
			id_executor INTEGER,
			brand_auto TEXT, 
			num_tractor TEXT,
			num_trailer TEXT,
			fio_driver TEXT)
			""")
		self.conn.commit()

		# таблица для пути сохранения
		self.c.execute(
			""" CREATE TABLE IF NOT EXISTS save ( 
			id_save INTEGER PRIMARY KEY AUTOINCREMENT,
			address_save TEXT)
			""")
		self.conn.commit()

	# добавление заказчика
	def insert_customer(self, organization,job_title_customer, fio_customer, address_customer, inn_customer,
						rc_customer, name_bank_customer, bik_customer):
		self.c.execute("""INSERT INTO customer (organization,jon_title_customer, fio_customer, address_customer, inn_customer,
						rc_customer, name_bank_customer, bik_customer)
						  VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (organization, job_title_customer, fio_customer, address_customer, inn_customer,
						rc_customer, name_bank_customer, bik_customer))
		self.conn.commit()

	# добавление исполнителя
	def insert_executor(self, organization, fio_executor, address_executor, inn_executor, rc_executor, bik_executor):
		self.c.execute("""INSERT INTO executor (organization, fio_executor, address_executor, inn_executor, rc_executor, bik_executor)
						  VALUES (?,?, ?, ?, ?, ?, ?)""",(organization, fio_executor, address_executor, inn_executor, rc_executor, bik_executor))
		self.conn.commit()

	# добавление авто
	def insert_auto(self, id_executor, brand_auto, num_tractor, num_trailer, fio_driver):
		self.c.execute(f"""INSERT INTO auto (id_executor, brand_auto, num_tractor, num_trailer,fio_driver)
						  VALUES ({id_executor}, '{brand_auto}', '{num_tractor}', '{num_trailer}', '{fio_driver}')""")
		self.conn.commit()

	#изменить заказчика
	def update_customer(self, id_customer, organization, job_title_customer, fio_customer, address_customer, inn_customer,
						rc_customer, name_bank_customer, bik_customer):
		self.c.execute(f"""UPDATE customer 
						SET organization='{organization}',jon_title_customer='{job_title_customer}' fio_customer='{fio_customer}', address_customer='{address_customer}',
						inn_customer={inn_customer}, rc_customer='{rc_customer}', name_bank_customer='{name_bank_customer}',
						bik_customer={bik_customer}
						WHERE id_customer={id_customer}""")
		self.conn.commit()

	# изменить исполнителя
	def update_executor(self, id_executor, organization, fio_executor, address_executor, inn_executor,
						rc_executor, bik_executor):
		self.c.execute(f"""UPDATE executor 
						SET organization='{organization}', fio_executor='{fio_executor}', address_executor='{address_executor}',
						inn_executor={inn_executor}, rc_executor='{rc_executor}', bik_executor={bik_executor}
						WHERE id_executor={id_executor}""")
		self.conn.commit()

	# изменить авто
	def update_auto(self, id_auto, brand_auto, num_tractor, num_trailer, fio_driver):
		self.c.execute(f"""UPDATE auto
						SET brand_auto='{brand_auto}', num_tractor='{num_tractor}', num_trailer='{num_trailer}',
						fio_driver='{fio_driver}'
						WHERE id_auto={id_auto}""")
		self.conn.commit()

	# удалить заказчика
	def delete_customer(self, id_customer):
		self.c.execute(f"DELETE FROM customer WHERE id_customer = {id_customer}")
		self.conn.commit()

	# удалить исполнителя
	def delete_executor(self, id_executor):
		self.c.execute(f"DELETE FROM executor WHERE id_executor = {id_executor}")
		self.conn.commit()

	# удалить авто
	def delete_auto(self, id_auto):
		self.c.execute(f"DELETE FROM auto WHERE id_auto = {id_auto}")
		self.conn.commit()

	# поиск заказчика
	def search_customer(self, name_search):
		self.c.execute(f"""SELECT * FROM customer WHERE organization LIKE '%{name_search}%' 
		or fio_customer LIKE '%{name_search}%' or inn_customer LIKE '%{name_search}%'""")
		return self.c.fetchall()

	# поиск заказчика по айди
	def search_customer_id(self, id_customer):
		self.c.execute(f"""SELECT * FROM customer WHERE id_customer={id_customer}""")
		return self.c.fetchall()

	# поиск исполнителя
	def search_executor(self, name_search):
		self.c.execute(f"""SELECT *
		FROM executor WHERE organization LIKE '%{name_search}%' 
		or fio_executor LIKE '%{name_search}%' or inn_executor LIKE '%{name_search}%'""")
		return self.c.fetchall()

	# поиск исполнителя по айди
	def search_executor_id(self, id_executor):
		self.c.execute(f"""SELECT * FROM executor WHERE id_executor={id_executor}""")
		return self.c.fetchall()

	# вывод заказчика
	def view_customer(self):
		self.c.execute(f"SELECT id_customer,organization,fio_customer,inn_customer FROM customer")
		return self.c.fetchall()
		#self.conn.commit()

	# вывод исполнителя
	def view_executor(self):
		self.c.execute(f"SELECT id_executor,organization,jon_title_executor,fio_executor,inn_executor FROM executor")
		return self.c.fetchall()
		#self.conn.commit()

	# вывод авто
	def view_auto(self):
		self.c.execute(f"SELECT * FROM auto")
		return self.c.fetchall()

	#добавить адресс сохранения
	def insert_save_address(self, address_save):
		self.c.execute(f"""INSERT INTO save (address_save) VALUES '{address_save}' """)
		self.conn.commit()

	# изменить адресс сохранения
	def update_save_address(self, address_save):
		self.c.execute(f"""UPDATE save SET address_save='{address_save}'WHERE id_save= 1""")
		self.conn.commit()

	# вывести адрес сохранения
	def view_save_address(self):
		self.c.execute(f"SELECT * FROM save")
		return self.c.fetchall()








