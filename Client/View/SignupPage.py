import json

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi

from Client.View.LoginPage import LoginScreen
from Client.client import requestFactory


class CreateAccScreen(QDialog):
    def __init__(self, widget):
        super(CreateAccScreen, self).__init__()
        self.widget = widget
        loadUi("E:/Network Project/Stackoverflow/Client/View/ui/signup.ui", self)
        self.passwordLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confrimPasswordLE.setEchoMode(QtWidgets.QLineEdit.Password)
        self.signupButton.clicked.connect(self.signupFunction)

    def signupFunction(self):
        firstName = self.firstNameLE.text()
        lastName = self.lastNameLE.text()
        email = self.emailLE.text()
        username = self.usernameLE.text()
        password = self.passwordLE.text()
        confirmPassword = self.confrimPasswordLE.text()

        if len(firstName) == 0 or len(lastName) == 0 or len(username) == 0 or len(email) == 0 or len(
                password) == 0 or len(confirmPassword) == 0:
            self.errorLabel.setText("Please fill in all inputs.")
        elif password != confirmPassword:
            self.errorLabel.setText("Passwords do not match.")
        else:
            user = json.dumps({"firstName": firstName, "lastName": lastName, "email": email, "username": username,
                               "password": password, "questions": [], "answers": []})
            registered = requestFactory("UserBL╪insertUser╪{}".format(user), 0)
            if registered == '1':
                print("Successfully signup.")
                self.errorLabel.setText("")
                gotoLogin(self.widget)
            else:
                self.errorLabel.setText("There is a user with this profile")


def gotoLogin(widget):
    login = LoginScreen(widget)
    widget.addWidget(login)
    widget.setCurrentIndex(widget.currentIndex() + 1)
