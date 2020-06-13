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
        self.setGeometry(100, 100, 600, 500)
        self.setStyleSheet("background-color: #FFFFFF;")
        positionLabel = QLabel('추천받을 포지션')
        titleFont = positionLabel.font()
        titleFont.setPointSize(19)
        titleFont.setBold(True)
        titleFont.setFamily("나눔스퀘어 ExtraBold")
        positionLabel.setFont(titleFont)
        positionLabel.setStyleSheet('color:#1428a0')

        self.topRadioButton = QRadioButton('TOP', self)
        self.jungleRadioButton = QRadioButton('JUNGLE', self)
        self.midRadioButton = QRadioButton('MID', self)
        self.adcRadioButton = QRadioButton('ADC', self)
        self.supportRadioButton = QRadioButton('SUPPORT', self)

        positionFont = positionLabel.font()
        positionFont.setPointSize(16)
        positionFont.setBold(True)
        positionFont.setItalic(True)
        positionFont.setFamily("나눔스퀘어 ExtraBold")

        self.topRadioButton.setFont(positionFont)
        self.jungleRadioButton.setFont(positionFont)
        self.midRadioButton.setFont(positionFont)
        self.adcRadioButton.setFont(positionFont)
        self.supportRadioButton.setFont(positionFont)

        self.topRadioButton.setStyleSheet('color:#FFFFFF;'
                                          'background-color:#8A2BE2;')
        self.jungleRadioButton.setStyleSheet('color:#FFFFFF;'
                                             'background-color:#9400D3;')
        self.midRadioButton.setStyleSheet('color:#FFFFFF;'
                                          'background-color:#9932CC;')
        self.adcRadioButton.setStyleSheet('color:#FFFFFF;'
                                          'background-color:#8B008B;')
        self.supportRadioButton.setStyleSheet('color:#FFFFFF;'
                                              'background-color:#6A5ACD;')

        titleFont.setItalic(False)

        idDescription = QLabel("당신의 닉네임을 입력하세요.", self)
        idDescription.move(100, 20)
        titleFont.setPointSize(15)
        idDescription.setFont(titleFont)
        idDescription.setStyleSheet('color:#1428a0')

        champListLable = QLabel('챔피언 추천 순위')
        titleFont.setPointSize(19)
        champListLable.setFont(titleFont)
        champListLable.setStyleSheet('color:#1428a0')

        self.summonerNameField = QTextEdit()
        self.summonerNameField.setMaximumHeight(35)
        self.summonerNameField.setMaximumWidth(250)
        titleFont.setPointSize(14)
        self.summonerNameField.setFont(titleFont)
        self.summonerNameField.setStyleSheet('color:#ff4c4c')

        applyButton = QPushButton('Apply')
        applyButton.setFont(titleFont)
        applyButton.setMaximumWidth(125)
        applyButton.setStyleSheet('color:#FFFFFF;'
                                  'background-color:#483D8B;')
        # 'background-color:#DC143C;')
        applyButton.clicked.connect(self.onApplyBtnClick)

        leftVBox = QVBoxLayout()
        leftVBox.addWidget(positionLabel)
        leftVBox.addWidget(self.topRadioButton)
        leftVBox.addWidget(self.jungleRadioButton)
        leftVBox.addWidget(self.midRadioButton)
        leftVBox.addWidget(self.adcRadioButton)
        leftVBox.addWidget(self.supportRadioButton)
        leftVBox.addStretch(1)
        leftVBox.addWidget(idDescription)
        leftVBox.addWidget(self.summonerNameField)
        leftVBox.addStretch(1)
        leftVBox.addWidget(applyButton)

        self.listWidget = QListWidget()
        self.listWidget.setViewMode(QListWidget.IconMode)

        rightVBox = QVBoxLayout()
        rightVBox.addWidget(champListLable)
        rightVBox.addWidget(self.listWidget)

        hBox = QHBoxLayout()
        hBox.addLayout(leftVBox)
        hBox.addStretch(1)
        hBox.addLayout(rightVBox)
        hBox.addStretch(1)

        description = QLabel('※ 주의사항 ※', self)
        font1 = description.font()
        font1.setPointSize(19)
        font1.setBold(True)
        font1.setFamily("나눔스퀘어 ExtraBold")
        description.setStyleSheet('color:#DF3A01')
        description.setFont(font1)

        description2 = QLabel('하기의 내용을 반드시 숙지 후 프로그램을 실행하십시오.')
        font2 = description2.font()
        font2.setPointSize(14)
        font2.setFamily("나눔스퀘어 ExtraBold")
        description2.setFont(font2)
        description2.setStyleSheet('color:#DF3A01')

        description3 = QLabel(' 1. 본인의 챔피언을 미리 선택하지 마시고 빈칸으로 두십시오.', self)
        font3 = description3.font()
        font3.setPointSize(10.5)
        # font3.setBold(True)
        font3.setFamily("나눔스퀘어 Bold")
        description3.setFont(font3)
        description3.setStyleSheet('color:#DF3A01')

        description4 = QLabel(' 2. 추천받고 싶은 Position을 선택하고 본인의 닉네임을 입력하세요.', self)
        description4.setFont(font3)
        description4.setStyleSheet('color:#DF3A01')

        description5 = QLabel(' 3. 본인의 차례가 되었을때 Apply 버튼을 클릭해주세요\n', self)
        description5.setFont(font3)
        description5.setStyleSheet('color:#DF3A01')

        totalBox = QVBoxLayout()
        totalBox.addWidget(description)
        totalBox.addWidget(description2)
        totalBox.addWidget(description3)
        totalBox.addWidget(description4)
        totalBox.addWidget(description5)

        totalBox.addLayout(hBox)

        self.setLayout(totalBox)
        self.setWindowTitle('PickCounter')
        self.setWindowIcon(QIcon("PC_icon2.png"))

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
