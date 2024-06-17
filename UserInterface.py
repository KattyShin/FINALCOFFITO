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

        self.product_buttons = {
            'AMERICANO': self.product1,
            'CARAMEL': self.product2,
            'LATTE': self.product3,
            'VANILLA': self.product4,
            'MOCHA': self.product5,
            'MATCHA': self.product6,
            'ICED CHOCO': self.product7,
            'SPANISH LATTE': self.product8,
            'AMERICAN VANILLA': self.product9,
            'VIETNAMESE LATTE': self.product10,
            'STRAWBERRY LATTE': self.product11,
            'MATCHA COFFEE': self.product12,
            'UBE LATTE': self.product13,
        }

        self.product_widgets = {
            'AMERICANO': self.widget_5,
            'CARAMEL': self.widget_6,
            'LATTE': self.widget_7,
            'VANILLA': self.widget_8,
            'MOCHA': self.widget_14,
            'MATCHA': self.widget_15,
            'ICED CHOCO': self.widget_16,
            'SPANISH LATTE': self.widget_13,
            'AMERICAN VANILLA': self.widget_19,
            'VIETNAMESE LATTE': self.widget_18,
            'STRAWBERRY LATTE': self.widget_20,
            'MATCHA COFFEE': self.widget_17,
            'UBE LATTE': self.widget_23,
        }
        
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
        
        

        for product_name, button in self.product_buttons.items():
            button.clicked.connect(lambda _, name=product_name: self.prodBtnClicked(name))

        self.removeProdOrder.clicked.connect(self.removeSelectedRow)

        self.timer = QTimer(self)
        self.timer.setInterval(1000)  # Update time every second
        self.timer.timeout.connect(self.update_date_time)
        self.timer.start()

        self.date_time_label = self.DateTimeLabel

        self.searchMenuItem.textChanged.connect(self.filter_products)

        self.Amt_ContactNum_Val.textChanged.connect(self.calculate_change)

        self.payButton.clicked.connect(self.payButtonClicked)
        

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
            # Move items from order_table to order_table_2
            self.proceed_to_summary_page()

            # Set current index to order summary page
            self.stackedWidget_2.setCurrentIndex(1)
        

    def switch_to_orderListPage(self):
        self.stackedWidget_2.setCurrentIndex(0)
        

    def filter_products(self):
        search_text = self.searchMenuItem.text().lower()
        
        for product_name, widget in self.product_widgets.items():
            if search_text in product_name.lower():
                widget.show()
            else:
                widget.hide()

    def update_date_time(self):
        current_date_time = self.get_current_date_time()
        self.date_time_label.setText(current_date_time)

    def get_current_date_time(self):
        current_time = QTime.currentTime().toString('hh:mm:ss')
        current_date = QDate.currentDate()
        month_number = current_date.month()
        month_text = MONTHS[month_number]  # Convert month number to text
        date_string = f"{month_text} {current_date.day()} {current_date.year()}"
        return f"{date_string} {current_time}"

    def show_database_error(self):
        QMessageBox.critical(self, "Database Connection Error", "Failed to connect to the database. Please check your configuration.")

    # def prodBtnClicked(self, productName):
    #     cursor = self.conn.cursor()
    #     query = "SELECT PROD_NAME, PROD_PRICE, PROD_QUANTITY FROM PRODUCT WHERE PROD_NAME = %s"
    #     cursor.execute(query, (productName,))
    #     product = cursor.fetchone()
    #     cursor.close()

    #     if product:
    #         prod_name, prod_price, prod_quantity = product
    #         print(f"Product Name: {prod_name}, Price: {prod_price}, Quantity: {prod_quantity}")
    #         self.updateOrderTable(prod_name, prod_price, prod_quantity)
    #         self.calculateTotalPrice()
    #     else:
    #         print(f"Product '{productName}' not found in the database.")
    

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
            self.conn.rollback()  # Rollback the transaction on error
            # Optionally handle the error or notify the user

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

            # Set item name
            name_item = QTableWidgetItem(item_name)
            name_item.setTextAlignment(Qt.Alignment.AlignCenter)  
            self.order_table_2.setItem(row_position, 0, name_item)
            

            # Set item price
            price_item = QTableWidgetItem(str(item_price))
            price_item.setTextAlignment(Qt.Alignment.AlignCenter)
            self.order_table_2.setItem(row_position, 1, price_item)

            # Set item quantity
            quantity_item = QTableWidgetItem(str(item_quantity))
            quantity_item.setTextAlignment(Qt.Alignment.AlignCenter)
            self.order_table_2.setItem(row_position, 2, quantity_item)

            # Update total price for order summary
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
                item.setForeground(QColor("white"))  # Set foreground color to white
                item.setTextAlignment(Qt.Alignment.AlignCenter)  # Center align text again

                # Ensure quantity_item alignment stays centered
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
            QMessageBox.information(self, "No Row Selected", "Please select a row to remove.")

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
        
        # Update the QLabel with the calculated total price
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

        self.handle_pay_button()

    # def insert_order_to_database(self, payment_method):
    #     try:
    #         # Insert into ORDER_SUMMARY
    #         cursor = self.conn.cursor()

    #         # Assuming you have the staff ID and customer ID available
    #         staff_id = 8742  # Replace with actual staff ID
    #         # cus_id = 1242  # Replace with actual customer ID
            

    #         # Insert into CUSTOMER to get new CUS_ID
    #         cursor.execute("INSERT INTO CUSTOMER DEFAULT VALUES RETURNING CUS_ID;")
    #         cus_id = cursor.fetchone()[0]
                

    #         order_summary_query = """
    #         INSERT INTO ORDER_SUMMARY (STAFF_ID, CUS_ID, TOTAL_AMOUNT, PAYMENT_METHOD, PAYMENT_DETAILS)
    #         VALUES (%s, %s, %s, %s, %s) RETURNING ORDER_SUM_ID;
    #         """
    #         order_summary_values = (
    #             staff_id,
    #             cus_id,
    #             self.total_price,
    #             payment_method,
    #             self.Amt_ContactNum_Val.text() if self.Amt_ContactNum_Val.isVisible() else None
    #         )

    #         cursor.execute(order_summary_query, order_summary_values)
    #         order_sum_id = cursor.fetchone()[0]

    #         # Insert into ORDER_ITEMS
    #         order_items_query = """
    #         INSERT INTO ORDER_ITEMS (ORDER_SUM_ID, PROD_ID, QUANTITY, PRICE)
    #         VALUES (%s, %s, %s, %s);
    #         """

    #         for row in range(self.order_table.rowCount()):
    #             item_name = self.order_table.item(row, 0).text()
    #             item_price = float(self.order_table.item(row, 1).text())
    #             item_quantity = int(self.order_table.item(row, 2).text())

    #             cursor.execute("SELECT PROD_ID FROM PRODUCT WHERE PROD_NAME = %s", (item_name,))
    #             prod_id = cursor.fetchone()[0]

    #             order_items_values = (order_sum_id, prod_id, item_quantity, item_price)
    #             cursor.execute(order_items_query, order_items_values)

    #         self.conn.commit()
    #         cursor.close()
    #         return True
    #     except (Exception, psycopg2.Error) as error:
    #         print("Error while inserting order into the database:", error)
    #         self.conn.rollback()
    #         return False

    def insert_order_to_database(self, payment_method):
        try:
            cursor = self.conn.cursor()

            # Assuming you have the staff ID available
            staff_id = 8742  # Replace with actual staff ID

            # Insert into CUSTOMER to get new CUS_ID
            cursor.execute("INSERT INTO CUSTOMER DEFAULT VALUES RETURNING CUS_ID;")
            cus_id = cursor.fetchone()[0]

            # Insert into ORDERS
            order_summary_query = """
            INSERT INTO ORDERS (STAFF_ID, CUS_ID)
            VALUES (%s, %s) RETURNING ORDER_ID;
            """
            cursor.execute(order_summary_query, (staff_id, cus_id))
            order_id = cursor.fetchone()[0]

            # Insert into ORDER_ITEMS
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
                order_item_id = cursor.fetchone()[0]  # Fetch the ORDER_ITEM_ID if needed

            # Insert into PAYMENT_TRANSACTION
            payment_trans_query = """
            INSERT INTO PAYMENT_TRANSACTION (ORDER_ID, PAYMENT_TRANS_TOT_AMOUNT, PAYMENT_TRANS_METHOD, PAYMENT_TRANS_DETAILS)
            VALUES (%s, %s, %s, %s);
            """
            cursor.execute(payment_trans_query, (order_id, self.total_price, payment_method, self.Amt_ContactNum_Val.text() if self.Amt_ContactNum_Val.isVisible() else None))

            self.conn.commit()
            cursor.close()
            return True
        except (Exception, psycopg2.Error) as error:
            print("Error while inserting order into the database:", error)
            self.conn.rollback()
            return False






    def handle_pay_button(self):
        confirmation_reply = QMessageBox.question(
            self, 'Payment Confirmation', 'Are you sure you want to confirm the payment?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if confirmation_reply == QMessageBox.Yes:
            if self.insert_order_to_database(self.get_payment_method()):
                QMessageBox.information(self, 'Payment Successful', 'Payment has been successfully processed.')
                self.reset_order()
                self.switch_to_orderListPage()
            else:
                QMessageBox.critical(self, 'Payment Failed', 'An error occurred while processing the payment. Please try again.')

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


    def show_empty_order_message(self):
        QMessageBox.warning(self, "Empty Order", "Please add products to the order before proceeding.")

    def show_payment_method_error(self):
        QMessageBox.warning(self, "Payment Method", "Please select a payment method before proceeding.")

    def show_invalid_cash_amount_error(self):
        QMessageBox.warning(self, "Invalid Cash Amount", "Please enter a valid cash amount.")

    def show_insufficient_cash_error(self):
        QMessageBox.warning(self, "Insufficient Cash", "The cash amount is less than the total price.")

    def show_invalid_gcash_number_error(self):
        QMessageBox.warning(self, "Invalid Gcash Number", "Please enter a valid Gcash number.")

    def show_order_success_message(self):
        QMessageBox.information(self, "Order Successful", "The order has been successfully placed.")

    def show_order_error_message(self):
        QMessageBox.critical(self, "Order Error", "There was an error placing the order. Please try again.")
    
    def show_empty_order_message(self):
        message_box = QMessageBox(self)
        message_box.setWindowTitle("Order List Empty")
        message_box.setText("Please select your order on the Menu...")
        message_box.setIcon(QMessageBox.Icon.Warning)

        # Customize the stylesheet for the QMessageBox
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

            existing_products = set(self.product_buttons.keys())
            new_products = set(products_in_db) - existing_products

            if new_products:
                self.add_new_products(new_products)
                print(f"New products added: {', '.join(new_products)}")
            else:
                print("No new products found in the database.")

        except (Exception, psycopg2.Error) as error:
            print("Error while checking for new products:", error)

    # def add_new_products(self, new_products):
    #     if not self.scrollAreaWidgetContents.layout():
    #         self.scrollAreaWidgetContents.setLayout(QBoxLayout())

    #     for product_name in new_products:
    #         cursor = self.conn.cursor()
    #         query = "SELECT PROD_NAME, PROD_PRICE, PROD_QUANTITY FROM PRODUCT WHERE PROD_NAME = %s"
    #         cursor.execute(query, (product_name,))
    #         product = cursor.fetchone()
    #         cursor.close()

    #         if product:
    #             prod_name, prod_price, prod_quantity = product

    #             new_product_container = QWidget()
    #             ui = Ui_Form()
    #             ui.setupUi(new_product_container)

    #             ui.prodNameLabel.setText(prod_name)
                


    #             ui.productBtn.clicked.connect(lambda _, name=prod_name, quantity=prod_quantity: self.prodBtnClicked(name, quantity))

    #             self.scrollAreaWidgetContents.layout().addWidget(new_product_container)

    #             self.product_buttons[prod_name] = ui.productBtn
    #             self.product_widgets[prod_name] = new_product_container

    def add_new_products(self, new_products):
        if not self.scrollAreaWidgetContents.layout():
            self.scrollAreaWidgetContents.setLayout(QBoxLayout())

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
                ui.prodPriceLabel.setText(f"Price: {prod_price} PHP")  # Displaying product price

                ui.productBtn.clicked.connect(lambda _, name=prod_name: self.prodBtnClicked(name))

                self.scrollAreaWidgetContents.layout().addWidget(new_product_container)

                self.product_buttons[prod_name] = ui.productBtn
                self.product_widgets[prod_name] = new_product_container


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

    


    