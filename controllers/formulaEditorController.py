
from PySide6.QtGui import QValidator, QKeyEvent
from PySide6.QtWidgets import QMessageBox
from PySide6 import QtWidgets
import sys

class FloatValidator(QValidator):
    def validate(self, input_text, pos):
        # Empty input is considered intermediate
        if not input_text:
            return QValidator.Intermediate, input_text, pos

        # Allow a single dot
        if input_text.count('.') > 1:
            return QValidator.Invalid, input_text, pos

        # Check if the input is a valid float
        try:
            float(input_text)
            return QValidator.Acceptable, input_text, pos
        except ValueError:
            # Allow a single leading minus sign
            if input_text == '-' and pos == 1:
                return QValidator.Intermediate, input_text, pos
            # Allow a single dot as intermediate if not already present
            elif input_text == '.' and pos == 1 and '.' not in input_text:
                return QValidator.Intermediate, input_text, pos
            else:
                return QValidator.Invalid, input_text, pos

class FormulaEditorController():
    def __init__(self,ui, MainWindow, sqlite_connector):
        self.ui = ui
        self.MainWindow = MainWindow
        self.sqlite_connector = sqlite_connector
        
        self.edit_mode = ""
        
        # set validator for lineEdit
        self.ui.sand_lineEdit.setValidator(FloatValidator())
        self.ui.rock1_lineEdit.setValidator(FloatValidator())
        self.ui.rock2_lineEdit.setValidator(FloatValidator())
        self.ui.flyash_lineEdit.setValidator(FloatValidator())
        self.ui.cement_lineEdit.setValidator(FloatValidator())
        self.ui.water_lineEdit.setValidator(FloatValidator())
        self.ui.chem1_lineEdit.setValidator(FloatValidator())
        self.ui.chem2_lineEdit.setValidator(FloatValidator())
        
        # add event listener
        self.ui.newFormula_pushButton.clicked.connect(self.addNewFormula)
        self.ui.editFormula_pushButton.clicked.connect(self.editFormula)
        self.ui.deleteFormula_pushButton.clicked.connect(self.deleteFormula)
        self.ui.save_pushButton.clicked.connect(self.saveFormula)
        self.ui.cancel_pushButton.clicked.connect(self.cancelSubmition)
        
        # enable buttons
        self.ui.newFormula_pushButton.setEnabled(True)
        self.ui.editFormula_pushButton.setEnabled(True)
        self.ui.deleteFormula_pushButton.setEnabled(True)
        
        # disable buttons
        self.ui.save_pushButton.setEnabled(False)
        self.ui.cancel_pushButton.setEnabled(False)
        
        self.enableForm(False)
        
    def cancelSubmition(self):
        self.edit_mode = ""
        self.resetForm()
        
        # enable buttons
        self.ui.newFormula_pushButton.setEnabled(True)
        self.ui.editFormula_pushButton.setEnabled(True)
        self.ui.deleteFormula_pushButton.setEnabled(True)
        
        # disable buttons
        self.ui.save_pushButton.setEnabled(False)
        self.ui.cancel_pushButton.setEnabled(False)
        
        
    def saveFormula(self):
        success = False
        if self.edit_mode == "edit":
            if self.updateFormula():
                success = True
        elif self.edit_mode == "new":
            if self.insertFormula():
                success = True
        
        if success:
            self.enableForm(False)
            # reload
            self.loadConcreteFormula()
            # enable buttons
            self.ui.newFormula_pushButton.setEnabled(True)
            self.ui.editFormula_pushButton.setEnabled(True)
            self.ui.deleteFormula_pushButton.setEnabled(True)
            
            # disable buttons
            self.ui.save_pushButton.setEnabled(False)
            self.ui.cancel_pushButton.setEnabled(False)
        
    def updateFormula(self):
        formula_id = self.ui.id_lineEdit.text()
        formula_name = self.ui.formulaName_lineEdit.text()
        rock1_weight = self.ui.rock1_lineEdit.text()
        sand_weight = self.ui.sand_lineEdit.text()
        rock2_weight = self.ui.rock2_lineEdit.text()
        cement_weight = self.ui.cement_lineEdit.text()
        fly_ash_weight = self.ui.flyash_lineEdit.text()
        water_weight = self.ui.water_lineEdit.text()
        chemical1_weight = self.ui.chem1_lineEdit.text()
        chemical2_weight = self.ui.chem2_lineEdit.text()
        age = self.ui.age_lineEdit.text()
        slump = self.ui.slump_lineEdit.text()
        
        cursor = self.sqlite_connector.cursor()
        # clear previous data
        cursor.execute("UPDATE concrete_formula SET status = 0 WHERE id = ?", (formula_id,))
        # add new data
        cursor.execute("INSERT INTO concrete_formula (formula_name, rock1_weight, sand_weight, rock2_weight, cement_weight, fly_ash_weight, water_weight, chemical1_weight, chemical2_weight, age, slump, status) VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (formula_name, rock1_weight, sand_weight, rock2_weight, cement_weight, fly_ash_weight, water_weight, chemical1_weight, chemical2_weight, age, slump, 1))
        self.sqlite_connector.commit()
        cursor.close()
        
        self.resetForm()
        return True
    
    def insertFormula(self):
        formula_name = self.ui.formulaName_lineEdit.text()
        rock1_weight = self.ui.rock1_lineEdit.text()
        sand_weight = self.ui.sand_lineEdit.text()
        rock2_weight = self.ui.rock2_lineEdit.text()
        cement_weight = self.ui.cement_lineEdit.text()
        fly_ash_weight = self.ui.flyash_lineEdit.text()
        water_weight = self.ui.water_lineEdit.text()
        chemical1_weight = self.ui.chem1_lineEdit.text()
        chemical2_weight = self.ui.chem2_lineEdit.text()
        age = self.ui.age_lineEdit.text()
        slump = self.ui.slump_lineEdit.text()
        
        # if any field is empty, show error message
        error_message = ""
        if formula_name == "":
            error_message += "กรุณากรอกชื่อสูตร\n"
        if rock1_weight == "":
            error_message += "กรุณากรอกน้ำหนักหิน1\n"
        if sand_weight == "":
            error_message += "กรุณากรอกน้ำหนักทราย\n"
        if rock2_weight == "":
            error_message += "กรุณากรอกน้ำหนักหิน2\n"
        if cement_weight == "":
            error_message += "กรุณากรอกน้ำหนักปูน\n"
        if fly_ash_weight == "":
            error_message += "กรุณากรอกน้ำหนักเถ้า\n"
        if water_weight == "":
            error_message += "กรุณากรอกน้ำหนักน้ำ\n"
        if chemical1_weight == "":
            error_message += "กรุณากรอกน้ำหนักสารเคมี1\n"
        if chemical2_weight == "":
            error_message += "กรุณากรอกน้ำหนักสารเคมี2\n"
        if age == "":
            error_message += "กรุณากรอกอายุปูน\n"
        if slump == "":
            error_message += "กรุณากรอกค่าสลัมป์\n"
            
        if error_message != "":
            QtWidgets.QMessageBox.critical(self.MainWindow, "Error", error_message)
            return
        
        cursor = self.sqlite_connector.cursor()
        cursor.execute("INSERT INTO concrete_formula (formula_name, rock1_weight, sand_weight, rock2_weight, cement_weight, fly_ash_weight, water_weight, chemical1_weight, chemical2_weight, status) VALUES (?,?,?,?,?,?,?,?,?,?)", (formula_name, rock1_weight, sand_weight, rock2_weight, cement_weight, fly_ash_weight, water_weight, chemical1_weight, chemical2_weight, 1))
        self.sqlite_connector.commit()
        cursor.close()
        self.resetForm() 
        # enable buttons
        self.ui.newFormula_pushButton.setEnabled(True)
        self.ui.editFormula_pushButton.setEnabled(True)
        self.ui.deleteFormula_pushButton.setEnabled(True)
            
        # disable buttons
        self.ui.save_pushButton.setEnabled(False)
        self.ui.cancel_pushButton.setEnabled(False)
        return True
        
    def deleteFormula(self):
        if self.ui.concreteFormula_treeWidget.currentItem() is None:
            # show error message
            QtWidgets.QMessageBox.critical(self.MainWindow, "Error", "กรุณาเลือกสูตรที่ต้องการลบ")
        else:
            # get formula id
            formula_id = self.ui.concreteFormula_treeWidget.currentItem().text(0)
            # update status to 0
            cursor = self.sqlite_connector.cursor()
            cursor.execute("UPDATE concrete_formula SET status = 0 WHERE id = ?", (formula_id,))
            self.sqlite_connector.commit()
            cursor.close()            
            # reload formula
            self.loadConcreteFormula()
        
    def editFormula(self):
        # if no selected item
        selected_item = self.ui.concreteFormula_treeWidget.currentItem()
        if selected_item is None:
            # show error message
            QtWidgets.QMessageBox.critical(self.MainWindow, "Error", "กรุณาเลือกสูตรที่ต้องการแก้ไข")
        else:
            # load data to lineEdit
            self.ui.id_lineEdit.setText(selected_item.text(0))
            self.ui.formulaName_lineEdit.setText(selected_item.text(1))
            self.ui.rock1_lineEdit.setText(selected_item.text(2))
            self.ui.sand_lineEdit.setText(selected_item.text(3))
            self.ui.rock2_lineEdit.setText(selected_item.text(4))
            self.ui.flyash_lineEdit.setText(selected_item.text(5))
            self.ui.cement_lineEdit.setText(selected_item.text(6))
            self.ui.water_lineEdit.setText(selected_item.text(7))
            self.ui.chem1_lineEdit.setText(selected_item.text(8))
            self.ui.chem2_lineEdit.setText(selected_item.text(9))
            self.ui.age_lineEdit.setText(selected_item.text(10))
            self.ui.slump_lineEdit.setText(selected_item.text(11))
            
            self.enableForm()
            self.ui.formulaName_lineEdit.setEnabled(False)
            
            self.edit_mode = "edit"
            
            # disable buttons
            self.ui.newFormula_pushButton.setEnabled(False)
            self.ui.editFormula_pushButton.setEnabled(False)
            self.ui.deleteFormula_pushButton.setEnabled(False)
            
            # enable buttons
            self.ui.save_pushButton.setEnabled(True)
            self.ui.cancel_pushButton.setEnabled(True)
            
    def addNewFormula(self):
        self.resetForm()
        self.enableForm()
        self.edit_mode = "new"
        
        # set focus to formulaName_lineEdit
        self.ui.formulaName_lineEdit.setFocus()
        
        # disable buttons
        self.ui.newFormula_pushButton.setEnabled(False)
        self.ui.editFormula_pushButton.setEnabled(False)
        self.ui.deleteFormula_pushButton.setEnabled(False)

        # enable buttons
        self.ui.save_pushButton.setEnabled(True)
        self.ui.cancel_pushButton.setEnabled
        
    def resetForm(self):
        lineEditWidgets = [ self.ui.id_lineEdit,
                            self.ui.formulaName_lineEdit, 
                            self.ui.rock1_lineEdit, 
                            self.ui.sand_lineEdit, 
                            self.ui.rock2_lineEdit, 
                            self.ui.flyash_lineEdit, 
                            self.ui.cement_lineEdit,
                            self.ui.water_lineEdit,
                            self.ui.chem1_lineEdit,
                            self.ui.chem2_lineEdit,
                            self.ui.age_lineEdit,
                            self.ui.slump_lineEdit]
        
        # disable all lineEdit
        for lineEdit in lineEditWidgets:
            lineEdit.setEnabled(False)
            lineEdit.clear()
            
    def enableForm(self,enable_logic = True):
        lineEditWidgets = [ self.ui.formulaName_lineEdit, 
                            self.ui.rock1_lineEdit, 
                            self.ui.sand_lineEdit, 
                            self.ui.rock2_lineEdit, 
                            self.ui.flyash_lineEdit, 
                            self.ui.cement_lineEdit,
                            self.ui.water_lineEdit,
                            self.ui.chem1_lineEdit,
                            self.ui.chem2_lineEdit,
                            self.ui.age_lineEdit,
                            self.ui.slump_lineEdit]
        
        # enable all lineEdit
        for lineEdit in lineEditWidgets:
            lineEdit.setEnabled(enable_logic)
        
    def loadConcreteFormula(self):
        cursor = self.sqlite_connector.cursor()
        cursor.execute("SELECT id,formula_name, rock1_weight, sand_weight, rock2_weight, cement_weight, fly_ash_weight, water_weight, chemical1_weight, chemical2_weight, age, slump FROM concrete_formula WHERE status = 1 ORDER BY id ASC")
        rows = cursor.fetchall()
        
        self.ui.concreteFormula_treeWidget.clear()
        for row in rows:
            item = QtWidgets.QTreeWidgetItem(self.ui.concreteFormula_treeWidget)
            for col, value in enumerate(row):
                item.setText(col, str(value))
        cursor.close()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self.MainWindow, "ปิดโปรแกรม", "คุณต้องการปิดโปรแกรมแก้ไขสูตรปูน?", QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    