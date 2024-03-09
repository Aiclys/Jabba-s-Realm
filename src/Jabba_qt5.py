import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QFrame
from PyQt5.QtGui import QPixmap
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, Qt

class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Login Screen")
        self.setGeometry(100, 100, 500, 300)

        # Set background image
        self.background_label = QLabel()
        self.background_label.setScaledContents(True)
        self.set_background_image(self.background_label, "pictures/Background_stern.png")
        
        # Add a yellow title
        title_label = QLabel("Jabba's Realm")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #ffcc00")
        
        # Create and add username input field
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        
        # Create and add password input field
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        
        # Create and add login button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.open_new_screen)
        self.login_button.setStyleSheet("font-size: 12px; background-color: #ffcc00; color: black")


        # Layout setup
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(title_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.username_input, alignment=Qt.AlignCenter)
        layout.addWidget(self.password_input, alignment=Qt.AlignCenter)
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)
        
        # Horizontal layout for logo
        h_layout = QHBoxLayout()
        h_layout.addStretch(1)
        #h_layout.addWidget(self.logo_label)
        layout.addLayout(h_layout)

        # Play background music for login screen
        self.play_background_music(r"C:\Users\quent\OneDrive\Desktop\App_Programming\Audio\Tatooine.mp3")

    def set_background_image(self, label, image_path):
        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap)

    def open_new_screen(self):
        self.mediaPlayer.stop()
        self.new_screen = MainScreen()
        self.new_screen.show()
        self.close()

    def play_background_music(self, music_file):
        self.mediaPlayer = QMediaPlayer()
        url = QUrl.fromLocalFile(music_file)
        content = QMediaContent(url)
        self.mediaPlayer.setMedia(content)
        self.mediaPlayer.setVolume(30)
        self.mediaPlayer.play()

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Main Screen")
        self.setGeometry(100, 100, 500, 500)

        # Set background image
        self.background_label = QLabel()
        self.background_label.setScaledContents(True)
        self.set_background_image(self.background_label, r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\Background_stern.png")

        # Add a fancy title
        title_label = QLabel("Jabba's Realm")
        title_label.setStyleSheet("font-size: 36px; font-weight: bold; color: #ffcc00")

        # Create and add buttons for news feed
        button_names = ["Marketplace", "Jabba's Stocks", "Hutts Playground", "Jabba's Hangout"]
        self.button_widgets = []
        for name in button_names:
            button = QPushButton(name)
            button.clicked.connect(lambda state, button_name=name: self.open_sub_window(button_name))
            button.setStyleSheet("font-size: 14px; font-weight: bold; background-color: #ffcc00; color: black")
            self.button_widgets.append(button)

        # Add image in the top right corner
        self.logo_label = QLabel()
        self.logo_label.setScaledContents(True)
        self.set_background_image(self.logo_label, r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\credits.png")

        # Layout setup
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(title_label, alignment=Qt.AlignCenter)
        for button in self.button_widgets:
            layout.addWidget(button, alignment=Qt.AlignCenter)
        layout.addStretch(1)

        # Horizontal layout for logo
        h_layout = QHBoxLayout()
        h_layout.addStretch(1)
        h_layout.addWidget(self.logo_label)
        layout.addLayout(h_layout)

        # Play background music for main screen
        self.play_background_music(r"C:\Users\quent\OneDrive\Desktop\App_Programming\Audio\cantina.mp3")

    def set_background_image(self, label, image_path):
        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap)

    def open_sub_window(self, name):
        if name == "Marketplace":
            marketplace_window = MarketplaceWindow()
            marketplace_window.show()
        elif name == "Jabba's Stocks":
            stocks_window = StocksWindow()
            stocks_window.show()
        elif name == "Hutts Playground":
            playground_window = PlaygroundWindow()
            playground_window.show()
        elif name == "Jabba's Hangout":
            hangout_window = HangoutWindow()
            hangout_window.show()

    def play_background_music(self, music_file):
        self.mediaPlayer = QMediaPlayer()
        url = QUrl.fromLocalFile(music_file)
        content = QMediaContent(url)
        self.mediaPlayer.setMedia(content)
        self.mediaPlayer.setVolume(30)
        self.mediaPlayer.play()

class MarketplaceWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Marketplace")
        self.setGeometry(100, 100, 300, 200)

        label = QLabel("Marketplace")
        label.setStyleSheet("font-size: 16px;")
        layout = QVBoxLayout(self)
        layout.addWidget(label, alignment=Qt.AlignCenter)

class StocksWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Jabba's Stocks")
        self.setGeometry(100, 100, 300, 200)

        label = QLabel("This is the Jabba's Stocks window.")
        label.setStyleSheet("font-size: 16px;")
        layout = QVBoxLayout(self)
        layout.addWidget(label, alignment=Qt.AlignCenter)

class PlaygroundWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Hutts Playground")
        self.setGeometry(100, 100, 300, 200)

        label = QLabel("This is the Hutts Playground window.")
        label.setStyleSheet("font-size: 16px;")
        layout = QVBoxLayout(self)
        layout.addWidget(label, alignment=Qt.AlignCenter)

class HangoutWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Jabba's Hangout")
        self.setGeometry(100, 100, 300, 200)

        label = QLabel("This is the Jabba's Hangout window.")
        label.setStyleSheet("font-size: 16px;")
        layout = QVBoxLayout(self)
        layout.addWidget(label, alignment=Qt.AlignCenter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec_())
