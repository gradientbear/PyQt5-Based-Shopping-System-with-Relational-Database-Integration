from PyQt5.QtWidgets import QDialog, QTableWidgetItem, QMessageBox, QAbstractScrollArea
from PyQt5.uic import loadUi
from main import widget, CusName, CusCartInv, CusCartInv2, Total, DatabaseConfig
import mysql.connector as con
from datetime import date, timedelta, datetime

#CusPro terminal start --------------------------------------------------------------------------------------------------------------------------------------------Done
class CusPro(QDialog):
	def __init__(self):
		super(CusPro,self).__init__()
		loadUi("ui_forms/CustomerProducts.ui",self)
		self.CustomerCart.clicked.connect(self.checkO)
		self.AdminPanLogOff.clicked.connect(self.show_login)
		self.btn_refresh.clicked.connect(self.Get_Data)
		self.btn_return.clicked.connect(self.ReturnProd)
		self.CustomerTableProd
		self.btn_search.clicked.connect(self.Disp_Data)
		self.btn_add_product.clicked.connect(self.CartTable)
		self.CustProdType.setReadOnly(True)
		self.CustProdName.setReadOnly(True)
		self.CustQuanInStock.setReadOnly(True)
		self.CustUnitPrice.setReadOnly(True)
		self.Balance.setReadOnly(True)
		self.CustQuanPurchased.setReadOnly(False)
		self.return_name.setReadOnly(False)
		self.added=[]
		self.CusName = CusName
		self.CusCartInv = CusCartInv
		self.CusCartInv2 = CusCartInv2
		self.Total = Total
		self.CheckOutTable.setRowCount(10)
		self.PayInIns
		self.Close.clicked.connect(self.close)
		
		self.db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		self.cartcursor=self.db.cursor()
		Cname = (''.join(str(x) for x in CusName))
		command = "SELECT PaymentBalance FROM Customer WHERE customername = '"+ Cname +"'"
		self.cartcursor.execute(command)
		r = self.cartcursor.fetchmany(1)
		self.Balance.setText(str(r))

	def ReturnProd(self):
		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()

		ItemToRet = self.return_name.text()
		allids=cursor.execute("select max(INV_ID) from invoice")
		newidtup = cursor.fetchone()
		newidint = (int((''.join(str(x) for x in newidtup)))+int(1)) # To manulay insert the Primary Key if is int
		newidsrt = str(newidint)

		Cname = (''.join(str(x) for x in CusName))
		cursor.execute("select PRODUCT_NAME from INVOICE where (CUS_NAME = '"+ Cname +"')&(PRODUCT_NAME = '"+ ItemToRet +"')")
		result = cursor.fetchone()
		cursor.execute("select Diffrence_IN_Date from PRODUCT where prod_name = '"+ ItemToRet +"'")
		result1 = cursor.fetchone()
		print(result1)
		result1str = str(result1)
		print(result1str)

		if int(result1str[1]) >=30:
			QMessageBox.information(self,"Invoice Error","You Did not purchase this product")
		else:
			new = "new"
			ref = "Referbished"
			CurrentDate = date.today()
			CurrentDatestr = str(CurrentDate)

			DatPur =self.DatePurchased.text()
			Cname = (''.join(str(x) for x in CusName))
			cursor.execute("select PaymentInitial from INVOICE where (PRODUCT_NAME = '"+ ItemToRet +"')&(CUS_NAME = '"+ Cname +"')&(PaymentInitial = '"+ DatPur +"')")
			Invresult = cursor.fetchall()
			Invdate = Invresult[0][0]
			Invdatestr = str(Invdate)

			start = datetime.strptime(Invdatestr, "%Y-%m-%d")
			end =   datetime.strptime(CurrentDatestr, "%Y-%m-%d")
			# get the difference between wo dates as timedelta object
			diff = end.date() - start.date()
			diffstr = str(diff)

			cursor.execute("select PAYMENT_METHOD from INVOICE where (PRODUCT_NAME = '"+ ItemToRet +"')&(CUS_NAME = '"+ Cname +"')&(PaymentInitial = '"+ DatPur +"')")
			Invresult2 = cursor.fetchall()
			Invmeth = Invresult2[0][0]
			Invmethstr = str(Invmeth)
			cursor.execute("select * from PRODUCT where (prod_name = '"+ ItemToRet +"')&(prod_Cond = '"+ new +"')")
			result2 = cursor.fetchall()
			r0 = result2[0][0]
			r1 = result2[0][1]
			r1str = str(r1)
			r2 = result2[0][2]
			r2str = str(r2)
			r3 = result2[0][3]
			r3str = str(r3)
			r4 = result2[0][4]
			r5 = result2[0][5]
			r6 = result2[0][6]
			r7 = result2[0][7]
			r8 = result2[0][8]
			r9 = result2[0][9]
			r10 = result2[0][10]
			r11 = result2[0][11]
			r12 = result2[0][12]
			r13 = result2[0][13]
			cursor.execute("select * from PRODUCT where (prod_name = '"+ ItemToRet +"')&(prod_Cond = '"+ ref +"')")
			result3 = cursor.fetchall()
			_r0 = result2[0][0]
			_r1 = result2[0][1]
			_r2 = result2[0][2]
			_r3 = result2[0][3]
			_r4 = result2[0][4]
			_r5 = result2[0][5]
			print(_r5)
			if _r5 == None:
				QIS = 1
				QISstr = str(QIS)
			else:
				QISstr = str(_r5)
			_r6 = result2[0][6]
			_r7 = result2[0][7]
			_r8 = result2[0][8]
			_r9 = result2[0][9]
			_r10 = result2[0][10]
			_r11 = result2[0][11]
			_r12 = result2[0][12]
			_r13 = result2[0][13]
			if r8 != _r8:
				command = "INSERT INTO sample_database.PRODUCT (PRODUCT_ID, product_type, supplier_id, prod_name, QuantityInStock, prod_price, prod_desc, prod_Cond, Pay_Me_METH, Pro_Reternability, prod_SoldDate, prod_ReturnDate, Diffrence_IN_Date, other_details) VALUES ('"+ newidsrt +"','"+ r1str +"','"+ r2str +"','"+ r3str +"','"+ QISstr +"','"+ r5 +"','"+ r6 +"','"+ ref +"','"+ Invmethstr +"','"+ ref +"','"+ Invdatestr +"','"+ CurrentDatestr +"','"+ diffstr +"','"+ r13 +"')"
				cursor.execute(command)
				db.commit()
				QMessageBox.information(self,"Done","Returned Succesfuly")
			else:
				command = "UPDATE sample_database.PRODUCT SET QuantityInStock = '"+ QISstr +"' WHERE prod_Cond = '"+ ref +"'"
				cursor.execute(command)
				db.commit()
				command = "UPDATE sample_database.PRODUCT SET prod_ReturnDate = '"+ CurrentDatestr +"' WHERE prod_Cond = '"+ ref +"'"
				cursor.execute(command)
				db.commit()
				QMessageBox.information(self,"Done","Returned Succesfuly")

	def updatebox(self):
		print("Reached Here")
		cursor = self.db.cursor()
		command = "SELECT distinct prod_name from Product"
		cursor.execute(command)
		result = cursor.fetchall()
		print("Reached Here")
		self.search_combo.clear()
		self.search_combo.setEditable(False)
		self.search_combo.addItem("---- Products ----")
		print("Reached Here")
		for r in result:
			if r[0] not in self.added:self.search_combo.addItem(r[0])


	def Get_Data(self):
		self.CustomerTableProd.clear()
		cursor = self.db.cursor()
		command = "select prod_name,product_type,Prod_price,QuantityInStock from Product"
		cursor.execute(command)
		result = cursor.fetchall()
		self.CustomerTableProd.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
		self.updatebox()

		for row_num, row_data in enumerate(result):

			self.CustomerTableProd.insertRow(row_num)
			for column_num, data in enumerate(row_data):
				self.CustomerTableProd.setItem(row_num, column_num, QTableWidgetItem(str(data)))

	def Disp_Data(self):
		try:
			cursor = self.db.cursor()
			product_val = self.search_combo.currentText()
			print(product_val)
			command="SELECT product_id, product_type, prod_name, QuantityInStock, prod_price, prod_Cond FROM product WHERE prod_name = '"+ product_val +"'"	
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
			self.CustProdType.setText(str(r2))
			self.CustProdName.setText(str(r3))
			self.CustQuanInStock.setText(str(r4))
			self.CustUnitPrice.setText(str(r5))
			self.CustRef.setText(str(r6))
		except:
			self.id_label.setText("N°")
			self.CustProdType.clear()
			self.CustProdName.clear()
			self.CustQuanInStock.clear()
			self.CustUnitPrice.clear()
			self.CustRef.clear()
			pass

	
	def CartTable(self):
		
		Total = self.Total

		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cartcursor = db.cursor()
		product_val = self.search_combo.currentText()
		print(product_val)
		command = "select product_id, prod_name, prod_price from Product where prod_name = '"+ product_val +"'"
		cartcursor.execute(command)
		result = cartcursor.fetchmany(1)
		print(result)
		result2=[]
		for item in result:
			print("Test")
			print (item)
			for x in item:
				print("Test2")
				print(x)
				result2.append(x)
		print("result2")
		print(result2)
		print("CusCartInv2")
		print(CusCartInv2)
		print("result2[0]")
		print(result2[0])
		print(result)
		CusCartInv2.append(result2[0])
		print(CusCartInv2)

		ProdQuan = self.CustQuanPurchased.text()
		ProdQuanInt = int(ProdQuan)
		result2.append(ProdQuan)
		print("result2 New")
		print(result2)

		command = "select prod_price from Product where prod_name = '"+ product_val +"'"
		cartcursor.execute(command)
		CostResultTup = cartcursor.fetchmany(1)
		print(CostResultTup)
		stri = ''
		for item in CostResultTup:
			print (item)
			for CostResultStr in item:
				print(CostResultStr)
		print(CostResultStr)
		CostResultint = int(CostResultStr)
		print(CostResultint)

		Total.append(CostResultint*ProdQuanInt)

		L = [result2[1:4]]
		CusCartInv.append(L)

		for row_num, row_data in enumerate(L):

			self.CheckOutTable.insertRow(row_num)
			for column_num, data in enumerate(row_data):
				self.CheckOutTable.setItem(row_num, column_num, QTableWidgetItem(str(data)))
				#CusCartInv[row_num] = QTableWidgetItem(str(data))
				#print (CusCartInv)

	def show_login(self):
		self.id_label.setText("N°")
		self.CustProdType.clear()
		self.CustProdName.clear()
		self.CustQuanInStock.clear()
		self.CustUnitPrice.clear()
		self.CustRef.clear()
		self.CustQuanPurchased.clear()
		widget.setCurrentIndex(0)
		widget.setFixedWidth(400)
		widget.setFixedHeight(500)


	def checkO(self):
		QuanInt = self.CustQuanPurchased.text()
		self.id_label.setText("N°")
		self.CustProdType.clear()
		self.CustProdName.clear()
		self.CustQuanInStock.clear()
		self.CustUnitPrice.clear()
		self.CustRef.clear()
		self.CustQuanPurchased.clear()

		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()
		allids=cursor.execute("select max(INV_ID) from INVOICE")
		newidtup = cursor.fetchone()
		newidstr = (''.join(str(x) for x in newidtup))
		if newidstr == "None":
			newidint = 1
		else:
			newidint = (int(newidstr)+int(1)) # To manulay insert the Primary Key if is int
		newidsrt = str(newidint)

		PayInIns = self.PayInIns

		Total = self.Total
		
	
		for product_val in CusCartInv2:
			
			product_valstr = str(product_val)
			command = "select prod_name, prod_price, QuantityInStock from Product where PRODUCT_ID = '"+ product_valstr +"'"
			cursor.execute(command)
			result1 = cursor.fetchmany(1)
			print(result1)

			r1 = result1[0][0] # Name
			r2 = result1[0][1] # Price
			r3 = result1[0][2] # QIS
			print(CusName)
			Cname = (''.join(str(x) for x in CusName))
			command = "select CanCheckOut, PaymentBalance from Customer where customername = '"+ Cname +"'"
			cursor.execute(command)
			result2 = cursor.fetchmany(1)
			print(result2)

			R11 = result2[0][0] # CanChack
			R11str = str(R11)
			R22 = result2[0][1] # Balance
			R22str = str(R22)

			
			if PayInIns.isChecked():
				Paymeth = "installments"
				CurrentDate = date.today()
				DateAgg = timedelta(365)
				FutureDate = CurrentDate + DateAgg
				CurrentDateStr = str(CurrentDate)
				FutureDateStr = str(FutureDate)
			else:
				Paymeth = "cash"
				CurrentDate = date.today()
				DateAgg = timedelta(365)
				FutureDate = CurrentDate
				CurrentDateStr = str(CurrentDate)
				FutureDateStr = str(FutureDate)

			Emplo = "ramzy"
			print(r3)
			print(QuanInt)
			x = r3 - int(QuanInt)
			print(x)
			if r3 - int(QuanInt) <= 0:
				QMessageBox.information(self,"Can't chack out","You oredered an excess amount of " + r1)
			else:
				Cname = (''.join(str(x) for x in CusName))
				tot = (''.join(str(x) for x in Total))
				print(newidsrt)
				newidsrtstr = str(newidsrt)
				print(Cname)
				Cnamestr = str(Cname)
				print(r1)
				r1str = str(r1)
				print(CurrentDateStr)
				CurrentDateStrStr = str(CurrentDateStr)
				print(FutureDateStr)
				FutureDateStrStr = str(FutureDateStr)
				print(r2)
				r2str = str(r2)
				print(Paymeth)
				Paymethstr = str(Paymeth)
				print(tot)
				totstr = str(tot)
				print(Emplo)
				Emplostr = str(Emplo)
				print(R11str)
				R11strStr = str(R11str)
				print(R22str)
				R22strStr = str(R22str)
				command = "INSERT INTO sample_database.INVOICE VALUES ('"+ newidsrtstr +"','"+ Cnamestr +"','"+ r1str +"','"+ CurrentDateStrStr +"','"+ FutureDateStrStr +"','"+ r2str +"','"+ Paymethstr +"','"+ totstr +"','"+ Emplostr +"','"+ R11strStr +"','"+ R22strStr +"')"
				cursor.execute(command)
				db.commit()
				QIS = int(r3) - int(1)
				QISstr = str(QIS)
				command = "UPDATE sample_database.PRODUCT SET QuantityInStock = '"+ QISstr +"' WHERE prod_name = '"+ r1str +"'"
				cursor.execute(command)
				db.commit()
				ChO = True
				noo = "No"
				oos = "OutOfStock"
				ins = "installments"
				unre = "Unreternable"


				cursor.execute("UPDATE sample_database.INVOICE SET PRICE = PRICE*1.2 WHERE (PAYMENT_METHOD = '"+ ins +"')&(PaymentInitial = '"+ CurrentDateStrStr +"')")
				db.commit()
				cursor.execute("UPDATE sample_database.INVOICE SET CanCheckOut = '"+ noo +"' WHERE (PaymentBalance <> 0)&(PaymentInitial = '"+ CurrentDateStrStr +"')")
				db.commit()
				cursor.execute("UPDATE sample_database.INVOICE SET PaymentInitial = PaymentFull/12 WHERE (PAYMENT_METHOD = '"+ ins +"')&(PaymentInitial = '"+ CurrentDateStrStr +"')")
				db.commit()
				cursor.execute("UPDATE sample_database.INVOICE SET PaymentBalance = PaymentFull-PaymentInitial WHERE (PAYMENT_METHOD = '"+ ins +"')&(PaymentInitial = '"+ CurrentDateStrStr +"')")
				db.commit()

				LoopSet = 0
				if PayInIns.isChecked():
					print("______Here is the CusCartIn2_____________")
					print(CusCartInv2)
					for row_data in enumerate(self.CusCartInv2):
						print("___rowData____")
						print(row_data)
						PlaceH = row_data[LoopSet]
						PlaceHstr = str(PlaceH)
						print(row_data)
						cursor.execute("UPDATE sample_database.Product SET Pay_Me_METH = '"+ ins +"' WHERE product_id = '"+ PlaceHstr +"'")
						LoopSet = LoopSet + 1
				else:
					for row_data in enumerate(self.CusCartInv2):
						print("___rowData____")
						print(row_data)
						print(row_data[1])
						print("---LoopSet---")
						print(LoopSet)
						print(row_data[LoopSet])
						PlaceH = row_data[LoopSet]
						print(PlaceH)
						PlaceHstr = str(PlaceH)
						cash ="Cash"
						cursor.execute("UPDATE sample_database.Product SET Pay_Me_METH = '"+ cash +"' WHERE product_id = '"+ PlaceHstr +"'")
						LoopSet = LoopSet + 1
				
				self.CustomerTableProd.clear()
				self.CheckOutTable.clear()
				CusCartInv2.clear()
				widget.setCurrentIndex(14)
				widget.setFixedWidth(1010)
				widget.setFixedHeight(1000)
