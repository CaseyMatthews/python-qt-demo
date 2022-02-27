import sys

from PySide2.QtCore import Qt
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow, QTextEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Click in this window")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")

    def mousePressEvent(self,e):
        if e.button() == Qt.LeftButton:
            # handle left-button press
            self.label.setText("mousePressEvent LEFT")

        elif e.button() == Qt.MiddleButton:
            
            self.label.setText("mousePressEvent MIDDLE")
        
        elif e.button() == Qt.RightButton:
            self.label.setTExt("mousePressEvent RIGHT")

    def mouseReleaseEvent(self,e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self,e):
        self.label.setText("mouseDoubleClickEvent")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()