import sys
from PySide2.QtWidgets import (
    QMainWindow, QApplication, QCheckBox,
    QLabel, QToolBar, QAction, QStatusBar
)
from PySide2.QtGui import QIcon, QKeySequence
from PySide2.QtCore import Qt, QSize

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Menus')
        label = QLabel("Hello")
        label.setAlignment(Qt.AlignCenter)

        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        button_action = QAction(QIcon("assets/acorn.png"), "&Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)

        button_action.setShortcut(QKeySequence("Ctrl+p"))

        toolbar.addAction(button_action)

        toolbar.addSeparator()

        button_action2 = QAction(QIcon('assets/acorn.png'), "Your &button2", self)
        button_action2.setStatusTip("This is your button 2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)

        toolbar.addWidget(QLabel("hello"))
        toolbar.addWidget(QCheckBox())
        self.setStatusBar(QStatusBar(self))

        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)

        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)

    def onMyToolBarButtonClick(self, s):
        print("click", s)

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()