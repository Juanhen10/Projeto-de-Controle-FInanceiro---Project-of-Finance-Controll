import platform
import sys
from typing import Optional

import PySide6.QtWidgets
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QEvent,
                            QMetaObject, QObject, QPoint, QPropertyAnimation,
                            QRect, QSize, Qt, QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient,
                           QPainter, QPalette, QPixmap, QRadialGradient)
from PySide6.QtWidgets import *
################################
# SPLASH SCREEN
from splash import Ui_SplashWindow
################################
# MAIN WINDOW
from ui_main import Ui_MainWindow

##################################
# Global
counter = 0

# YOUR APLICATION


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MAIN WINDOW TEXT
        # QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText(
        #     "<strong>THANK</strong> FOR WATCHING"))

        # QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setStyleSheet(
        #     "background-colo: #222; calor: #FFF"))

# SCREEN


class FirstWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashWindow()
        self.ui.setupUi(self)

        # REMOVE O TIULO
        ###########################################################
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # type: ignore
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # type: ignore

        # DROP SHAWOW EFFECT
        ###########################################################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)  # type: ignore

        # QTIMER ==> START
        ###########################################################
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)  # type: ignore
        # TIMER IN MILLESECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial text
        self.ui.label_description.setText(
            "<strong>WELLCOME</strong> TO MY APPLICATION")

        # Charge Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText(
            "<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText(
            "<strong>LOADING</strong> YOUR FINANCE CONTROL"))

        # SHOW -->> MAIN WINDOW
        ##########################################################
        self.show()

    # ==> APP FUNCTIONS
    ################################################################
    def progress(self):
        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)  # type: ignore

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FirstWindow()
    sys.exit(app.exec_())
