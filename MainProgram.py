import sys
import os
from InstallWindow import InstallWindow
from LoginWindow import LoginScreen
from PyQt5.QtWidgets import QApplication,QSplashScreen,QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt,QTimer

class MainScreen():
    def showSplashScreen(self):                          # function to show splash screen
        self.pix=QPixmap("car_parking.jpg")
        self.splassh=QSplashScreen(self.pix,Qt.WindowStaysOnTopHint) #passing Qpixmap object to Qsplashscreen
        self.splassh.show()


def showSetupWindow():                            #function to show Install window
    mainScreen.splassh.close()
    installWindow.show()                          #calling the function showinstallwindow


def showLoginWindow():                   # function to show login window
    mainScreen.splassh.close()           #if config.json  file then it will show login window else show setup window
    login.showLoginScreen()              #calling the function showloginscreen



app=QApplication(sys.argv)
login=LoginScreen()
mainScreen=MainScreen()
mainScreen.showSplashScreen()
installWindow=InstallWindow()

if os.path.exists("./config.json"):       #calliing the setupwindow and loginwindow after 3 second delay
    QTimer.singleShot(3000,showLoginWindow)
else:
    QTimer.singleShot(3000,showSetupWindow)


sys.exit(app.exec_())