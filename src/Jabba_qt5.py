import sys
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPalette, QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, Qt
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


class SubWindow(QWidget):
    def __init__(self, name, window_class):
        super().__init__()
        self.name = name
        self.window_class = window_class


        self.button = QPushButton(name)
        self.button.clicked.connect(self.open_window)
        self.button.setStyleSheet("font-size: 14px; font-weight: bold; background-color: #ffcc00; color: black")


    def open_window(self):
        self.window = self.window_class()
        self.window.show()


class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Login Screen")
        self.setFixedSize(500, 300)

        # Create and set the background image directly on the central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Set background image using Stylesheet
        background_image_path = r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\Background_stern.png"  # Replace "background_image.jpg" with the path to your image
        central_widget.setStyleSheet(f"background-image: url({background_image_path}); background-repeat: no-repeat; background-position: center;")

        layout = QVBoxLayout(central_widget)
        
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
        self.login_button.clicked.connect(self.login)
        self.login_button.setStyleSheet("font-size: 12px; background-color: #ffcc00; color: black")
        
        # Create and add register button
        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register)
        self.register_button.setStyleSheet("font-size: 12px; background-color: #ffcc00; color: black")

        # Create and add forgot password button
        self.forgot_password_button = QPushButton("Forgot Password?")
        self.forgot_password_button.clicked.connect(self.forgot_password)
        self.forgot_password_button.setStyleSheet("font-size: 12px; background-color: #ffcc00; color: black")

        # Layout setup
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(title_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.username_input, alignment=Qt.AlignCenter)
        layout.addWidget(self.password_input, alignment=Qt.AlignCenter)
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.register_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.forgot_password_button, alignment=Qt.AlignCenter)
        
        # Horizontal layout for logo
        h_layout = QHBoxLayout()
        h_layout.addStretch(1)
        #h_layout.addWidget(self.logo_label)
        layout.addLayout(h_layout)

        # Play background music for login screen
        self.play_background_music(r"H:\Inf10\App_Programming\music\Intro.mp3")

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
    
        # Check if username or password fields are empty
        if not username or not password:
            QMessageBox.warning(self, "Login Failed", "Please enter both username and password.")
            return

        # Check credentials against the database
        conn = sqlite3.connect(r"H:\Inf10\App_Programming\database\jabbas-data_voll.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
    
        # If user exists, go to main screen, otherwise show error message
        if user:
            self.mediaPlayer.stop()
            self.new_screen = MainScreen()
            self.new_screen.show()
            self.close()
        else:
            QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        
        # Open registration dialog
        dialog = RegisterDialog(self)
        if dialog.exec_():
            email = dialog.email_input.text()
            region = dialog.region_dropdown.currentText()  # Get the selected region from the dropdown

    def forgot_password(self):
        dialog = ForgotPasswordDialog(self)
        dialog.exec_()

    def play_background_music(self, music_file):
        self.mediaPlayer = QMediaPlayer()
        url = QUrl.fromLocalFile(music_file)
        content = QMediaContent(url)
        self.mediaPlayer.setMedia(content)
        self.mediaPlayer.setVolume(10)
        self.mediaPlayer.play()

class RegisterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Register")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.region_dropdown = QComboBox()
        self.region_dropdown.addItems(["Abafar", "Agamar", "Ahch-To", "Ajan Kloss", "Akiva", "Alderaan", "Aldhani", "Aleen", "Alzoc III", "Anaxes", "Ando", "Anoat", "Atollon", "Barton 4", "Balnab", "Batuu", "Bespin", "Bogano", "Bora Vio", "Bracca", "Cantonica", "Castilon", "Cato Neimoidia", "Chandrilla", "Chrustophsis", "Concord Dawn", "Corellia", "Coruscant", "Crait", "Daiyu", "D'Qar", "Dagobah", "Dantooine", "Dathomir", "Devaron", "Eadu", "Endor", "Er´kit", "Eriadu", "Esseles", "Exegol", "Felucia", "Ferrix", "Florrum", "Fondor", "Geonosis", "Hosnian Prime", "Hoth", "Illum", "Iridonia", "Jabiim", "Jakku", "Jedha", "Jelucan", "Jestefad", "Kamino", "Kashyyyk", "Kef Bir", "Kessel", "Kijimi", "Koboh", "Kuat", "Lah'mu", "Lothal", "Lotho Minor", "Malachor", "Malastare", "Mandalore", "Mapuzo", "Maridun", "Miban", "Mon Cala", "Moraband", "Mortis", "Mustafar", "Mygeeto", "Naboo", "Nal Hutta", "Nevarro", "Niamos", "Numidian Prime", "Nur", "Onderon", "Ord Mantell", "Ossus", "Pasaana", "Pillio", "Polis Massa", "Rishi", "Rodia", "Rugosa", "Ruusan", "Ryloth", "Saleucami", "Savareen", "Scarif", "Seatos", "Serenno", "Shili", "Sissubo", "Skako Minor", "Sorgan", "Subterrel", "Sullust", "Takodana", "Tanalor", "Umbara", "Utapau", "Vandor-1", "Vardos", "Wobani", "Wrea", "Yavin", "Yavin 4", "Zeffo", "Zygerria"
])  # Add your region options here

        register_button = QPushButton("Register")
        register_button.clicked.connect(self.register)
        
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)
        layout.addWidget(self.email_input)
        layout.addWidget(self.region_dropdown)
        layout.addWidget(register_button)

        self.setLayout(layout)
    
    def register(self):
        username = self.username_input.text()
        password = self.password_input.text()
        email = self.email_input.text()
        region = self.region_dropdown.currentText()

        # Save user to the database
        conn = sqlite3.connect(r"H:\Inf10\App_Programming\database\jabbas-data_voll.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users(username, password, email, region) VALUES (?, ?, ?, ?)", (username, password, email, region))
        conn.commit()
        conn.close()

        self.accept()





class ForgotPasswordDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Forgot Password")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        retrieve_password_button = QPushButton("Retrieve Password")
        retrieve_password_button.clicked.connect(self.retrieve_password_from_database)
        
        layout.addWidget(self.email_input)
        layout.addWidget(retrieve_password_button)

        self.setLayout(layout)

    def retrieve_password_from_database(self):
        email = self.email_input.text()
        password = self.parent().retrieve_password_from_database(email)
        if password:
            self.send_password_email(email, password)  # Sendet das Passwort per E-Mail
            QMessageBox.information(self, "Password Retrieval", "An email has been sent to your email address with the password.")  # Anzeige der Bestätigungsmeldung
            self.accept()
        else:
            QMessageBox.warning(self, "Password Retrieval Failed", "No user with this email exists.")


    def send_password_email(self, email, password):
        sender_email = "jabbasrealm@outlook.com"  # Ihre E-Mail-Adresse
        sender_password = "realmjabbas123"  # Ihr E-Mail-Passwort
        recipient_email = email
        subject = "Password Recovery"
        body = f"Ihr Passwort lautet: {password}"

        # E-Mail-Nachricht zusammenstellen
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Verbindung zum SMTP-Server herstellen und E-Mail senden
        with smtplib.SMTP_SSL("smtp-mail.outlook.com", 587) as server:
            server.login(sender_email, sender_password)  # Anmeldung am Server
            server.send_message(message)  # E-Mail senden

    def retrieve_password_from_database(self, email):
        conn = sqlite3.connect(r"H:\Inf10\App_Programming\database\jabbas-data_voll.db")
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM users WHERE email=?", (email,))
        password = cursor.fetchone()
        conn.close()
        return password[0] if password else None

class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle("Main Screen")
        self.setGeometry(100, 100, 500, 500)

        # Set background image
        self.background_label = QLabel()
        self.background_label.setScaledContents(True)
        self.set_background_image(self.background_label, "pictures/Background_stern.png")

        # Add a fancy title
        title_label = QLabel("Jabba's Realm")
        title_label.setStyleSheet("font-size: 36px; font-weight: bold; color: #ffcc00")

        # Create and add buttons for news feed
        button_names = ["Marketplace", "Jabba's Stocks", "Hutts Playground", "Jabba's Hangout"]
        self.button_widgets = []
        self.windows = {}  # Dictionary to store window objects
        for name in button_names:
            button = QPushButton(name)
            button.clicked.connect(lambda state, button_name=name: self.open_sub_window(button_name))
            button.setStyleSheet("font-size: 14px; font-weight: bold; background-color: #ffcc00; color: black")
            self.button_widgets.append(button)

        # Add image in the top right corner
        self.logo_label = QLabel()
        self.logo_label.setScaledContents(True)
        self.set_background_image(self.logo_label, "pictures/credits.png")

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
        self.play_background_music(r"H:\Inf10\App_Programming\music\cantina.mp3")

    def set_background_image(self, label, image_path):
        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap)

    def open_sub_window(self, name):
        if name not in self.windows:
            if name == "Marketplace":
                self.windows[name] = MarketplaceWindow()  # Store the window object in the dictionary
            elif name == "Jabba's Stocks":
                self.windows[name] = StocksWindow()
            elif name == "Hutts Playground":
                self.windows[name] = PlaygroundWindow()
            elif name == "Jabba's Hangout":
                self.windows[name] = HangoutWindow()
        self.windows[name].show()  # Show the window

    def play_background_music(self, music_file):
        self.mediaPlayer = QMediaPlayer()
        url = QUrl.fromLocalFile(music_file)
        content = QMediaContent(url)
        self.mediaPlayer.setMedia(content)
        self.mediaPlayer.setVolume(30)
        self.mediaPlayer.play()


