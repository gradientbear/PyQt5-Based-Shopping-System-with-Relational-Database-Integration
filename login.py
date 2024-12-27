import mysql.connector as con
from PyQt5.QtWidgets import QDialog, QMessageBox, QInputDialog
from PyQt5.uic import loadUi
from main import widget, CusName, DatabaseConfig
from datetime import date


#Log In terminal Start --------------------------------------------------------------------------------------------------------------------------------------------Done
class LoginApp(QDialog):
	def __init__(self):
		super(LoginApp,self).__init__()
		loadUi("ui_forms/login-form.ui",self)
		self.LogInButton.clicked.connect(self.login)
		self.LogInRegisterButton.clicked.connect(self.show_reg)
		self.CusName = CusName
		self.Close.clicked.connect(self.close)

	def login(self):
		UserName = self.LogInUser.text()
		PassWord = self.LogInPassword.text()
		EmpCheck = self.EmpCheckBoxLog

		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()
		if EmpCheck.isChecked():
			cursor.execute("select employee_name, employee_pass from Employees where employee_name = '"+ UserName +"' and employee_pass = '"+ PassWord +"'")
			result = cursor.fetchone()
			self.LogInUser.setText("")
			self.LogInPassword.setText("")
			if result:
				QMessageBox.information(self,"Welcome Back","You Sucessuly Logged In")
				self.show_adminpan()
			else:
				QMessageBox.information(self,"Failed to Log In","Please Sign up through the register button.")
		else:
			cursor.execute("select customername, customer_pass from Customer where customername = '"+ UserName +"' and customer_pass = '"+ PassWord +"'")
			result = cursor.fetchone()
			self.LogInUser.setText("")
			self.LogInPassword.setText("")
			if result:
				CusName.append(UserName)
				QMessageBox.information(self,"Welcome Back","You Sucessuly Logged In")
				self.show_CustomerBench()
			else:
				QMessageBox.information(self,"Failed to Log In","Please Sign up through the register button.")
	
	def show_reg(self):
		widget.setCurrentIndex(1)
		widget.setFixedWidth(400)
		widget.setFixedHeight(500)

	def show_adminpan(self):
		widget.setCurrentIndex(2)
		widget.setFixedWidth(800)
		widget.setFixedHeight(600)

	def show_CustomerBench(self):
		widget.setCurrentIndex(12)
		widget.setFixedWidth(1900)
		widget.setFixedHeight(1200)
#Log In terminal End --------------------------------------------------------------------------------------------------------------------------------------------Done


#Registratuion terminal start --------------------------------------------------------------------------------------------------------------------------------------------Done
class RegApp(QDialog):
	def __init__(self):
		super(RegApp,self).__init__()

		loadUi("ui_forms/Register-form.ui",self)
		
		self.RegisterConfermButton.clicked.connect(self.fun)
		self.RegisterLogInPageButton.clicked.connect(self.show_login)
		self.Close.clicked.connect(self.close)

	def fun(self):
		if self.EmpCheckBox.isChecked():
			text, ok = QInputDialog.getText(self, 'Passcode', 'Enter registration passcode:')
			if ok and text=='1234':
				self.reg(True)
				return
			else:
				QMessageBox.information(self,"Failed to Register","Please try again.")
				return
		else:
			self.reg(False)
			return
	def reg(self,regcode=False):
		AddID = self.RegisterAdress.text()
		UserName = self.RegisterUserName.text()
		PassWord = self.RegisterPassword.text()
		Email = self.RegisterEmail.text()
		PhoneNum = self.RegisterNumber.text()

		db = con.connect(host=DatabaseConfig["host"], user = DatabaseConfig["user"], password = DatabaseConfig["password"], database = DatabaseConfig["database"])
		cursor = db.cursor()
		if regcode:
			cursor.execute("select * from Employees where employee_email = '"+ Email +"'")
			result = cursor.fetchone()
			self.RegisterAdress.setText("")
			self.RegisterUserName.setText("")
			self.RegisterPassword.setText("")
			self.RegisterEmail.setText("")
			self.RegisterNumber.setText("")
			if result:
				QMessageBox.information(self,"Oops","You already registed with that Email")
			else:
				allids=cursor.execute("select max(employee_id) from Employees")
				newidtup = cursor.fetchone()
				newidint = (int((''.join(str(x) for x in newidtup)))+int(1)) # To manulay insert the Primary Key if is int
				newidsrt = str(newidint)
				Null = "null"
				Delivery = "Delivery"
				cursor.execute("insert into Employees values( '"+ newidsrt +"' ,'"+ AddID +"','"+ UserName +"',1,'"+ Delivery +"','"+ PassWord +"','"+ Email +"','"+ PhoneNum +"','"+ Null +"')")
				db.commit()


				QMessageBox.information(self,"Welcome!!","You Registered Sucessfully as an Employee")
		else:
			cursor.execute("select * from Customer where customer_email = '"+ Email +"'")
			result = cursor.fetchone()
			self.RegisterAdress.setText("")
			self.RegisterUserName.setText("")
			self.RegisterPassword.setText("")
			self.RegisterEmail.setText("")
			self.RegisterNumber.setText("")
			if result:
				QMessageBox.information(self,"Oops","You already registed with that Email")
			else:
				allids=cursor.execute("select max(customer_id) from Customer")
				newidtup = cursor.fetchone()
				newidint = (int((''.join(str(x) for x in newidtup)))+int(1)) # To manulay insert the Primary Key if is int
				newidsrt = str(newidint)
				Null = "null"
				CurrentDate = date.today()
				CurrentDateStr = str(CurrentDate)
				Y = "YES"
				cursor.execute("insert into Customer values( '"+ newidsrt +"' ,'"+ AddID +"','"+ UserName +"','"+ PassWord +"','"+ Email +"','"+ PhoneNum +"','"+ CurrentDateStr +"','"+ Y +"',0)")
				db.commit()


				QMessageBox.information(self,"Welcome!!","You Registered Sucessfully a Cutomer")


	def show_login(self):
		CusName.clear()
		widget.setCurrentIndex(0)
		widget.setFixedWidth(400)
		widget.setFixedHeight(500)
#Registratuion terminal END --------------------------------------------------------------------------------------------------------------------------------------------Done

