from PySide6.QtWidgets import QApplication, QWidget

# processing cli argumetns
import sys

# enclose all
app = QApplication(sys.argv)

window = QWidget()
# default: hidden
window.show()

# start event loop
app.exec()