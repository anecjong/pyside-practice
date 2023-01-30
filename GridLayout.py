from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget,  QSizePolicy, QGridLayout, QPushButton, QLabel

class GridLayout(QWidget):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("QGridLayout Demo")

        button_1 = QPushButton("Button 1")
        button_2 = QPushButton("Button 2")
        button_3 = QPushButton("Button 3")
        button_4 = QPushButton("Button 4")
        button_5 = QPushButton("Button 5")
        img_label = QLabel()
        img_label.setPixmap(QPixmap("logo.jpg"))

        grid_layout = QGridLayout()
        grid_layout.addWidget(button_1,0,0)
        grid_layout.addWidget(button_2,0,1) #Take up 1 row and 2 columns
        grid_layout.addWidget(button_3,0,2) #Take up 2 rows and 1 column
        grid_layout.addWidget(button_4,1,0)
        grid_layout.addWidget(button_5,2,0)
        grid_layout.addWidget(img_label,1,1, 2, 2)

        self.setLayout(grid_layout)