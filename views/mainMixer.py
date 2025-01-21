# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainMixer.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QGroupBox, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1650, 800)
        MainWindow.setMinimumSize(QSize(1650, 800))
        MainWindow.setMaximumSize(QSize(1650, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.customer_groupBox = QGroupBox(self.centralwidget)
        self.customer_groupBox.setObjectName(u"customer_groupBox")
        self.customer_groupBox.setGeometry(QRect(10, 10, 421, 171))
        font = QFont()
        font.setPointSize(11)
        self.customer_groupBox.setFont(font)
        self.gridLayout = QGridLayout(self.customer_groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.customerName_label = QLabel(self.customer_groupBox)
        self.customerName_label.setObjectName(u"customerName_label")

        self.gridLayout.addWidget(self.customerName_label, 0, 0, 1, 1)

        self.address_label = QLabel(self.customer_groupBox)
        self.address_label.setObjectName(u"address_label")

        self.gridLayout.addWidget(self.address_label, 2, 0, 1, 1)

        self.phone_label = QLabel(self.customer_groupBox)
        self.phone_label.setObjectName(u"phone_label")

        self.gridLayout.addWidget(self.phone_label, 1, 0, 1, 1)

        self.phoneNumber_lineEdit = QLineEdit(self.customer_groupBox)
        self.phoneNumber_lineEdit.setObjectName(u"phoneNumber_lineEdit")
        self.phoneNumber_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.phoneNumber_lineEdit, 1, 1, 1, 1)

        self.customerName_lineEdit = QLineEdit(self.customer_groupBox)
        self.customerName_lineEdit.setObjectName(u"customerName_lineEdit")
        self.customerName_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout.addWidget(self.customerName_lineEdit, 0, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 1)

        self.address_plainTextEdit = QPlainTextEdit(self.customer_groupBox)
        self.address_plainTextEdit.setObjectName(u"address_plainTextEdit")
        self.address_plainTextEdit.setAutoFillBackground(True)
        self.address_plainTextEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.address_plainTextEdit.setFrameShape(QFrame.Shape.Box)
        self.address_plainTextEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.address_plainTextEdit.setLineWidth(2)
        self.address_plainTextEdit.setBackgroundVisible(False)

        self.gridLayout.addWidget(self.address_plainTextEdit, 2, 1, 2, 1)

        self.order_groupBox = QGroupBox(self.centralwidget)
        self.order_groupBox.setObjectName(u"order_groupBox")
        self.order_groupBox.setGeometry(QRect(450, 10, 241, 91))
        self.order_groupBox.setFont(font)
        self.gridLayout_2 = QGridLayout(self.order_groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.order_groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.concreteFormula_comboBox = QComboBox(self.order_groupBox)
        self.concreteFormula_comboBox.setObjectName(u"concreteFormula_comboBox")

        self.gridLayout_2.addWidget(self.concreteFormula_comboBox, 0, 1, 1, 2)

        self.label_16 = QLabel(self.order_groupBox)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_2.addWidget(self.label_16, 1, 0, 1, 1)

        self.concreteOrder_lineEdit = QLineEdit(self.order_groupBox)
        self.concreteOrder_lineEdit.setObjectName(u"concreteOrder_lineEdit")
        self.concreteOrder_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_2.addWidget(self.concreteOrder_lineEdit, 1, 1, 1, 1)

        self.label_17 = QLabel(self.order_groupBox)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_2.addWidget(self.label_17, 1, 2, 1, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(1130, 360, 501, 431))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.groupBox_3.setFont(font1)
        self.gridLayout_4 = QGridLayout(self.groupBox_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.label_25 = QLabel(self.groupBox_3)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_4.addWidget(self.label_25, 4, 1, 1, 1)

        self.label_29 = QLabel(self.groupBox_3)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout_4.addWidget(self.label_29, 8, 1, 1, 1)

        self.label_22 = QLabel(self.groupBox_3)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_4.addWidget(self.label_22, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 4, 1, 1)

        self.label_23 = QLabel(self.groupBox_3)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_4.addWidget(self.label_23, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.label_26 = QLabel(self.groupBox_3)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_4.addWidget(self.label_26, 5, 1, 1, 1)

        self.label_20 = QLabel(self.groupBox_3)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_20, 0, 5, 1, 1)

        self.label_21 = QLabel(self.groupBox_3)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.label_21, 0, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 3, 6, 1, 1)

        self.label_27 = QLabel(self.groupBox_3)
        self.label_27.setObjectName(u"label_27")

        self.gridLayout_4.addWidget(self.label_27, 6, 1, 1, 1)

        self.label_24 = QLabel(self.groupBox_3)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_4.addWidget(self.label_24, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 46, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.label_28 = QLabel(self.groupBox_3)
        self.label_28.setObjectName(u"label_28")

        self.gridLayout_4.addWidget(self.label_28, 7, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 9, 3, 1, 1)

        self.rock1Finish_lcdNumber = QLCDNumber(self.groupBox_3)
        self.rock1Finish_lcdNumber.setObjectName(u"rock1Finish_lcdNumber")
        self.rock1Finish_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.rock1Finish_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.rock1Finish_lcdNumber, 1, 3, 1, 1)

        self.rock1Target_lcdNumber = QLCDNumber(self.groupBox_3)
        self.rock1Target_lcdNumber.setObjectName(u"rock1Target_lcdNumber")
        self.rock1Target_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.rock1Target_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.rock1Target_lcdNumber, 1, 5, 1, 1)

        self.sandTarget_lcdNumber = QLCDNumber(self.groupBox_3)
        self.sandTarget_lcdNumber.setObjectName(u"sandTarget_lcdNumber")
        self.sandTarget_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.sandTarget_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.sandTarget_lcdNumber, 2, 5, 1, 1)

        self.sandFinish_lcdNumber = QLCDNumber(self.groupBox_3)
        self.sandFinish_lcdNumber.setObjectName(u"sandFinish_lcdNumber")
        self.sandFinish_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.sandFinish_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.sandFinish_lcdNumber, 2, 3, 1, 1)

        self.rock2Finish_lcdNumber = QLCDNumber(self.groupBox_3)
        self.rock2Finish_lcdNumber.setObjectName(u"rock2Finish_lcdNumber")
        self.rock2Finish_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.rock2Finish_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.rock2Finish_lcdNumber, 3, 3, 1, 1)

        self.cementFinish_lcdNumber = QLCDNumber(self.groupBox_3)
        self.cementFinish_lcdNumber.setObjectName(u"cementFinish_lcdNumber")
        self.cementFinish_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cementFinish_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.cementFinish_lcdNumber, 4, 3, 1, 1)

        self.flyashFinish_lcdNumber = QLCDNumber(self.groupBox_3)
        self.flyashFinish_lcdNumber.setObjectName(u"flyashFinish_lcdNumber")
        self.flyashFinish_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.flyashFinish_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.flyashFinish_lcdNumber, 5, 3, 1, 1)

        self.waterFinish_lcdNumber = QLCDNumber(self.groupBox_3)
        self.waterFinish_lcdNumber.setObjectName(u"waterFinish_lcdNumber")
        self.waterFinish_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.waterFinish_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.waterFinish_lcdNumber, 6, 3, 1, 1)

        self.chem1Finish_lcdNumber = QLCDNumber(self.groupBox_3)
        self.chem1Finish_lcdNumber.setObjectName(u"chem1Finish_lcdNumber")
        self.chem1Finish_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.chem1Finish_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.chem1Finish_lcdNumber, 7, 3, 1, 1)

        self.chem2Finish_lcdNumber = QLCDNumber(self.groupBox_3)
        self.chem2Finish_lcdNumber.setObjectName(u"chem2Finish_lcdNumber")
        self.chem2Finish_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.chem2Finish_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.chem2Finish_lcdNumber, 8, 3, 1, 1)

        self.rock2Target_lcdNumber = QLCDNumber(self.groupBox_3)
        self.rock2Target_lcdNumber.setObjectName(u"rock2Target_lcdNumber")
        self.rock2Target_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.rock2Target_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.rock2Target_lcdNumber, 3, 5, 1, 1)

        self.cementTarget_lcdNumber = QLCDNumber(self.groupBox_3)
        self.cementTarget_lcdNumber.setObjectName(u"cementTarget_lcdNumber")
        self.cementTarget_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cementTarget_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.cementTarget_lcdNumber, 4, 5, 1, 1)

        self.flyashTarget_lcdNumber = QLCDNumber(self.groupBox_3)
        self.flyashTarget_lcdNumber.setObjectName(u"flyashTarget_lcdNumber")
        self.flyashTarget_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.flyashTarget_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.flyashTarget_lcdNumber, 5, 5, 1, 1)

        self.waterTarget_lcdNumber = QLCDNumber(self.groupBox_3)
        self.waterTarget_lcdNumber.setObjectName(u"waterTarget_lcdNumber")
        self.waterTarget_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.waterTarget_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.waterTarget_lcdNumber, 6, 5, 1, 1)

        self.chem1Target_lcdNumber = QLCDNumber(self.groupBox_3)
        self.chem1Target_lcdNumber.setObjectName(u"chem1Target_lcdNumber")
        self.chem1Target_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.chem1Target_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.chem1Target_lcdNumber, 7, 5, 1, 1)

        self.chem2Target_lcdNumber = QLCDNumber(self.groupBox_3)
        self.chem2Target_lcdNumber.setObjectName(u"chem2Target_lcdNumber")
        self.chem2Target_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.chem2Target_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_4.addWidget(self.chem2Target_lcdNumber, 8, 5, 1, 1)

        self.keepSample_groupBox = QGroupBox(self.centralwidget)
        self.keepSample_groupBox.setObjectName(u"keepSample_groupBox")
        self.keepSample_groupBox.setGeometry(QRect(450, 100, 241, 81))
        self.keepSample_groupBox.setFont(font)
        self.verticalLayout = QVBoxLayout(self.keepSample_groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.keepSample_radioButton = QRadioButton(self.keepSample_groupBox)
        self.keepSample_radioButton.setObjectName(u"keepSample_radioButton")

        self.verticalLayout.addWidget(self.keepSample_radioButton)

        self.noKeepSample_radioButton = QRadioButton(self.keepSample_groupBox)
        self.noKeepSample_radioButton.setObjectName(u"noKeepSample_radioButton")

        self.verticalLayout.addWidget(self.noKeepSample_radioButton)

        self.sending_groupBox = QGroupBox(self.centralwidget)
        self.sending_groupBox.setObjectName(u"sending_groupBox")
        self.sending_groupBox.setGeometry(QRect(10, 180, 681, 121))
        self.sending_groupBox.setFont(font)
        self.gridLayout_3 = QGridLayout(self.sending_groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_18 = QLabel(self.sending_groupBox)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_3.addWidget(self.label_18, 0, 0, 1, 1)

        self.truckID_lineEdit = QLineEdit(self.sending_groupBox)
        self.truckID_lineEdit.setObjectName(u"truckID_lineEdit")
        self.truckID_lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_3.addWidget(self.truckID_lineEdit, 0, 1, 1, 1)

        self.label_19 = QLabel(self.sending_groupBox)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_3.addWidget(self.label_19, 1, 0, 1, 1)

        self.comment_plainTextEdit = QPlainTextEdit(self.sending_groupBox)
        self.comment_plainTextEdit.setObjectName(u"comment_plainTextEdit")
        self.comment_plainTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comment_plainTextEdit.setFrameShape(QFrame.Shape.Box)
        self.comment_plainTextEdit.setFrameShadow(QFrame.Shadow.Plain)
        self.comment_plainTextEdit.setLineWidth(2)

        self.gridLayout_3.addWidget(self.comment_plainTextEdit, 1, 1, 2, 1)

        self.verticalSpacer_2 = QSpacerItem(41, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.groupBox_6 = QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(10, 310, 1111, 351))
        font2 = QFont()
        font2.setPointSize(14)
        self.groupBox_6.setFont(font2)
        self.water_frame = QFrame(self.groupBox_6)
        self.water_frame.setObjectName(u"water_frame")
        self.water_frame.setGeometry(QRect(700, 30, 111, 80))
        self.water_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.water_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.water_label = QLabel(self.water_frame)
        self.water_label.setObjectName(u"water_label")
        self.water_label.setGeometry(QRect(10, 10, 91, 20))
        self.water_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.waterValue_lcdNumber = QLCDNumber(self.water_frame)
        self.waterValue_lcdNumber.setObjectName(u"waterValue_lcdNumber")
        self.waterValue_lcdNumber.setGeometry(QRect(20, 40, 71, 23))
        self.waterValue_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.rock1_frame = QFrame(self.groupBox_6)
        self.rock1_frame.setObjectName(u"rock1_frame")
        self.rock1_frame.setGeometry(QRect(20, 30, 111, 80))
        self.rock1_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.rock1_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.rock1_label = QLabel(self.rock1_frame)
        self.rock1_label.setObjectName(u"rock1_label")
        self.rock1_label.setGeometry(QRect(10, 10, 91, 20))
        self.rock1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rock1Value_lcdNumber = QLCDNumber(self.rock1_frame)
        self.rock1Value_lcdNumber.setObjectName(u"rock1Value_lcdNumber")
        self.rock1Value_lcdNumber.setGeometry(QRect(20, 40, 71, 23))
        self.rock1Value_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.conveyor_frame = QFrame(self.groupBox_6)
        self.conveyor_frame.setObjectName(u"conveyor_frame")
        self.conveyor_frame.setGeometry(QRect(20, 120, 351, 41))
        self.conveyor_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.conveyor_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.conveyor_label = QLabel(self.conveyor_frame)
        self.conveyor_label.setObjectName(u"conveyor_label")
        self.conveyor_label.setGeometry(QRect(10, 10, 331, 20))
        self.conveyor_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.chem1_frame = QFrame(self.groupBox_6)
        self.chem1_frame.setObjectName(u"chem1_frame")
        self.chem1_frame.setGeometry(QRect(860, 30, 111, 80))
        self.chem1_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.chem1_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.chem1_label = QLabel(self.chem1_frame)
        self.chem1_label.setObjectName(u"chem1_label")
        self.chem1_label.setGeometry(QRect(10, 9, 91, 21))
        self.chem1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.chem1Value_lcdNumber = QLCDNumber(self.chem1_frame)
        self.chem1Value_lcdNumber.setObjectName(u"chem1Value_lcdNumber")
        self.chem1Value_lcdNumber.setGeometry(QRect(20, 40, 71, 23))
        self.chem1Value_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.chem1Value_lcdNumber.setDigitCount(3)
        self.chem1Value_lcdNumber.setProperty("value", 0.000000000000000)
        self.chem1Value_lcdNumber.setProperty("intValue", 0)
        self.chemValve_frame = QFrame(self.groupBox_6)
        self.chemValve_frame.setObjectName(u"chemValve_frame")
        self.chemValve_frame.setGeometry(QRect(940, 120, 71, 41))
        self.chemValve_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.chemValve_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.rock2_frame = QFrame(self.groupBox_6)
        self.rock2_frame.setObjectName(u"rock2_frame")
        self.rock2_frame.setGeometry(QRect(260, 30, 111, 80))
        self.rock2_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.rock2_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.rock2_label = QLabel(self.rock2_frame)
        self.rock2_label.setObjectName(u"rock2_label")
        self.rock2_label.setGeometry(QRect(10, 10, 91, 20))
        self.rock2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rock2Value_lcdNumber = QLCDNumber(self.rock2_frame)
        self.rock2Value_lcdNumber.setObjectName(u"rock2Value_lcdNumber")
        self.rock2Value_lcdNumber.setGeometry(QRect(20, 40, 71, 23))
        self.rock2Value_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.flyash_frame = QFrame(self.groupBox_6)
        self.flyash_frame.setObjectName(u"flyash_frame")
        self.flyash_frame.setGeometry(QRect(540, 30, 111, 80))
        self.flyash_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.flyash_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.flyash_label = QLabel(self.flyash_frame)
        self.flyash_label.setObjectName(u"flyash_label")
        self.flyash_label.setGeometry(QRect(10, 10, 91, 20))
        self.flyash_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.flyashValue_lcdNumber = QLCDNumber(self.flyash_frame)
        self.flyashValue_lcdNumber.setObjectName(u"flyashValue_lcdNumber")
        self.flyashValue_lcdNumber.setGeometry(QRect(20, 40, 71, 23))
        self.flyashValue_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.mixerValve_frame = QFrame(self.groupBox_6)
        self.mixerValve_frame.setObjectName(u"mixerValve_frame")
        self.mixerValve_frame.setGeometry(QRect(570, 280, 351, 41))
        self.mixerValve_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mixerValve_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.valveMixer_label = QLabel(self.mixerValve_frame)
        self.valveMixer_label.setObjectName(u"valveMixer_label")
        self.valveMixer_label.setGeometry(QRect(10, 10, 331, 20))
        self.valveMixer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mixer_frame = QFrame(self.groupBox_6)
        self.mixer_frame.setObjectName(u"mixer_frame")
        self.mixer_frame.setGeometry(QRect(420, 170, 671, 101))
        self.mixer_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.mixer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.mixer_label = QLabel(self.mixer_frame)
        self.mixer_label.setObjectName(u"mixer_label")
        self.mixer_label.setGeometry(QRect(10, 10, 651, 81))
        self.mixer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.waterValve_frame = QFrame(self.groupBox_6)
        self.waterValve_frame.setObjectName(u"waterValve_frame")
        self.waterValve_frame.setGeometry(QRect(720, 120, 71, 41))
        self.waterValve_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.waterValve_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.cement_frame = QFrame(self.groupBox_6)
        self.cement_frame.setObjectName(u"cement_frame")
        self.cement_frame.setGeometry(QRect(420, 30, 111, 80))
        self.cement_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cement_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.cemen_label = QLabel(self.cement_frame)
        self.cemen_label.setObjectName(u"cemen_label")
        self.cemen_label.setGeometry(QRect(10, 10, 91, 20))
        self.cemen_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cementValue_lcdNumber = QLCDNumber(self.cement_frame)
        self.cementValue_lcdNumber.setObjectName(u"cementValue_lcdNumber")
        self.cementValue_lcdNumber.setGeometry(QRect(20, 40, 71, 23))
        self.cementValue_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.cementValve_frame = QFrame(self.groupBox_6)
        self.cementValve_frame.setObjectName(u"cementValve_frame")
        self.cementValve_frame.setGeometry(QRect(500, 120, 71, 41))
        self.cementValve_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.cementValve_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.chem2_frame = QFrame(self.groupBox_6)
        self.chem2_frame.setObjectName(u"chem2_frame")
        self.chem2_frame.setGeometry(QRect(980, 30, 111, 80))
        self.chem2_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.chem2_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.chem2_label = QLabel(self.chem2_frame)
        self.chem2_label.setObjectName(u"chem2_label")
        self.chem2_label.setGeometry(QRect(10, 10, 91, 20))
        self.chem2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.chem2Value_lcdNumber = QLCDNumber(self.chem2_frame)
        self.chem2Value_lcdNumber.setObjectName(u"chem2Value_lcdNumber")
        self.chem2Value_lcdNumber.setGeometry(QRect(20, 40, 71, 23))
        self.chem2Value_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.sand_frame = QFrame(self.groupBox_6)
        self.sand_frame.setObjectName(u"sand_frame")
        self.sand_frame.setGeometry(QRect(140, 30, 111, 80))
        self.sand_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.sand_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.sand_label = QLabel(self.sand_frame)
        self.sand_label.setObjectName(u"sand_label")
        self.sand_label.setGeometry(QRect(10, 10, 91, 20))
        self.sand_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sandValue_lcdNumber = QLCDNumber(self.sand_frame)
        self.sandValue_lcdNumber.setObjectName(u"sandValue_lcdNumber")
        self.sandValue_lcdNumber.setGeometry(QRect(20, 40, 71, 23))
        self.sandValue_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.processStatus_groupBox = QGroupBox(self.centralwidget)
        self.processStatus_groupBox.setObjectName(u"processStatus_groupBox")
        self.processStatus_groupBox.setGeometry(QRect(10, 660, 1111, 131))
        self.processStatus_groupBox.setFont(font)
        self.groupBox_8 = QGroupBox(self.centralwidget)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(1130, 10, 501, 351))
        self.groupBox_8.setFont(font1)
        self.gridLayout_5 = QGridLayout(self.groupBox_8)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_35 = QLabel(self.groupBox_8)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_35, 3, 5, 1, 1)

        self.label_31 = QLabel(self.groupBox_8)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_31, 2, 1, 1, 1)

        self.label_34 = QLabel(self.groupBox_8)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_34, 2, 5, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_7, 2, 4, 1, 1)

        self.label_32 = QLabel(self.groupBox_8)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_32, 3, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 2, 2, 1, 1)

        self.label_33 = QLabel(self.groupBox_8)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_33, 0, 5, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_8, 2, 6, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)

        self.label_30 = QLabel(self.groupBox_8)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_30, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 4, 3, 1, 1)

        self.startProcess_pushButton = QPushButton(self.groupBox_8)
        self.startProcess_pushButton.setObjectName(u"startProcess_pushButton")
        self.startProcess_pushButton.setMinimumSize(QSize(0, 70))

        self.gridLayout_5.addWidget(self.startProcess_pushButton, 5, 3, 1, 4)

        self.terminateProcess_pushButton = QPushButton(self.groupBox_8)
        self.terminateProcess_pushButton.setObjectName(u"terminateProcess_pushButton")
        self.terminateProcess_pushButton.setMinimumSize(QSize(0, 70))

        self.gridLayout_5.addWidget(self.terminateProcess_pushButton, 6, 3, 1, 4)

        self.inProcessAmount_lcdNumber = QLCDNumber(self.groupBox_8)
        self.inProcessAmount_lcdNumber.setObjectName(u"inProcessAmount_lcdNumber")
        self.inProcessAmount_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.inProcessAmount_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_5.addWidget(self.inProcessAmount_lcdNumber, 2, 3, 1, 1)

        self.finishAmount_lcdNumber = QLCDNumber(self.groupBox_8)
        self.finishAmount_lcdNumber.setObjectName(u"finishAmount_lcdNumber")
        self.finishAmount_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.finishAmount_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_5.addWidget(self.finishAmount_lcdNumber, 3, 3, 1, 1)

        self.targetAmount_lcdNumber = QLCDNumber(self.groupBox_8)
        self.targetAmount_lcdNumber.setObjectName(u"targetAmount_lcdNumber")
        self.targetAmount_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.targetAmount_lcdNumber.setProperty("value", 0.000000000000000)

        self.gridLayout_5.addWidget(self.targetAmount_lcdNumber, 0, 3, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(700, 10, 421, 291))
        self.groupBox.setFont(font2)
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.chem2Waiting_lcdNumber = QLCDNumber(self.groupBox)
        self.chem2Waiting_lcdNumber.setObjectName(u"chem2Waiting_lcdNumber")
        self.chem2Waiting_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_6.addWidget(self.chem2Waiting_lcdNumber, 6, 5, 1, 1)

        self.label_39 = QLabel(self.groupBox)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout_6.addWidget(self.label_39, 6, 0, 1, 1)

        self.cementWaiting_lcdNumber = QLCDNumber(self.groupBox)
        self.cementWaiting_lcdNumber.setObjectName(u"cementWaiting_lcdNumber")
        self.cementWaiting_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_6.addWidget(self.cementWaiting_lcdNumber, 7, 2, 1, 1)

        self.sandWaiting_lcdNumber = QLCDNumber(self.groupBox)
        self.sandWaiting_lcdNumber.setObjectName(u"sandWaiting_lcdNumber")
        self.sandWaiting_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_6.addWidget(self.sandWaiting_lcdNumber, 3, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 9, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_9, 3, 3, 1, 1)

        self.label_43 = QLabel(self.groupBox)
        self.label_43.setObjectName(u"label_43")

        self.gridLayout_6.addWidget(self.label_43, 2, 0, 1, 1)

        self.label_41 = QLabel(self.groupBox)
        self.label_41.setObjectName(u"label_41")

        self.gridLayout_6.addWidget(self.label_41, 8, 0, 1, 1)

        self.rock2Waiting_lcdNumber = QLCDNumber(self.groupBox)
        self.rock2Waiting_lcdNumber.setObjectName(u"rock2Waiting_lcdNumber")
        self.rock2Waiting_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_6.addWidget(self.rock2Waiting_lcdNumber, 6, 2, 1, 1)

        self.waterWaiting_lcdNumber = QLCDNumber(self.groupBox)
        self.waterWaiting_lcdNumber.setObjectName(u"waterWaiting_lcdNumber")
        self.waterWaiting_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_6.addWidget(self.waterWaiting_lcdNumber, 2, 5, 1, 1)

        self.label_42 = QLabel(self.groupBox)
        self.label_42.setObjectName(u"label_42")

        self.gridLayout_6.addWidget(self.label_42, 3, 0, 1, 1)

        self.rock1Waiting_lcdNumber = QLCDNumber(self.groupBox)
        self.rock1Waiting_lcdNumber.setObjectName(u"rock1Waiting_lcdNumber")
        self.rock1Waiting_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_6.addWidget(self.rock1Waiting_lcdNumber, 2, 2, 1, 1)

        self.label_36 = QLabel(self.groupBox)
        self.label_36.setObjectName(u"label_36")

        self.gridLayout_6.addWidget(self.label_36, 7, 0, 1, 1)

        self.chem1Waiting_lcdNumber = QLCDNumber(self.groupBox)
        self.chem1Waiting_lcdNumber.setObjectName(u"chem1Waiting_lcdNumber")
        self.chem1Waiting_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_6.addWidget(self.chem1Waiting_lcdNumber, 3, 5, 1, 1)

        self.flyashWaiting_lcdNumber = QLCDNumber(self.groupBox)
        self.flyashWaiting_lcdNumber.setObjectName(u"flyashWaiting_lcdNumber")
        self.flyashWaiting_lcdNumber.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_6.addWidget(self.flyashWaiting_lcdNumber, 8, 2, 1, 1)

        self.label_38 = QLabel(self.groupBox)
        self.label_38.setObjectName(u"label_38")

        self.gridLayout_6.addWidget(self.label_38, 2, 4, 1, 1)

        self.label_40 = QLabel(self.groupBox)
        self.label_40.setObjectName(u"label_40")

        self.gridLayout_6.addWidget(self.label_40, 6, 4, 1, 1)

        self.label_37 = QLabel(self.groupBox)
        self.label_37.setObjectName(u"label_37")

        self.gridLayout_6.addWidget(self.label_37, 3, 4, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_11, 2, 6, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.customer_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32", None))
        self.customerName_label.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e37\u0e48\u0e2d", None))
        self.address_label.setText(QCoreApplication.translate("MainWindow", u"\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e39\u0e48", None))
        self.phone_label.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e1a\u0e2d\u0e23\u0e4c\u0e42\u0e17\u0e23", None))
        self.order_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e2a\u0e34\u0e19\u0e04\u0e49\u0e32", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e19\u0e34\u0e14\u0e1b\u0e39\u0e19", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0e08\u0e33\u0e19\u0e27\u0e19", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e34\u0e27\u0e1a\u0e34\u0e04", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0e01\u0e32\u0e23\u0e17\u0e33\u0e07\u0e32\u0e19", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u0e0b\u0e35\u0e40\u0e21\u0e19\u0e15\u0e4c", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e22\u0e32 2", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e34\u0e19 1", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0e17\u0e23\u0e32\u0e22", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e16\u0e49\u0e32\u0e25\u0e2d\u0e22", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e40\u0e1b\u0e49\u0e32\u0e2b\u0e21\u0e32\u0e22", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e17\u0e35\u0e48\u0e42\u0e2b\u0e25\u0e14\u0e41\u0e25\u0e49\u0e27", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e34\u0e19 2", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e22\u0e32 1", None))
        self.keepSample_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0e01\u0e32\u0e23\u0e40\u0e01\u0e47\u0e1a\u0e25\u0e39\u0e01\u0e1b\u0e39\u0e19", None))
        self.keepSample_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0e15\u0e49\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e40\u0e01\u0e47\u0e1a\u0e25\u0e39\u0e01\u0e1b\u0e39\u0e19", None))
        self.noKeepSample_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0e44\u0e21\u0e48\u0e40\u0e01\u0e47\u0e1a\u0e25\u0e39\u0e01\u0e1b\u0e39\u0e19", None))
        self.sending_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0e01\u0e32\u0e23\u0e08\u0e31\u0e14\u0e2a\u0e48\u0e07", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e25\u0e02\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e23\u0e16", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e2b\u0e15\u0e38", None))
        self.groupBox_6.setTitle("")
        self.water_label.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33", None))
        self.rock1_label.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e34\u0e19 1", None))
        self.conveyor_label.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e32\u0e22\u0e1e\u0e32\u0e19\u0e25\u0e33\u0e40\u0e25\u0e35\u0e22\u0e07", None))
        self.chem1_label.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e22\u0e32 1", None))
        self.rock2_label.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e34\u0e19 2", None))
        self.flyash_label.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e16\u0e49\u0e32\u0e25\u0e2d\u0e22", None))
        self.valveMixer_label.setText(QCoreApplication.translate("MainWindow", u"\u0e27\u0e32\u0e25\u0e4c\u0e27\u0e1b\u0e25\u0e48\u0e2d\u0e22\u0e1b\u0e39\u0e19", None))
        self.mixer_label.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e1c\u0e2a\u0e21\u0e04\u0e2d\u0e19\u0e01\u0e23\u0e35\u0e15", None))
        self.cemen_label.setText(QCoreApplication.translate("MainWindow", u"\u0e0b\u0e35\u0e40\u0e21\u0e19\u0e15\u0e4c", None))
        self.chem2_label.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e22\u0e32 2", None))
        self.sand_label.setText(QCoreApplication.translate("MainWindow", u"\u0e17\u0e23\u0e32\u0e22", None))
        self.processStatus_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e16\u0e32\u0e19\u0e30\u0e01\u0e32\u0e23\u0e17\u0e33\u0e07\u0e32\u0e19", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e23\u0e38\u0e1b\u0e01\u0e32\u0e23\u0e42\u0e2b\u0e25\u0e14\u0e1b\u0e39\u0e19", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e34\u0e27\u0e1a\u0e34\u0e04", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u0e1b\u0e39\u0e19\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e39\u0e48\u0e23\u0e30\u0e2b\u0e27\u0e48\u0e32\u0e07\u0e1c\u0e2a\u0e21", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e34\u0e27\u0e1a\u0e34\u0e04", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u0e1b\u0e39\u0e19\u0e17\u0e35\u0e48\u0e1c\u0e2a\u0e21\u0e40\u0e2a\u0e23\u0e47\u0e08", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e34\u0e27\u0e1a\u0e34\u0e04", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u0e1b\u0e39\u0e19\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e42\u0e2b\u0e25\u0e14", None))
        self.startProcess_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e23\u0e34\u0e48\u0e21\u0e01\u0e32\u0e23\u0e42\u0e2b\u0e25\u0e14", None))
        self.terminateProcess_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e22\u0e38\u0e14\u0e42\u0e2b\u0e25\u0e14", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e42\u0e2b\u0e25\u0e14", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e34\u0e19 2", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e34\u0e19 1", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e16\u0e49\u0e32\u0e25\u0e2d\u0e22", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u0e17\u0e23\u0e32\u0e22", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u0e0b\u0e35\u0e40\u0e21\u0e19\u0e15\u0e4c", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e22\u0e32 2", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e22\u0e32 1", None))
    # retranslateUi

