from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import AutoCropAlertDialog
import AutoCropCore
import sys

class Ui_MainWindow(object):

    def __init__(self):
        self.core = None

    def setupUi(self, MainWindow) :
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 100)
        self.initComponents(MainWindow)
        self.initLayout()
        self.initConnect()

    def initComponents(self,MainWindow):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.csvFileLabel = QtWidgets.QLabel("CSV File")
        self.csvFilePathLine = QtWidgets.QLineEdit()
        self.csvFilePathLine.setReadOnly(True)

        self.finalFolderLabel = QtWidgets.QLabel("Final Folder")
        self.finalFolderPathLine = QtWidgets.QLineEdit()
        self.finalFolderPathLine.setReadOnly(True)

        self.checkHeaderBox = QtWidgets.QCheckBox("CSV has got a header ?")

        self.croppingBtn = QtWidgets.QPushButton("Crop")

    def initLayout(self) :
        self.vbox = QtWidgets.QVBoxLayout(self.centralwidget)

        self.hbox1 = QtWidgets.QHBoxLayout()
        self.hbox2 = QtWidgets.QHBoxLayout()
        self.hbox3 = QtWidgets.QHBoxLayout()

        self.hbox1.addWidget(self.csvFileLabel)
        self.hbox1.addWidget(self.csvFilePathLine)

        self.hbox2.addWidget(self.finalFolderLabel)
        self.hbox2.addWidget(self.finalFolderPathLine)

        self.hbox3.addWidget(self.checkHeaderBox)
        self.hbox3.addWidget(self.croppingBtn)

        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)

    def initConnect(self):
        self.csvFilePathLine.selectionChanged.connect(self.openFile)
        self.finalFolderPathLine.selectionChanged.connect(self.openFinalFolder)
        self.croppingBtn.clicked.connect(self.didTapOnCrop)
        self.checkHeaderBox.stateChanged.connect(self.changeHeader)

    def setCore(self, core) :
        self.core = core

    def openFile(self) :
        fname = QtWidgets.QFileDialog.getOpenFileName(None, "Select the csv file","/", filter="*.csv")
        if isinstance(fname,tuple) :
            self.csvFilePathLine.setText(fname[0])
            self.core.sendCSVPath(fname[0])

    def openFinalFolder(self) :
        fname = QtWidgets.QFileDialog.getExistingDirectory(None, "Select the final Folder", "/")
        if fname :
            self.finalFolderPathLine.setText(fname)
            self.core.sendFinalFolder(fname)

    def changeHeader(self) :
        self.core.sendChangeHeader(bool(self.checkHeaderBox.checkState()))

    def didTapOnCrop(self) :
        self.core.startCropping()

    def showAlert(self, message) :
        u_dialog = QtWidgets.QDialog()
        dialog = AutoCropAlertDialog.AutoCropAlertDialog(u_dialog, message)
        u_dialog.exec_()



if __name__ == "__main__" :
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    core = AutoCropCore.AutoCropCore()
    ui.setupUi(MainWindow)
    ui.setCore(core)
    core.setView(ui)
    MainWindow.show()
    sys.exit(app.exec_())
