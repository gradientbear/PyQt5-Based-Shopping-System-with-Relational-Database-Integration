from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from main import widget, CusName, DatabaseConfig
import mysql.connector as con
from datetime import date

#AdminCust_1 terminal start --------------------------------------------------------------------------------------------------------------------------------------------Done
class AdminCust_1(QDialog):
	def __init__(self):
		super(AdminCust_1,self).__init__()
		loadUi("ui_forms/AdminCustomers_1.ui",self)
		self.AdminProBack.clicked.connect(self.back)
		self.btn_add.clicked.connect(self.proadd)
		self.btn_edit.clicked.connect(self.proedit)
		self.AdminPanLogOff.clicked.connect(self.show_login)
		self.btn_refresh.clicked.connect(self.Get_Data)
		self.AdminTableCus
		self.Close.clicked.connect(self.close)

	def Get_Data(self):
		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()
		command = "select * from Customer"
		cursor.execute(command)
		result = cursor.fetchall()
		print(result)

		self.AdminTableCus.setRowCount(0)

		for row_num, row_data in enumerate(result):

			self.AdminTableCus.insertRow(row_num)
			for column_num, data in enumerate(row_data):
				self.AdminTableCus.setItem(row_num, column_num, QTableWidgetItem(str(data)))

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
		widget.setCurrentIndex(10)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(625)

	def proedit(self):
		widget.setCurrentIndex(11)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(700)
#AdminCust_1 terminal END --------------------------------------------------------------------------------------------------------------------------------------------Done


#AdminCust_2 terminal start --------------------------------------------------------------------------------------------------------------------------------------------Done
class AdminCust_2(QDialog):
	def __init__(self):
		super(AdminCust_2,self).__init__()
		loadUi("ui_forms/AdminCustomers_2.ui",self)
		self.AdminProBack.clicked.connect(self.back)
		self.btn_all.clicked.connect(self.proall)
		self.btn_edit.clicked.connect(self.proedit)
		self.AdminPanLogOff.clicked.connect(self.show_login)
		self.btn_add_Customer.clicked.connect(self.AddPro)
		self.Close.clicked.connect(self.close)

	def AddPro(self):
		CusAddID = self.AdminCusAddID.text()
		CusName1 = self.AdminCusName.text()
		CusPass = self.AdminCusPass.text()
		CusEmail = self.AdminCusEmail.text()
		CusNamePhn = self.AdminCusNamePhn.text()
		CusDetails = self.AdminCusDetails.text()

		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()


		allids=cursor.execute("select max(customer_id) from customer")
		newidtup = cursor.fetchone()
		newidint = (int((''.join(str(x) for x in newidtup)))+int(1)) # To manulay insert the Primary Key if is int
		newidsrt = str(newidint)
		CurrentDate = date.today()
		CurrentDateStr = str(CurrentDate)
		cursor.execute("INSERT INTO sample_database.customer (customer_id,customer_address_id, customername, customer_pass, customer_email, customer_phn, date_bec_cust, other_cust_details) VALUES ('"+ newidsrt +"' ,'"+ CusAddID +"','"+ CusName1 +"','"+ CusPass +"','"+ CusEmail +"','"+ CusNamePhn +"','"+ CurrentDateStr +"','"+ CusDetails +"')")
		db.commit()

		QMessageBox.information(self," ","You Sucessfully added a Cutomer")

		self.AdminCusAddID.setText("")
		self.AdminCusName.setText("")
		self.AdminCusPass.setText("")
		self.AdminCusEmail.setText("")
		self.AdminCusNamePhn.setText("")
		self.AdminCusDetails.setText("")

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
		widget.setCurrentIndex(9)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(625)

	def proedit(self):
		widget.setCurrentIndex(11)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(700)
#AdminCust_2 terminal END --------------------------------------------------------------------------------------------------------------------------------------------Done



