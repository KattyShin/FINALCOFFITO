import sys
import os
from PyQt6 import uic, QtCore, QtGui, QtWidgets
from PySide6.QtGui import QMouseEvent
from PySide6.QtWidgets import *
import PySide6
from PySide6.QtGui import QIcon, QColor, QPainter
from PySide6.QtCore import Qt, QTimer, QTime, QDate
from PySide6.QtGui import QGuiApplication
from PySide6.QtGui import QRegion, QPainter, QBitmap

from ui_MainUserInterface import Ui_MainWindow
import psycopg2
from database_config import get_database_config
from productContainer import Ui_Form
from PySide6.QtWidgets import QWidget, QWidgetItem
from PySide6.QtWidgets import QBoxLayout

MONTHS = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

class userInterface(QMainWindow, Ui_MainWindow):
    

    def connect_to_database(self):
        try:
            config = get_database_config()
            conn = psycopg2.connect(**config)
            print("Database connection established successfully!")
            return conn
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL:", error)
            return None
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Coffito Cafe")
        self.setWindowIcon(QIcon(r'C:\Users\Dennis\Desktop\POS System Coffito\CoffitoLogo (40 x 40 px).png'))
        self.product_containers = []      
        
        self.conn = self.connect_to_database()
        if self.conn is None:
            self.show_database_error()
        else:
            self.check_new_products()

        self.word_iicon.setHidden(True)

        self.gcashSelectRBtn.clicked.connect(self.set_gcash_selected)
        self.cashSelectBtn.clicked.connect(self.set_cash_selected)

        self.Amt_ContactNum_Val.setHidden(True)
        self.changeAmount.setHidden(True)

        self.proceedBtn.clicked.connect(self.switch_to_orderSummaryPage)
        self.backBtn.clicked.connect(self.switch_to_orderListPage)
        
        self.logout1.clicked.connect(self.show_login_window)
        self.logout2.clicked.connect(self.show_login_window)


        self.removeProdOrder.clicked.connect(self.removeSelectedRow)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)  
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start()

        self.date_time_label = self.DateTimeLabel

        self.Amt_ContactNum_Val.textChanged.connect(self.calculate_change)

        self.payButton.clicked.connect(self.payButtonClicked)
        self.Amt_ContactNum_Val.returnPressed.connect(self.payButtonClicked)

        self.dashboard1.clicked.connect(self.switch_to_dashboardPage)
        self.dashboard2.clicked.connect(self.switch_to_dashboardPage)
        self.directToDashboard.clicked.connect(self.switch_to_dashboardPage)

        
    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)
        
    def show_login_window(self):
        from ui_loginPage import Login_MainWindow

        self.login_window = Login_MainWindow()
        self.login_window.show()

    def set_gcash_selected(self):
        self.Amount_ContactNum.setText("Mobile Number:")
        self.Amt_ContactNum_Val.setHidden(False)
        self.changeLbl.setText("") 
        self.changeAmount.setHidden(True)  

    def set_cash_selected(self):
        self.Amount_ContactNum.setText("Cash Amount:")
        self.Amt_ContactNum_Val.setHidden(False)  
        self.changeLbl.setText("Change Amount:")  
        self.changeAmount.setHidden(False) 

    def calculate_change(self):
        try:
            cash_amount = float(self.Amt_ContactNum_Val.text())
            total_payment = self.total_price 
            change = cash_amount - total_payment

            self.changeAmount.setText(f"{change:.2f} PHP")

        except ValueError:
            self.changeAmount.setText("")



    def switch_to_orderSummaryPage(self):
        if self.order_table.rowCount() == 0:
            self.show_empty_order_message()
        else:
            self.proceed_to_summary_page()
            self.stackedWidget_2.setCurrentIndex(1)
        
    def switch_to_orderListPage(self):
        self.stackedWidget_2.setCurrentIndex(0)
        
    def update_date_time(self):
        current_date_time = self.get_current_date_time()
        self.date_time_label.setText(current_date_time)

    def get_current_date_time(self):
        current_time = QTime.currentTime().toString('hh:mm:ss')
        current_date = QDate.currentDate()
        month_number = current_date.month()
        month_text = MONTHS[month_number]  
        date_string = f"{month_text} {current_date.day()} {current_date.year()}"
        return f"{date_string} {current_time}"

    def show_database_error(self):
        QMessageBox.critical(self, "Database Connection Error", "Failed to connect to the database. Please check your configuration.")

   
    def prodBtnClicked(self, productName):
        try:
            cursor = self.conn.cursor()
            query = "SELECT PROD_NAME, PROD_PRICE FROM PRODUCT WHERE PROD_NAME = %s"
            cursor.execute(query, (productName,))
            product = cursor.fetchone()

            if product:
                prod_name, prod_price = product
                print(f"Product Name: {prod_name}, Price: {prod_price}")
                self.updateOrderTable(prod_name, prod_price)
                self.calculateTotalPrice()
            else:
                print(f"Product '{productName}' not found in the database.")

        except (Exception, psycopg2.Error) as error:
            print("Error fetching product from database:", error)
            self.conn.rollback()  
        finally:
            if cursor:
                cursor.close()


    def proceed_to_summary_page(self):
        self.order_table_2.setRowCount(0)
        self.order_table.setAlternatingRowColors(True)

        self.total_price = 0.0

        for row in range(self.order_table.rowCount()):
            item_name = self.order_table.item(row, 0).text()
            item_price = float(self.order_table.item(row, 1).text())
            item_quantity = int(self.order_table.item(row, 2).text())

            row_position = self.order_table_2.rowCount()
            self.order_table_2.insertRow(row_position)

            name_item = QTableWidgetItem(item_name)
            name_item.setTextAlignment(Qt.Alignment.AlignCenter)  
            self.order_table_2.setItem(row_position, 0, name_item)
            
            price_item = QTableWidgetItem(str(item_price))
            price_item.setTextAlignment(Qt.Alignment.AlignCenter)
            self.order_table_2.setItem(row_position, 1, price_item)

            quantity_item = QTableWidgetItem(str(item_quantity))
            quantity_item.setTextAlignment(Qt.Alignment.AlignCenter)
            self.order_table_2.setItem(row_position, 2, quantity_item)

            self.total_price += item_price * item_quantity

        self.totalPymtLbl_2.setText(f"{self.total_price:.2f} PHP")

    def updateOrderTable(self, prod_name, prod_price):
        self.order_table.setAlternatingRowColors(True)

        found = False
        for row in range(self.order_table.rowCount()):
            item = self.order_table.item(row, 0)
            if item is not None and item.text() == prod_name:
                current_quantity = int(self.order_table.item(row, 2).text())
                new_quantity = current_quantity + 1
                self.order_table.setItem(row, 2, QTableWidgetItem(str(new_quantity)))
                item.setForeground(QColor("white"))  
                item.setTextAlignment(Qt.Alignment.AlignCenter) 

                quantity_item = self.order_table.item(row, 2)
                if quantity_item:
                    quantity_item.setTextAlignment(Qt.Alignment.AlignCenter)
                found = True
                break

        if not found:
            row_position = self.order_table.rowCount()
            self.order_table.insertRow(row_position)

            item_name = QTableWidgetItem(prod_name)
            item_name.setForeground(QColor("white"))
            item_name.setTextAlignment(Qt.Alignment.AlignCenter)
            self.order_table.setItem(row_position, 0, item_name)

            item_price = QTableWidgetItem(str(prod_price))
            item_price.setForeground(QColor("white"))
            item_price.setTextAlignment(Qt.Alignment.AlignCenter)
            self.order_table.setItem(row_position, 1, item_price)

            quantity_item = QTableWidgetItem("1")
            quantity_item.setForeground(QColor("white"))
            quantity_item.setTextAlignment(Qt.Alignment.AlignCenter)
            self.order_table.setItem(row_position, 2, quantity_item)        

    def removeSelectedRow(self):
        selected_row = self.order_table.currentRow()
        if selected_row >= 0:
            self.order_table.removeRow(selected_row)
            self.calculateTotalPrice()
        else:
            self.show_message_box('Error','"No Row Selected", "Please select a row to remove.', QMessageBox.Critical)

    def calculateTotalPrice(self):
        total_price = 0.0

        for row in range(self.order_table.rowCount()):
            price_item = self.order_table.item(row, 1)
            quantity_item = self.order_table.item(row, 2)
            
            if price_item and quantity_item:
                price = float(price_item.text())
                quantity = int(quantity_item.text())
                subtotal = price * quantity
                total_price += subtotal
        
        self.totalPymtLbl.setText(f"{total_price:.2f} PHP")

    def payButtonClicked(self):
        if self.order_table.rowCount() == 0:
            self.show_empty_order_message()
            return

        payment_method = self.get_payment_method()
        if not payment_method:
            self.show_payment_method_error()
            return

        if payment_method == "Cash":
            try:
                cash_amount = float(self.Amt_ContactNum_Val.text())
            except ValueError:
                self.show_invalid_cash_amount_error()
                return

            if cash_amount < self.total_price:
                self.show_insufficient_cash_error()
                return
        elif payment_method == "GCash":
            contact_number = self.Amt_ContactNum_Val.text().strip()
            if not contact_number or not contact_number.isdigit():
                self.show_invalid_gcash_number_error()
                return
            if len(contact_number) != 11 or not contact_number.startswith("09"):
                self.show_length_error_message()
                return
        self.handle_pay_button()

  
    def insert_order_to_database(self, payment_method):
        try:
            cursor = self.conn.cursor()

            staff_id = 8742  #STAFF ID

            cursor.execute("INSERT INTO CUSTOMER DEFAULT VALUES RETURNING CUS_ID;")
            cus_id = cursor.fetchone()[0]

            order_summary_query = """
            INSERT INTO ORDERS (STAFF_ID, CUS_ID)
            VALUES (%s, %s) RETURNING ORDER_ID;
            """
            cursor.execute(order_summary_query, (staff_id, cus_id))
            order_id = cursor.fetchone()[0]

            order_items_query = """
            INSERT INTO ORDER_ITEMS (ORDER_ID, PROD_ID, ORDER_ITEM_QTY)
            VALUES (%s, %s, %s) RETURNING ORDER_ITEM_ID;
            """
            for row in range(self.order_table.rowCount()):
                item_name = self.order_table.item(row, 0).text()
                item_quantity = int(self.order_table.item(row, 2).text())

                cursor.execute("SELECT PROD_ID FROM PRODUCT WHERE PROD_NAME = %s", (item_name,))
                prod_id = cursor.fetchone()[0]

                cursor.execute(order_items_query, (order_id, prod_id, item_quantity))
                order_item_id = cursor.fetchone()[0] #IN CASE NEEDED

            payment_trans_query = """
            INSERT INTO PAYMENT_TRANSACTION (ORDER_ID, PAYMENT_TRANS_TOT_AMOUNT, PAYMENT_TRANS_METHOD, PAYMENT_TRANS_DETAILS)
            VALUES (%s, %s, %s, %s) RETURNING PAYMENT_TRANS_ID;
            """
            cursor.execute(payment_trans_query, (order_id, self.total_price, payment_method, self.Amt_ContactNum_Val.text() if self.Amt_ContactNum_Val.isVisible() else None))
            payment_trans_id = cursor.fetchone()[0]

            sales_report_query = """
            INSERT INTO SALES_REPORT (SALES_DATE, PAYMENT_TRANS_ID)
            VALUES (CURRENT_DATE, %s) RETURNING SALES_ID;
            """
            cursor.execute(sales_report_query, (payment_trans_id,))
            sales_id = cursor.fetchone()[0]

            sales_history_query = """
            INSERT INTO SALES_HISTORY (DAILY_TOTAL_SALES, GENERAL_TOTAL_SALES, SALES_ID)
            SELECT SUM(pt.PAYMENT_TRANS_TOT_AMOUNT) AS DAILY_TOTAL,
                (SELECT SUM(pt.PAYMENT_TRANS_TOT_AMOUNT) FROM PAYMENT_TRANSACTION pt) AS GENERAL_TOTAL,
                %s
            FROM PAYMENT_TRANSACTION pt
            WHERE pt.ORDER_ID = %s
            GROUP BY pt.ORDER_ID
            """
            cursor.execute(sales_history_query, (sales_id, order_id))

            self.conn.commit()
            cursor.close()
            return True

        except (Exception, psycopg2.Error) as error:
            print("Error while inserting order into the database:", error)
            self.conn.rollback()
            return False

    def handle_pay_button(self):
        confirmation_reply = self.show_confirmation_dialog(
            'Payment Confirmation', 'Are you sure you want to confirm the payment?'
        )
        if confirmation_reply == QMessageBox.Yes:
            if self.insert_order_to_database(self.get_payment_method()):
                self.show_message_box('Payment Successful', 'Payment has been successfully processed.', QMessageBox.Information)
                self.reset_order()
                self.switch_to_orderListPage()
            else:
                self.show_message_box('Payment Failed', 'An error occurred while processing the payment. Please try again.', QMessageBox.Critical)

    def get_payment_method(self):
        if self.gcashSelectRBtn.isChecked():
            return "GCash"
        elif self.cashSelectBtn.isChecked():
            return "Cash"
        else:
            return None

    def reset_order(self):
        self.order_table.setRowCount(0)
        self.order_table_2.setRowCount(0)
        self.total_price = 0.0
        self.totalPymtLbl.setText("0.00 PHP")
        self.totalPymtLbl_2.setText("0.00 PHP")
        self.Amt_ContactNum_Val.clear()
        self.changeAmount.clear()

    def show_message_box(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #1F1F1F;
            }
            QLabel {
                color: white;
            }
            QPushButton {
                background-color: #0d6efd; 
                color: white;
                border: none;
                padding: 7px;
                border-radius: 5px;
                width: 40px;
            }
            QPushButton:hover {
                background-color: #0a58ca; 
            }
            QPushButton:pressed {
                background-color: #084298; 
            } 
                                               
        """)
        msg_box.exec_()
    def show_confirmation_dialog(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Question)
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg_box.setDefaultButton(QMessageBox.No)
        msg_box.setStyleSheet("""
            QMessageBox {
                background-color: #1F1F1F;
            }
            QLabel {
                color: white;
            }
            QPushButton {
                background-color: #0d6efd; 
                color: white;
                border: none;
                padding: 7px;
                border-radius: 5px;
                width:40px;
                              
                
            }
            QPushButton:hover {
                background-color: #0a58ca; 
            }
            QPushButton:pressed {
                background-color: #084298; 
            } 
        """)
        reply = msg_box.exec_()
        return reply

       


    def show_empty_order_message(self):
        self.show_message_box("Empty Order", "Please add products to the order before proceeding.", QMessageBox.Warning)

    def show_payment_method_error(self):
        self.show_message_box("Payment Method", "Please select a payment method before proceeding.", QMessageBox.Warning)

    def show_invalid_cash_amount_error(self):
        self.show_message_box("Invalid Cash Amount", "Please enter a valid cash amount.", QMessageBox.Warning)

    def show_insufficient_cash_error(self):
        self.show_message_box("Insufficient Cash", "The cash amount is less than the total price.", QMessageBox.Warning)

    def show_invalid_gcash_number_error(self):
        self.show_message_box("Invalid Gcash Number", "Please enter a valid Gcash number.", QMessageBox.Warning)

    def show_order_success_message(self):
        self.show_message_box("Order Successful", "The order has been successfully placed.", QMessageBox.Information)

    def show_order_error_message(self):
        self.show_message_box("Order Error", "There was an error placing the order. Please try again.", QMessageBox.Critical)

    def show_length_error_message(self):
        self.show_message_box("Error", "Invalid mobile number.", QMessageBox.Critical)
    
    def show_empty_order_message(self):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Order List Empty")
        message_box.setText("Please select your order on the Menu...")
        message_box.setIcon(QMessageBox.Icon.Warning)

        message_box.setStyleSheet("""
            QMessageBox {
                
                color: #ffffff; /* White text */

                font-size: 12px; /* Text size */
                border-radius: 10px; /* Rounded corners */
            }
            QMessageBox QLabel {
                color: #ffffff; 
                font-size: 12px;
            }
            QMessageBox QPushButton {
                background-color: #0d6efd; /* Button background color */
                color: #ffffff; /* Button text color */
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QMessageBox QPushButton:hover {
                background-color: #0a58ca; /* Button hover color */
            }
            QMessageBox QPushButton:pressed {
                background-color: #084298; /* Button pressed color */
            }
        """)

        message_box.exec()

    def check_new_products(self):
        try:
            cursor = self.conn.cursor()
            query = "SELECT PROD_NAME FROM PRODUCT"
            cursor.execute(query)
            products_in_db = [product[0] for product in cursor.fetchall()]
            cursor.close()

            existing_products = []
            for child in self.scrollAreaWidgetContents.children():
                if isinstance(child, QWidget):
                    ui = child.findChild(Ui_Form)
                    if ui:
                        existing_products.append(ui.prodNameLabel.text())

            new_products = set(products_in_db) - set(existing_products)

            if new_products:
                self.add_new_products(new_products)
                print(f"New products added: {', '.join(new_products)}")
            else:
                print("No new products found in the database.")

        except (Exception, psycopg2.Error) as error:
            print("Error while checking for new products:", error)

  
    def add_new_products(self, new_products):
        if not self.scrollAreaWidgetContents.layout():
            grid_layout = QGridLayout()
            self.scrollAreaWidgetContents.setLayout(grid_layout)
        else:
            grid_layout = self.scrollAreaWidgetContents.layout()

        row, col = 0, 0
        max_cols = 4

        for product_name in new_products:
            cursor = self.conn.cursor()
            query = "SELECT PROD_NAME, PROD_PRICE FROM PRODUCT WHERE PROD_NAME = %s"
            cursor.execute(query, (product_name,))
            product = cursor.fetchone()
            cursor.close()

            if product:
                prod_name, prod_price = product

                new_product_container = QWidget()
                ui = Ui_Form()
                ui.setupUi(new_product_container)

                ui.prodNameLabel.setText(prod_name)
                ui.productBtn.clicked.connect(lambda _, name=prod_name: self.prodBtnClicked(name))

                grid_layout.addWidget(new_product_container, row, col)

                col += 1
                if col >= max_cols:
                    col = 0
                    row += 1

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            if event.pos().y() < 30:
                self.draggable = True
                self.drag_pos = event.globalPos() - self.frameGeometry().topLeft()
            else:
                self.resizing = True
                self.resize_start_pos = event.globalPos()
                self.resize_start_geometry = self.geometry()

    def mouseMoveEvent(self, event):
        if self.draggable:
            self.move(event.globalPos() - self.drag_pos)
        elif self.resizing:
            delta = event.globalPos() - self.resize_start_pos
            new_geometry = self.resize_start_geometry.adjusted(
                0, 0, delta.x(), delta.y())
            self.setGeometry(new_geometry)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False
            self.resizing = False

    


    