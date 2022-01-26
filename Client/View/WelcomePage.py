from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Client.View.LoginPage import LoginScreen
from Client.View.SignupPage import CreateAccScreen


class WelcomeScreen(QDialog):
    def __init__(self, widget):
        super(WelcomeScreen, self).__init__()
        loadUi("D:\\My Works\\Projects\\Python Projects\\Project StackOverFlow\\Stackoverflow\\Client\\View\\ui\\welcome.ui",
               self)
        self.login.clicked.connect(lambda: gotoLogin(widget))
        self.create.clicked.connect(lambda: gotoCreate(widget))


def gotoLogin(widget):
    login = LoginScreen(widget)
    widget.addWidget(login)
    widget.setCurrentIndex(widget.currentIndex() + 1)


def gotoCreate(widget):
    create = CreateAccScreen(widget)
    widget.addWidget(create)
    widget.setCurrentIndex(widget.currentIndex() + 1)
