# # 1 - button click
# from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow

# def button_clicked(data):
#     print(f"you clicked the button, checked: {data}")

# app = QApplication()
# main_window = QMainWindow()
# main_window.show()

# button = QPushButton("press")
# button.setCheckable(True)
# main_window.setCentralWidget(button)

# button.clicked.connect(button_clicked)

# app.exec()

# # 2 - slider
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QSlider

def respond_to_slider(data):
    print(f"slider moved to : {data}")

app = QApplication()

main_window = QMainWindow()
main_window.show()

slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

slider.valueChanged.connect(respond_to_slider)
main_window.setCentralWidget(slider)

app.exec()