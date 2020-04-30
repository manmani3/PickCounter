from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap

class Ui_Dialog(object):
    def __init__(self):
        self.label = QtWidgets.QLabel(Dialog)
        self.pushButton = QtWidgets.QPushButton(Dialog)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 471)
        self.pushButton.setGeometry(QtCore.QRect(30, 420, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onApplyBtnClick)

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

    def onApplyBtnClick(self): {
        # TODO :

    }

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
