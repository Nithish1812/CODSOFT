import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QLabel, QTableWidget, 
                             QTableWidgetItem, QMessageBox, QHeaderView)
from PyQt5.QtCore import Qt

class ContactHub(QWidget):
    def __init__(self):
        super().__init__()
        # Professional Branding
        self.setWindowTitle("Nithish-ContactHub | CodSoft Task 5")
        self.setFixedSize(600, 700)
        
        # Data storage (In-memory for this task)
        self.contacts = {} 
        
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)

        # --- BRANDED HEADER ---
        self.title_label = QLabel("NITHISH-CONTACTHUB")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            QLabel {
                color: #FF5722; 
                font-size: 26px; 
                font-weight: bold;
                background-color: #2D2D2D;
                padding: 15px;
                border-radius: 12px;
            }
        """)
        layout.addWidget(self.title_label)

        # --- INPUT FIELDS ---
        input_layout = QVBoxLayout()
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Full Name")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Phone Number")
        
        field_style = """
            QLineEdit {
                font-size: 16px; 
                padding: 10px; 
                border: 2px solid #DDD; 
                border-radius: 8px;
                margin-bottom: 5px;
            }
            QLineEdit:focus { border: 2px solid #FF5722; }
        """
        self.name_input.setStyleSheet(field_style)
        self.phone_input.setStyleSheet(field_style)
        
        input_layout.addWidget(self.name_input)
        input_layout.addWidget(self.phone_input)
        layout.addLayout(input_layout)

        # --- BUTTONS ---
        btn_layout = QHBoxLayout()
        self.add_btn = QPushButton("Add Contact")
        self.del_btn = QPushButton("Delete Selected")
        
        self.add_btn.setStyleSheet("background-color: #FF5722; color: white; font-weight: bold; height: 40px; border-radius: 8px;")
        self.del_btn.setStyleSheet("background-color: #757575; color: white; font-weight: bold; height: 40px; border-radius: 8px;")
        
        self.add_btn.clicked.connect(self.add_contact)
        self.del_btn.clicked.connect(self.delete_contact)
        
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.del_btn)
        layout.addLayout(btn_layout)

        # --- SEARCH BAR ---
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Search contacts by name...")
        self.search_input.setStyleSheet("font-size: 14px; padding: 8px; border-radius: 20px; border: 1px solid #FF5722; margin-top: 10px;")
        self.search_input.textChanged.connect(self.search_contact)
        layout.addWidget(self.search_input)

        # --- CONTACT TABLE ---
        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["NAME", "PHONE NUMBER"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setStyleSheet("""
            QTableWidget { gridline-color: #EEE; font-size: 14px; border: 1px solid #DDD; border-radius: 5px; }
            QHeaderView::section { background-color: #F5F5F5; font-weight: bold; border: none; padding: 5px; }
        """)
        layout.addWidget(self.table)

        self.setLayout(layout)

    def add_contact(self):
        name = self.name_input.text().strip().title()
        phone = self.phone_input.text().strip()
        
        if name and phone:
            self.contacts[name] = phone
            self.update_table()
            self.name_input.clear()
            self.phone_input.clear()
        else:
            QMessageBox.warning(self, "Error", "Please fill in both Name and Phone!")

    def update_table(self, data_dict=None):
        if data_dict is None:
            data_dict = self.contacts
            
        self.table.setRowCount(0)
        for name, phone in data_dict.items():
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(name))
            self.table.setItem(row_position, 1, QTableWidgetItem(phone))

    def delete_contact(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            name_to_del = self.table.item(selected_row, 0).text()
            del self.contacts[name_to_del]
            self.update_table()
        else:
            QMessageBox.information(self, "Select Row", "Please click a row to delete.")

    def search_contact(self):
        query = self.search_input.text().title()
        filtered = {k: v for k, v in self.contacts.items() if query in k}
        self.update_table(filtered)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = ContactHub()
    window.show()
    sys.exit(app.exec_())