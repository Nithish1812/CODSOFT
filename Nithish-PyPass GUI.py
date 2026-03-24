import sys
import random
import string
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLineEdit, QPushButton, QLabel, QCheckBox, QSlider)
from PyQt5.QtCore import Qt

class NithishPyPass(QWidget):
    def __init__(self):
        super().__init__()
        # Professional Branding
        self.setWindowTitle("Nithish-PyPass | Strong Generator")
        self.setFixedSize(400, 500)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(25, 25, 25, 25)

        # --- HEADER ---
        self.title_label = QLabel("NITHISH-PYPASS")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            QLabel {
                color: #FF5722; 
                font-size: 24px; 
                font-weight: bold;
                background-color: #2D2D2D;
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 10px;
            }
        """)
        layout.addWidget(self.title_label)

        # --- PASSWORD DISPLAY ---
        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setPlaceholderText("Your Password Appears Here")
        self.result_display.setAlignment(Qt.AlignCenter)
        self.result_display.setFixedHeight(60)
        self.result_display.setStyleSheet("""
            QLineEdit {
                font-size: 18px;
                border: 2px solid #FF5722;
                border-radius: 8px;
                color: #333;
                background: #FFF;
            }
        """)
        layout.addWidget(self.result_display)

        # --- LENGTH CONTROL ---
        self.len_label = QLabel("Password Length: 12")
        self.len_label.setStyleSheet("font-weight: bold; margin-top: 10px;")
        layout.addWidget(self.len_label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(8)
        self.slider.setMaximum(32)
        self.slider.setValue(12)
        self.slider.valueChanged.connect(self.update_label)
        layout.addWidget(self.slider)

        # --- OPTIONS ---
        self.nums_cb = QCheckBox("Include Numbers (0-9)")
        self.syms_cb = QCheckBox("Include Symbols (!@#$)")
        self.nums_cb.setChecked(True)
        self.syms_cb.setChecked(True)
        
        cb_style = "QCheckBox { font-size: 14px; padding: 5px; }"
        self.nums_cb.setStyleSheet(cb_style)
        self.syms_cb.setStyleSheet(cb_style)
        
        layout.addWidget(self.nums_cb)
        layout.addWidget(self.syms_cb)

        # --- BUTTONS ---
        self.gen_btn = QPushButton("GENERATE STRONG PASSWORD")
        self.gen_btn.setFixedHeight(50)
        self.gen_btn.setStyleSheet("""
            QPushButton {
                background-color: #FF5722;
                color: white;
                font-weight: bold;
                border-radius: 8px;
                margin-top: 10px;
            }
            QPushButton:hover { background-color: #E64A19; }
        """)
        self.gen_btn.clicked.connect(self.generate)
        layout.addWidget(self.gen_btn)

        self.copy_btn = QPushButton("Copy to Clipboard")
        self.copy_btn.clicked.connect(self.copy)
        self.copy_btn.setStyleSheet("color: #555; border: none; text-decoration: underline;")
        layout.addWidget(self.copy_btn)

        self.setLayout(layout)

    def update_label(self, value):
        self.len_label.setText(f"Password Length: {value}")

    def generate(self):
        length = self.slider.value()
        char_pool = string.ascii_letters
        if self.nums_cb.isChecked():
            char_pool += string.digits
        if self.syms_cb.isChecked():
            char_pool += string.punctuation

        password = "".join(random.choice(char_pool) for _ in range(length))
        self.result_display.setText(password)

    def copy(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.result_display.text())
        self.copy_btn.setText("✅ Copied!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = NithishPyPass()
    window.show()
    sys.exit(app.exec_())