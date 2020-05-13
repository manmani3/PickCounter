import sys
from io import BytesIO

import requests
import win32gui
from PIL import ImageGrab, Image
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QListView, \
    QListWidget, QListWidgetItem


class UiDialog(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        description = QLabel()
        description.setText('This is guide')

        applyButton = QPushButton()
        applyButton.setText('Apply')
        applyButton.clicked.connect(self.onApplyBtnClick)

        leftVBox = QVBoxLayout()
        leftVBox.addWidget(description)
        leftVBox.addWidget(applyButton)

        listWidget = QListWidget()
        listWidget.setViewMode(QListWidget.IconMode)

        for i in range(0, 3):
            item = QListWidgetItem()
            item.setText('Garen' + str(i))
            icon = QIcon()
            icon.addPixmap(self.getChampImage('tmp'))
            item.setIcon(icon)
            listWidget.addItem(item)

        hBox = QHBoxLayout()
        hBox.addLayout(leftVBox)
        hBox.addWidget(listWidget)
        self.setLayout(hBox)

        self.setWindowTitle('PickCounter')
        self.setGeometry(200, 200, 500, 300)

    def getChampImage(self, name):
        return QPixmap('C:\\Users\\YunJeongHyeon\\Pictures\\suninatas\\0.PNG')

    # get All Champion name/image from official LoL site
    def getAllChampDatas(self): {

    }

    def onApplyBtnClick(self):
        ourBanList, ourPickList, yourBanList, yourPickList = self.cropImages(self.captureClient(), 1600, 900)
        ourBanList, ourPickList, yourBanList, yourPickList \
            = self.getChampNames(ourBanList, ourPickList, yourBanList, yourPickList)

    # return ImageFile
    def captureClient(self):
        client = win32gui.FindWindow(None, 'PickCounter') #r'League of Legends')

        win32gui.SetForegroundWindow(client)
        dimensions = win32gui.GetWindowRect(client)
        print(dimensions)

        capture = ImageGrab.grab(bbox=(dimensions[0], dimensions[1], dimensions[2], dimensions[3]))
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

    # paremeters : 4 Array<ImageFile>
    # return : 4 Array<String>
    def getChampNames(self, ourBanList, ourPickList, yourBanList, yourPickList):
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UiDialog()
    ui.show()
    sys.exit(app.exec_())
