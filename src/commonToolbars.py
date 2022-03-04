import sys
from PySide2.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QAction, QStatusBar
)
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("My Awesome App")

        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        toolbar = QToolBar("My Main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        button_action = QAction(QIcon("assets/acorn.png"),"Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click",s)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()