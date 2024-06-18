import psycopg2
import os
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QMainWindow, QApplication
from addItemUI import AddItemWindow
from ui_updateItemUI2 import UpdateItemWindow
from AdminMain import Ui_MainWindow
from PySide6.QtCore import Qt
from PySide6.QtGui import QGuiApplication
from database_config import get_database_config  
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMessageBox
from updateAdminModal import UpdateAdminWindow
from updateStaffModal import UpdateStaffWindow
import datetime
import re      

MONTHS = {
    1: "January",   2: "February",   3: "March",
    4: "April",     5: "May",        6: "June",
    7: "July",      8: "August",     9: "September",
    10: "October",  11: "November",  12: "December"
}

class mySideBar(QMainWindow, Ui_MainWindow):
   
    from database_config import get_database_config

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
        self.setWindowTitle("Coffito Admin")
        self.setWindowIcon(QIcon(r'C:\Users\Dennis\Desktop\POS System Coffito\CoffitoLogo (40 x 40 px).png'))

        self.conn = self.connect_to_database()
        self.draggable = False
        self.drag_pos = None
        self.resizing = False
        self.resize_start_pos = None
        self.resize_start_geometry = None
       
        # Initialize selected product attributes
        self.selected_prod_id = None
        self.selected_prod_name = None
        self.selected_prod_price = None
        self.selected_prod_category = None
       
        self.showNormal()

        self.word_iicon.setHidden(True)
        self.center_on_screen()

        self.logout1.clicked.connect(self.show_login_window)
        self.logout2.clicked.connect(self.show_login_window)

        self.dashboard1.clicked.connect(self.switch_to_dashboardPage)
        self.dashboard2.clicked.connect(self.switch_to_dashboardPage)

        self.add_item1.clicked.connect(self.switch_to_addProductPage)
        self.add_item2.clicked.connect(self.switch_to_addProductPage)

        self.update_item1.clicked.connect(self.switch_to_updateProductPage)
        self.update_item2.clicked.connect(self.switch_to_updateProductPage)

        self.delete_item1.clicked.connect(self.switch_to_deleteProductPage)
        self.delete_item1_2.clicked.connect(self.switch_to_deleteProductPage)

        self.sales_report1.clicked.connect(self.switch_to_salesReportPage)
        self.sales_report2.clicked.connect(self.switch_to_salesReportPage)

        self.mng_account1.clicked.connect(self.switch_to_manageAccountsPage)
        self.mng_account2.clicked.connect(self.switch_to_manageAccountsPage)

        self.toolButton.clicked.connect(self.maximizeOrNormalize)

        self.add_prod_button.clicked.connect(self.show_add_item_window)
       
        self.dashboardTxt.setHidden(True)
        self.fetch_total_products() #ADDED
        self.fetch_items_sold_today()  #ADDED
        self.fetch_total_sales() #ADDED

        self.AddItemWindow = AddItemWindow()
        self.AddItemWindow.addProdButton.clicked.connect(self.add_product_to_db)
        self.AddItemWindow.addProd_Name.returnPressed.connect(self.add_product_to_db)
        self.AddItemWindow.addProd_Price.returnPressed.connect(self.add_product_to_db)


        self.update_prod_button_2.clicked.connect(self.delete_selected_product)
        self.update_prod_button.clicked.connect(self.display_and_show_update_item_window)


        self.UpdateItemWindow = UpdateItemWindow()
        self.UpdateItemWindow.pushButton_32.clicked.connect(self.update_product_details)
        self.UpdateItemWindow.upProd_Name.returnPressed.connect(self.update_product_details)
        self.UpdateItemWindow.upProd_Price.returnPressed.connect(self.update_product_details)


        self.lineEdit_3.textChanged.connect(self.search_AddItem)
        self.lineEdit_4.textChanged.connect(self.search_Update)
        self.lineEdit_5.textChanged.connect(self.search_Delete)


        #admin password
        self.UpdateAdminWindow = UpdateAdminWindow()  
        self.UpdateAdminWindow.updateAdmin.clicked.connect(self.update_admin_acc)
        self.UpdateAdminWindow.adminUsername.returnPressed.connect(self.update_admin_acc)
        self.UpdateAdminWindow.admin_new_pass.returnPressed.connect(self.update_admin_acc)

        self.pushButton_21.clicked.connect(self.show_update_admin_window)

        #staff    
        self.UpdateStaffWindow = UpdateStaffWindow()
        self.UpdateStaffWindow.updateStaffBtn.clicked.connect(self.update_staff_acc)
        self.UpdateStaffWindow.staff_new_pass.returnPressed.connect(self.update_staff_acc)
        self.UpdateStaffWindow.staffUsername.returnPressed.connect(self.update_staff_acc)

        self.pushButton_22.clicked.connect(self.show_update_staff_window)

        self.dailySalesBtn.clicked.connect(self.switch_to_dailySales)
        self.monthlySalesBtn.clicked.connect(self.switch_to_monthlySales)
        self.yearlySalesBtn.clicked.connect(self.switch_to_yearlySales)
        self.itemSoldBtn.clicked.connect(self.switch_to_itemSold)

    def switch_to_dailySales(self):
        self.SalesReportStackedWidget.setCurrentIndex(0)
        self.dailySales()

    def switch_to_monthlySales(self):
        self.SalesReportStackedWidget.setCurrentIndex(1)
        self.monthlySales()
    
    def switch_to_yearlySales(self):
        self.SalesReportStackedWidget.setCurrentIndex(2)
        self.yearlySales()

    def switch_to_itemSold(self):
        self.SalesReportStackedWidget.setCurrentIndex(3) 
        
    

    def dailySales(self):
        self.dailySalesTbl.setRowCount(0)
        self.dailySalesTbl.setAlternatingRowColors(True)  # Keep alternating row colors
        
        try:
            cur = self.conn.cursor()
            query = """
                SELECT sr.SALES_DATE, SUM(pt.PAYMENT_TRANS_TOT_AMOUNT) AS TOTAL_SALES
                FROM SALES_REPORT sr
                JOIN PAYMENT_TRANSACTION pt ON sr.PAYMENT_TRANS_ID = pt.PAYMENT_TRANS_ID
                GROUP BY sr.SALES_DATE
                ORDER BY sr.SALES_DATE DESC;
            """
            cur.execute(query)
            rows = cur.fetchall()
            cur.close()

            self.dailySalesTbl.setRowCount(0)
            self.dailySalesTbl.setColumnCount(2)
            self.dailySalesTbl.setHorizontalHeaderLabels(["Date", "Total Sales"])

            # Set header properties
            header = self.dailySalesTbl.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

            font = QtGui.QFont("Inter", 10, QtGui.QFont.Medium)
            white_color = QtGui.QColor("white")

            for row_num, row_data in enumerate(rows):
                sales_date = row_data[0].strftime("%B %d, %Y")  # Format date as "Month Day, Year"
                total_sales = row_data[1]

                self.dailySalesTbl.insertRow(row_num)

                # Set item alignment, font color, and font
                item_date = QtWidgets.QTableWidgetItem(str(sales_date))
                item_date.setTextAlignment(QtCore.Qt.AlignCenter)
                item_date.setForeground(white_color)
                item_date.setFont(font)
                self.dailySalesTbl.setItem(row_num, 0, item_date)

                item_sales = QtWidgets.QTableWidgetItem(str(total_sales))
                item_sales.setTextAlignment(QtCore.Qt.AlignCenter)
                item_sales.setForeground(white_color)
                item_sales.setFont(font)
                self.dailySalesTbl.setItem(row_num, 1, item_sales)

        except (Exception, psycopg2.Error) as error:
            print("Error retrieving daily sales data from the database:", error)
            self.show_message_box("Error", f"Error retrieving daily sales data: {error}", QtWidgets.QMessageBox.Critical)


    def monthlySales(self):
        self.monthlySalesTbl.setRowCount(0)
        self.monthlySalesTbl.setAlternatingRowColors(True)  # Keep alternating row colors

        try:
            cur = self.conn.cursor()
            query = """
                SELECT TO_CHAR(sr.SALES_DATE, 'YYYY-MM') AS MONTH_YEAR, SUM(pt.PAYMENT_TRANS_TOT_AMOUNT) AS TOTAL_SALES
                FROM SALES_REPORT sr
                JOIN PAYMENT_TRANSACTION pt ON sr.PAYMENT_TRANS_ID = pt.PAYMENT_TRANS_ID
                GROUP BY TO_CHAR(sr.SALES_DATE, 'YYYY-MM')
                ORDER BY TO_CHAR(sr.SALES_DATE, 'YYYY-MM') DESC;
            """
            cur.execute(query)
            rows = cur.fetchall()
            cur.close()

            self.monthlySalesTbl.setRowCount(0)
            self.monthlySalesTbl.setColumnCount(2)
            self.monthlySalesTbl.setHorizontalHeaderLabels(["Date", "Total Sales"])

            # Set header properties
            header = self.monthlySalesTbl.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

            font = QtGui.QFont("Inter", 10, QtGui.QFont.Medium)
            white_color = QtGui.QColor("white")

            for row_num, row_data in enumerate(rows):
                month_year = row_data[0]
                total_sales = row_data[1]

                self.monthlySalesTbl.insertRow(row_num)

                # Convert month_year to readable format
                year, month = map(int, month_year.split('-'))
                formatted_date = f"{MONTHS.get(month, 'Unknown')} {year}"
                
                # Set item alignment, font color, and font
                item_month_year = QtWidgets.QTableWidgetItem(str(formatted_date))
                item_month_year.setTextAlignment(QtCore.Qt.AlignCenter)
                item_month_year.setForeground(white_color)
                item_month_year.setFont(font)
                self.monthlySalesTbl.setItem(row_num, 0, item_month_year)

                item_sales = QtWidgets.QTableWidgetItem(str(total_sales))
                item_sales.setTextAlignment(QtCore.Qt.AlignCenter)
                item_sales.setForeground(white_color)
                item_sales.setFont(font)
                self.monthlySalesTbl.setItem(row_num, 1, item_sales)

        except (Exception, psycopg2.Error) as error:
            print("Error retrieving monthly sales data from the database:", error)
            self.show_message_box("Error", f"Error retrieving monthly sales data: {error}", QtWidgets.QMessageBox.Critical)

    def yearlySales(self):
        self.yearlySalesTbl.setRowCount(0)
        self.yearlySalesTbl.setAlternatingRowColors(True)  # Keep alternating row colors

        try:
            cur = self.conn.cursor()
            query = """
                SELECT EXTRACT(YEAR FROM sr.SALES_DATE) AS YEAR, SUM(pt.PAYMENT_TRANS_TOT_AMOUNT) AS TOTAL_SALES
                FROM SALES_REPORT sr
                JOIN PAYMENT_TRANSACTION pt ON sr.PAYMENT_TRANS_ID = pt.PAYMENT_TRANS_ID
                GROUP BY EXTRACT(YEAR FROM sr.SALES_DATE)
                ORDER BY EXTRACT(YEAR FROM sr.SALES_DATE) DESC;
            """
            cur.execute(query)
            rows = cur.fetchall()
            cur.close()

            self.yearlySalesTbl.setRowCount(0)
            self.yearlySalesTbl.setColumnCount(2)
            self.yearlySalesTbl.setHorizontalHeaderLabels(["Date", "Total Sales"])

            # Set header properties
            header = self.yearlySalesTbl.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

            font = QtGui.QFont("Inter", 10, QtGui.QFont.Medium)
            white_color = QtGui.QColor("white")

            for row_num, row_data in enumerate(rows):
                year = row_data[0]
                total_sales = row_data[1]

                self.yearlySalesTbl.insertRow(row_num)

                # Set item alignment, font color, and font
                item_year = QtWidgets.QTableWidgetItem(str(year))
                item_year.setTextAlignment(QtCore.Qt.AlignCenter)
                item_year.setForeground(white_color)
                item_year.setFont(font)
                self.yearlySalesTbl.setItem(row_num, 0, item_year)

                item_sales = QtWidgets.QTableWidgetItem(str(total_sales))
                item_sales.setTextAlignment(QtCore.Qt.AlignCenter)
                item_sales.setForeground(white_color)
                item_sales.setFont(font)
                self.yearlySalesTbl.setItem(row_num, 1, item_sales)

        except (Exception, psycopg2.Error) as error:
            print("Error retrieving yearly sales data from the database:", error)
            self.show_message_box("Error", f"Error retrieving yearly sales data: {error}", QtWidgets.QMessageBox.Critical)

    def show_login_window(self):
        from ui_loginPage import Login_MainWindow

        self.login_window = Login_MainWindow()
        self.login_window.show()

    def switch_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)
        self.dashboardTxt.setText("Dashboard")
        self.dashboardTxt.setHidden(False)
        self.fetch_total_products() #ADDED
        self.fetch_items_sold_today()  #ADDED
        self.fetch_total_sales() #ADDED

    def switch_to_addProductPage(self):
        self.stackedWidget.setCurrentIndex(1)
        self.dashboardTxt.setText("Add Item")
        self.dashboardTxt.setHidden(False)
        self.fetch_products()

    def switch_to_updateProductPage(self):
        self.stackedWidget.setCurrentIndex(2)
        self.dashboardTxt.setText("Update Item")
        self.dashboardTxt.setHidden(False)
        self.fetch_products_up()

    def switch_to_deleteProductPage(self):
        self.stackedWidget.setCurrentIndex(3)
        self.dashboardTxt.setText("Delete Item")
        self.dashboardTxt.setHidden(False)
        self.fetch_products_del()

    def switch_to_salesReportPage(self):
        self.stackedWidget.setCurrentIndex(4)
        self.dashboardTxt.setText("Sales Report")
        self.dashboardTxt.setHidden(False)
        self.fetch_grand_total_sales()
        self.fetch_grand_items_sold()

    def switch_to_manageAccountsPage(self):
        self.stackedWidget.setCurrentIndex(5)
        self.dashboardTxt.setText("Manage Accounts")
        self.dashboardTxt.setHidden(False)
        self.fetch_admin_acc()
        self.fetch_staff_acc()

    def show_add_item_window(self):
        self.AddItemWindow.show()

    def show_update_item_window(self):
        self.UpdateItemWindow.show()

    def show_update_admin_window(self):
        self.UpdateAdminWindow.show()
        self.dispaly_admin_acc()

    def show_update_staff_window(self):
        self.UpdateStaffWindow.show()
        self.display_staff_acc()

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

    # def show_message_box(self, title, message, icon):
    #     msg_box = QMessageBox()
    #     msg_box.setWindowTitle(title)
    #     msg_box.setText(message)
    #     msg_box.setIcon(icon)
    #     msg_box.setStyleSheet("""
    #         QMessageBox {
    #             background-color: #1F1F1F;
    #         }
    #         QLabel {
    #             color: white;
    #         }
    #         QPushButton {
    #             background-color: #1F1F1F;
    #             color: white;
    #         }
    #     """)
    #     msg_box.exec_()
       
    def dispaly_admin_acc(self):
        username = self.label_50.text()
        password = self.label_52.text()

        self.UpdateAdminWindow.adminUsername.setText(username)
        self.UpdateAdminWindow.admin_new_pass.setText(password)

    def update_admin_acc(self):
        username = self.UpdateAdminWindow.adminUsername.text()
        newpass = self.UpdateAdminWindow.admin_new_pass.text()
        user_id = 9242

        if not username or not newpass:
            self.show_message_box("Error", f"Please Fill in all fields", QMessageBox.Critical)
            return
             
        if len(newpass) < 7:
            self.show_message_box("Error", "New password must be at least 7 characters long", QMessageBox.Critical)
            return
       
        if not re.search("[a-zA-Z]", newpass) or not re.search("[0-9]", newpass):
            self.show_message_box("Error", "New password must contain both letters and digits", QMessageBox.Critical)
            return        
        else:
            try:
                cur = self.conn.cursor()
                update_query = """
                    UPDATE USERS
                    SET USERNAME = %s,
                        PASS_WORD = %s
                    WHERE USER_ID = %s
                    """
                cur.execute(update_query, (username,newpass,user_id))
                self.conn.commit()
                cur.close()
                self.show_message_box("Success", "Updated successfully.", QMessageBox.Information)


                self.UpdateAdminWindow.hide()
                self.fetch_admin_acc()

            except (Exception, psycopg2.Error) as error:
                print("Error updating product in PostgreSQL:", error)
                self.conn.rollback()
                self.show_message_box("Error", f"{error}", QMessageBox.Critical)

    def fetch_admin_acc(self):
        user_id = 9242
        try:
            cur =self.conn.cursor()
            select_query = """
            SELECT USERNAME, PASS_WORD
            FROM USERS
            WHERE USER_ID = %s
          """
            cur.execute(select_query, (user_id,))  # Notice the comma after user_id
            row = cur.fetchone()
     
            if row:
                username = row[0]
                password = row[1]

                # Set the label text to display the username
                self.label_50.setText(username)
                self.label_52.setText(password)
                self.conn.commit()      
       
            else:
                 print("User not found.")          


        except (Exception, psycopg2.Error) as error:
            print("Error updating product in PostgreSQL:", error)
            self.conn.rollback()
            self.show_message_box("Error", f"{error}", QMessageBox.Critical)

    def fetch_staff_acc(self):
        user_id = 9243
        try:
            cur =self.conn.cursor()
            select_query = """
            SELECT USERNAME, PASS_WORD
            FROM USERS
            WHERE USER_ID = %s
          """
            cur.execute(select_query, (user_id,))  # Notice the comma after user_id
            row = cur.fetchone()
     
            if row:
                username = row[0]
                password = row[1]

                # Set the label text to display the username
                self.label_54.setText(username)
                self.label_56.setText(password)
                self.conn.commit()      
       
            else:
                 print("User not found.")          

        except (Exception, psycopg2.Error) as error:
            print("Error updating product in PostgreSQL:", error)
            self.conn.rollback()
            self.show_message_box("Error", f"{error}", QMessageBox.Critical)

    def display_staff_acc(self):
        username = self.label_54.text()
        password = self.label_56.text()

        self.UpdateStaffWindow.staffUsername.setText(username)
        self.UpdateStaffWindow.staff_new_pass.setText(password)

    def update_staff_acc(self):
        username = self.UpdateStaffWindow.staffUsername.text().lower()
        newpass = self.UpdateStaffWindow.staff_new_pass.text()
        user_id = 9243

        if not username or not newpass:
            self.show_message_box("Error", f"Please Fill in all fields", QMessageBox.Critical)
            return
             
        if len(newpass) < 7:
            self.show_message_box("Error", "New password must be at least 7 characters long", QMessageBox.Critical)
            return
       
        if not re.search("[a-zA-Z]", newpass) or not re.search("[0-9]", newpass):
            self.show_message_box("Error", "New password must contain both letters and digits", QMessageBox.Critical)
            return        
        else:
            try:
                cur = self.conn.cursor()
                update_query = """
                    UPDATE USERS
                    SET USERNAME = %s,
                        PASS_WORD = %s
                    WHERE USER_ID = %s
                    """
                cur.execute(update_query, (username,newpass,user_id))
                self.conn.commit()
                cur.close()
                self.show_message_box("Success", "Updated successfully.", QMessageBox.Information)

                self.UpdateStaffWindow.hide()
                self.fetch_staff_acc()

            except (Exception, psycopg2.Error) as error:
                print("Error updating product in PostgreSQL:", error)
                self.conn.rollback()
                self.show_message_box("Error", f"{error}", QMessageBox.Critical)

    def display_and_show_update_item_window(self):
        selected_items = self.product_table_2.selectedItems()
        if not selected_items:
            self.show_message_box("Error", "No Row Selected", QMessageBox.Warning)
            return
        else:
            row = selected_items[0].row()
            self.selected_prod_id = self.product_table_2.item(row, 0).text()
            self.selected_prod_name = self.product_table_2.item(row, 1).text()
            self.selected_prod_price = self.product_table_2.item(row, 2).text()
            self.selected_prod_category = self.product_table_2.item(row, 3).text()

            # Set retrieved data into UpdateItemWindow fields before showing it
            self.UpdateItemWindow.prodId_Label.setText(self.selected_prod_id)
            self.UpdateItemWindow.upProd_Name.setText(self.selected_prod_name)
            self.UpdateItemWindow.upProd_Price.setText(self.selected_prod_price)
            self.UpdateItemWindow.upProd_Category.setCurrentText(self.selected_prod_category)

            self.UpdateItemWindow.show()

    def update_product_details(self):
        updated_prod_id = self.UpdateItemWindow.prodId_Label.text()
        updated_prod_name = self.UpdateItemWindow.upProd_Name.text().title()
        updated_prod_price = self.UpdateItemWindow.upProd_Price.text()
        updated_prod_category = self.UpdateItemWindow.upProd_Category.currentText()

        try:
            cur = self.conn.cursor()
            update_query = """
                UPDATE PRODUCT
                SET PROD_NAME = %s,
                    PROD_PRICE = %s,
                    PROD_CATEGORY = %s
                WHERE PROD_ID = %s
            """
            cur.execute(update_query, (updated_prod_name, updated_prod_price, updated_prod_category, updated_prod_id))
            self.conn.commit()
            cur.close()

            print(f"Product with PROD_ID {updated_prod_id} updated successfully.")
            self.show_message_box("Success", "Updated successfully.", QMessageBox.Information)

            # Hide UpdateItemWindow
            self.UpdateItemWindow.hide()          
            self.fetch_products_up()

        except (Exception, psycopg2.Error) as error:
            print("Error updating product in PostgreSQL:", error)
            self.conn.rollback()  
            self.show_message_box("Error", f"{error}", QMessageBox.Critical)

     #ADDED
    def fetch_grand_total_sales(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT SUM(PAYMENT_TRANS_TOT_AMOUNT) FROM PAYMENT_TRANSACTION")
            grand_total_sales = cur.fetchone()[0]
            cur.close()
           
            # Convert the total_products to a string before setting it to the label
            self.grandTotalSalesValue.setText(str(grand_total_sales))


        except (Exception, psycopg2.Error) as error:
            print("Error retrieving products from the database: ", error)
            self.show_message_box("Error", f"Error retrieving products from the database: {error}", QMessageBox.Critical)
            return None
 #ADDED
    def fetch_total_sales(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT SUM(PAYMENT_TRANS_TOT_AMOUNT) FROM PAYMENT_TRANSACTION WHERE PAYMENT_TRANS_DATE = CURRENT_DATE")
            total_sales_today= cur.fetchone()[0]
            cur.close()
           
            # Convert the total_products to a string before setting it to the label
            if total_sales_today is not None:
                self.Dash_TotalSalesValue.setText("₱ " + str(total_sales_today))
            else:
                self.Dash_TotalSalesValue.setText("₱ 0")


        except (Exception, psycopg2.Error) as error:
            print("Error retrieving products from the database: ", error)
            self.show_message_box("Error", f"Error retrieving products from the database: {error}", QMessageBox.Critical)
            return None

    # ADDED
    def fetch_items_sold_today(self):
        try:
            cur = self.conn.cursor()
           
            # Query to get the total items sold based on the current date
            query = """
            SELECT SUM(oi.ORDER_ITEM_QTY)
            FROM ORDER_ITEMS oi
            JOIN ORDERS o ON oi.ORDER_ID = o.ORDER_ID
            WHERE o.ORDER_DATE = CURRENT_DATE
            """
           
            cur.execute(query)
            total_items_sold_today = cur.fetchone()[0]
            cur.close()
           
            # Convert the total_items_sold_today to a string before setting it to the label
            self.Dash_Total_Items_Sold.setText(str(total_items_sold_today))


        except (Exception, psycopg2.Error) as error:
            print("Error retrieving items sold from the database: ", error)
            self.show_message_box("Error", f"Error retrieving items sold from the database: {error}", QMessageBox.Critical)
            return None

    # ADDED
    def fetch_grand_items_sold(self):
        try:
            cur = self.conn.cursor()
           
            # Query to get the total items sold based on the current date
            query = """
            SELECT SUM(oi.ORDER_ITEM_QTY)
            FROM ORDER_ITEMS oi
            JOIN ORDERS o ON oi.ORDER_ID = o.ORDER_ID
            """
           
            cur.execute(query)
            total_grand_items_sold= cur.fetchone()[0]
            cur.close()
           
            # Convert the total_items_sold_today to a string before setting it to the label
            self.totat_items_sold_value.setText(str(total_grand_items_sold))


        except (Exception, psycopg2.Error) as error:
            print("Error retrieving items sold from the database: ", error)
            self.show_message_box("Error", f"Error retrieving items sold from the database: {error}", QMessageBox.Critical)
            return None

    #ADDED
    def fetch_total_products(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT COUNT(PROD_ID) FROM PRODUCT")
            total_products = cur.fetchone()[0]
            cur.close()
           
            # Convert the total_products to a string before setting it to the label
            self.DashTotalProducts.setText(str(total_products))


        except (Exception, psycopg2.Error) as error:
            print("Error retrieving products from the database: ", error)
            self.show_message_box("Error", f"Error retrieving products from the database: {error}", QMessageBox.Critical)
            return None

    def fetch_products(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT PROD_ID, PROD_NAME, PROD_PRICE, PROD_CATEGORY, TO_CHAR(CREATED_AT, 'MM-DD-YYYY') AS CREATED_DATE FROM PRODUCT")
            products = cur.fetchall()
            cur.close()
           
            self.product_table.setRowCount(0)
            self.product_table.setAlternatingRowColors(True)  # Keep alternating row colors

            # Set the header properties
            header = self.product_table.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            header.setDefaultAlignment(QtCore.Qt.AlignCenter)

            for row, product in enumerate(products):
                self.product_table.insertRow(row)
                for col, val in enumerate(product):
                    item = QtWidgets.QTableWidgetItem(str(val))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setForeground(QtGui.QColor("white"))  # Set text color to white
                    self.product_table.setItem(row, col, item)

            vertical_header = self.product_table.verticalHeader()
            vertical_header.setDefaultAlignment(QtCore.Qt.AlignCenter)

        except (Exception, psycopg2.Error) as error:
            print("Error retrieving products from the database: ", error)
            self.show_message_box("Error", f"Error retrieving products from the database:  {error}", QMessageBox.Critical)

    def fetch_products_up(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT PROD_ID, PROD_NAME, PROD_PRICE, PROD_CATEGORY, TO_CHAR(CREATED_AT, 'MM-DD-YYYY') AS CREATED_DATE FROM PRODUCT")
            products = cur.fetchall()
            cur.close()
           
            self.product_table_2.setRowCount(0)
            self.product_table_2.setAlternatingRowColors(True)  # Keep alternating row colors

            # Set the header properties
            header = self.product_table_2.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            header.setDefaultAlignment(QtCore.Qt.AlignCenter)

            for row, product in enumerate(products):
                self.product_table_2.insertRow(row)
                for col, val in enumerate(product):
                    item = QtWidgets.QTableWidgetItem(str(val))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setForeground(QtGui.QColor("white"))  # Set text color to white
                    self.product_table_2.setItem(row, col, item)


            # Center align all items in the vertical header as well
            vertical_header = self.product_table_2.verticalHeader()
            vertical_header.setDefaultAlignment(QtCore.Qt.AlignCenter)

        except (Exception, psycopg2.Error) as error:
            print("Error retrieving products from the database: ", error)
            self.show_message_box("Error", f"Error retrieving products from the database:{error}", QMessageBox.Critical)


    def fetch_products_del(self):
        try:
            cur = self.conn.cursor()
            cur.execute("SELECT PROD_ID, PROD_NAME, PROD_PRICE, PROD_CATEGORY, TO_CHAR(CREATED_AT, 'MM-DD-YYYY') AS CREATED_DATE FROM PRODUCT")
            products = cur.fetchall()
            cur.close()

            self.product_table_3.setRowCount(0)
            self.product_table_3.setAlternatingRowColors(True)  # Keep alternating row colors

            # Set the header properties
            header = self.product_table_3.horizontalHeader()
            header.setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
            header.setDefaultAlignment(QtCore.Qt.AlignCenter)

            for row, product in enumerate(products):
                self.product_table_3.insertRow(row)
                for col, val in enumerate(product):
                    item = QtWidgets.QTableWidgetItem(str(val))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    item.setForeground(QtGui.QColor("white"))  # Set text color to white
                    self.product_table_3.setItem(row, col, item)

            vertical_header = self.product_table_3.verticalHeader()
            vertical_header.setDefaultAlignment(QtCore.Qt.AlignCenter)


        except (Exception, psycopg2.Error) as error:
            print("Error retrieving products from the database: ", error)
            self.show_message_box("Error", f"Error retrieving products from the database: {error}", QMessageBox.Critical)


    def add_product_to_db(self):
        product_name = self.AddItemWindow.addProd_Name.text().title()
        product_price = self.AddItemWindow.addProd_Price.text()
        product_category = self.AddItemWindow.addProd_Category.currentText()

        if product_price == "" or product_name == " ":
                self.show_message_box("Error", "Please fill in the fields", QMessageBox.Critical)
                return
        try:
            float(product_price)        
        except ValueError:
            self.show_message_box("Error", "Product price must be a valid numeric value.", QMessageBox.Critical)
            return
   
        try:
            cur = self.conn.cursor()
            insert_query = """
                INSERT INTO PRODUCT (PROD_NAME, PROD_PRICE, PROD_CATEGORY)
                VALUES (%s, %s, %s)
                RETURNING PROD_ID, PROD_NAME, PROD_PRICE, PROD_CATEGORY, TO_CHAR(CREATED_AT, 'MM-DD-YYYY') AS CREATED_DATE
            """
            cur.execute(insert_query, (product_name, product_price, product_category))
            self.conn.commit()

            # Fetch the newly inserted product
            new_product = cur.fetchone()
            cur.close()
            print("Product added successfully:", new_product)
            self.show_message_box("Success", "Product added successfully.", QMessageBox.Information)

            # Clear input fields
            self.AddItemWindow.addProd_Name.clear()
            self.AddItemWindow.addProd_Price.clear()
            self.AddItemWindow.addProd_Category.setCurrentIndex(0)

            # Hide the AddItemWindow and switch back to the "Add Product" page
            self.AddItemWindow.hide()
            self.stackedWidget.setCurrentIndex(1)  # Switch to the "Add Product" page
            self.fetch_products()
               
        except (Exception, psycopg2.Error) as error:
            print("Error while inserting product to PostgreSQL:", error)
            self.conn.rollback()  # Rollback the transaction to ensure the connection is in a good state
            self.show_message_box("Error", f" {error}", QMessageBox.Critical)


    def delete_selected_product(self):
        selected_row = self.product_table_3.currentRow()
        if selected_row == -1:
            self.show_message_box("Error", "No Row Selected", QMessageBox.Warning)
            return
       
        prod_id = int(self.product_table_3.item(selected_row, 0).text())  # Assuming PROD_ID is in the first column
        try:
         
            print(f"Product with PROD_ID {prod_id} deleted successfully.")
            result = self.show_confirmation_dialog("Confirmation", "Are you sure you want to delete this product?")
            if result == QMessageBox.Yes:
                cur = self.conn.cursor()
                delete_query = "DELETE FROM PRODUCT WHERE PROD_ID = %s"
                cur.execute(delete_query, (prod_id,))
                self.conn.commit()
                cur.close()
                # Code to delete the product...
                self.show_message_box("Success", "Deleted successfully.", QMessageBox.Information)
                self.fetch_products_del()  # Assuming fetch_products_del refreshes product_table_3
            else:
                self.fetch_products_del()  # Assuming fetch_products_del refreshes product_table_3
                                     
        except (Exception, psycopg2.Error) as error:
            print("Error deleting product:", error)
            # QMessageBox.critical(self, "Error", f"Error deleting product: {error}")
            self.show_message_box("Error", f"Error deleting product:{error}", QMessageBox.Critical)


#SEARCH BAR
    def search_AddItem(self):
        search_text = self.lineEdit_3.text()

        # Clear previous search results in the table
        self.product_table.setRowCount(0)

        try:
            cur = self.conn.cursor()
            if search_text:
                # Adjust the query as needed based on the table structure
                search_query = """
                    SELECT PROD_ID, PROD_NAME, PROD_PRICE, PROD_CATEGORY, TO_CHAR(CREATED_AT, 'MM-DD-YYYY') AS CREATED_DATE
                    FROM PRODUCT
                    WHERE PROD_NAME ILIKE %s OR CAST(PROD_ID AS TEXT) ILIKE %s OR PROD_PRICE::TEXT ILIKE %s OR PROD_CATEGORY ILIKE %s
                    OR PROD_CATEGORY ILIKE %s OR TO_CHAR(CREATED_AT, 'MM-DD-YYYY') ILIKE %s
                """
                search_params = (f"%{search_text}%",) * 6  # Repeat %s six times for six placeholders
                cur.execute(search_query, search_params)


            else:              
                self.fetch_products()
                return

            results = cur.fetchall()
            cur.close()

            if results:
                for row, result in enumerate(results):
                    self.product_table.insertRow(row)
                    for col, val in enumerate(result):
                        item = QtWidgets.QTableWidgetItem(str(val))
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        item.setForeground(QtGui.QColor("white"))  # Set text color to white
                        self.product_table.setItem(row, col, item)

        except (Exception, psycopg2.Error) as error:
            print("Error retrieving search results from the database:", error)
            self.show_message_box("Error", f"Error retrieving search results: {error}", QMessageBox.Critical)


    def search_Update(self):
        search_text = self.lineEdit_4.text()

        self.product_table_2.setRowCount(0)

        try:
            cur = self.conn.cursor()
            if search_text:
            # Adjust the query as needed based on the table structure
                search_query = """
                    SELECT PROD_ID, PROD_NAME, PROD_PRICE, PROD_CATEGORY, TO_CHAR(CREATED_AT, 'MM-DD-YYYY') AS CREATED_DATE
                    FROM PRODUCT
                    WHERE PROD_NAME ILIKE %s OR CAST(PROD_ID AS TEXT) ILIKE %s OR PROD_PRICE::TEXT ILIKE %s OR PROD_CATEGORY ILIKE %s
                    OR PROD_CATEGORY ILIKE %s OR TO_CHAR(CREATED_AT, 'MM-DD-YYYY') ILIKE %s
                """
                search_params = (f"%{search_text}%",) * 6  # Repeat %s six times for six placeholders
                cur.execute(search_query, search_params)
            else:              
                self.fetch_products_up()
                return

            results = cur.fetchall()
            cur.close()

            if results:
                for row, result in enumerate(results):
                    self.product_table_2.insertRow(row)
                    for col, val in enumerate(result):
                        item = QtWidgets.QTableWidgetItem(str(val))
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        item.setForeground(QtGui.QColor("white"))  # Set text color to white
                        self.product_table_2.setItem(row, col, item)

        except (Exception, psycopg2.Error) as error:
            print("Error retrieving search results from the database:", error)
            self.show_message_box("Error", f"Error retrieving search results: {error}", QMessageBox.Critical)
   
    def search_Delete(self):
        search_text = self.lineEdit_5.text()

        # Clear previous search results in the table
        self.product_table_3.setRowCount(0)

        try:
            cur = self.conn.cursor()
            if search_text:
                # Adjust the query as needed based on the table structure
                search_query = """
                    SELECT PROD_ID, PROD_NAME, PROD_PRICE, PROD_CATEGORY, TO_CHAR(CREATED_AT, 'MM-DD-YYYY') AS CREATED_DATE
                    FROM PRODUCT
                    WHERE PROD_NAME ILIKE %s OR CAST(PROD_ID AS TEXT) ILIKE %s OR PROD_PRICE::TEXT ILIKE %s OR PROD_CATEGORY ILIKE %s
                    OR PROD_CATEGORY ILIKE %s OR TO_CHAR(CREATED_AT, 'MM-DD-YYYY') ILIKE %s
                """
                search_params = (f"%{search_text}%",) * 6  # Repeat %s six times for six placeholders
                cur.execute(search_query, search_params)


            else:              
                self.fetch_products_del()
                return


            results = cur.fetchall()
            cur.close()

            if results:
                for row, result in enumerate(results):
                    self.product_table_3.insertRow(row)
                    for col, val in enumerate(result):
                        item = QtWidgets.QTableWidgetItem(str(val))
                        item.setTextAlignment(QtCore.Qt.AlignCenter)
                        item.setForeground(QtGui.QColor("white"))  # Set text color to white
                        self.product_table_3.setItem(row, col, item)

        except (Exception, psycopg2.Error) as error:
            print("Error retrieving search results from the database:", error)
            self.show_message_box("Error", f"Error retrieving search results: {error}", QMessageBox.Critical)


    def maximizeOrNormalize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

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

    def normalizeWindow(self):
        self.showNormal()

    def center_on_screen(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()

        center_point = screen_geometry.center()

        window_rect = self.frameGeometry()
        window_rect.moveCenter(center_point)

        self.move(window_rect.topLeft())
