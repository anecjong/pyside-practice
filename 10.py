from PySide6.QtWidgets import QApplication
from SizePolicyStretch import SizePolicyStretch
import sys

app = QApplication(sys.argv)

widget = SizePolicyStretch()
widget.show()

app.exec()