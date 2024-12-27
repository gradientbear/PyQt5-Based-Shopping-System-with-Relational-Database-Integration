from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi
import mysql.connector as con
from main import widget, CusName, DatabaseConfig

#Admsuppliers_1 terminal start --------------------------------------------------------------------------------------------------------------------------------------------Done
class Admsuppliers_1(QDialog):
	def __init__(self):
		super(Admsuppliers_1,self).__init__()
		loadUi("ui_forms/AdminSuppliers_1.ui",self)
		self.AdminProBack.clicked.connect(self.back)
		self.btn_add.clicked.connect(self.proadd)
		self.btn_edit.clicked.connect(self.proedit)
		self.AdminPanLogOff.clicked.connect(self.show_login)
		self.btn_refresh.clicked.connect(self.Get_Data)
		self.AdminTableSupp
		self.Close.clicked.connect(self.close)


	def Get_Data(self):
		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()
		command = "select * from Suppliers"
		cursor.execute(command)
		result = cursor.fetchall()
		print(result)

		self.AdminTableSupp.setRowCount(0)

		for row_num, row_data in enumerate(result):

			self.AdminTableSupp.insertRow(row_num)
			for column_num, data in enumerate(row_data):
				self.AdminTableSupp.setItem(row_num, column_num, QTableWidgetItem(str(data)))

	def show_login(self):
		CusName.clear()
		widget.setCurrentIndex(0)
		widget.setFixedWidth(400)
		widget.setFixedHeight(500)

	def back(self):
		widget.setCurrentIndex(2)
		widget.setFixedWidth(800)
		widget.setFixedHeight(600)

	def proadd(self):
		widget.setCurrentIndex(7)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(625)

	def proedit(self):
		widget.setCurrentIndex(8)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(700)
#Admsuppliers_1 terminal END --------------------------------------------------------------------------------------------------------------------------------------------Done

#Admsuppliers_2 terminal start --------------------------------------------------------------------------------------------------------------------------------------------Done
class Admsuppliers_2(QDialog):
	def __init__(self):
		super(Admsuppliers_2,self).__init__()
		loadUi("ui_forms/AdminSuppliers_2.ui",self)
		self.AdminProBack.clicked.connect(self.back)
		self.btn_all.clicked.connect(self.proall)
		self.btn_edit.clicked.connect(self.proedit)
		self.AdminPanLogOff.clicked.connect(self.show_login)
		self.btn_add_Supplier.clicked.connect(self.AddPro)
		self.Close.clicked.connect(self.close)

	def AddPro(self):
		SuppAddID = self.AdminSuppAddID.text()
		SuppName = self.AdminSuppName.text()
		SuppContName = self.AdminConName.text()
		SuppPhn = self.AdminSuppPhn.text()
		SuppEmail = self.AdminSuppEmail.text()
		SuppDet = self.AdminSuppDetails.text()

		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()


		allids=cursor.execute("select max(supplier_id) from suppliers")
		newidtup = cursor.fetchone()
		newidint = (int((''.join(str(x) for x in newidtup)))+int(1)) # To manulay insert the Primary Key if is int
		newidsrt = str(newidint)
		cursor.execute("INSERT INTO sample_database.suppliers (supplier_id, supplier_add_id, supplier_name, contact_name, supplier_phn, supplier_email, other_details) VALUES ('"+ newidsrt +"' ,'"+ SuppAddID +"','"+ SuppName +"','"+ SuppContName +"','"+ SuppPhn +"','"+ SuppEmail +"','"+ SuppDet +"')")
		db.commit()

		QMessageBox.information(self," ","You Sucessfully added a supplier")

		self.AdminSuppAddID.setText("")
		self.AdminSuppName.setText("")
		self.AdminConName.setText("")
		self.AdminSuppPhn.setText("")
		self.AdminSuppEmail.setText("")
		self.AdminSuppDetails.setText("")

	def show_login(self):
		CusName.clear()
		widget.setCurrentIndex(0)
		widget.setFixedWidth(400)
		widget.setFixedHeight(500)

	def back(self):
		widget.setCurrentIndex(2)
		widget.setFixedWidth(800)
		widget.setFixedHeight(600)

	def proall(self):
		widget.setCurrentIndex(6)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(625)

	def proedit(self):
		widget.setCurrentIndex(8)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(700)
#Admsuppliers_2 terminal END --------------------------------------------------------------------------------------------------------------------------------------------Done

