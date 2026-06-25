# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1070, 697)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setGeometry(QRect(200, 0, 871, 651))
        self.main_widget.setStyleSheet(u"background-color: rgb(226, 255, 227);")
        self.your_notes_text = QLabel(self.main_widget)
        self.your_notes_text.setObjectName(u"your_notes_text")
        self.your_notes_text.setGeometry(QRect(40, 80, 61, 31))
        self.your_notes_text.setStyleSheet(u"font: 600 9pt \"Yu Gothic UI Semibold\";\n"
"color: rgb(0, 85, 0);")
        self.submit_btn = QPushButton(self.main_widget)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setGeometry(QRect(180, 510, 101, 41))
        self.submit_btn.setStyleSheet(u"background-color: rgb(85, 170, 127);\n"
"color: white;")
        self.result_text = QLabel(self.main_widget)
        self.result_text.setObjectName(u"result_text")
        self.result_text.setGeometry(QRect(460, 80, 61, 31))
        self.result_text.setStyleSheet(u"font: 600 9pt \"Yu Gothic UI Semibold\";\n"
"color: rgb(0, 85, 0);")
        self.input_box = QPlainTextEdit(self.main_widget)
        self.input_box.setObjectName(u"input_box")
        self.input_box.setGeometry(QRect(40, 110, 361, 391))
        self.input_box.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(85, 170, 127);\n"
"border-radius: 5px;\n"
"color: black;")
        self.output_box = QPlainTextEdit(self.main_widget)
        self.output_box.setObjectName(u"output_box")
        self.output_box.setGeometry(QRect(460, 110, 361, 391))
        self.output_box.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(85, 170, 127);\n"
"border-radius: 5px;\n"
"color: black;")
        self.side_bar_widget = QWidget(self.centralwidget)
        self.side_bar_widget.setObjectName(u"side_bar_widget")
        self.side_bar_widget.setGeometry(QRect(0, 0, 201, 641))
        self.side_bar_widget.setStyleSheet(u"background-color: rgb(85, 170, 127);")
        self.layoutWidget = QWidget(self.side_bar_widget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 200, 161, 211))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.concepts_box = QCheckBox(self.layoutWidget)
        self.concepts_box.setObjectName(u"concepts_box")
        self.concepts_box.setStyleSheet(u"font: 600 9pt \"Yu Gothic UI Semibold\";")

        self.verticalLayout.addWidget(self.concepts_box)

        self.analogy_box = QCheckBox(self.layoutWidget)
        self.analogy_box.setObjectName(u"analogy_box")
        self.analogy_box.setStyleSheet(u"font: 600 9pt \"Yu Gothic UI Semibold\";")

        self.verticalLayout.addWidget(self.analogy_box)

        self.example_box = QCheckBox(self.layoutWidget)
        self.example_box.setObjectName(u"example_box")
        self.example_box.setStyleSheet(u"font: 600 9pt \"Yu Gothic UI Semibold\";")

        self.verticalLayout.addWidget(self.example_box)

        self.definitions_box = QCheckBox(self.layoutWidget)
        self.definitions_box.setObjectName(u"definitions_box")
        self.definitions_box.setStyleSheet(u"font: 600 9pt \"Yu Gothic UI Semibold\";")

        self.verticalLayout.addWidget(self.definitions_box)

        self.practice_box = QCheckBox(self.layoutWidget)
        self.practice_box.setObjectName(u"practice_box")
        self.practice_box.setStyleSheet(u"font: 600 9pt \"Yu Gothic UI Semibold\";")

        self.verticalLayout.addWidget(self.practice_box)

        self.logo = QLabel(self.side_bar_widget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(60, 80, 81, 81))
        self.logo.setPixmap(QPixmap(u"ui/LOGO.png"))
        self.logo.setScaledContents(True)
        self.add_text = QLabel(self.side_bar_widget)
        self.add_text.setObjectName(u"add_text")
        self.add_text.setGeometry(QRect(20, 180, 49, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1070, 33))
        self.menuNotezz = QMenu(self.menubar)
        self.menuNotezz.setObjectName(u"menuNotezz")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuNotezz.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.your_notes_text.setText(QCoreApplication.translate("MainWindow", u"Your notes:", None))
        self.submit_btn.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.result_text.setText(QCoreApplication.translate("MainWindow", u"Result:", None))
        self.input_box.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Paste your text here....", None))
        self.concepts_box.setText(QCoreApplication.translate("MainWindow", u"Simple Concepts", None))
        self.analogy_box.setText(QCoreApplication.translate("MainWindow", u"Analogy", None))
        self.example_box.setText(QCoreApplication.translate("MainWindow", u"Example", None))
        self.definitions_box.setText(QCoreApplication.translate("MainWindow", u"Definitions", None))
        self.practice_box.setText(QCoreApplication.translate("MainWindow", u"Practice Questions", None))
        self.logo.setText("")
        self.add_text.setText(QCoreApplication.translate("MainWindow", u"Add:", None))
        self.menuNotezz.setTitle(QCoreApplication.translate("MainWindow", u"Notezz", None))
    # retranslateUi

