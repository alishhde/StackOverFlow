import sys
from PyQt5 import QtWidgets
# from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QDialog, QApplication, QInputDialog, QListWidgetItem, QMessageBox, QPushButton

# Import UIs
import Client.View.Login_Page
import Client.View.Register_Page


# ---------------------------------------- Main Code Start ---------------------------------------- #

class Main:
    def __init__(self):
        self.register_page = Client.View.Register_Page.RegisterPage()
        self.login_page = Client.View.Login_Page.LoginPage()
        self.login_page.show()

        self.login_page.RegisterButton.clicked.connect(self.show_register_page)

    def show_register_page(self):
        self.login_page.hide()
        self.register_page.show()

    def __str__(self):
        pass


# ---------------------------------------- Main Code End   ---------------------------------------- #

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    sys.exit(app.exec_())
