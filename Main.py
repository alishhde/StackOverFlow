import sys

import Login_Page
import Register_Page
import DataBase.Sqlite3_module

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem, QMessageBox, QPushButton

# ---------------------------------------- Main Code Start ---------------------------------------- #

class Main():
    def __init__(self):
        self.loginpage = Login_Page.LoginPage()
        self.loginpage.show()
        
        self.loginpage.RegisterButton.clicked.connect(self.showRegisterPage)
        
    
    def showRegisterPage(self):
        self.registerpage = Register_Page.RegisterPage()
        self.loginpage.hide()
        self.registerpage.show()
    
    def __str__(self):
        pass


# ---------------------------------------- Main Code End   ---------------------------------------- #


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())