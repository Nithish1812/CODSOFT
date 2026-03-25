import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
                             QPushButton, QLabel)
from PyQt5.QtCore import Qt

class NithishPyGame(QWidget):
    def __init__(self):
        super().__init__()
        # Professional Branding for Task 4
        self.setWindowTitle("Nithish-PyGame | CodSoft Task")
        # Widened to 600 to ensure everything fits comfortably
        self.setFixedSize(600, 800) 
        
        self.user_score = 0
        self.comp_score = 0
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(25, 30, 25, 30)
        layout.setSpacing(15)

        # --- BRANDED HEADER ---
        self.title_label = QLabel("NITHISH-PYGAME")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            QLabel {
                color: #FF5722; 
                font-size: 32px; 
                font-weight: bold;
                background-color: #2D2D2D;
                padding: 20px;
                border-radius: 15px;
            }
        """)
        layout.addWidget(self.title_label)

        # --- BIG & COLORFUL RULES BOX ---
        # Made this section larger and colored for high visibility
        self.rules_label = QLabel("📜 GAME RULES\nRock > Scissors | Scissors > Paper | Paper > Rock")
        self.rules_label.setAlignment(Qt.AlignCenter)
        self.rules_label.setStyleSheet("""
            QLabel {
                color: #2D2D2D; 
                font-size: 18px; 
                font-weight: bold;
                background-color: #FFECB3; /* Light Yellow Highlight */
                border: 2px solid #FFA000;
                padding: 15px;
                border-radius: 10px;
            }
        """)
        layout.addWidget(self.rules_label)

        # --- SCOREBOARD ---
        self.score_label = QLabel("YOU: 0  ⭐  COMP: 0")
        self.score_label.setAlignment(Qt.AlignCenter)
        self.score_label.setStyleSheet("font-size: 26px; font-weight: bold; color: #333; margin: 10px;")
        layout.addWidget(self.score_label)

        # --- BIG RESULT DISPLAY ---
        self.result_display = QLabel("READY TO PLAY?")
        self.result_display.setAlignment(Qt.AlignCenter)
        self.result_display.setFixedHeight(150)
        self.result_display.setStyleSheet("""
            QLabel {
                font-size: 22px;
                border: 4px dashed #FF5722;
                border-radius: 20px;
                background: #FFFFFF;
                color: #888;
                padding: 10px;
            }
        """)
        layout.addWidget(self.result_display)

        # --- CHOICE BUTTONS ---
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(15)
        
        choices = [("Rock", "✊"), ("Paper", "✋"), ("Scissors", "✌️")]
        
        for name, emoji in choices:
            btn = QPushButton(f"{emoji}\n{name}")
            # Buttons widened to 170px to prevent "Scissors" clipping
            btn.setFixedSize(175, 175) 
            btn.setCursor(Qt.PointingHandCursor)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #333;
                    color: white;
                    font-size: 30px; 
                    font-weight: bold;
                    border-radius: 25px;
                }
                QPushButton:hover {
                    background-color: #FF5722;
                    margin-top: -5px;
                }
            """)
            btn.clicked.connect(lambda checked, m=name: self.play_round(m))
            btn_layout.addWidget(btn)
        
        layout.addLayout(btn_layout)

        # --- RESET BUTTON ---
        self.reset_btn = QPushButton("Reset Game History")
        self.reset_btn.clicked.connect(self.reset_game)
        self.reset_btn.setStyleSheet("color: #999; border: none; font-size: 16px; text-decoration: underline; margin-top: 20px;")
        layout.addWidget(self.reset_btn, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def play_round(self, user_choice):
        options = ["Rock", "Paper", "Scissors"]
        comp_choice = random.choice(options)
        emojis = {"Rock": "✊", "Paper": "✋", "Scissors": "✌️"}
        
        if user_choice == comp_choice:
            msg = f"TIE! {emojis[user_choice]}\nBoth chose {user_choice}"
            border_color = "#9E9E9E"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            msg = f"WINNER! 🏆\n{user_choice} {emojis[user_choice]} beats {comp_choice}"
            self.user_score += 1
            border_color = "#4CAF50"
        else:
            msg = f"LOST! 💀\n{comp_choice} {emojis[comp_choice]} beats {user_choice}"
            self.comp_score += 1
            border_color = "#F44336"

        self.result_display.setText(msg)
        self.result_display.setStyleSheet(f"""
            QLabel {{
                font-size: 24px; 
                font-weight: bold;
                border: 5px solid {border_color}; 
                border-radius: 20px; 
                color: {border_color}; 
                background: white;
            }}
        """)
        self.score_label.setText(f"YOU: {self.user_score}  ⭐  COMP: {self.comp_score}")

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.score_label.setText("YOU: 0  ⭐  COMP: 0")
        self.result_display.setText("NEW GAME STARTED!")
        self.result_display.setStyleSheet("font-size: 22px; border: 4px dashed #FF5722; border-radius: 20px; background: #FFF; color: #888;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = NithishPyGame()
    window.show()
    sys.exit(app.exec_())