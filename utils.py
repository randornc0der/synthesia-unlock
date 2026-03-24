from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtGui import QColor
import os

listr = []

appdata = str(os.getenv("APPDATA"))
appfolder = appdata + "\\Synthesia"

shadow = QGraphicsDropShadowEffect()
shadow.setBlurRadius(10)
shadow.setOffset(3, 3)
shadow.setColor(QColor(0, 0, 0, 150))

shadow1 = QGraphicsDropShadowEffect()
shadow1.setBlurRadius(10)
shadow1.setOffset(3, 5)
shadow1.setColor(QColor(0, 0, 0, 150))