#AdminCust_3 terminal start --------------------------------------------------------------------------------------------------------------------------------------------
class AdminCust_3(QDialog):
	def __init__(self):
		super(AdminCust_3,self).__init__()
		loadUi("ui_forms/AdminCustomers_3.ui",self)
		self.AdminProBack.clicked.connect(self.back)
		self.btn_all.clicked.connect(self.proall)
		self.btn_add.clicked.connect(self.proadd)
		self.AdminPanLogOff.clicked.connect(self.show_login)
		self.btn_refresh.clicked.connect(self.updatebox)
		self.btn_search.clicked.connect(self.Disp_Data)
		self.btn_delete.clicked.connect(self.delentry)
		self.btn_update.clicked.connect(self.UpData)
		self.AdminCusAddID.setReadOnly(False)
		self.AdminCusPass.setReadOnly(False)
		self.AdminCusEmail.setReadOnly(False)
		self.AdminCusPhn.setReadOnly(False)
		self.AdminCusDate.setReadOnly(False)
		self.AdminCusDet.setReadOnly(False)
		self.Close.clicked.connect(self.close)
		self.added=[]
		
		self.db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		self.cartcursor=self.db.cursor()

	def updatebox(self):
		print("Reached Here")
		cursor = self.db.cursor()
		command = "SELECT distinct customername from Customer"
		cursor.execute(command)
		result = cursor.fetchall()
		print("Reached Here")
		self.search_combo.clear()
		self.search_combo.setEditable(False)
		self.search_combo.addItem("---- Customer ----")
		print("Reached Here")
		for r in result:
			if r[0] not in self.added:self.search_combo.addItem(r[0])

	def delentry(self):
		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()
		product_val = self.search_combo.currentText()
		Command = "Delete from Customer customername = '"+ product_val +"'"
		cursor.execute(Command)
		db.commit()

	def Disp_Data(self):
		try:
			cursor = self.db.cursor()
			product_val = self.search_combo.currentText()
			print(product_val)
			command="SELECT customer_id, customer_address_id, customer_pass, customer_email, customer_phn, date_bec_cust, other_cust_details FROM Customer WHERE customername = '"+ product_val +"'"	
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
			r7 = result[0][6]

			self.id_label.setText(str(r1))
			self.AdminCusAddID.setText(str(r2))
			self.AdminCusPass.setText(str(r3))
			self.AdminCusEmail.setText(str(r4))
			self.AdminCusPhn.setText(str(r5))
			self.AdminCusDate.setText(str(r6))
			self.AdminCusDet.setText(str(r7))
		except:
			self.id_label.setText("N°")
			self.AdminCusAddID.clear()
			self.AdminCusPass.clear()
			self.AdminCusEmail.clear()
			self.AdminCusPhn.clear()
			self.AdminCusDate.clear()
			self.AdminCusDet.clear()
			pass

	def UpData(self):
		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()

		AdID = self.AdminCusAddID.text()
		CusPass = self.AdminCusPass.text()
		CusEma = self.AdminCusEmail.text()
		CusPhn = self.AdminCusPhn.text()
		CusDat = self.AdminCusDate.text()
		CusDet = self.AdminCusDet.text()

		cursor = self.db.cursor()
		product_val = self.search_combo.currentText()

		command="UPDATE sample_database.Customer SET customer_address_id =  '"+ AdID +"' WHERE customername = '"+ product_val +"'"	
		cursor.execute(command)
		db.commit()
		command="UPDATE sample_database.Customer SET customer_pass =  '"+ CusPass +"' WHERE customername = '"+ product_val +"'"	
		cursor.execute(command)
		db.commit()
		command="UPDATE sample_database.Customer SET customer_email =  '"+ CusEma +"' WHERE customername = '"+ product_val +"'"	
		cursor.execute(command)
		db.commit()
		command="UPDATE sample_database.Customer SET customer_phn =  '"+ CusPhn +"' WHERE customername = '"+ product_val +"'"	
		cursor.execute(command)
		db.commit()
		command="UPDATE sample_database.Customer SET date_bec_cust =  '"+ CusDat +"' WHERE customername = '"+ product_val +"'"	
		cursor.execute(command)
		db.commit()
		command="UPDATE sample_database.Customer SET other_cust_details =  '"+ CusDet +"' WHERE customername = '"+ product_val +"'"	
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
		widget.setCurrentIndex(9)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(625)

	def proadd(self):
		widget.setCurrentIndex(10)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(625)
#AdminCust_3 terminal END --------------------------------------------------------------------------------------------------------------------------------------------
