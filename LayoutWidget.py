from PySide6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout

class LayoutWidget(QWidget):
    def __init__(self, ):
        super().__init__()
        self.setWindowTitle("LayoutWidget")

        # button location? -> layout
        # button_layout = QHBoxLayout()
        button_layout = QVBoxLayout()

        self.button1 = QPushButton("Button 1")
        button_layout.addWidget(self.button1)

        self.button2 = QPushButton("Button 2")
        button_layout.addWidget(self.button2)

        self.set_signal()

        self.setLayout(button_layout)
    
    def set_signal(self,):
        self.button1.clicked.connect(self.button1_clicked)
        self.button2.clicked.connect(self.button2_clicked)
    
    def button1_clicked(self, ):
        print("button1 clicked")

    def button2_clicked(self, ):
        print("button2 clicked")

