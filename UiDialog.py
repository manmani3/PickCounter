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
            icon = QIcon()
            icon.addPixmap(QPixmap('C:\\Users\\YunJeongHyeon\\Pictures\\suninatas\\0.PNG'))
            item.setIcon(icon)
            listWidget.addItem(item)

        hBox = QHBoxLayout()
        hBox.addLayout(leftVBox)
        hBox.addWidget(listWidget)
        self.setLayout(hBox)

        self.setWindowTitle('PickCounter')
        self.setGeometry(200, 200, 400, 500)

    # get All Champion name/image from official LoL site
    def getAllChampDatas(self): {

    }

    def onApplyBtnClick(self):
        ourBanList, ourPickList, yourBanList, yourPickList = self.cropImages(self.captureClient())
        ourBanList, ourPickList, yourBanList, yourPickList \
            = self.getChampNames(ourBanList, ourPickList, yourBanList, yourPickList)

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
