from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi
from main import widget, CusName

#AdminPanel terminal start --------------------------------------------------------------------------------------------------------------------------------------------Done
class AdmPan(QDialog):#AdminPanel
	def __init__(self):
		super(AdmPan,self).__init__()
		loadUi("ui_forms/AdminPanel.ui",self)
		self.AdminEditSup.clicked.connect(self.adminsup)
		self.AdminEditPro.clicked.connect(self.adminpro)
		self.AdminEditCus.clicked.connect(self.admincus)
		self.AdminPanLogOff.clicked.connect(self.show_login)
		self.Close.clicked.connect(self.close)

	def show_login(self):
		CusName.clear()
		widget.setCurrentIndex(0)
		widget.setFixedWidth(400)
		widget.setFixedHeight(500)

	def adminsup(self):
		widget.setCurrentIndex(6)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(625)

	def adminpro(self):
		widget.setCurrentIndex(3)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(625)

	def admincus(self):
		widget.setCurrentIndex(9)
		widget.setFixedWidth(1100)
		widget.setFixedHeight(625)
#AdminPanel terminal END --------------------------------------------------------------------------------------------------------------------------------------------Done