#Admsuppliers_3 terminal start --------------------------------------------------------------------------------------------------------------------------------------------
class Admsuppliers_3 (QDialog):
	def __init__(self):
		super(Admsuppliers_3 ,self).__init__()
		loadUi("ui_forms/AdminSuppliers_3.ui",self)
		self.AdminProBack.clicked.connect(self.back)
		self.btn_all.clicked.connect(self.proall)
		self.btn_add.clicked.connect(self.proadd)
		self.AdminPanLogOff.clicked.connect(self.show_login)
		self.btn_refresh.clicked.connect(self.updatebox)
		self.btn_search.clicked.connect(self.Disp_Data)
		self.btn_delete.clicked.connect(self.delentry)
		self.btn_update.clicked.connect(self.UpData)
		self.AdminSupplierAddressID.setReadOnly(False)
		self.AdminSuppContacName.setReadOnly(False)
		self.AdminSuppPhn.setReadOnly(False)
		self.AdminSuppEmail.setReadOnly(False)
		self.AdminSuppDet.setReadOnly(False)
		self.Close.clicked.connect(self.close)
		self.added=[]
		
		self.db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		self.cartcursor=self.db.cursor()

	def updatebox(self):
		print("Reached Here")
		cursor = self.db.cursor()
		command = "SELECT distinct supplier_name from Suppliers"
		cursor.execute(command)
		result = cursor.fetchall()
		print("Reached Here")
		self.search_combo.clear()
		self.search_combo.setEditable(False)
		self.search_combo.addItem("---- Suppliers ----")
		print("Reached Here")
		for r in result:
			if r[0] not in self.added:self.search_combo.addItem(r[0])

	def delentry(self):
		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()
		product_val = self.search_combo.currentText()
		Command = "Delete from Suppliers supplier_name = '"+ product_val +"'"
		cursor.execute(Command)
		db.commit()

	def Disp_Data(self):
		try:
			cursor = self.db.cursor()
			product_val = self.search_combo.currentText()
			print(product_val)
			command="SELECT supplier_id, supplier_add_id, contact_name, supplier_phn, supplier_email, other_details WHERE supplier_name = '"+ product_val +"'"	
			cursor.execute(command)
			print(command)
			
			result = cursor.fetchall()
			print(result)
			
			
			r1 = result[0][0]
			r2 = result[0][1]
			r3 = result[0][2]
			r4 = result[0][3]
			r5 = result[0][4]
			r6 = result[0][5]

			self.id_label.setText(str(r1))
			self.AdminSupplierAddressID.setText(str(r2))
			self.AdminSuppContacName.setText(str(r3))
			self.AdminSuppPhn.setText(str(r4))
			self.AdminSuppEmail.setText(str(r5))
			self.AdminSuppDet.setText(str(r6))
		except:
			self.id_label.setText("N°")
			self.AdminSupplierAddressID.clear()
			self.AdminSuppContacName.clear()
			self.AdminSuppPhn.clear()
			self.AdminSuppEmail.clear()
			self.AdminSuppDet.clear()
			pass

	def UpData(self):
		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()

		AdID = self.AdminSupplierAddressID.text()
		SuppCon = self.AdminSuppContacName.text()
		Suppphn = self.AdminSuppPhn.text()
		SuppEma = self.AdminSuppEmail.text()
		Suppdet = self.AdminSuppDet.text()

		cursor = self.db.cursor()
		product_val = self.search_combo.currentText()

		command="UPDATE sample_database.Suppliers SET supplier_add_id =  '"+ AdID +"' WHERE supplier_name = '"+ product_val +"'"	
		cursor.execute(command)
		db.commit()
		command="UPDATE sample_database.Suppliers SET contact_name =  '"+ SuppCon +"' WHERE supplier_name = '"+ product_val +"'"	
		cursor.execute(command)
		db.commit()
		command="UPDATE sample_database.Suppliers SET supplier_phn =  '"+ Suppphn +"' WHERE supplier_name = '"+ product_val +"'"	
		cursor.execute(command)
		db.commit()
		command="UPDATE sample_database.Suppliers SET supplier_email =  '"+ SuppEma +"' WHERE supplier_name = '"+ product_val +"'"	
		cursor.execute(command)
		db.commit()
		command="UPDATE sample_database.Suppliers SET other_details =  '"+ Suppdet +"' WHERE supplier_name = '"+ product_val +"'"	
		cursor.execute(command)
		db.commit()

	def show_login(self):
		CusName.clear()
		widget.setCurrentIndex(0)
		widget.setFixedWidth(400)
		widget.setFixedHeight(500)

	def back(self):
		widget.setCurrentIndex(2)
		widget.setFixedWidth(800)
		widget.setFixedHeight(600)
		
	def proall(self):
		widget.setCurrentIndex(6)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(625)

	def proadd(self):
		widget.setCurrentIndex(7)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(625)
#Admsuppliers_3 terminal END --------------------------------------------------------------------------------------------------------------------------------------------

