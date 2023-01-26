from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("custom mainwindow")

        # menubar and menus
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("&Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        # A bunch of other menu options...
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")

        # toolbars
        toolbar = QToolBar()
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action)

        action1 = QAction("some action", self)
        action1.setStatusTip("status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)
        
        action2 = QAction(QIcon("logo.png"), "some other action", self)
        action2.setStatusTip("status message for some other action")
        action2.triggered.connect(self.toolbar_button_click)
        # action2.setCheckable(True)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("click here"))

        # status bar
        self.setStatusBar(QStatusBar(self))

        button1 = QPushButton("button1")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)

    def quit_app(self, ):
        self.app.quit()
    
    def button1_clicked(self, ):
        print("button1 clicked")
    
    def toolbar_button_click(self,):
        self.statusBar().showMessage("Message from my app", 3000) # mill seconds
        print("action triggerd")
        