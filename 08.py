from PySide6.QtWidgets import QApplication
from TextEditWidget import TextEditWidget
import sys

app = QApplication(sys.argv)

widget = TextEditWidget()
widget.show()

app.exec()