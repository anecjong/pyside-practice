from PySide6.QtWidgets import QApplication
from LabelImage import LabelImage
import sys

app = QApplication(sys.argv)

widget = LabelImage()
widget.show()

app.exec()