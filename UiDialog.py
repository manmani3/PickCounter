from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PIL import ImageGrab
import win32gui


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

    def onApplyBtnClick(self):
        ourBanList, ourPickList, yourBanList, yourPickList = self.cropImages(self.captureClient())
        ourBanList, ourPickList, yourBanList, yourPickList \
            = self.getChampNames(ourBanList, ourPickList, yourBanList, yourPickList)

        

    # return ImageFile
    def captureClient(self):
        client = win32gui.FindWindow(None, r'League of Legends')
        win32gui.SetForegroundWindow(client)
        dimensions = win32gui.GetWindowRect(client)
        capture = ImageGrab.grab(dimensions)
        width, height = capture.size
        return capture, width, height

    # return 4 Array<ImageFile>
    def cropImages(self, imageFile, width, height):
        pickPos1600 = [83, 144, 50, 50]
        banPos1600 = [20, 40, 33, 33]

        #testvalue
        pickPosTest = [0, 0, 50, 50]
        banPosTest = [0, 0, 33, 33]

        ourPicks, ourBans, yourPicks, yourBans = []
        pickMargin, banMargin = 0

        if width == 1600 and height == 900:
            pickPos = pickPos1600
            banPos = banPos1600
        else :
            #window size not found #testvalue
            pickPos = pickPosTest
            banPos = banPosTest

        for i in range(0, 5) :
            pickPos[1] = pickPos[1] + pickMargin #margin added START_Y
            banPos[0] = banPos[0] + banMargin #margin added START_X

            ourPicks[i] = imageFile.crop((pickPos[0], pickPos[1], pickPos[2], pickPos[3]))
            ourBans[i] = imageFile.crop((banPos[0], banPos[1], banPos[2], banPos[3]))
            #yourPicks[i] = client.crop(()) #? need to check position
            #yourBans[i] = client.crop(())
        return ourPicks, ourBans, yourPicks, yourBans

    # return 4 Array<String>
    def getChampNames(self, ourBanList, ourPickList, yourBanList, yourPickList): {

    }

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
