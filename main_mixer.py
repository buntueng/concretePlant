# main_mixer.py
import sys
from PySide6 import QtWidgets
from views.mainMixer import Ui_MainWindow as MainMixer
from controllers.mainMixerController import MainMixerController

# import QMainWindow
from PySide6.QtWidgets import QMainWindow
import sqlite3
import os

class MainMixerApp(QMainWindow):
    def __init__(self):
        super().__init__()    
        self.ui = MainMixer()
        self.ui.setupUi(self)
        
        concrete_db_path = os.path.join(os.path.dirname(__file__), 'concretePlant.db')
        
        # if database file does not exist, show error message
        if not os.path.exists(concrete_db_path):
            QtWidgets.QMessageBox.critical(self, "Error", "Database file not found")
            sys.exit(1)
        else:
            # Initialize database connection
            sqlite_connector = sqlite3.connect(concrete_db_path)
            self.controller = MainMixerController(self.ui, self, sqlite_connector)  # Pass self
            
            # load all formula from formula table
            self.ui.concreteFormula_comboBox.clear()
            sql_query = "SELECT name FROM concrete_formula"
            cursor = sqlite_connector.cursor()
            cursor.execute(sql_query)
            result = cursor.fetchall()
            for row in result:
                self.ui.concreteFormula_comboBox.addItem(row[0])
            cursor.close()
            
            
    def resetForm(self):
        self.ui.customerName_lineEdit.clear()
        self.ui.phoneNumber_lineEdit.clear()
        self.ui.customerName_lineEdit.setFocus()
        
        self.ui.customerName_lineEdit.setEnabled(True)
    

    def closeEvent(self, event):
        self.controller.closeEvent(event=event)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainMixerApp()
    window.show()
    sys.exit(app.exec())