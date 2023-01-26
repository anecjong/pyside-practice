from PySide6.QtWidgets import QApplication
from LayoutWidget import LayoutWidget
import sys

app = QApplication(sys.argv)

window = LayoutWidget()
window.show()

app.exec()