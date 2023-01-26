from PySide6.QtWidgets import QApplication
from PushButtonWIdget import PushButtonWidget
import sys

app = QApplication(sys.argv)

widget = PushButtonWidget()
widget.show()

app.exec()