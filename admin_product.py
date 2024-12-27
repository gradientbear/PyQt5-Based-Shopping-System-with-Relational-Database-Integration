import mysql.connector as con
from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from main import widget, CusName, DatabaseConfig
from datetime import date

#AdminProducts_1 terminal start --------------------------------------------------------------------------------------------------------------------------------------------Done
class AdmProduct_1(QDialog):
	def __init__(self):
		super(AdmProduct_1,self).__init__()
		loadUi("ui_forms/AdminProducts_1.ui",self)
		self.AdminProBack.clicked.connect(self.back)
		self.btn_add.clicked.connect(self.proadd)
		self.btn_edit.clicked.connect(self.proedit)
		self.AdminPanLogOff.clicked.connect(self.show_login)
		self.btn_refresh.clicked.connect(self.Get_Data)
		self.AdminTableProd
		self.Close.clicked.connect(self.close)


	def Get_Data(self):
		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()
		command = "select * from Product"
		cursor.execute(command)
		result = cursor.fetchall()
		print(result)

		self.AdminTableProd.setRowCount(0)

		for row_num, row_data in enumerate(result):

			self.AdminTableProd.insertRow(row_num)
			for column_num, data in enumerate(row_data):
				self.AdminTableProd.setItem(row_num, column_num, QTableWidgetItem(str(data)))
	   

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
		widget.setCurrentIndex(4)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(625)

	def proedit(self):
		widget.setCurrentIndex(5)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(700)
#AdminProducts_1 terminal END --------------------------------------------------------------------------------------------------------------------------------------------Done


#AdminProducts_2 terminal start --------------------------------------------------------------------------------------------------------------------------------------------Done
class AdmProduct_2(QDialog):
	def __init__(self):
		super(AdmProduct_2,self).__init__()
		loadUi("ui_forms/AdminProducts_2.ui",self)
		self.AdminProBack.clicked.connect(self.back)
		self.btn_all.clicked.connect(self.proall)
		self.btn_edit.clicked.connect(self.proedit)
		self.AdminPanLogOff.clicked.connect(self.show_login)
		self.btn_add_product.clicked.connect(self.AddPro)
		self.Close.clicked.connect(self.close)

	def AddPro(self):
		ProdType = self.AdminProdType.text()
		ProdSuppID = self.AdminProdSupp.text()
		ProName = self.AdminProdName.text()
		Quantity = self.AdminProdQuantity.text()
		ProPrice = self.AdminProdPrice.text()
		ProCon = self.AdminProdCond.text()
		ProMeth = self.AdminProdPayMeth.text()

		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()


		allids=cursor.execute("select max(product_id) from Product")
		newidtup = cursor.fetchone()
		newidint = (int((''.join(str(x) for x in newidtup)))+int(1)) # To manulay insert the Primary Key if is int
		newidsrt = str(newidint)
		Null = "null"
		New = "new"
		None1 = "None"
		PHDate = "1800-1-1"
		zero = "0"
		CurrentDate = date.today()
		CurrentDateStr = str(CurrentDate)
		cursor.execute("INSERT INTO sample_database.product (product_id, product_type, supplier_id, prod_name, QuantityInStock, prod_price, prod_Cond, Pay_Me_METH, Pro_Reternability) VALUES ('"+ newidsrt +"' ,'"+ ProdType +"','"+ ProdSuppID +"','"+ ProName +"','"+ Quantity +"','"+ ProPrice +"','"+ ProCon +"','"+ ProMeth +"','Not Sold')")
		db.commit()

		QMessageBox.information(self," ","You Sucessfully added a product")

		self.AdminProdType.setText("")
		self.AdminProdSupp.setText("")
		self.AdminProdName.setText("")
		self.AdminProdQuantity.setText("")
		self.AdminProdPrice.setText("")
		self.AdminProdCond.setText("")
		self.AdminProdPayMeth.setText("")
		
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
		widget.setCurrentIndex(3)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(625)

	def proedit(self):
		widget.setCurrentIndex(5)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(700)		
