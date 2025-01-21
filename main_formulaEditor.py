# main_mixer.py
import sys
from PySide6 import QtWidgets
from views.formulaEditor import Ui_Form as FormulaEditor
from controllers.formulaEditorController import FormulaEditorController

# import QMainWindow
from PySide6.QtWidgets import QMainWindow
import sqlite3
import os

class FormulaEditorApp(QMainWindow):
    def __init__(self):
        super().__init__()    
        self.ui = FormulaEditor()
        self.ui.setupUi(self)
        
        self.initTreeWidget()
        
        concrete_db_path = os.path.join(os.path.dirname(__file__), 'concretePlant.db')
        
        # if database file does not exist, show error message
        if not os.path.exists(concrete_db_path):
            QtWidgets.QMessageBox.critical(self, "Error", "Database file not found")
            sys.exit(1)
        else:
            # Initialize database connection
            sqlite_connector = sqlite3.connect(concrete_db_path)
            self.controller = FormulaEditorController(self.ui, self, sqlite_connector)  # Pass self
            
            self.controller.resetForm()
            self.controller.loadConcreteFormula()
            
            
    def initTreeWidget(self):
        self.ui.concreteFormula_treeWidget.setColumnWidth(0, 50)
        self.ui.concreteFormula_treeWidget.setColumnWidth(1, 200)
        self.ui.concreteFormula_treeWidget.setColumnWidth(2, 80)
        self.ui.concreteFormula_treeWidget.setColumnWidth(3, 80)
        self.ui.concreteFormula_treeWidget.setColumnWidth(4, 80)
        self.ui.concreteFormula_treeWidget.setColumnWidth(5, 80)
        self.ui.concreteFormula_treeWidget.setColumnWidth(6, 80)
        self.ui.concreteFormula_treeWidget.setColumnWidth(7, 80)
        self.ui.concreteFormula_treeWidget.setColumnWidth(8, 80)
        self.ui.concreteFormula_treeWidget.setColumnWidth(9, 80)
        self.ui.concreteFormula_treeWidget.setColumnWidth(10, 80)
    

    def closeEvent(self, event):
        self.controller.closeEvent(event=event)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FormulaEditorApp()
    # set the window title
    window.setWindowTitle("Concrete Formula Editor")
    window.show()
    sys.exit(app.exec())