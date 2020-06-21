# exe파일 만들기 : pyinstaller UiDialog.spec

import sys
import os

from PyQt5.QtGui import QIcon, QPixmap, QFontDatabase
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, \
    QListWidget, QListWidgetItem, QTextEdit, QRadioButton, QLayout

import LoLSocketClient

from os import walk

import LoLTemplateMatch
import LolData
import UiCapture

class UiDialog(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(30, 220, 550, 600)
        self.setStyleSheet("background-color: #FFFFFF;")

        fontDB = QFontDatabase()
        fontDB.addApplicationFont('NanumSquareB.ttf')
        fontDB.addApplicationFont('NanumSquareEB.ttf')

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

        label_notice = QLabel('※ 주의사항 ※', self)
        font1 = label_notice.font()
        font1.setPointSize(19)
        font1.setBold(True)
        font1.setFamily("나눔스퀘어 ExtraBold")
        label_notice.setStyleSheet('color:#DF3A01')
        label_notice.setFont(font1)

        label_sub_notice = QLabel('하기의 내용을 반드시 숙지 후 프로그램을 실행하십시오.')
        font2 = label_sub_notice.font()
        font2.setPointSize(14)
        font2.setFamily("나눔스퀘어 ExtraBold")
        label_sub_notice.setFont(font2)
        label_sub_notice.setStyleSheet('color:#DF3A01')

        description1 = QLabel(' 1. 클라이언트 해상도는 1280x720을 권장', self)
        font = description1.font()
        font.setPointSize(10.5)
        font.setFamily("나눔스퀘어 Bold")
        description1.setFont(font)
        description1.setStyleSheet('color:#DF3A01')

        description2 = QLabel(' 2. 추천받고 싶은 Position을 선택하고 본인의 닉네임을 입력하세요.', self)
        description2.setFont(font)
        description2.setStyleSheet('color:#DF3A01')

        description3 = QLabel(' 3. 본인의 픽 순서가 되었을때 Apply 버튼을 클릭해 주세요.\n' +
                              '  잠시 후에 추천 순위 리스트가 나타납니다.\n\n', self)

        description3.setFont(font)
        description3.setStyleSheet('color:#DF3A01')


        totalBox = QVBoxLayout()
        totalBox.addWidget(label_notice)
        totalBox.addWidget(label_sub_notice)
        totalBox.addWidget(description1)
        totalBox.addWidget(description2)
        totalBox.addWidget(description3)

        totalBox.addLayout(hBox)
        '''
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.red)
        self.setPalette(p)
        '''

        self.setLayout(totalBox)
        self.setWindowTitle('PickCounter')
        relativePath = 'assets\\PC_icon2.png'
        self.setWindowIcon(QIcon(self.resource_path(relativePath)))


    def updateRecommendChampions(self, champList):
        self.listWidget.clear()

        rank = 1
        try:
            for champ in champList:
                champId = LolData.getChampionId(champ['name'])
                print('\nchamp:', champ['name'], "(", champId, ")")
                for (dirpath, dirnames, filenames) in walk('.\\assets\\'):
                    for filename in filenames:
                        if str(champId) == filename.split('_')[1].split('.')[0]:
                            item = QListWidgetItem()

                            champName = QLabel(champ['name'])
                            champNameFont = champName.font()
                            champNameFont.setBold(True)
                            champName.setFont(champNameFont)
                            text = 'score:' + str(round(champ['score'], 4)) +\
                                   '\nO:' + str(round(champ['O'], 4)) + '\nM:' + str(round(champ['M'], 4)) +\
                                   '\nC:' + str(round(champ['C'], 4))

                            vl = QVBoxLayout()
                            vl.addWidget(champName)
                            vl.addWidget(QLabel(text))

                            widget = QWidget()
                            widgetLayout = QHBoxLayout()

                            rankText = QLabel(str(rank) + ') ')
                            rankFont = rankText.font()
                            rankFont.setPointSize(20)
                            rankFont.setBold(True)
                            rankText.setFont(rankFont)

                            widgetLayout.addWidget(rankText)
                            relativePath = 'assets\\' + filename
                            pixmap = QPixmap(self.resource_path(relativePath))

                            smaller_pixmap = pixmap.scaled(75, 75)
                            img = QLabel()
                            img.setPixmap(smaller_pixmap)
                            widgetLayout.addWidget(img)
                            widgetLayout.addLayout(vl)
                            widgetLayout.addStretch()

                            widgetLayout.setSizeConstraint(QLayout.SetFixedSize)
                            widget.setLayout(widgetLayout)
                            item.setSizeHint(widget.sizeHint())

                            self.listWidget.addItem(item)
                            self.listWidget.setItemWidget(item, widget)
                            rank = rank + 1
                            break
                    break

        except Exception as e:
            print('updateRecommendChampions error`', e)

    def onApplyBtnClick(self):
        try:
            self.listWidget.clear()
            item = QListWidgetItem()
            item.setText('서버에서 데이터를 가져오는 중...')
            self.listWidget.addItem(item)

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
            ourPickList, yourPickList, ourBanList, yourBanList = UiCapture.cropImages(UiCapture.captureClient()) # [81, 350], [105, 523, 53], [1, 2, 3, 4, 5], [6, 7, 8, 9, 10]

            # classify images to champion info
            ourPickList = LoLTemplateMatch.matching(ourPickList)
            yourPickList = LoLTemplateMatch.matching(yourPickList)
            ourBanList = LoLTemplateMatch.matching(ourBanList)
            yourBanList = LoLTemplateMatch.matching(yourBanList)

            recommendList = LoLSocketClient.requestRecommendChampionList(position, summonerName, ourPickList, yourPickList,
                                                                         ourBanList, yourBanList)
        except Exception as e:
            print(str(e))

        self.updateRecommendChampions(recommendList)
        self.listWidget.raise_()
        self.listWidget.activateWindow()

        print('final result\n', recommendList)

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UiDialog()
    ui.show()
    sys.exit(app.exec_())
