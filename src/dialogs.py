import sys

from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QDialogButtonBox, QVBoxLayout, QLabel

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Dialogs')

        button = QPushButton("Press me for dialog")
        button.clicked.connect(self.button_clicked)
        self.setCentralWidget(button)

    def button_clicked(self, s):
        print("click", s)

        dlg = CustomDialog()
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel!")

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("HELLO!")
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonbox = QDialogButtonBox(QBtn)
        self.buttonbox.accepted.connect(self.accept)
        self.buttonbox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonbox)
        self.setLayout(self.layout)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()