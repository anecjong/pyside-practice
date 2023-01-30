from PySide6.QtWidgets import QApplication
from CheckboxWidget import CheckboxWidget
import sys

app = QApplication(sys.argv)

widget = CheckboxWidget()
widget.show()

app.exec()