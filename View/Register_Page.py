
from PyQt5 import QtCore, QtWidgets

import View.GUI.Login_Page_icons_rc
from View.GUI.Login_Page_customized import PasswordEdit


class RegisterPage(QtWidgets.QWidget):
    """Basic login form.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_ui()

    def setup_ui(self):
        """Setup the login form.
        """
        self.resize(480, 825)
        # remove the title bar
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setStyleSheet(
            """
            QPushButton {
                border-style: outset;
                border-radius: 0px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #cf7500;
                border-style: inset;
            }
            QPushButton:pressed {
                background-color: #ffa126;
                border-style: inset;
            }
            """
        )

        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()

        self.widget = QtWidgets.QWidget(self)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget.setStyleSheet(".QWidget{background-color: rgb(20, 20, 40);}")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(9, 0, 0, 0)

        self.Login_PageCloseButton = QtWidgets.QPushButton(self.widget)
        self.Login_PageCloseButton.setMinimumSize(QtCore.QSize(35, 25))
        self.Login_PageCloseButton.setMaximumSize(QtCore.QSize(35, 25))
        self.Login_PageCloseButton.setStyleSheet("color: white;\n"
                                        "font: 13pt \"Verdana\";\n"
                                        "border-radius: 1px;\n"
                                        "opacity: 200;\n")
        self.Login_PageCloseButton.clicked.connect(self.close)
        self.verticalLayout_2.addWidget(self.Login_PageCloseButton, 0, QtCore.Qt.AlignRight)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 15, -1, -1)

        self.RegisterPage_label_StackPNG = QtWidgets.QLabel(self.widget)
        self.RegisterPage_label_StackPNG.setMinimumSize(QtCore.QSize(100, 150))
        self.RegisterPage_label_StackPNG.setMaximumSize(QtCore.QSize(150, 150))
        self.RegisterPage_label_StackPNG.setStyleSheet("image: url(:/icons/icons/StackOverFlow.png);")
        self.verticalLayout_3.addWidget(self.RegisterPage_label_StackPNG, 0, QtCore.Qt.AlignHCenter)

        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setContentsMargins(50, 35, 59, -1)

        self.RegisterPage_label_UsernamePNG = QtWidgets.QLabel(self.widget)
        self.RegisterPage_label_UsernamePNG.setStyleSheet("color: rgb(231, 231, 231);\n"
                                   "font: 15pt \"Verdana\";")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.RegisterPage_label_UsernamePNG)

        self.RegisterPage_lineEdit_UsernameInput = QtWidgets.QLineEdit(self.widget)
        self.RegisterPage_lineEdit_UsernameInput.setMinimumSize(QtCore.QSize(0, 40))
        self.RegisterPage_lineEdit_UsernameInput.setPlaceholderText("Username...") 
        self.RegisterPage_lineEdit_UsernameInput.setStyleSheet("QLineEdit {\n"
                                    "color: rgb(231, 231, 231);\n"
                                    "font: 15pt \"Verdana\";\n"
                                    "border: None;\n"
                                    "border-bottom-color: white;\n"
                                    "border-radius: 10px;\n"
                                    "padding: 0 8px;\n"
                                    "background: rgb(20, 20, 40);\n"
                                    "selection-background-color: darkgray;\n"
                                    "}")
        self.RegisterPage_lineEdit_UsernameInput.setFocus(True)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.RegisterPage_lineEdit_UsernameInput)

        self.RegisterPage_label_MailPNG = QtWidgets.QLabel(self.widget)
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.RegisterPage_label_MailPNG)

        self.RegisterPage_label_PasswordPNG = QtWidgets.QLabel(self.widget)
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.RegisterPage_label_PasswordPNG)

        self.RegisterPage_label_PasswordAgainPNG = QtWidgets.QLabel(self.widget)
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.RegisterPage_label_PasswordAgainPNG)
        
        self.RegisterPage_lineEdit_EmailInput = QtWidgets.QLineEdit(self.widget)
        self.RegisterPage_lineEdit_EmailInput.setMinimumSize(QtCore.QSize(0, 40))
        self.RegisterPage_lineEdit_EmailInput.setPlaceholderText("Email...")
        self.RegisterPage_lineEdit_EmailInput.setStyleSheet("QLineEdit {\n"
                                      "color: rgb(231, 231, 231);\n"
                                      "font: 15pt \"Verdana\";\n"
                                      "border: None;\n"
                                      "border-bottom-color: white;\n"
                                      "border-radius: 10px;\n"
                                      "padding: 0 8px;\n"
                                      "background: rgb(20, 20, 40);\n"
                                      "selection-background-color: darkgray;\n"
                                      "}")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.RegisterPage_lineEdit_EmailInput)
              
        self.RegisterPage_lineEdit_passwordInput = PasswordEdit(self.widget)
        self.RegisterPage_lineEdit_passwordInput.setMinimumSize(QtCore.QSize(0, 40))
        self.RegisterPage_lineEdit_passwordInput.setPlaceholderText("Password...")
        self.RegisterPage_lineEdit_passwordInput.setStyleSheet("QLineEdit {\n"
                                      "color: orange;\n"
                                      "font: 15pt \"Verdana\";\n"
                                      "border: None;\n"
                                      "border-bottom-color: white;\n"
                                      "border-radius: 10px;\n"
                                      "padding: 0 8px;\n"
                                      "background: rgb(20, 20, 40);\n"
                                      "selection-background-color: darkgray;\n"
                                      "}")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.RegisterPage_lineEdit_passwordInput)
        self.RegisterPage_lineEdit_passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        
        
        self.RegisterPage_lineEdit_password_againInput = PasswordEdit(self.widget)
        self.RegisterPage_lineEdit_password_againInput.setMinimumSize(QtCore.QSize(0, 40))
        self.RegisterPage_lineEdit_password_againInput.setPlaceholderText("Password again...")
        self.RegisterPage_lineEdit_password_againInput.setStyleSheet("QLineEdit {\n"
                                      "color: orange;\n"
                                      "font: 15pt \"Verdana\";\n"
                                      "border: None;\n"
                                      "border-bottom-color: white;\n"
                                      "border-radius: 10px;\n"
                                      "padding: 0 8px;\n"
                                      "background: rgb(20, 20, 40);\n"
                                      "selection-background-color: darkgray;\n"
                                      "}")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.RegisterPage_lineEdit_password_againInput)
        self.RegisterPage_lineEdit_password_againInput.setEchoMode(QtWidgets.QLineEdit.Password)
        
        
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setStyleSheet("border: 2px solid white;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line)

        self.line_2 = QtWidgets.QFrame(self.widget)
        self.line_2.setStyleSheet("border: 2px solid orange;")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.line_2)

        self.line_3 = QtWidgets.QFrame(self.widget)
        self.line_3.setStyleSheet("border: 2px solid white;")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.line_3)

        self.line_4 = QtWidgets.QFrame(self.widget)
        self.line_4.setStyleSheet("border: 2px solid orange;")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.line_4)
        
        self.RegisterButton = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RegisterButton.sizePolicy().hasHeightForWidth())

        self.RegisterButton.setSizePolicy(sizePolicy)
        self.RegisterButton.setMinimumSize(QtCore.QSize(0, 60))
        self.RegisterButton.setAutoFillBackground(False)
        self.RegisterButton.setStyleSheet("color: rgb(231, 231, 231);\n"
                                      "font: 17pt \"Verdana\";\n"
                                      "border: 2px solid orange;\n"
                                      "padding: 5px;\n"
                                      "border-radius: 3px;\n"
                                      "opacity: 200;\n"
                                      "")
        self.RegisterButton.setAutoDefault(True)
        self.formLayout_2.setWidget(10, QtWidgets.QFormLayout.SpanningRole, self.RegisterButton)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(8, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.verticalLayout_3.addLayout(self.formLayout_2)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.horizontalLayout_3.addWidget(self.widget)
        self.horizontalLayout_3.setStretch(0, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.Login_PageCloseButton.setText(_translate("Form", "X"))
        self.RegisterPage_label_UsernamePNG.setText(_translate(
            "Form",
            "<html><head/><body><p><img src=\":/icons/icons/user_32x32.png\"/></p></body></html>"))
        self.RegisterPage_label_PasswordPNG.setText(_translate(
            "Form",
            "<html><head/><body><p><img src=\":/icons/icons/lock_32x32.png\"/></p></body></html>"))
        
        self.RegisterPage_label_PasswordAgainPNG.setText(_translate(
            "Form",
            "<html><head/><body><p><img src=\":/icons/icons/lock_32x32.png\"/></p></body></html>"))
        
        self.RegisterPage_label_MailPNG.setText(_translate(
            "Form",
            "<html><head/><body><p><img src=\":/icons/icons/mail_32x32.png\"/></p></body></html>"))
        self.RegisterButton.setText(_translate("Form", "Register me!"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login_form = RegisterPage()
    login_form.show()

    sys.exit(app.exec_())
