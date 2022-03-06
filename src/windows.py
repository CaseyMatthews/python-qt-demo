from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
import sys
from random import randint

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window %s" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.w = AnotherWindow()
        self.w.show()
        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self,checked):
        print("Visible: %s" % self.w.isVisible())
        if self.w.isVisible():
            self.w.hide()
            print("Hide it")
        else:
            self.w.show()
            print("Show it")

class MainWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()

        l = QVBoxLayout()

        button1 = QPushButton("Push for Window 1")
        button1.clicked.connect(lambda checked : self.toggle_window(self.window1))
        l.addWidget(button1)

        button2 = QPushButton("Push for Window 2")
        button2.clicked.connect(lambda checked : self.toggle_window(self.window2))
        l.addWidget(button2)

        w = QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)

    def toggle_window(self, window):
        if window.isVisible():
            window.hide()
        else:
            window.show()
    

app = QApplication(sys.argv)
w = MainWindow2()
w.show()
app.exec_()