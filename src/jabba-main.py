import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPixmap

class Constants:
    width = 1920  # Adjust width as needed
    height = 1080  # Adjust height as needed
    backgroundColor = "#ffffff"  # Adjust background color


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, Constants.width, Constants.height)
        self.setStyleSheet("background-color: " + Constants.backgroundColor + ";")

        self.animated_image = QLabel(self)
        self.animated_image.setPixmap(QPixmap(""))
        self.animated_image.setGeometry(0, 0, Constants.width, Constants.height)

        self.animated_image1 = QLabel(self)
        self.animated_image1.setPixmap(QPixmap(""))
        self.animated_image1.setGeometry(1283, 157, 467, 159)

        self.button4 = QPushButton("Newest Deliveries", self)
        self.button4.setGeometry(1283, 370, 467, 579)

        self.image = QLabel(self)
        self.image.setPixmap(QPixmap(""))
        self.image.setGeometry(1812, 22, 100, 100)

        self.button = QPushButton("Marketplace", self)
        self.button.setGeometry(143, 196, 571, 139)

        self.button1 = QPushButton("Forum", self)
        self.button1.setGeometry(143, 385, 571, 150)

        self.button2 = QPushButton("Hutts Playground", self)
        self.button2.setGeometry(143, 595, 571, 151)

        self.button3 = QPushButton("Jabba's Stocks", self)
        self.button3.setGeometry(143, 826, 571, 128)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
