from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
import sys

# command line arguments -> sys.argv
app = QApplication(sys.argv)
print(sys.argv)

# create qt widget
# window is hidden by default
# window = QWidget()
# window.show()

# push button
# window = QPushButton("push button")
# window.show()

class MainWindow(QMainWindow):
    def __init__(self, ) -> None:
        super().__init__()
        self.setWindowTitle("My Application")
        button = QPushButton("press button")
        self.setCentralWidget(button)
        self.setFixedSize(400, 300)

window = MainWindow()
window.show()

# start event loop
app.exec()