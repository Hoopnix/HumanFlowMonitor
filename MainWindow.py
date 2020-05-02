from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
import sys
import cv2
from packages import detector, yolo
import threading
import json
import time
import numpy
from os import remove
from PIL import Image


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        self.varInit()
        self.form = MainWindow
        window.setWindowFlags(Qt.FramelessWindowHint)  # 无边框及标题栏
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)

        MainWindow.setStyleSheet("background-color: rgb(9, 13, 40);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(80, 190, 900, 600))
        self.graphicsView.setAutoFillBackground(True)
        self.graphicsView.setStyleSheet("background-color: rgb(27, 30, 68);")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.Box)
        self.graphicsView.setFrameShadow(QtWidgets.QFrame.Plain)
        self.graphicsView.setLineWidth(0)
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1120, 190, 400, 250))
        self.label.setAutoFillBackground(False)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./layout/res/todayData.png"))
        self.label.setObjectName("label")
        self.history = QtWidgets.QLabel(self.centralwidget)
        self.history.setGeometry(QtCore.QRect(1120, 540, 400, 250))
        self.history.setAutoFillBackground(False)
        self.history.setText("")
        self.history.setPixmap(QtGui.QPixmap("./layout/res/historyData.png"))
        self.history.setObjectName("history")
        self.legend = QtWidgets.QLabel(self.centralwidget)
        self.legend.setGeometry(QtCore.QRect(1319, 100, 201, 40))
        self.legend.setAutoFillBackground(False)
        self.legend.setText("")
        self.legend.setPixmap(QtGui.QPixmap("./layout/res/legend.png"))
        self.legend.setObjectName("legend")
        self.topbar = QtWidgets.QLabel(self.centralwidget)
        self.topbar.setGeometry(QtCore.QRect(0, 0, 1600, 80))
        self.topbar.setAutoFillBackground(False)
        self.topbar.setText("")
        self.topbar.setPixmap(QtGui.QPixmap("./layout/res/titleBg.png"))
        self.topbar.setObjectName("topbar")
        self.logoCQUPT = QtWidgets.QLabel(self.centralwidget)
        self.logoCQUPT.setGeometry(QtCore.QRect(64, 20, 40, 40))
        self.logoCQUPT.setAutoFillBackground(True)
        self.logoCQUPT.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.logoCQUPT.setLineWidth(0)
        self.logoCQUPT.setText("")
        self.logoCQUPT.setPixmap(QtGui.QPixmap("./layout/res/cqupt.png"))
        self.logoCQUPT.setObjectName("logoCQUPT")
        self.logoNMID = QtWidgets.QLabel(self.centralwidget)
        self.logoNMID.setGeometry(QtCore.QRect(130, 20, 40, 40))
        self.logoNMID.setAutoFillBackground(True)
        self.logoNMID.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.logoNMID.setLineWidth(0)
        self.logoNMID.setText("")
        self.logoNMID.setPixmap(QtGui.QPixmap("./layout/res/nmid.png"))
        self.logoNMID.setObjectName("logoNMID")
        self.todayIn = QtWidgets.QLabel(self.centralwidget)
        self.todayIn.setGeometry(QtCore.QRect(1270, 275, 120, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.todayIn.setFont(font)
        self.todayIn.setAutoFillBackground(False)
        self.todayIn.setStyleSheet("color: rgb(195, 42, 252);\n"
                                   "background-color: rgba(255, 255, 255, 0);")
        self.todayIn.setAlignment(QtCore.Qt.AlignCenter)
        self.todayIn.setObjectName("todayIn")
        self.todayOut = QtWidgets.QLabel(self.centralwidget)
        self.todayOut.setGeometry(QtCore.QRect(1270, 345, 120, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(28)
        self.todayOut.setFont(font)
        self.todayOut.setAutoFillBackground(False)
        self.todayOut.setStyleSheet("color: rgb(41, 187, 255);\n"
                                    "background-color: rgba(255, 255, 255, 0);")
        self.todayOut.setAlignment(QtCore.Qt.AlignCenter)
        self.todayOut.setObjectName("todayOut")
        self.historyIn = QtWidgets.QLabel(self.centralwidget)
        self.historyIn.setGeometry(QtCore.QRect(1270, 630, 120, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(28)
        self.historyIn.setFont(font)
        self.historyIn.setAutoFillBackground(False)
        self.historyIn.setStyleSheet("color: rgb(195, 42, 252);\n"
                                     "background-color: rgba(255, 255, 255, 0);")
        self.historyIn.setAlignment(QtCore.Qt.AlignCenter)
        self.historyIn.setObjectName("historyIn")
        self.historyOut = QtWidgets.QLabel(self.centralwidget)
        self.historyOut.setGeometry(QtCore.QRect(1270, 695, 120, 35))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(28)
        self.historyOut.setFont(font)
        self.historyOut.setAutoFillBackground(False)
        self.historyOut.setStyleSheet("color: rgb(41, 187, 255);\n"
                                      "background-color: rgba(255, 255, 255, 0);")
        self.historyOut.setAlignment(QtCore.Qt.AlignCenter)
        self.historyOut.setObjectName("historyOut")
        self.setting = QtWidgets.QPushButton(self.centralwidget)
        self.setting.setGeometry(QtCore.QRect(1456, 24, 36, 36))
        self.setting.setAutoFillBackground(False)
        self.setting.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.setting.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./layout/res/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("./layout/res/setting.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.setting.setIcon(icon)
        self.setting.setIconSize(QtCore.QSize(32, 32))
        self.setting.setObjectName("setting")
        self.setting.clicked.connect(self.jump)
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(1536, 24, 36, 36))
        self.exit.setAutoFillBackground(False)
        self.exit.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.exit.setText("")
        self.exit.clicked.connect(self.closeApp)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./layout/res/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon1)
        self.exit.setIconSize(QtCore.QSize(32, 32))
        self.exit.setObjectName("exit")
        MainWindow.setCentralWidget(self.centralwidget)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pool = []
        self.loadRecordData()
        self.loadSettings()
        self.createThread()

    def varInit(self):
        self.isClose = 0
        self.writeLock = 0
        self.cap = cv2.VideoCapture(0)

    def closeApp(self):
        self.isClose = 1
        self.recordData['todayin'] = 0
        self.recordData['todayout'] = 0
        self.recordData['today'] = 0
        with open('./config/recordData.json', 'w') as f:
            json.dump(self.recordData, f)
        self.form.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人流量数据监控实报系统"))
        self.todayIn.setText(_translate("MainWindow", "0"))
        self.todayOut.setText(_translate("MainWindow", "0"))
        self.historyIn.setText(_translate("MainWindow", "0"))
        self.historyOut.setText(_translate("MainWindow", "0"))

    def loadRecordData(self):
        with open('./config/recordData.json', 'r') as f:
            self.recordData = json.load(f)

    def loadSettings(self):
        with open('./config/settings.json', 'r') as f:
            self.settings = json.load(f)

    def jump(self):
        self.form.hide()
        form1 = settingDialog()
        ui = settingDialog()
        ui.setupUi(form1)
        form1.exec_()
        self.form.show()

    def createThread(self):
        threadUpdateUI = threading.Thread(target=self.updateUI)
        threadDetect = threading.Thread(target=self.detect, args=[self.settings['algorithm']])
        threadDetect.start()
        threadUpdateUI.start()

    def updateUI(self):
        pass

    def detect(self, method):
        line = [self.settings['line1'], self.settings['line2']]
        if method == 'hogsvm':
            while not self.isClose:
                # frame = Image.open('./cache/' + str(self.pool[0]) + '.jpg')
                # num, frame = detector.hogSvmDetector(frame, num)
                # cv2.imwrite('./cache/image.jpg', frame)
                pass
        else:
            cap = cv2.VideoCapture(0)
            detector = yolo.YOLO()
            while not self.isClose:
                ret, image = cap.read()
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = Image.fromarray(image)
                # image = Image.open('E:/Database/mall_dataset_backup/frames/seq_000' + str(f) + '.jpg')
                image, box = detector.detect_image(image)
                image.save('./cache/detected.jpg')
                if len(box):
                    for i in box[:][0]:
                        if line[0] < i < line[1]:
                            self.recordData['todayin'] += 1
                            self.recordData['historyin'] += 1
                self.graphicsView.setStyleSheet("border-image: url({});".format('./cache/detected.jpg'))
                self.historyIn.setText(str(self.recordData['historyin']))
                self.todayIn.setText(str(self.recordData['todayin']))


class settingDialog(QtWidgets.QDialog):
    def setupUi(self, settingDialog):
        self.dialog = settingDialog
        self.dialog.setWindowModality(Qt.WindowModal)
        self.loadSettings()
        settingDialog.setWindowFlags(Qt.FramelessWindowHint)
        settingDialog.setObjectName("settingDialog")
        settingDialog.resize(400, 300)
        settingDialog.setStyleSheet("background-color: rgb(9, 13, 40);")
        self.algoSelect = QtWidgets.QLabel(settingDialog)
        self.algoSelect.setGeometry(QtCore.QRect(30, 60, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.algoSelect.setFont(font)
        self.algoSelect.setAutoFillBackground(False)
        self.algoSelect.setStyleSheet("background-color: rgb(36, 36, 77, 0);\n"
                                      "")
        self.algoSelect.setText("")
        self.algoSelect.setPixmap(QtGui.QPixmap("./layout/res/settingsBg.png"))
        self.algoSelect.setAlignment(QtCore.Qt.AlignCenter)
        self.algoSelect.setObjectName("algoSelect")
        self.threshold = QtWidgets.QLabel(settingDialog)
        self.threshold.setGeometry(QtCore.QRect(30, 120, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.threshold.setFont(font)
        self.threshold.setStyleSheet("background-color: rgb(36, 36, 77, 0);")
        self.threshold.setText("")
        self.threshold.setPixmap(QtGui.QPixmap("./layout/res/settingsBg.png"))
        self.threshold.setAlignment(QtCore.Qt.AlignCenter)
        self.threshold.setObjectName("threshold")
        self.label = QtWidgets.QLabel(settingDialog)
        self.label.setGeometry(QtCore.QRect(30, 180, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: rgb(36, 36, 77, 0);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./layout/res/settingsBg.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(settingDialog)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(settingDialog)
        self.label_3.setGeometry(QtCore.QRect(30, 180, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(settingDialog)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                   "color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.exit = QtWidgets.QPushButton(settingDialog)
        self.exit.setGeometry(QtCore.QRect(353, 15, 32, 32))
        self.exit.setAutoFillBackground(False)
        self.exit.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./layout/res/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit.setIcon(icon)
        self.exit.setIconSize(QtCore.QSize(32, 32))
        self.exit.setObjectName("exit")
        self.exit.clicked.connect(self.closeDialog)
        self.svm = QtWidgets.QCheckBox(settingDialog)
        self.svm.setGeometry(QtCore.QRect(160, 60, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.svm.setFont(font)
        self.svm.setStyleSheet("color: rgb(255, 255, 255);\n"
                               "background-color: rgba(255, 255, 255, 0);")
        self.svm.setObjectName("svm")
        if self.config['algorithm'] == 'svm':
            self.svm.setChecked(True)
        else:
            self.svm.setChecked(False)
        self.svm.clicked.connect(lambda: self.algorithmSelect('svm'))
        self.YOLO = QtWidgets.QCheckBox(settingDialog)
        self.YOLO.setGeometry(QtCore.QRect(270, 60, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.YOLO.setFont(font)
        self.YOLO.setStyleSheet("color: rgb(255, 255, 255);\n"
                                "background-color: rgba(255, 255, 255, 0);")
        if self.config['algorithm'] == 'YOLO':
            self.YOLO.setChecked(True)
        else:
            self.YOLO.setChecked(False)
        self.YOLO.setObjectName("YOLO")
        self.YOLO.clicked.connect(lambda: self.algorithmSelect('YOLO'))
        self.label_5 = QtWidgets.QLabel(settingDialog)
        self.label_5.setGeometry(QtCore.QRect(270, 260, 80, 20))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
                                   "background-color: rgba(255, 255, 255, 0);")
        self.label_5.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(settingDialog)
        self.label_7.setGeometry(QtCore.QRect(150, 180, 200, 30))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("./layout/res/settingsBgLong.png"))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(settingDialog)
        self.label_8.setGeometry(QtCore.QRect(150, 120, 200, 30))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("./layout/res/settingsBgLong.png"))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(settingDialog)
        self.label_9.setGeometry(QtCore.QRect(150, 60, 200, 30))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("./layout/res/settingsBgLong.png"))
        self.label_9.setObjectName("label_9")
        self.line1 = QtWidgets.QLineEdit(settingDialog)
        self.line1.setGeometry(QtCore.QRect(150, 120, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.line1.setFont(font)
        self.line1.setAutoFillBackground(False)
        self.line1.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgba(255, 255, 255, 0);")
        self.line1.setAlignment(QtCore.Qt.AlignCenter)
        self.line1.setObjectName("line1")
        self.line2 = QtWidgets.QLineEdit(settingDialog)
        self.line2.setGeometry(QtCore.QRect(260, 120, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.line2.setFont(font)
        self.line2.setAutoFillBackground(False)
        self.line2.setStyleSheet("color: rgb(255, 255, 255);\n"
                                 "background-color: rgba(255, 255, 255, 0);")
        self.line2.setAlignment(QtCore.Qt.AlignCenter)
        self.line2.setObjectName("line2")
        self.fps = QtWidgets.QLineEdit(settingDialog)
        self.fps.setGeometry(QtCore.QRect(150, 180, 200, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.fps.setFont(font)
        self.fps.setAutoFillBackground(False)
        self.fps.setStyleSheet("color: rgb(255, 255, 255);\n"
                               "background-color: rgba(255, 255, 255, 0);")
        self.fps.setAlignment(QtCore.Qt.AlignCenter)
        self.fps.setObjectName("fps")
        self.algoSelect.raise_()
        self.threshold.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.exit.raise_()
        self.label_5.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.svm.raise_()
        self.YOLO.raise_()
        self.line1.raise_()
        self.line2.raise_()
        self.fps.raise_()

        self.retranslateUi(settingDialog)
        QtCore.QMetaObject.connectSlotsByName(settingDialog)

    def retranslateUi(self, settingDialog):
        _translate = QtCore.QCoreApplication.translate
        settingDialog.setWindowTitle(_translate("settingDialog", "Dialog"))
        self.label_2.setText(_translate("settingDialog", "算法选择"))
        self.label_3.setText(_translate("settingDialog", "插帧频率"))
        self.label_4.setText(_translate("settingDialog", "检测阈值"))
        self.svm.setText(_translate("settingDialog", "HoG+SVM"))
        self.YOLO.setText(_translate("settingDialog", "YOLO"))
        self.label_5.setText(_translate("settingDialog", "v 1.0.0"))
        self.line1.setText(_translate("settingDialog", str(self.config['line1'])))
        self.line2.setText(_translate("settingDialog", str(self.config['line2'])))
        self.fps.setText(_translate("settingDialog", str(self.config['sampleRate'])))

    def algorithmSelect(self, algo):
        if algo == 'svm':
            self.YOLO.setChecked(False)
            self.svm.setChecked(True)
            self.config['algorithm'] = 'svm'
        else:
            self.YOLO.setChecked(True)
            self.svm.setChecked(False)
            self.config['algorithm'] = 'YOLO'

    def loadSettings(self):
        with open('./config/settings.json', 'r') as f:
            self.config = json.load(f)

    def saveSettings(self):
        with open('./config/settings.json', 'w') as f:
            json.dump(self.config, f)

    def closeDialog(self):
        self.config['line1'] = int(self.line1.text())
        self.config['line2'] = int(self.line2.text())
        self.config['sampleRate'] = int(self.fps.text())
        self.saveSettings()
        self.dialog.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Ui_MainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
