import sys
from tkinter import W
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QStackedLayout, QPushButton, QTabWidget
from PySide2.QtGui import QPalette, QColor

class Color(QWidget):

    def __init__(self,color):
        super(Color,self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")

        layout = self.tab_layout()

        # widget = QWidget()
        # widget.setLayout(layout)
        self.setCentralWidget(layout)

        

    def vbox_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        return layout

    def hbox_layout(self):
        layout = QHBoxLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        return layout

    def nested_layout(self):
        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()
        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))
        layout1.addLayout( layout2 )
        layout1.addWidget(Color('green'))
        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))
        layout1.addLayout(layout3)
        return layout1

    def grid_layout(self):
        layout = QGridLayout()
        layout.addWidget(Color('red'), 0,0)
        layout.addWidget(Color('green'), 1,0)
        layout.addWidget(Color('blue'), 1,1)
        layout.addWidget(Color('purple'),2,1)
        return layout

    def stack_layout(self):
        layout = QStackedLayout()
        layout.addWidget(Color('red'))
        layout.addWidget(Color('green'))
        layout.addWidget(Color('blue'))
        layout.addWidget(Color('yellow'))
        layout.setCurrentIndex(1)
        return layout

    def stack_button_layout(self):
        layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        self.stackedLayout= QStackedLayout()
        layout.addLayout(button_layout)
        layout.addLayout(self.stackedLayout)
        btn = QPushButton('red')
        btn.pressed.connect(self.activate_tab_1)
        button_layout.addWidget(btn)
        self.stackedLayout.addWidget(Color('red'))
        btn = QPushButton('green')
        btn.pressed.connect(self.activate_tab_2)
        button_layout.addWidget(btn)
        self.stackedLayout.addWidget(Color('green'))
        btn = QPushButton('yellow')
        btn.pressed.connect(self.activate_tab_3)
        button_layout.addWidget(btn)
        self.stackedLayout.addWidget(Color('yellow'))
        return layout

    def activate_tab_1(self):
        self.stackedLayout.setCurrentIndex(0)

    def activate_tab_2(self):
        self.stackedLayout.setCurrentIndex(1)

    def activate_tab_3(self):
        self.stackedLayout.setCurrentIndex(2)

    def tab_layout(self):
        layout = QTabWidget()
        layout.setTabPosition(QTabWidget.West)
        layout.setMovable(True)

        for n,color in enumerate(['red','green','blue','purple']):
            layout.addTab(Color(color), color)

        return layout
    
app = QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()