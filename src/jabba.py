import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import Qt, QUrl

class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Login Screen")
        self.setGeometry(0, 0, 500, 300)


        # Set central widget for the main window
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Create vertical layout
        layout = QVBoxLayout()
        self.central_widget.setLayout(layout)

        
        # Add a yellow title
        title_label = QLabel("Jabba's Realm", self)
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("color: #ffcc00; font-size: 24px; font-weight: bold;")
        layout.addWidget(title_label)

        # Create and add username input field
        self.username_input = QLineEdit(self)
        self.username_input.setPlaceholderText("Username")
        self.username_input.setMaximumWidth(100)
        self.username_input.setStyleSheet("color: black;")  # Set text color to white
        layout.addWidget(self.username_input, alignment=Qt.AlignCenter)

        # Create and add password input field
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setMaximumWidth(100)
        self.password_input.setStyleSheet("color: black;")  # Set text color to white
        layout.addWidget(self.password_input, alignment=Qt.AlignCenter)

        # Create and add login button
        self.login_button = QPushButton("Login", self)# Set the width to 100 and height to 50
        self.login_button.move(960, 50)
        self.login_button.clicked.connect(self.open_new_screen)
        self.login_button.setStyleSheet("color:;")
        self.login_button.setFixedSize(100,50)
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)

        # Play background music
        self.play_background_music()

    # Method to open the new screen
    def open_new_screen(self):
        self.new_screen = MainScreen()
        self.new_screen.show()

    # Method to play background music
    def play_background_music(self):
        self.background_music = QMediaPlayer()
        url = QUrl.fromLocalFile(r"C:\Users\quent\OneDrive\Desktop\App_Programming\Audio\cantina.mp3")  # Replace with the path to your audio file
        content = QMediaContent(url)
        self.background_music.setMedia(content)
        self.background_music.setVolume(30)
        self.background_music.play()


class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Main Screen")
        self.setGeometry(0, 0, 1920, 1080)

        # Set background image for the main screen
        self.setStyleSheet("background-image: url('background_image.jpg'); background-repeat: no-repeat; background-position: center;")

        # Create vertical layout
        layout = QVBoxLayout()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.central_widget.setLayout(layout)

        # Create and add buttons
        button_names = ["Marketplace", "Jabba's Stocks", "Jabba's Hangout", "Jabba's Playground"]
        for name in button_names:
            button = QPushButton(name, self)
            button.clicked.connect(self.button_clicked)
            button.setMaximumWidth(200)
            button.setFixedSize(200,100)
            layout.addWidget(button)

    # Method to handle button clicks
    def button_clicked(self):
        sender_button = self.sender()
        if sender_button:
            button_name = sender_button.text()
            # Show corresponding placeholder image based on button clicked
            if button_name == "Marketplace":
                self.show_image_placeholder(r'')
            elif button_name == "Jabba's Stocks":
                self.show_image_placeholder("stocks_image.jpg")
            elif button_name == "Jabba's Hangout":
                self.show_image_placeholder("hangout_image.jpg")
            elif button_name == "Jabba's Playground":
                self.show_image_placeholder("playground_image.jpg")

    # Method to show placeholder images
    def show_image_placeholder(self, image_path):
        # Placeholder for image, adjust size of QLabel as per the button size
        label = QLabel(self)
        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap)
        label.setGeometry(0, 0, 150, 150)  # Adjust the size as needed
        label.show()
        # Show window in full screen
        self.showFullScreen()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec_())