#CusPro terminal END --------------------------------------------------------------------------------------------------------------------------------------------Done


#Cuscart terminal start --------------------------------------------------------------------------------------------------------------------------------------------Done
class CusCart(QDialog):#Customer Cart
	def __init__(self):
		super(CusCart,self).__init__()
		loadUi("ui_forms/CustCart.ui",self)
		self.CusCartInv = CusCartInv
		self.CusCartInv2 = CusCartInv2
		self.CartTable.setRowCount(10)
		self.CartTable.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
		self.CustomerCartBack.clicked.connect(self.Back)
		self.check_purchase.clicked.connect(self.checklist)
		self.CustConferm.clicked.connect(self.checkO)
		self.AdminPanLogOff.clicked.connect(self.show_login)
		self.Close.clicked.connect(self.close)
		


	def checklist(self):
		n=0
		m=0
		for row_num, row_data in enumerate(self.CusCartInv):

			self.CartTable.insertRow(row_num)
			for column_num, data in enumerate(row_data):
				self.CartTable.setItem(row_num, column_num, QTableWidgetItem(str(data)))
		self.CartTable.resizeColumnsToContents()

	def show_login(self):
		CusName.clear()
		widget.setCurrentIndex(0)
		widget.setFixedWidth(400)
		widget.setFixedHeight(500)


	def checkO(self):
		EmpCheck = self.checkBox

		


		widget.setCurrentIndex(14)
		widget.setFixedWidth(1010)
		widget.setFixedHeight(1000)

	def Back(self):
		widget.setCurrentIndex(12)
		widget.setFixedWidth(1900)
		widget.setFixedHeight(1200)
