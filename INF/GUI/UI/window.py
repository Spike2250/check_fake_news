# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(810, 600)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(238, 238, 238, 255), stop:1 rgba(190, 190, 190, 255));\n"
"font-family: Roboto;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.centralwidget)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setStyleSheet(u"font-size: 12pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout = QGridLayout(self.top_frame)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.load_model = QPushButton(self.top_frame)
        self.load_model.setObjectName(u"load_model")
        self.load_model.setEnabled(False)
        self.load_model.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 12pt;\n"
"color: White;\n"
"border: None;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")

        self.gridLayout.addWidget(self.load_model, 3, 1, 1, 1)

        self.train_model = QPushButton(self.top_frame)
        self.train_model.setObjectName(u"train_model")
        self.train_model.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 12pt;\n"
"color: White;\n"
"border: None;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")

        self.gridLayout.addWidget(self.train_model, 0, 1, 1, 1)

        self.save_model = QPushButton(self.top_frame)
        self.save_model.setObjectName(u"save_model")
        self.save_model.setEnabled(False)
        self.save_model.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 12pt;\n"
"color: White;\n"
"border: None;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")

        self.gridLayout.addWidget(self.save_model, 2, 1, 1, 1)

        self.show_info = QPushButton(self.top_frame)
        self.show_info.setObjectName(u"show_info")
        self.show_info.setEnabled(False)
        self.show_info.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 12pt;\n"
"color: White;\n"
"border: None;\n"
"padding: 5px;\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")

        self.gridLayout.addWidget(self.show_info, 4, 1, 1, 1)

        self.model_status = QLabel(self.top_frame)
        self.model_status.setObjectName(u"model_status")
        self.model_status.setStyleSheet(u"color: #326273;\n"
"font-size: 15pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.model_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.model_status, 0, 0, 5, 1)

        self.process = QLabel(self.top_frame)
        self.process.setObjectName(u"process")
        self.process.setStyleSheet(u"color: #326273;\n"
"font-size: 12pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")
        self.process.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.process, 0, 2, 5, 1)


        self.verticalLayout.addWidget(self.top_frame)

        self.center_frame = QFrame(self.centralwidget)
        self.center_frame.setObjectName(u"center_frame")
        self.center_frame.setStyleSheet(u"font-size: 12pt;\n"
"color: rgba(50, 98, 115, 255);\n"
"border: 1px solid  rgba(50, 98, 115, 255);\n"
"background-color: rgba(50, 98, 115, 40);")
        self.gridLayout_2 = QGridLayout(self.center_frame)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.news_text = QPlainTextEdit(self.center_frame)
        self.news_text.setObjectName(u"news_text")
        self.news_text.setStyleSheet(u"background-color: #EEEEEE;\n"
"color: #13242B;\n"
"border: 1px solid #326273;\n"
"font-weight: bold;\n"
"font-size: 11pt;\n"
"")

        self.gridLayout_2.addWidget(self.news_text, 1, 0, 1, 4)

        self.label = QLabel(self.center_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"background-color: rgba(50, 98, 115, 40);\n"
"border: none;")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 3, 1, 1)

        self.label_3 = QLabel(self.center_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"border: none;\n"
"background-color: transparent;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.check_news = QPushButton(self.center_frame)
        self.check_news.setObjectName(u"check_news")
        self.check_news.setEnabled(False)
        self.check_news.setStyleSheet(u"QPushButton {\n"
"background-color: rgba(50, 98, 115, 190);\n"
"font-size: 12pt;\n"
"color: White;\n"
"border: None;\n"
"padding: 10px\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"background-color: rgba(50, 98, 115, 255);\n"
"border: 2px solid rgba(92, 158, 173, 255);\n"
"}\n"
"\n"
"QPushButton::pressed {\n"
"background-color: rgba(92, 158, 173, 255);\n"
"border: 1px solid rgba(255, 255, 255, 255);\n"
"}\n"
"\n"
"QPushButton::disabled {\n"
"background-color:  rgba(50, 98, 115, 40);\n"
"border: 1px solid rgba(50, 98, 115, 150);\n"
"color:  rgba(50, 98, 115, 150);\n"
"}")

        self.gridLayout_2.addWidget(self.check_news, 2, 1, 1, 2)

        self.result = QLineEdit(self.center_frame)
        self.result.setObjectName(u"result")
        self.result.setEnabled(False)
        self.result.setStyleSheet(u"color: #326273;\n"
"font-weight: bold;\n"
"font-size: 14pt;\n"
"border: none;\n"
"background-color: transparent;")
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.result, 3, 1, 1, 3)


        self.verticalLayout.addWidget(self.center_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Is news fake?", None))
        self.load_model.setText(QCoreApplication.translate("MainWindow", u"Load model", None))
        self.train_model.setText(QCoreApplication.translate("MainWindow", u"Train new model", None))
        self.save_model.setText(QCoreApplication.translate("MainWindow", u"Save model", None))
        self.show_info.setText(QCoreApplication.translate("MainWindow", u"Show confusion matrix", None))
        self.model_status.setText("")
        self.process.setText("")
        self.news_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"copy the news into this field", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"News:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Result:    ", None))
        self.check_news.setText(QCoreApplication.translate("MainWindow", u"Check!", None))
    # retranslateUi

