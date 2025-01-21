# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'billCreator.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1372, 734)
        Form.setStyleSheet(u"")
        self.reload_pushButton = QPushButton(Form)
        self.reload_pushButton.setObjectName(u"reload_pushButton")
        self.reload_pushButton.setGeometry(QRect(1220, 20, 141, 51))
        font = QFont()
        font.setPointSize(12)
        self.reload_pushButton.setFont(font)
        self.orderDetail_treeWidget = QTreeWidget(Form)
        self.orderDetail_treeWidget.setObjectName(u"orderDetail_treeWidget")
        self.orderDetail_treeWidget.setGeometry(QRect(20, 60, 1191, 671))
        self.orderDetail_treeWidget.setFont(font)
        self.print_pushButton = QPushButton(Form)
        self.print_pushButton.setObjectName(u"print_pushButton")
        self.print_pushButton.setGeometry(QRect(1220, 80, 141, 51))
        self.print_pushButton.setFont(font)
        self.searchDate_label = QLabel(Form)
        self.searchDate_label.setObjectName(u"searchDate_label")
        self.searchDate_label.setGeometry(QRect(20, 10, 101, 31))
        self.searchDate_label.setFont(font)
        self.searchDate_dateEdit = QDateEdit(Form)
        self.searchDate_dateEdit.setObjectName(u"searchDate_dateEdit")
        self.searchDate_dateEdit.setGeometry(QRect(140, 10, 151, 31))
        self.searchDate_dateEdit.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.reload_pushButton.setText(QCoreApplication.translate("Form", u"Reload", None))
        ___qtreewidgetitem = self.orderDetail_treeWidget.headerItem()
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("Form", u"slump", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("Form", u"\u0e2d\u0e32\u0e22\u0e38", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("Form", u"\u0e17\u0e30\u0e40\u0e1a\u0e35\u0e22\u0e19\u0e23\u0e16", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("Form", u"\u0e17\u0e35\u0e48\u0e2d\u0e22\u0e39\u0e48", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"\u0e0a\u0e37\u0e48\u0e2d\u0e25\u0e39\u0e01\u0e04\u0e49\u0e32", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e1c\u0e25\u0e34\u0e15", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"id", None));
        self.print_pushButton.setText(QCoreApplication.translate("Form", u"\u0e1e\u0e34\u0e21\u0e1e\u0e4c", None))
        self.searchDate_label.setText(QCoreApplication.translate("Form", u"\u0e04\u0e49\u0e19\u0e2b\u0e32\u0e27\u0e31\u0e19\u0e17\u0e35\u0e48\u0e1c\u0e25\u0e34\u0e15", None))
    # retranslateUi

