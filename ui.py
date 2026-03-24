from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from core import inject, getit
from utils import shadow, shadow1

def build_ui():
    global win

    win = QWidget()
    win.setWindowTitle("Synthesia Tooler 1.0")
    win.setGeometry(10, 580, 304, 130)

    vbox = QVBoxLayout()
    vbox.setSpacing(0)

    title = QLabel("Press The Button Below\nTo Use Synthesia")
    button = QPushButton("Synthesia")

    win.setStyleSheet("background-color:#1c718c;")
    title.setStyleSheet("color: White; font-style: bold; background-color:")
    title.setGraphicsEffect(shadow)
    button.setStyleSheet("background-color: #00A9FF;")
    button.setGraphicsEffect(shadow1)

    vbox.addWidget(title, alignment=Qt.AlignmentFlag.AlignCenter)
    vbox.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)

    win.setLayout(vbox)

    timer = QTimer()
    timer.timeout.connect(getit)
    timer.start(1000)

    button.pressed.connect(inject)

    return win