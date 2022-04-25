from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

class AutoCropAlertDialog(QtWidgets.QDialog) :

    def __init__(self, dialog, message=""):
        self.dialog = dialog
        self.message = message
        self.initComponents()
        self.initLayout()

    def initComponents(self) :
        self.messageLabel = QtWidgets.QLabel(self.message)

    def initLayout(self) :
        self.vbox = QtWidgets.QVBoxLayout(self.dialog)

        self.vbox.addWidget(self.messageLabel)