#AdminProducts_2 terminal END --------------------------------------------------------------------------------------------------------------------------------------------Done



#AdminProducts_3 terminal start --------------------------------------------------------------------------------------------------------------------------------------------
class AdmProduct_3(QDialog):
	def __init__(self):
		super(AdmProduct_3,self).__init__()
		loadUi("ui_forms/AdminProducts_3.ui",self)
		self.AdminProBack.clicked.connect(self.back)
		self.btn_all.clicked.connect(self.proall)
		self.btn_add.clicked.connect(self.proadd)
		self.AdminPanLogOff.clicked.connect(self.show_login)

		self.Close.clicked.connect(self.close)
		self.btn_refresh.clicked.connect(self.updatebox)
		self.btn_search.clicked.connect(self.Disp_Data)
		self.btn_delete.clicked.connect(self.delentry)
		self.btn_update.clicked.connect(self.UpData)
		self.AdminProdType.setReadOnly(False)
		self.AdminProdSupp.setReadOnly(False)
		self.AdminProdName.setReadOnly(False)
		self.AdminProdQuantity.setReadOnly(False)
		self.AdminProdPrice.setReadOnly(False)
		self.AdminProdCond.setReadOnly(False)
		self.AdminProdPayMeth.setReadOnly(False)
		self.added=[]
		
		self.db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		self.cartcursor=self.db.cursor()


	def updatebox(self):
		self.search_combo.clear()
		result = []
		print("Reached clear")
		cursor = self.db.cursor()
		command = "SELECT distinct prod_name from Product"
		cursor.execute(command)
		result = cursor.fetchall()
		print("Reached fetch")
		self.search_combo.setEditable(False)
		self.search_combo.addItem("---- Products ----")
		print("Reached iteration")
		for r in result:
			if r[0] not in self.added:self.search_combo.addItem(r[0])
		print("Reached complete")

	def delentry(self):
		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()
		product_val = self.search_combo.currentText()
		Command = "DELETE from sample_database.PRODUCT WHERE prod_name = '"+ product_val +"'"
		cursor.execute(Command)
		db.commit()

		self.id_label.setText("N°")
		self.AdminProdType.clear()
		self.AdminProdSupp.clear()
		self.AdminProdName.clear()
		self.AdminProdQuantity.clear()
		self.AdminProdPrice.clear()
		self.AdminProdCond.clear()
		self.AdminProdPayMeth.clear()

	def Disp_Data(self):
		try:
			cursor = self.db.cursor()
			product_val = self.search_combo.currentText()
			print(product_val)
			command="SELECT PRODUCT_ID, product_type, supplier_id, prod_name, QuantityInStock, prod_price, prod_Cond, Pay_Me_METH FROM sample_database.PRODUCT WHERE prod_name = '"+ product_val +"'"	
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
			r8 = result[0][7]

			self.id_label.setText(str(r1))
			self.AdminProdType.setText(str(r2))
			self.AdminProdSupp.setText(str(r3))
			self.AdminProdName.setText(str(r4))
			self.AdminProdQuantity.setText(str(r5))
			self.AdminProdPrice.setText(str(r6))
			self.AdminProdCond.setText(str(r7))
			self.AdminProdPayMeth.setText(str(r8))
		except:
			self.id_label.setText("N°")
			self.AdminProdType.clear()
			self.AdminProdSupp.clear()
			self.AdminProdName.clear()
			self.AdminProdQuantity.clear()
			self.AdminProdPrice.clear()
			self.AdminProdCond.clear()
			self.AdminProdPayMeth.clear()
			pass

	def UpData(self):
		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()

		type = self.AdminProdType.text()
		supplier = self.AdminProdSupp.text()
		name = self.AdminProdName.text()
		Quan = self.AdminProdQuantity.text()
		price = self.AdminProdPrice.text()
		condition = self.AdminProdCond.text()
		paymeth = self.AdminProdPayMeth.text()

		cursor = self.db.cursor()
		product_val = self.search_combo.currentText()

		command="UPDATE sample_database.PRODUCT SET product_type =  '"+ type +"' WHERE prod_name = '"+ product_val +"'"	
		cursor.execute(command)
		print(command)
		reult = cursor.fetchall()
		print(reult)
		db.commit()
		command="UPDATE sample_database.PRODUCT SET supplier_id =  '"+ supplier +"' WHERE prod_name = '"+ product_val +"'"	
		cursor.execute(command)
		print(command)
		reult = cursor.fetchall()
		print(reult)
		db.commit()
		command="UPDATE sample_database.PRODUCT SET prod_name =  '"+ name +"' WHERE prod_name = '"+ product_val +"'"	
		cursor.execute(command)
		print(command)
		reult = cursor.fetchall()
		print(reult)
		db.commit()
		command="UPDATE sample_database.PRODUCT SET QuantityInStock =  '"+ Quan +"' WHERE prod_name = '"+ product_val +"'"	
		cursor.execute(command)
		print(command)
		reult = cursor.fetchall()
		print(reult)
		db.commit()
		command="UPDATE sample_database.PRODUCT SET prod_price =  '"+ price +"' WHERE prod_name = '"+ product_val +"'"	
		cursor.execute(command)
		print(command)
		reult = cursor.fetchall()
		print(reult)
		db.commit()
		command="UPDATE sample_database.PRODUCT SET prod_Cond =  '"+ condition +"' WHERE prod_name = '"+ product_val +"'"	
		cursor.execute(command)
		print(command)
		reult = cursor.fetchall()
		print(reult)
		db.commit()
		command="UPDATE sample_database.PRODUCT SET Pay_Me_METH =  '"+ paymeth +"' WHERE prod_name = '"+ product_val +"'"	
		cursor.execute(command)
		print(command)
		reult = cursor.fetchall()
		print(reult)
		db.commit()
		
		command="SELECT * FROM sample_database.PRODUCT WHERE prod_name = '"+ product_val +"'"	
		cursor.execute(command)
		print(command)
		reult = cursor.fetchall()
		print("From PRODUCT")
		print(reult)


		Ref = "Referbished"
		oos = "OutOfStock"
		ins = "installments"
		unre = "Unreternable"

		command="UPDATE sample_database.Product SET Diffrence_IN_Date = DATEDIFF(prod_SoldDate, prod_ReturnDate)"	
		cursor.execute(command)
		command="UPDATE sample_database.Product SET prod_Cond = '"+ Ref +"' WHERE (Diffrence_IN_Date > 14)&(Diffrence_IN_Date <= 29)"	
		cursor.execute(command)
		command="UPDATE sample_database.Product SET prod_Cond = '"+ oos +"' WHERE Diffrence_IN_Date > 29"	
		cursor.execute(command)
		command="UPDATE sample_database.Product SET prod_price = prod_price*0.9 WHERE prod_Cond = '"+ Ref +"'"	
		cursor.execute(command)
		command="UPDATE sample_database.Product SET Pro_Reternability = '"+ unre +"' WHERE Pay_Me_METH = '"+ ins +"'"	
		cursor.execute(command)
		command="UPDATE sample_database.Product SET prod_price = prod_price*0.85 WHERE (Diffrence_IN_Date > 14)&(Diffrence_IN_Date <31)"	
		cursor.execute(command)

		self.id_label.setText("N°")
		self.AdminProdType.clear()
		self.AdminProdSupp.clear()
		self.AdminProdName.clear()
		self.AdminProdQuantity.clear()
		self.AdminProdPrice.clear()
		self.AdminProdCond.clear()
		self.AdminProdPayMeth.clear()

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
		widget.setCurrentIndex(3)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(625)

	def proadd(self):
		widget.setCurrentIndex(4)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(625)
#AdminProducts_3 terminal END --------------------------------------------------------------------------------------------------------------------------------------------

