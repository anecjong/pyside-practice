from PySide6.QtWidgets import QApplication
from GridLayout import GridLayout
import sys

app = QApplication(sys.argv)

widget = GridLayout()
widget.show()

app.exec()