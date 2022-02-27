import sys
from PySide2.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QListWidget, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Common Widgets")

        widget = self.lineEdit_widget()
        self.setCentralWidget(widget)

    def label_widget(self):
        widget = QLabel("Hello")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)
        widget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        widget.setPixmap(QPixmap('assets\\neon-flowers.png'))
        return widget

    def checkbox_widget(self):
        widget = QCheckBox()
        widget.setCheckState(Qt.Checked)
        widget.stateChanged.connect(self.show_state)
        return widget

    def show_state(self, s):
        print(s==Qt.Checked)
        print(s)

    def combobox_widget(self):
        widget = QComboBox()
        widget.addItems(['One', 'Two', 'Three'])

        # The default signal from currentIndexChanged sends the index
        widget.currentIndexChanged.connect(self.index_changed)

        # The same signal can send a text string
        widget.currentTextChanged.connect(self.text_changed)

        return widget

    def index_changed(self, i):
        print(i)

    def text_changed(self, t):
        print(t)

    def return_pressed(self):
        print("return pressed!")
        self.centralWidget().setText("Boom!")
    
    def selection_changed(self):
        print("selection changed")
        print(self.centralWidget().selectedText())

    def text_edited(self,s):
        print("text edited...")
        print(s)

    def list_widget(self):
        widget = QListWidget()
        widget.addItems(['one', 'two', 'three'])
        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        return widget

    def lineEdit_widget(self):
        widget = QLineEdit()
        widget.setMaxLength(15)
        widget.setPlaceholderText("Enter your text")
        widget.setInputMask('000.000.000.000:_')

        widget.returnPressed.connect(self.return_pressed)
        widget.selectionChanged.connect(self.selection_changed)
        widget.textChanged.connect(self.text_changed)
        widget.textEdited.connect(self.text_edited)

        return widget


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec_()

