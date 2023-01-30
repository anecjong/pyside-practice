from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton

class LabelImage(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("QLabel Image Demo")

        image_label = QLabel()
        image_label.setPixmap(QPixmap("logo.jpg"))

        layout = QVBoxLayout()
        layout.addWidget(image_label)

        self.setLayout(layout)
        