class TooltipWindow(QDialog):
    def __init__(self, tooltip_text):
        super().__init__()
        self.setWindowTitle("Tooltip")
        self.setGeometry(300, 300, 200, 100)

        layout = QVBoxLayout()
        self.tooltip_label = QLabel(tooltip_text)
        self.tooltip_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.tooltip_label)

        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        layout.addWidget(exit_button)

        self.setLayout(layout)

class MarketplaceWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title and full-screen mode
        self.setWindowTitle("Marketplace")
        self.showFullScreen()

        # Dropdown menu for categories
        self.category_dropdown = QComboBox()
        self.category_dropdown.addItems(["droid", "vehicle", "weapon","spaceship","republic_destroyer"])  # Add your categories here
        self.category_dropdown.currentIndexChanged.connect(self.show_images)

        # Create a scroll area for the images
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.inner_widget = QWidget(self.scroll_area)
        self.scroll_area.setWidget(self.inner_widget)
        self.scroll_layout = QGridLayout(self.inner_widget)
        self.scroll_layout.setHorizontalSpacing(0)  # Set horizontal spacing to 0

        # Initial images (placeholder)
        self.show_images()

        # Create a layout for the window
        layout = QVBoxLayout(self)
        layout.addWidget(self.category_dropdown)
        layout.addWidget(self.scroll_area)

    def show_images(self):
        selected_category = self.category_dropdown.currentText()
        if selected_category == "droid":
            image_paths = [
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\b1.jpeg",
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\destroyer.jpeg",
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\droid3.jpeg",
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\droid4.jpeg",
                # Add more image paths for Category "droid"
            ]
            tooltips = [
                "B1 Battledroid",
                "Destroyer Droid",
                "Droid 3",
                "Droid 4",
                # Add more tooltips for Category "droid"
            ]
        elif selected_category == "vehicle":
            image_paths = [
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\xWing.jpeg",
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\vehicle2.jpeg",
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\vehicle3.jpeg",
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\vehicle4.jpeg",
                # Add more image paths for Category "vehicle"
            ]
            tooltips = [
                "x-Wing",
                "Vehicle 2",
                "Vehicle 3",
                "Vehicle 4",
                # Add more tooltips for Category "vehicle"
            ]
        elif selected_category == "weapon":
            image_paths = [
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\weapon1.jpeg",
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\weapon2.jpeg",
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\weapon3.jpeg",
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\weapon4.jpeg",
                # Add more image paths for Category "weapon"
            ]
            tooltips = [
                "Weapon 1",
                "Weapon 2",
                "Weapon 3",
                "Weapon 4",
                # Add more tooltips for Category "weapon"
            ]
        elif selected_category == "spaceship":
            image_paths = [
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\spaceship1.jpeg",
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\spaceship2.jpeg",
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\spaceship3.jpeg",
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\spaceship4.jpeg",
                # Add more image paths for Category "spaceship"
            ]
            tooltips = [
                "Spaceship 1",
                "Spaceship 2",
                "Spaceship 3",
                "Spaceship 4",
                # Add more tooltips for Category "spaceship"
            ]
        elif selected_category == "republic_destroyer":
            image_paths = [
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\destroyer1.jpeg",
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\destroyer2.jpeg",
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\destroyer3.jpeg",
                r"C:\Users\quent\OneDrive\Desktop\App_Programming\pictures\destroyer4.jpeg",
                # Add more image paths for Category "republic_destroyer"
            ]
            tooltips = [
                "Destroyer 1",
                "Destroyer 2",
                "Destroyer 3",
                "Destroyer 4",
                # Add more tooltips for Category "republic_destroyer"
            ]

        # Clear existing images
        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.itemAt(i).widget().deleteLater()

        # Add images to the scroll layout with tooltips
        row = 0
        col = 0
        for path, tooltip_text in zip(image_paths, tooltips):
            placeholder_image = QLabel()
            pixmap = QPixmap(path)
            pixmap = pixmap.scaled(200, 200, Qt.KeepAspectRatio)  # Resize images to fit properly
            placeholder_image.setPixmap(pixmap)
            placeholder_image.setAlignment(Qt.AlignCenter)
            placeholder_image.setToolTip(tooltip_text)  # Set the tooltip text
            placeholder_image.mousePressEvent = lambda event, tooltip=tooltip_text: self.show_tooltip(tooltip)
            self.scroll_layout.addWidget(placeholder_image, row, col)
            col += 1
            if col == 7:  # Limit to 7 images per row
                row += 1
                col = 0

    def show_tooltip(self, tooltip_text):
        self.tooltip_window = TooltipWindow(tooltip_text)
        self.tooltip_window.exec_()


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
