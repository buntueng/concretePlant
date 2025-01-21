# main_mixer.py
import sys
from PySide6 import QtWidgets
from views.billCreator import Ui_Form as BillCreator

# import QMainWindow
from PySide6.QtWidgets import QMainWindow
import sqlite3
import os

# import pdf creator libraries
from reportlab.lib.pagesizes import A5, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.fonts import addMapping

# Add Thai font
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

from PyPDF2 import PdfReader, PdfWriter
from io import BytesIO

# printer
from PySide6.QtGui import QPainter
from PySide6.QtPrintSupport import QPrintDialog
from PySide6.QtWidgets import QDialog

import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtGui import QPainter, QImage  # Import QPainter and QImage
from PySide6.QtCore import Qt  # Import Qt for Qt.KeepAspectRatio
from PySide6.QtCore import QSize

from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtGui import QTextDocument

from PySide6.QtWidgets import QMessageBox

import fitz
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtGui import QPainter, QPixmap

class BillCreatorApp(QMainWindow):
    def __init__(self):
        super().__init__()    
        self.ui = BillCreator()
        self.ui.setupUi(self)
        
        self.initTreeWidget()
        
        self.concrete_db_path = os.path.join(os.path.dirname(__file__), 'concretePlant.db')
        self.pdf_output_path = os.path.join(os.path.dirname(__file__),'tmp', 'billoutput.pdf')
        
        # if database file does not exist, show error message
        if not os.path.exists(self.concrete_db_path):
            QtWidgets.QMessageBox.critical(self, "Error", "Database file not found")
            sys.exit(1)
        else:
            # Initialize database connection
            sqlite_connector = sqlite3.connect(self.concrete_db_path)
            self.cursor = sqlite_connector.cursor()
        # bind events
        self.ui.reload_pushButton.clicked.connect(self.load_customer_data)
        self.ui.print_pushButton.clicked.connect(self.generate_bill)
        
        self.load_customer_data()
            
    def initTreeWidget(self):
        self.ui.orderDetail_treeWidget.setColumnWidth(0, 50)
        self.ui.orderDetail_treeWidget.setColumnWidth(1, 150)
        self.ui.orderDetail_treeWidget.setColumnWidth(2, 250)
        self.ui.orderDetail_treeWidget.setColumnWidth(3, 300)
        self.ui.orderDetail_treeWidget.setColumnWidth(4, 100)
        self.ui.orderDetail_treeWidget.setColumnWidth(5, 100)
        self.ui.orderDetail_treeWidget.setColumnWidth(6, 100)
        
        
    def generate_bill(self):
        # if no item is selected, show error message
        if self.ui.orderDetail_treeWidget.selectedItems() == []:
            QtWidgets.QMessageBox.critical(self, "Error", "กรุณาเลือกข้อมูลที่ต้องการปริ้น")
            return
        # get the selected item
        order_id = self.ui.orderDetail_treeWidget.selectedItems()[0].text(0)
        
        # add data to the pdf form
        self.font_path = os.path.join(os.path.dirname(__file__), "fonts", "THNiramitAS.ttf")
        self.template_path = os.path.join(os.path.dirname(__file__), "other_files","bill_templateA5.pdf")
        self.ouput_pdf_path = os.path.join(os.path.dirname(__file__), "tmp", "billoutput.pdf")
        
        # get the customer information
        if self.cursor is None:
            sqlite_connector = sqlite3.connect(self.concrete_db_path)
            self.cursor = sqlite_connector.cursor()
        sql_query = "SELECT dTime,customer_name,address,amount,truck_number,formula_name,age,slump FROM concrete_order WHERE id = ?"
        self.cursor.execute(sql_query, (order_id,))
        customer_informtaion = self.cursor.fetchone()
        
        # create the pdf form
        self.generate_pdf_output(customer_informtaion)
        
        # send the pdf form to the printer
        self.print_bill()
        
        # open print dialog
        self.print_pdf(self.ouput_pdf_path)
            
    def print_pdf(self,pdf_path):
        # Verify file existence
        try:
            pdf_document = fitz.open(pdf_path)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to open PDF file: {e}")
            return

        # Configure printer
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.NativeFormat)

        # Open the print dialog
        dialog = QPrintDialog(printer, self)
        if dialog.exec() != QPrintDialog.Accepted:
            return

        # Print the PDF content page by page
        painter = QPainter()
        for page_num in range(len(pdf_document)):
            page = pdf_document[page_num]
            pix = page.get_pixmap(dpi=300)  # Render the page as an image with 300 DPI

            # Convert PyMuPDF Pixmap to QImage
            img_data = pix.samples
            image = QImage(img_data, pix.width, pix.height, pix.stride, QImage.Format_RGB888)

            # Convert QImage to QPixmap
            pixmap = QPixmap.fromImage(image)

            # Start the painter and print to the printer
            painter.begin(printer)

            # Scale the image to fit the page
            rect = painter.viewport()

            scaled_pixmap = pixmap.scaled(rect.width(), rect.height(), Qt.KeepAspectRatio)
            painter.drawPixmap(rect, scaled_pixmap)

            painter.end()

            # Prepare for the next page
            if page_num < len(pdf_document) - 1:
                printer.newPage()

        
    def generate_pdf_output(self,customer_informtaion):
        # Create a PdfWriter object to write the output PDF
        output = PdfWriter()

        # Read the existing template PDF
        template_pdf = PdfReader(self.template_path)

        # Iterate through the pages of the template PDF
        for i in range(len(template_pdf.pages)):
            template_page = template_pdf.pages[i]

            # Create a new canvas with the name for the current page
            packet = self.create_canvas(customer_informtaion)
            new_pdf = PdfReader(packet)
            new_page = new_pdf.pages[0]

            # Merge the new content with the template page
            template_page.merge_page(new_page)
            output.add_page(template_page)

        # Write the output PDF to a file
        with open(self.ouput_pdf_path, "wb") as output_stream:
            output.write(output_stream)
        # close the packet
        packet.close()
        
    def create_canvas(self,customer_informtaion):
        # current_time = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
        # Extract the customer information
        [record_time, customer_name, address, amount, truck_number, strength,age,slump ] = customer_informtaion
        
        packet = BytesIO()
        c = canvas.Canvas(packet, pagesize=landscape(A5))
        pdfmetrics.registerFont(TTFont('THSarabunNew', self.font_path))
        addMapping('THSarabunNew', 0, 0, 'THSarabunNew')
        
        c.setFont("THSarabunNew", 12)
        c.drawString(120, 312, customer_name)
        c.drawString(120, 296, address)
        c.drawString(120, 280, address)
        c.drawString(120, 216, str(amount))
        # get only the data part of the record time
        record_date = record_time.split(" ")[0]
        
        # convert date to Thai date
        # previous format is yyyy-mm-dd
        # new format is dd-mm-yyyy in Thai
        record_date = record_date.split("-")
        month = ""
        if record_date[1] == "01":
            month = "ม.ค."
        elif record_date[1] == "02":
            month = "ก.พ."
        elif record_date[1] == "03":
            month = "มี.ค."
        elif record_date[1] == "04":
            month = "เม.ย."
        elif record_date[1] == "05":
            month = "พ.ค."
        elif record_date[1] == "06":
            month = "มิ.ย."
        elif record_date[1] == "07":
            month = "ก.ค."
        elif record_date[1] == "08":
            month = "ส.ค."
        elif record_date[1] == "09":
            month = "ก.ย."
        elif record_date[1] == "10":
            month = "ต.ค."
        elif record_date[1] == "11":
            month = "พ.ย."
        elif record_date[1] == "12":
            month = "ธ.ค."
        
        record_date = str(int(record_date[2])) + " " + month + " " + str(int(record_date[0])+543)
        c.drawString(120, 199, record_date)
        record_timestamp = record_time.split(" ")[1]
        c.drawString(280, 199, record_timestamp)
        c.drawString(120, 183, truck_number)
        
        c.drawString(220,264,strength)
        c.drawString(425,264,age)
        c.drawString(116,235,slump)
        c.save()
        packet.seek(0)
        return packet
        
    def load_customer_data(self):
        if self.cursor is None:
            sqlite_connector = sqlite3.connect(self.concrete_db_path)
            self.cursor = sqlite_connector.cursor()
        
        self.cursor.execute("SELECT id,dTime,customer_name,address,truck_number,age,slump FROM concrete_order WHERE batch_state >=2 ORDER BY id DESC LIMIT 40")
        customers = self.cursor.fetchall()
        # add data to the tree widget
        self.ui.orderDetail_treeWidget.clear()
        for customer in customers:
            item = QtWidgets.QTreeWidgetItem(self.ui.orderDetail_treeWidget)
            for col, value in enumerate(customer):
                item.setText(col, str(value))
        self.cursor.close()
        self.cursor = None
    
    def print_bill(self):
        # if pdf_path exists show print dialog, else show error message
        if os.path.exists(self.pdf_output_path):
            pass
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "ไม่มีไฟล์ที่ต้องการปริ้น")
            return

    def closeEvent(self, event):
        self.check_closeEvent(event=event)
        
    def check_closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 'Message',
            "ต้องการปิดโปรแกรม", QtWidgets.QMessageBox.Yes | 
            QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
            # close connection
            try:
                self.cursor.close()
                self.cursor = None
                self.sqlite_connector.close()
            except:
                pass
        else:
            event.ignore()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = BillCreatorApp()
    # set the window title
    window.setWindowTitle("ปริ้นบิลส่งคอนกรีตผสม")
    window.show()
    sys.exit(app.exec())