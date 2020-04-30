# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel


class Ui_Dialog(object):
    def __init__(self):
        self.label = QtWidgets.QLabel(Dialog)
        self.pushButton = QtWidgets.QPushButton(Dialog)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 471)
        self.pushButton.setGeometry(QtCore.QRect(30, 420, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onApplyBtnClick())

        self.label.setGeometry(QtCore.QRect(150, 100, 201, 231))
        self.label.setText("")
        self.label.setObjectName("label")

        # https://wikidocs.net/38038
        pixmap = QPixmap('C:\\Users\\YunJeongHyeon\\Pictures\\suninatas\\0.PNG')
        self.label.setPixmap(pixmap.scaled(self.label.size(), QtCore.Qt.IgnoreAspectRatio))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Apply"))

    def onApplyBtnClick(self):
        # TODO :

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
