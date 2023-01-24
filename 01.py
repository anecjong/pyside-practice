# version 1
# from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
# import sys

# class ButtonHolder(QMainWindow):
#     def __init__(self, ):
#         super().__init__()
#         self.setWindowTitle("Button Holder app")
#         button = QPushButton("Press")
#         self.setCentralWidget(button)

# app = QApplication(sys.argv)

# window = ButtonHolder()
# window.show()

# app.exec()

# version 2
from PySide6.QtWidgets import QApplication
import sys

from ButtonHolder import ButtonHolder

app = QApplication(sys.argv)
window = ButtonHolder()
window.show()

app.exec()