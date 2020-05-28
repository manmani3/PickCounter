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

        self.listWidget = QListWidget()
        self.listWidget.setViewMode(QListWidget.IconMode)

        hBox = QHBoxLayout()
        hBox.addLayout(leftVBox)
        hBox.addWidget(self.listWidget)
        self.setLayout(hBox)

        self.setWindowTitle('PickCounter')
        self.setGeometry(200, 200, 500, 300)

    # get All Champion name/image from official LoL site
    def getAllChampDatas(self): {

    }

    def updateRecommendChampions(self, champList):
        # self.listWidget.clear()
        for i in range(0, 5):
            champList[i].save('image'+str(self.index)+str(i)+'.png')
            item = QListWidgetItem()
            item.setText('champ' + str(i))
            icon = QIcon()
            icon.addPixmap(QPixmap('image'+str(i)+'.png'))
            item.setIcon(icon)
            self.listWidget.addItem(item)

    def onApplyBtnClick(self):
        import UiCapture
        ourBanList, ourPickList, yourBanList, yourPickList = UiCapture.cropImages(UiCapture.captureClient())

        try:
            self.index = 0
            self.updateRecommendChampions(ourBanList)
            self.index = 1
            self.updateRecommendChampions(ourPickList)
            self.index = 2
            self.updateRecommendChampions(yourBanList)
            self.index = 3
            self.updateRecommendChampions(yourPickList)
        except Exception as ex:
            print('updateRecommendChampions', ex)
        # ourBanList, ourPickList, yourBanList, yourPickList \
        #     = self.getChampNames(ourBanList, ourPickList, yourBanList, yourPickList)

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
