from PyQt5.QtWidgets import QDialog
from PyQt5.uic import loadUi


class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("E:/Network Project/Stackoverflow/Client/View/ui/MainWindow.ui", self)
