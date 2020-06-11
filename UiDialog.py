import sys

from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QListView, \
    QListWidget, QListWidgetItem, QTextEdit, QRadioButton

import LoLSocketClient
import LoLTemplateMatch

from os import walk
import LolData


class UiDialog(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.topRadioButton = QRadioButton('TOP', self)
        self.jungleRadioButton = QRadioButton('JUNGLE', self)
        self.midRadioButton = QRadioButton('MID', self)
        self.adcRadioButton = QRadioButton('ADC', self)
        self.supportRadioButton = QRadioButton('SUPPORT', self)

        idDescription = QLabel()
        idDescription.setText('input ID')

        self.summonerNameField = QTextEdit()
        self.summonerNameField.setMaximumHeight(30)
        print(self.summonerNameField.height())

        applyButton = QPushButton()
        applyButton.setText('Apply')
        applyButton.clicked.connect(self.onApplyBtnClick)

        leftVBox = QVBoxLayout()

        leftVBox.addWidget(self.topRadioButton)
        leftVBox.addWidget(self.jungleRadioButton)
        leftVBox.addWidget(self.midRadioButton)
        leftVBox.addWidget(self.adcRadioButton)
        leftVBox.addWidget(self.supportRadioButton)

        leftVBox.addWidget(idDescription)

        leftVBox.addWidget(self.summonerNameField)

        leftVBox.addWidget(applyButton)

        self.listWidget = QListWidget()
        self.listWidget.setViewMode(QListWidget.IconMode)

        hBox = QHBoxLayout()
        hBox.addLayout(leftVBox)
        hBox.addWidget(self.listWidget)

        description = QLabel()
        description.setText('This is guide')
        font = description.font()
        font.setPointSize(30)
        font.setBold(True)
        font.setFamily('Times New Roman')
        description.setFont(font)

        totalBox = QVBoxLayout()
        totalBox.addWidget(description)
        totalBox.addLayout(hBox)

        self.setLayout(totalBox)

        self.setWindowTitle('PickCounter')
        self.setGeometry(100, 100, 600, 500)

    def updateRecommendChampions(self, champList):
        self.listWidget.clear()

        try:
            for champ in champList:
                champId = LolData.getChampionId(champ['name'])
                print('\nchamp:', champ['name'], "(", champId, ")")
                for (dirpath, dirnames, filenames) in walk('.\\assets\\champion\\'):
                    for filename in filenames:
                        if str(champId) == filename.split('_')[1].split('.')[0]:
                            item = QListWidgetItem()
                            text = champ['name'] + ' / score:' + str(champ['score']) + '\nO:' + str(champ['O']) + \
                                   '\nGm:' + str(champ['Gm']) + '\nGy:' + str(champ['Gy']) + '\nM:' + str(champ['M'])
                            print(text)
                            item.setText(text)
                            icon = QIcon()
                            icon.addPixmap(QPixmap('.\\assets\\champion\\' + filename))
                            item.setIcon(icon)
                            self.listWidget.addItem(item)
                            break
                    break

        except Exception as e:
            print('error', e)

        '''
        for i in range(0, 5):
            champList[i].save('.\\data\\image' + str(self.index) + str(i) + '.png')
            item = QListWidgetItem()
            item.setText('champ' + str(i))
            icon = QIcon()
            icon.addPixmap(QPixmap('.\\data\\image' + str(self.index) + str(i) + '.png'))
            item.setIcon(icon)
            self.listWidget.addItem(item)
        '''

    def onApplyBtnClick(self):
        import UiCapture
        # TODO : remove
        '''
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
            
        # classify images to champion info
        ourPickList = LoLTemplateMatch.matching(ourPickList)
        yourPickList = LoLTemplateMatch.matching(yourPickList)
        ourBanList = LoLTemplateMatch.matching(ourBanList)
        yourBanList = LoLTemplateMatch.matching(yourBanList)
        '''

        summonerName = self.summonerNameField.toPlainText()

        position = 'NONE'
        if self.topRadioButton.isChecked():
            position = 'TOP'
        elif self.jungleRadioButton.isChecked():
            position = 'JUNGLE'
        elif self.midRadioButton.isChecked():
            position = 'MID'
        elif self.adcRadioButton.isChecked():
            position = 'ADC'
        elif self.supportRadioButton.isChecked():
            position = 'SUPPORT'

        # Test
        ourPickList, yourPickList, ourBanList, yourBanList = [81, 350, 122, 245], [64, 266, 105, 523, 53], [1], [3]

        recommendList = LoLSocketClient.requestRecommendChampionList(position, summonerName, ourPickList, yourPickList,
                                                                     ourBanList, yourBanList)

        self.updateRecommendChampions(recommendList)

        print('final result\n', recommendList)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UiDialog()
    ui.show()
    sys.exit(app.exec_())
