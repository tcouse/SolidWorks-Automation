from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Solidworks Automation Beta")

        button = QPushButton("Press Me!")

        # self.setFixedSize(QSize(1600, 1000))

        # Set the central widget of the Window.
        self.setCentralWidget(button)


app = QApplication([])

window = MainWindow()
window.show()

app.exec()
