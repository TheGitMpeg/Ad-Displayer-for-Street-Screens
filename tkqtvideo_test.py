#Internal module(s)
import os
import sys
from colorama import Fore, Back, Style, init
from time import sleep
from PyQt5 import QtWidgets, QtMultimediaWidgets, QtGui, QtCore, QtWebEngineWidgets, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

#Modules
print("Starting the application...")
print("Importing modules...")
import webbrowser
init()
#Variables
#No internal variables!
#Window class and definitions
def count_3secs_GRJT(timerInSeconds):
    while timerInSeconds:
        minutes, seconds = divmod(timerInSeconds, 60)
        timerInThreeSecondsFmt = "{:2d}:{:02d}".format(minutes, seconds)
        print("Exiting in:", timerInThreeSecondsFmt, end="\r")
        sleep(1)
        timerInSeconds -= 1
    print(Back.BLUE + Fore.LIGHTWHITE_EX + "Program has been ended automatically by pressing the button and waiting some seconds." + Style.RESET_ALL)
    sys.exit(0)
class initializeAppGUIWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print("Ready.")
        #GUI window
        self.resize(640, 480)
        self.setMinimumWidth(640)
        self.setMinimumHeight(360)
        self.setMaximumWidth(1280)
        self.setMaximumHeight(720)
        self.setWindowTitle("A video playback window.")
        gridApplicationLayout = QGridLayout(self)
        self.setLayout(gridApplicationLayout)
        videoPlaybackLabelApplication = QLabel("No video has been opened!", self)
#        videoPlaybackLabelApplication.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        gridApplicationLayout.addWidget(videoPlaybackLabelApplication, 0, 0)
        videoItemWidgetApp = QVideoWidget()
        openVideoApplication = QAction("Open video", self)
        openVideoApplication.setStatusTip("Open a video from your PC.\nAccepted formats are MP4, OGG and WEBM.")
        openVideoApplication.triggered.connect(self.openAVideoDialog)
        exitApplication = QAction("Exit", self)
        exitApplication.triggered.connect(self.mainButtonFunctionalityQuit)
#        menuApplicationBar = self.menuBar()
#        fileMenuApplicationBar = menuApplicationBar.addMenu("&File")
#        fileMenuApplicationBar.addAction(openVideoApplication)
#        fileMenuApplicationBar.addAction(exitApplication)
    def mainButtonFunctionalityQuit(self):
        print(Back. BLUE + Fore.LIGHTWHITE_EX + "Program has been ended by pressing the button." + Style.RESET_ALL)
        sys.exit(0)
    def openAVideoDialog(self):
        importVideoDialog = QFileDialog.getOpenFileName(self, "Open a video", "", "MP4 Videos (*.mp4);;OGG Videos (*.ogg);;WEBM Videos (*.webm)")
        if importVideoDialog != "":
            self.videoItemWidgetApp.setMedia(QMediaContent(QUrl.fromLocalFile(importVideoDialog)))
class initializeRemoteControl(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(240, 360)
        self.setMinimumWidth(180)
        self.setMinimumHeight(300)
        self.setMaximumWidth(320)
        self.setMaximumHeight(360)
        self.setWindowTitle("Virtual Control")
        labelOfRemoteControl1 = QLabel("Remote Control", self)
        labelOfRemoteControl2 = QLabel("Remote Control", self)
        exitBtn = QPushButton(self)
        exitBtn.setText("EXIT")
        exitBtn.setStyleSheet("""font-family: "Inter", "Argentum Sans", "Montserrat", "Nunito Sans", "Frutiger", "Helvetica Neue", "Helvetica", "Arial", system-ui; font-size: 14px; background-color: firebrick; color: white;""")
        abBtn = QPushButton(self)
        abBtn.setText("About")
        abBtn.setStyleSheet("""font-family: "Inter", "Argentum Sans", "Montserrat", "Nunito Sans", "Frutiger", "Helvetica Neue", "Helvetica", "Arial", system-ui; font-size: 14px; background-color: white; color: black;""")
        abBtn.clicked.connect(mainButtonFunctionality5)
        remoteControlGrid = QGridLayout()
        self.setLayout(remoteControlGrid)
        remoteControlGrid.addWidget(labelOfRemoteControl1, 0, 0)
        remoteControlGrid.setColumnStretch(0, 6)
        remoteControlGrid.addWidget(abBtn, 2, 0)
        remoteControlGrid.setColumnStretch(0, 2)
        remoteControlGrid.addWidget(exitBtn, 2, 1)
        remoteControlGrid.setColumnStretch(2, 4)
        remoteControlGrid.addWidget(labelOfRemoteControl2, 6, 0)
        remoteControlGrid.setColumnStretch(0, 12)
class initializeAboutWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(320, 240)
        self.setMinimumWidth(320)
        self.setMinimumHeight(240)
        self.setMaximumWidth(640)
        self.setMaximumHeight(360)
        self.setWindowTitle("About")
        webViewFrameApplication = QWebEngineView()
        webViewFrameApplication.setUrl(QUrl("application_internal_resources\aboutPageForWebview.html"))
        webGrid = QGridLayout()
        self.setLayout(webGrid)
        webGrid.addWidget(webViewFrameApplication, 0, 0)
def mainButtonFunctionality1():
    print(Back. BLUE + Fore.LIGHTWHITE_EX + "An URL has been opened by pressing the button." + Style.RESET_ALL)
    webbrowser.open_new_tab("https://github.com/TheGitMpeg/Math-Calc-In-The-Console---0.28.6-BETA/tree/main/0.28.6.1%20Enhanced%20Beta")
def mainButtonFunctionality2():
    print(Back. BLUE + Fore.LIGHTWHITE_EX + "An URL has been opened and the program has been ended by pressing the button." + Style.RESET_ALL)
    webbrowser.open_new_tab("https://github.com/TheGitMpeg/Math-Calc-In-The-Console---0.28.6-BETA/tree/main/0.28.6.1%20Enhanced%20Beta")
    sys.exit(0)
def mainButtonFunctionality3():
    count_3secs_GRJT(3)
    sys.exit(0)
def mainButtonFunctionality4():
    count_3secs_GRJT(5)
    sys.exit(0)
def mainButtonFunctionality5():
    webLoad = initializeAboutWidget()
    webLoad.show()
def main():
    generalApplicationGUI = QApplication([])
    applicationLoad = initializeAppGUIWindow()
    applicationLoad.show()
    rcLoad = initializeRemoteControl()
    rcLoad.show()
    sys.exit(generalApplicationGUI.exec_())
try:
    main()
except IndexError:
    print(Back.RED + Fore.LIGHTWHITE_EX + "Error! Something went wrong during or before running the application and/or doing an operation! Exiting..." + Style.RESET_ALL)
    exit()