from PySide6.QtWidgets import QWidget,  QCheckBox, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton,QButtonGroup

class CheckboxWidget(QWidget):
    def __init__(self):
        super().__init__()
       
        self.setWindowTitle("QCheckBox and QRadioButton")

        credit = QGroupBox("Credit")
        credit_A = QCheckBox("A")
        credit_A.toggled.connect(self.a_box_toggled)
        credit_B = QCheckBox("B")
        credit_B.toggled.connect(self.b_box_toggled)
        credit_C = QCheckBox("C")
        credit_C.toggled.connect(self.c_box_toggled)

        credit_layout = QVBoxLayout()
        credit_layout.addWidget(credit_A)
        credit_layout.addWidget(credit_B)
        credit_layout.addWidget(credit_C)
        credit.setLayout(credit_layout)

        job = QGroupBox("Job status")
        student = QCheckBox("student")
        jobless = QCheckBox("jobless")
        professor = QCheckBox("professor")
        
        exclusive_button_group = QButtonGroup(self)
        exclusive_button_group.addButton(student)
        exclusive_button_group.addButton(jobless)
        exclusive_button_group.addButton(professor)
        exclusive_button_group.setExclusive(True)

        job_layout = QVBoxLayout()
        job_layout.addWidget(student)
        job_layout.addWidget(professor)
        job_layout.addWidget(jobless)
        job.setLayout(job_layout)

        h_layout = QHBoxLayout()
        h_layout.addWidget(credit)
        h_layout.addWidget(job)

        self.setLayout(h_layout)
    
    def a_box_toggled(self, checked):
        if checked:
            print("a? really?")

    def b_box_toggled(self, checked):
        if checked:
            print("b.. just b")

    def c_box_toggled(self, checked):
        if checked:
            print("c. under the sea")