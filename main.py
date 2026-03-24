from PySide6.QtWidgets import QApplication
from ui import build_ui
from core import check

import sys

check()

app = QApplication()
win = build_ui()
win.show()

app.exec()