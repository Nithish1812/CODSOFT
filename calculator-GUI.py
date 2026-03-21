import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QGridLayout, QLineEdit, QPushButton)
from PyQt5.QtCore import Qt

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CodSoft Task 2: Calculator")
        self.setFixedSize(300, 400)
        self.initUI()

    def initUI(self):
        # Main Layout
        layout = QVBoxLayout()

        # Display screen
        self.display = QLineEdit()
        self.display.setFixedHeight(50)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("font-size: 20px; padding: 5px;")
        layout.addWidget(self.display)

        # Buttons Grid
        grid = QGridLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row, col = 0, 0
        for button_text in buttons:
            btn = QPushButton(button_text)
            btn.setFixedSize(60, 60)
            btn.setStyleSheet("font-size: 18px;")
            btn.clicked.connect(self.on_click)
            grid.addWidget(btn, row, col)
            
            col += 1
            if col > 3:
                col = 0
                row += 1

        layout.addLayout(grid)
        self.setLayout(layout)

    def on_click(self):
        button = self.sender()
        text = button.text()

        if text == '=':
            try:
                # eval() handles the math logic automatically
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except Exception:
                self.display.setText("Error")
        elif text == 'C':
            self.display.clear()
        else:
            current_text = self.display.text()
            self.display.setText(current_text + text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = CalculatorApp()
    calc.show()
    sys.exit(app.exec_())