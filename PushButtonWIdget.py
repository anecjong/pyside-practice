from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

class PushButtonWidget(QWidget):
    def __init__(self,):
        super().__init__()

        self.setWindowTitle("Custom Mainwindow")
        
        button = QPushButton("Click")
        button.clicked.connect(self.button_clicked)
        button.pressed.connect(self.button_pressed)
        button.released.connect(self.button_released)

        layout = QVBoxLayout()
        layout.addWidget(button)

        self.setLayout(layout)


    def button_clicked(self):
        print("clicked")

    def button_pressed(self):
        print("pressed")

    def button_released(self):
        print("released")