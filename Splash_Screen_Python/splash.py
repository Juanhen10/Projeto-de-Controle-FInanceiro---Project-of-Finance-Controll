# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screen.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_SplashWindow(object):
    def setupUi(self, SplashWindow):
        if not SplashWindow.objectName():
            SplashWindow.setObjectName(u"SplashWindow")
        SplashWindow.resize(680, 400)
        self.centralwidget = QWidget(SplashWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.dropShadowFrame = QFrame(self.centralwidget)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.dropShadowFrame.setStyleSheet(u"QFrame {\n"
"	\n"
"	color: rgb(255, 0, 4);\n"
"	\n"
"	background-color: rgb(214, 0, 4);\n"
"	border-radius: 10px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(10, 110, 641, 61))
        font = QFont()
        font.setPointSize(40)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(40, 170, 561, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label_description.setFont(font1)
        self.label_description.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 290, 601, 23))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(108, 108, 108);\n"
"	\n"
"	color: rgba(200, 200, 200, 200);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.602, x2:1, y2:0.608, stop:0 rgba(159, 0, 37, 255), stop:1 rgba(255, 25, 29, 255));\n"
"}\n"
"	\n"
"")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(60, 320, 561, 31))
        self.label_loading.setFont(font1)
        self.label_loading.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setGeometry(QRect(440, 350, 251, 31))
        self.label_credits.setFont(font1)
        self.label_credits.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_credits.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.dropShadowFrame)

        SplashWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashWindow)

        QMetaObject.connectSlotsByName(SplashWindow)
    # setupUi

    def retranslateUi(self, SplashWindow):
        SplashWindow.setWindowTitle(QCoreApplication.translate("SplashWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("SplashWindow", u"<strong>FINANCE</strong> CONTROL", None))
        self.label_description.setText(QCoreApplication.translate("SplashWindow", u"<html><head/><body><p>THE APP THAT WILL HELP YOU</p></body></html>", None))
        self.label_loading.setText(QCoreApplication.translate("SplashWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">LOADING...</span></p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("SplashWindow", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:700;\">Created: </span><span style=\" font-size:10pt;\">Juan Henrique</span></p></body></html>", None))
    # retranslateUi