#Cuscart terminal END --------------------------------------------------------------------------------------------------------------------------------------------Done


#CusInv terminal start --------------------------------------------------------------------------------------------------------------------------------------------
class CusInv(QDialog):
	def __init__(self):
		super(CusInv,self).__init__()
		loadUi("ui_forms/CustInvoice.ui",self)
		self.CusCartInv = CusCartInv
		self.Total = Total
		self.CusName = CusName
		self.CusShopAgain.clicked.connect(self.Back2)
		self.AdminPanLogOff.clicked.connect(self.show_login)
		self.table_2.setRowCount(10)
		self.check_purchase.clicked.connect(self.checklist)
		y = 0
		for x in Total:
			y = x
		self.total.setText(str(y))
		self.Close.clicked.connect(self.close)

	def checklist(self):
		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()
		CurrentDate = date.today()
		CurrentDatestr = str(CurrentDate)
		Cname = (''.join(str(x) for x in CusName))
		command = "select * from INVOICE WHERE (CUS_NAME = '"+ Cname +"')&(PaymentInitial = '"+ CurrentDatestr +"')"
		cursor.execute(command)
		result = cursor.fetchall()
		print(result)

		self.table_2.setRowCount(0)

		for row_num, row_data in enumerate(result):

			self.table_2.insertRow(row_num)
			for column_num, data in enumerate(row_data):
				self.table_2.setItem(row_num, column_num, QTableWidgetItem(str(data)))

	def show_login(self):
		self.table_2.clearContents()
		self.Total.clear()
		widget.setCurrentIndex(0)
		widget.setFixedWidth(400)
		widget.setFixedHeight(500)


	def Back2(self):
		self.table_2.clearContents()
		widget.setCurrentIndex(12)
		widget.setFixedWidth(1900)
		widget.setFixedHeight(1200)
#CusInv terminal END --------------------------------------------------------------------------------------------------------------------------------------------

