from PySide6.QtWidgets import QApplication
from LabelLineWidget import LabelLineWidget
import sys

app = QApplication(sys.argv)

widget = LabelLineWidget()
widget.show()

app.exec()