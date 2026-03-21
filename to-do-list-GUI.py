import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QMessageBox, QListWidget, 
                             QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout)

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CodSoft Task 1: To-Do List")
        self.setGeometry(300, 300, 400, 400)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Type a new task here...")
        
        self.add_btn = QPushButton("Add Task")
        self.del_btn = QPushButton("Delete Selected")
        self.list_widget = QListWidget()

        self.add_btn.clicked.connect(self.add_task)
        self.del_btn.clicked.connect(self.delete_task)

        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_btn)
        self.layout.addWidget(self.list_widget)
        self.layout.addWidget(self.del_btn)
        self.setLayout(self.layout)

    def add_task(self):
        text = self.input_field.text()
        if text:
            self.list_widget.addItem(text)
            self.input_field.clear()

    def delete_task(self):
        selected = self.list_widget.currentRow()
        if selected >= 0:
            self.list_widget.takeItem(selected)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TodoApp()
    ex.show()
    sys.exit(app.exec_())