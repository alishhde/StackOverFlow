from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Client.View.MainWindow import MainWindow
from Client.client import requestFactory


class LoginScreen(QDialog):
    def __init__(self, widget):
        super(LoginScreen, self).__init__()
        self.widget = widget
        loadUi("E:/Network Project/Stackoverflow/Client/View/ui/login.ui", self)
        self.passwordLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginFunction)

    def loginFunction(self):
        username = self.usernameLE.text()
        password = self.passwordLE.text()

        if len(username) == 0 or len(password) == 0:
            self.error.setText("Please input all fields.")
        else:
            accepted = requestFactory("UserBL╪verifyUser╪{}╪{}".format(username, password))
            if accepted is '1':
                print("Successfully logged in.")
                self.error.setText("")
                # gotoMainWindow(self.widget)
            else:
                self.error.setText("Invalid username or password")


def gotoMainWindow(widget):
    mainWindow = MainWindow()
    widget.setFixedHeight(850)
    widget.setFixedWidth(1578)
    widget.addWidget(mainWindow)
    widget.setCurrentIndex(widget.currentIndex() + 1)
