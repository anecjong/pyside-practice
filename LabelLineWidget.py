from PySide6.QtWidgets import QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton

class LabelLineWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("QLabel and QLineEdit")

        label = QLabel("Full name: ")
        self.line_edit = QLineEdit()
        self.line_edit.textChanged.connect(self.text_changed)
        self.line_edit.cursorPositionChanged.connect(self.cursor_position_change)
        self.line_edit.editingFinished.connect(self.editing_finished)
        self.line_edit.returnPressed.connect(self.return_pressed)
        self.line_edit.selectionChanged.connect(self.selection_changed)
        self.line_edit.textEdited.connect(self.text_edited)

        button = QPushButton("Grab data")
        button.clicked.connect(self.button_clicked)

        self.text_grab_label = QLabel("text button click: ")
        self.text_change_label = QLabel("text changed: ")

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_grab_label)
        v_layout.addWidget(self.text_change_label)

        self.setLayout(v_layout)
    
    def button_clicked(self):
        self.text_grab_label.setText("text button click: " + self.line_edit.text())

    def text_changed(self):
        self.text_change_label.setText("text changed: " + self.line_edit.text())

    def cursor_position_change(self, old, new):
        print(f"cursor old position: {old}, new position: {new}")
    
    def editing_finished(self, ):
        print("Editing finished")

    def return_pressed(self, ):
        print("Return Pressed")
    
    def selection_changed(self):
        print("Selection Changed: ", self.line_edit.selectedText())
    
    def text_edited(self, new_text):
        print("text edited:", new_text)