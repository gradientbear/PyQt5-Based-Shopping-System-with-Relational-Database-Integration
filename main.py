import sys
import mysql.connector as con # for connecting to the database in postgresql
from PyQt5.QtWidgets import QApplication, QStackedWidget
from login import LoginApp, RegApp
from admin_customer import AdminCust_1, AdminCust_2, AdminCust_3
from admin_product import AdmProduct_1, AdmProduct_2, AdmProduct_3
from admin_supplier import Admsuppliers_1, Admsuppliers_2, Admsuppliers_3
from admin_panel import AdmPan
from customer import CusPro, CusCart, CusInv

CusCartInv = []
CusCartInv2 = []
CusName = []
Total = []
DatabaseConfig = {
    "host" : "localhost",
    "user" : "root",
    "password" : "admin1",
    "database" : "sample_1database"
}
#Program initialization --------------------------------------------------------------------------------------------------------------------------------------------
app = QApplication(sys.argv)		
widget = QStackedWidget()
loginform = LoginApp()
registrationform = RegApp()
AdminPanel = AdmPan()
AdmPro_1 = AdmProduct_1()
AdmPro_2 = AdmProduct_2()
AdmPro_3 = AdmProduct_3()
AdmSup_1 = Admsuppliers_1()
AdmSup_2 = Admsuppliers_2()
AdmSup_3 = Admsuppliers_3()
AdmCus_1 = AdminCust_1()
AdmCus_2 = AdminCust_2()
AdmCus_3 = AdminCust_3()
CustoPro = CusPro()
CustoCart = CusCart()
CustoInv = CusInv()
widget.addWidget(loginform) 	   #index 0
widget.addWidget(registrationform) #index 1
widget.addWidget(AdminPanel) 	   #index 2
widget.addWidget(AdmPro_1)	   	   #index 3
widget.addWidget(AdmPro_2)	   	   #index 4	
widget.addWidget(AdmPro_3)	   	   #index 5	
widget.addWidget(AdmSup_1)	   	   #index 6
widget.addWidget(AdmSup_2)	   	   #index 7	
widget.addWidget(AdmSup_3)	   	   #index 8
widget.addWidget(AdmCus_1)	   	   #index 9
widget.addWidget(AdmCus_2)	   	   #index 10	
widget.addWidget(AdmCus_3)	   	   #index 11
widget.addWidget(CustoPro)		   #index 12
widget.addWidget(CustoCart)		   #index 13
widget.addWidget(CustoInv)		   #index 14
widget.setCurrentIndex(0)

widget.setFixedSize(400,500)
widget.show()

app.exec_()