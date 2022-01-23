# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AskQ.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(542, 522)
        Form.setStyleSheet("background-color: rgb(54, 64, 82)")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 521, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.StckLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.StckLabel.setFont(font)
        self.StckLabel.setStyleSheet("color: rgb(10, 148, 254);\n"
"font: 20pt \"MV Boli\" ;\n"
"font-weight: bold;\n"
"")
        self.StckLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StckLabel.setObjectName("StckLabel")
        self.verticalLayout.addWidget(self.StckLabel)
        self.AskQuestionPage_plainTextEdit = QtWidgets.QPlainTextEdit(Form)
        self.AskQuestionPage_plainTextEdit.setGeometry(QtCore.QRect(30, 140, 491, 191))
        self.AskQuestionPage_plainTextEdit.setMaximumSize(QtCore.QSize(1100, 16777215))
        self.AskQuestionPage_plainTextEdit.setObjectName("AskQuestionPage_plainTextEdit")
        self.PostQuestion_button = QtWidgets.QPushButton(Form)
        self.PostQuestion_button.setGeometry(QtCore.QRect(190, 420, 165, 50))
        self.PostQuestion_button.setMinimumSize(QtCore.QSize(165, 50))
        self.PostQuestion_button.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.PostQuestion_button.setFont(font)
        self.PostQuestion_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.PostQuestion_button.setStyleSheet("background-color: rgb(10, 149, 255);\n"
"color: rgb(255, 255, 255);\n"
"border: 5px;")
        self.PostQuestion_button.setObjectName("PostQuestion_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.StckLabel.setText(_translate("Form", "Stack Over Flow"))
        self.AskQuestionPage_plainTextEdit.setPlainText(_translate("Form", "enter your question "))
        self.PostQuestion_button.setText(_translate("Form", "Post"))

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())