# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formulaEditor.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1362, 644)
        self.editFormula_pushButton = QPushButton(Form)
        self.editFormula_pushButton.setObjectName(u"editFormula_pushButton")
        self.editFormula_pushButton.setGeometry(QRect(1220, 70, 131, 51))
        font = QFont()
        font.setPointSize(12)
        self.editFormula_pushButton.setFont(font)
        self.concreteFormula_treeWidget = QTreeWidget(Form)
        self.concreteFormula_treeWidget.setObjectName(u"concreteFormula_treeWidget")
        self.concreteFormula_treeWidget.setGeometry(QRect(10, 10, 1191, 491))
        self.concreteFormula_treeWidget.setFont(font)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 510, 1191, 121))
        self.groupBox.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.chem1_lineEdit = QLineEdit(self.groupBox)
        self.chem1_lineEdit.setObjectName(u"chem1_lineEdit")
        self.chem1_lineEdit.setMinimumSize(QSize(70, 0))
        self.chem1_lineEdit.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.chem1_lineEdit, 1, 9, 1, 1)

        self.id_lineEdit = QLineEdit(self.groupBox)
        self.id_lineEdit.setObjectName(u"id_lineEdit")
        self.id_lineEdit.setMinimumSize(QSize(50, 0))
        self.id_lineEdit.setMaximumSize(QSize(50, 16777215))
        self.id_lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.id_lineEdit, 1, 0, 1, 1)

        self.flyash_label = QLabel(self.groupBox)
        self.flyash_label.setObjectName(u"flyash_label")
        self.flyash_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.flyash_label, 0, 5, 1, 1)

        self.cement_lineEdit = QLineEdit(self.groupBox)
        self.cement_lineEdit.setObjectName(u"cement_lineEdit")
        self.cement_lineEdit.setMinimumSize(QSize(70, 0))
        self.cement_lineEdit.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.cement_lineEdit, 1, 6, 1, 1)

        self.water_lineEdit = QLineEdit(self.groupBox)
        self.water_lineEdit.setObjectName(u"water_lineEdit")
        self.water_lineEdit.setMinimumSize(QSize(70, 0))
        self.water_lineEdit.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.water_lineEdit, 1, 7, 1, 1)

        self.chem1_label = QLabel(self.groupBox)
        self.chem1_label.setObjectName(u"chem1_label")
        self.chem1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.chem1_label, 0, 9, 1, 1)

        self.formulaName_lineEdit = QLineEdit(self.groupBox)
        self.formulaName_lineEdit.setObjectName(u"formulaName_lineEdit")
        self.formulaName_lineEdit.setMinimumSize(QSize(220, 0))
        self.formulaName_lineEdit.setMaximumSize(QSize(220, 16777215))

        self.gridLayout.addWidget(self.formulaName_lineEdit, 1, 1, 1, 1)

        self.chem2_label = QLabel(self.groupBox)
        self.chem2_label.setObjectName(u"chem2_label")
        self.chem2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.chem2_label, 0, 10, 1, 1)

        self.rock2_lineEdit = QLineEdit(self.groupBox)
        self.rock2_lineEdit.setObjectName(u"rock2_lineEdit")
        self.rock2_lineEdit.setMinimumSize(QSize(70, 0))
        self.rock2_lineEdit.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.rock2_lineEdit, 1, 4, 1, 1)

        self.formulaName_label = QLabel(self.groupBox)
        self.formulaName_label.setObjectName(u"formulaName_label")
        self.formulaName_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.formulaName_label, 0, 1, 1, 1)

        self.rock1_label = QLabel(self.groupBox)
        self.rock1_label.setObjectName(u"rock1_label")
        self.rock1_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.rock1_label, 0, 2, 1, 1)

        self.sand_lineEdit = QLineEdit(self.groupBox)
        self.sand_lineEdit.setObjectName(u"sand_lineEdit")
        self.sand_lineEdit.setMinimumSize(QSize(70, 0))
        self.sand_lineEdit.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.sand_lineEdit, 1, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.chem2_lineEdit = QLineEdit(self.groupBox)
        self.chem2_lineEdit.setObjectName(u"chem2_lineEdit")
        self.chem2_lineEdit.setMinimumSize(QSize(70, 0))
        self.chem2_lineEdit.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.chem2_lineEdit, 1, 10, 1, 1)

        self.rock2_label = QLabel(self.groupBox)
        self.rock2_label.setObjectName(u"rock2_label")
        self.rock2_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.rock2_label, 0, 4, 1, 1)

        self.water_label = QLabel(self.groupBox)
        self.water_label.setObjectName(u"water_label")
        self.water_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.water_label, 0, 7, 1, 1)

        self.sand_label = QLabel(self.groupBox)
        self.sand_label.setObjectName(u"sand_label")
        self.sand_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.sand_label, 0, 3, 1, 1)

        self.rock1_lineEdit = QLineEdit(self.groupBox)
        self.rock1_lineEdit.setObjectName(u"rock1_lineEdit")
        self.rock1_lineEdit.setMinimumSize(QSize(70, 0))
        self.rock1_lineEdit.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.rock1_lineEdit, 1, 2, 1, 1)

        self.flyash_lineEdit = QLineEdit(self.groupBox)
        self.flyash_lineEdit.setObjectName(u"flyash_lineEdit")
        self.flyash_lineEdit.setMinimumSize(QSize(70, 0))
        self.flyash_lineEdit.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.flyash_lineEdit, 1, 5, 1, 1)

        self.cement_label = QLabel(self.groupBox)
        self.cement_label.setObjectName(u"cement_label")
        self.cement_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.cement_label, 0, 6, 1, 1)

        self.id_label = QLabel(self.groupBox)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.id_label, 0, 0, 1, 1)

        self.age_label = QLabel(self.groupBox)
        self.age_label.setObjectName(u"age_label")
        self.age_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.age_label, 0, 11, 1, 1)

        self.slump_label = QLabel(self.groupBox)
        self.slump_label.setObjectName(u"slump_label")
        self.slump_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.slump_label, 0, 12, 1, 1)

        self.age_lineEdit = QLineEdit(self.groupBox)
        self.age_lineEdit.setObjectName(u"age_lineEdit")
        self.age_lineEdit.setMinimumSize(QSize(70, 0))
        self.age_lineEdit.setMaximumSize(QSize(70, 16777215))

        self.gridLayout.addWidget(self.age_lineEdit, 1, 11, 1, 1)

        self.slump_lineEdit = QLineEdit(self.groupBox)
        self.slump_lineEdit.setObjectName(u"slump_lineEdit")
        self.slump_lineEdit.setMinimumSize(QSize(120, 0))
        self.slump_lineEdit.setMaximumSize(QSize(120, 16777215))

        self.gridLayout.addWidget(self.slump_lineEdit, 1, 12, 1, 1)

        self.save_pushButton = QPushButton(Form)
        self.save_pushButton.setObjectName(u"save_pushButton")
        self.save_pushButton.setGeometry(QRect(1210, 520, 141, 51))
        self.save_pushButton.setFont(font)
        self.cancel_pushButton = QPushButton(Form)
        self.cancel_pushButton.setObjectName(u"cancel_pushButton")
        self.cancel_pushButton.setGeometry(QRect(1210, 580, 141, 51))
        self.cancel_pushButton.setFont(font)
        self.deleteFormula_pushButton = QPushButton(Form)
        self.deleteFormula_pushButton.setObjectName(u"deleteFormula_pushButton")
        self.deleteFormula_pushButton.setGeometry(QRect(1220, 130, 131, 51))
        self.deleteFormula_pushButton.setFont(font)
        self.newFormula_pushButton = QPushButton(Form)
        self.newFormula_pushButton.setObjectName(u"newFormula_pushButton")
        self.newFormula_pushButton.setGeometry(QRect(1220, 10, 131, 51))
        self.newFormula_pushButton.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.editFormula_pushButton.setText(QCoreApplication.translate("Form", u"\u0e41\u0e01\u0e49\u0e44\u0e02\u0e2a\u0e39\u0e15\u0e23", None))
        ___qtreewidgetitem = self.concreteFormula_treeWidget.headerItem()
        ___qtreewidgetitem.setText(11, QCoreApplication.translate("Form", u"slump", None));
        ___qtreewidgetitem.setText(10, QCoreApplication.translate("Form", u"age", None));
        ___qtreewidgetitem.setText(9, QCoreApplication.translate("Form", u"\u0e19\u0e49\u0e33\u0e22\u0e32\u0e40\u0e04\u0e21\u0e35 2", None));
        ___qtreewidgetitem.setText(8, QCoreApplication.translate("Form", u"\u0e19\u0e49\u0e33\u0e22\u0e32\u0e40\u0e04\u0e21\u0e35 1", None));
        ___qtreewidgetitem.setText(7, QCoreApplication.translate("Form", u"\u0e19\u0e49\u0e33", None));
        ___qtreewidgetitem.setText(6, QCoreApplication.translate("Form", u"\u0e1b\u0e39\u0e19", None));
        ___qtreewidgetitem.setText(5, QCoreApplication.translate("Form", u"\u0e40\u0e16\u0e49\u0e32\u0e25\u0e2d\u0e22", None));
        ___qtreewidgetitem.setText(4, QCoreApplication.translate("Form", u"\u0e2b\u0e34\u0e192", None));
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("Form", u"\u0e17\u0e23\u0e32\u0e22", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("Form", u"\u0e2b\u0e34\u0e191", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("Form", u"\u0e0a\u0e37\u0e48\u0e2d\u0e2a\u0e39\u0e15\u0e23", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"\u0e25\u0e33\u0e14\u0e31\u0e1a", None));
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u0e2a\u0e39\u0e15\u0e23\u0e17\u0e35\u0e48\u0e15\u0e49\u0e2d\u0e07\u0e01\u0e32\u0e23\u0e1b\u0e23\u0e31\u0e1a\u0e1b\u0e23\u0e38\u0e07", None))
        self.flyash_label.setText(QCoreApplication.translate("Form", u"\u0e40\u0e16\u0e49\u0e32\u0e25\u0e2d\u0e22", None))
        self.chem1_label.setText(QCoreApplication.translate("Form", u"\u0e19\u0e49\u0e33\u0e22\u0e32\u0e40\u0e04\u0e21\u0e35 1", None))
        self.chem2_label.setText(QCoreApplication.translate("Form", u"\u0e19\u0e49\u0e33\u0e22\u0e32\u0e40\u0e04\u0e21\u0e35 2", None))
        self.formulaName_label.setText(QCoreApplication.translate("Form", u"\u0e0a\u0e37\u0e48\u0e2d\u0e2a\u0e39\u0e15\u0e23", None))
        self.rock1_label.setText(QCoreApplication.translate("Form", u"\u0e2b\u0e34\u0e191", None))
        self.rock2_label.setText(QCoreApplication.translate("Form", u"\u0e2b\u0e34\u0e192", None))
        self.water_label.setText(QCoreApplication.translate("Form", u"\u0e19\u0e49\u0e33", None))
        self.sand_label.setText(QCoreApplication.translate("Form", u"\u0e17\u0e23\u0e32\u0e22", None))
        self.cement_label.setText(QCoreApplication.translate("Form", u"\u0e1b\u0e39\u0e19", None))
        self.id_label.setText(QCoreApplication.translate("Form", u"id", None))
        self.age_label.setText(QCoreApplication.translate("Form", u"\u0e2d\u0e32\u0e22\u0e38", None))
        self.slump_label.setText(QCoreApplication.translate("Form", u"slump", None))
        self.save_pushButton.setText(QCoreApplication.translate("Form", u"\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e04\u0e48\u0e32", None))
        self.cancel_pushButton.setText(QCoreApplication.translate("Form", u"\u0e22\u0e01\u0e40\u0e25\u0e34\u0e01", None))
        self.deleteFormula_pushButton.setText(QCoreApplication.translate("Form", u"\u0e25\u0e1a\u0e2a\u0e39\u0e15\u0e23", None))
        self.newFormula_pushButton.setText(QCoreApplication.translate("Form", u"\u0e40\u0e1e\u0e34\u0e48\u0e21\u0e2a\u0e39\u0e15\u0e23\u0e43\u0e2b\u0e21\u0e48", None))
    # retranslateUi

