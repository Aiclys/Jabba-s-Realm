import sys
import random
import numpy as np
import matplotlib
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas, 
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPalette, QColor, QShowEvent
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl, Qt, QTimer
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import uuid

class SubWindow(QWidget):
    def __init__(self, name, window_class):
        super().__init__()
        self.name = name
        self.window_class = window_class

        self.button = QPushButton(name)
        self.button.clicked.connect(self.open_window)
        self.button.setStyleSheet("font-size: 14px; font-weight: bold; background-color: #ffcc00; color: black")

        self.windows = {}

    def open_window(self):
        if self.name not in self.windows:
            self.windows[self.name] = self.window_class()
        self.window = self.windows[self.name]
        self.window.show()


class LoginScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_user = None
        self.mediaPlayer = None

        # Set window title and size
        self.setWindowTitle("Login Screen")
        self.setFixedSize(600, 400)

        # Set black background
        self.setStyleSheet("background-color: black;")

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignHCenter)

        # Add logo
        logo_label = QLabel()
        logo_pixmap = QPixmap("pictures\Background\logo.png")  
        logo_pixmap = logo_pixmap.scaledToWidth(200) 
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo_label)

        # Add title
        title_label = QLabel("Welcome to Jabba's Realm")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #ffcc00")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Create and add username input field
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet("background-color: #1a1a1a; color: #ffcc00; border: 2px solid #ffcc00; padding: 5px;")
        layout.addWidget(self.username_input)

        # Create and add password input field
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("background-color: #1a1a1a; color: #ffcc00; border: 2px solid #ffcc00; padding: 5px;")
        layout.addWidget(self.password_input)

        # Create and add login button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)
        self.login_button.setStyleSheet("font-size: 14px; background-color: #ffcc00; color: black")
        layout.addWidget(self.login_button)

        # Create horizontal layout for register and forgot password buttons
        button_layout = QHBoxLayout()

        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register)
        self.register_button.setStyleSheet("font-size: 12px; background-color: #ffcc00; color: black")
        button_layout.addWidget(self.register_button)

        self.forgot_password_button = QPushButton("Forgot Password?")
        self.forgot_password_button.clicked.connect(self.forgot_password)
        self.forgot_password_button.setStyleSheet("font-size: 12px; background-color: #ffcc00; color: black")
        button_layout.addWidget(self.forgot_password_button)

        layout.addLayout(button_layout)

        self.play_background_music(r"audio\\Login.mp3")

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Check if username or password fields are empty
        if not username or not password:
            QMessageBox.warning(self, "Login Failed", "Please enter both username and password.")
            return

        # Check credentials against the database
        conn = sqlite3.connect("./jabbas-data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()

        # If user exists, go to main screen, otherwise show error message
        if user:
            self.current_user = username  # Set the current user
            self.mediaPlayer.stop()
            self.new_screen = MainScreen(self.current_user)  # Pass the current user to MainScreen
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
            region = dialog.region_dropdown.currentText()

    def forgot_password(self):
        dialog = ForgotPasswordDialog(self)
        dialog.exec_()

    def play_background_music(self, music_file):
        self.mediaPlayer = QMediaPlayer()
        url = QUrl.fromLocalFile(music_file)
        content = QMediaContent(url)
        self.mediaPlayer.setMedia(content)
        self.mediaPlayer.setVolume(30)
        self.mediaPlayer.play()


class RegisterDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Register")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        self.username_input.setStyleSheet("background-color: #1a1a1a; color: #ffcc00; border: 2px solid #ffcc00; padding: 5px;")

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("background-color: #1a1a1a; color: #ffcc00; border: 2px solid #ffcc00; padding: 5px;")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        self.email_input.setStyleSheet("background-color: #1a1a1a; color: #ffcc00; border: 2px solid #ffcc00; padding: 5px;")

        self.region_dropdown = QComboBox()
        self.region_dropdown.addItems(["Abafar", "Agamar", "Ahch-To", "Ajan Kloss", "Akiva", "Alderaan", "Aldhani", "Aleen", "Alzoc III", "Anaxes", "Ando", "Anoat", "Atollon", "Barton 4", "Balnab", "Batuu", "Bespin", "Bogano", "Bora Vio", "Bracca", "Cantonica", "Castilon", "Cato Neimoidia", "Chandrilla", "Chrustophsis", "Concord Dawn", "Corellia", "Coruscant", "Crait", "Daiyu", "D'Qar", "Dagobah", "Dantooine", "Dathomir", "Devaron", "Eadu", "Endor", "Er´kit", "Eriadu", "Esseles", "Exegol", "Felucia", "Ferrix", "Florrum", "Fondor", "Geonosis", "Hosnian Prime", "Hoth", "Illum", "Iridonia", "Jabiim", "Jakku", "Jedha", "Jelucan", "Jestefad", "Kamino", "Kashyyyk", "Kef Bir", "Kessel", "Kijimi", "Koboh", "Kuat", "Lah'mu", "Lothal", "Lotho Minor", "Malachor", "Malastare", "Mandalore", "Mapuzo", "Maridun", "Miban", "Mon Cala", "Moraband", "Mortis", "Mustafar", "Mygeeto", "Naboo", "Nal Hutta", "Nevarro", "Niamos", "Numidian Prime", "Nur", "Onderon", "Ord Mantell", "Ossus", "Pasaana", "Pillio", "Polis Massa", "Rishi", "Rodia", "Rugosa", "Ruusan", "Ryloth", "Saleucami", "Savareen", "Scarif", "Seatos", "Serenno", "Shili", "Sissubo", "Skako Minor", "Sorgan", "Subterrel", "Sullust", "Takodana", "Tanalor", "Umbara", "Utapau", "Vandor-1", "Vardos", "Wobani", "Wrea", "Yavin", "Yavin 4", "Zeffo", "Zygerria"
])
        self.region_dropdown.setStyleSheet("background-color: #1a1a1a; color: #ffcc00; border: 2px solid #ffcc00; padding: 5px;")

        register_button = QPushButton("Register")
        register_button.clicked.connect(self.register)
        register_button.setStyleSheet("font-size: 14px; background-color: #ffcc00; color: black")

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
        conn = sqlite3.connect("./jabbas-data.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users(username, password, email, region, balance) VALUES (?, ?, ?, ?, ?)", (username, password, email, region, 99999999999999999))
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
        self.email_input.setStyleSheet("background-color: #1a1a1a; color: #ffcc00; border: 2px solid #ffcc00; padding: 5px;")

        retrieve_password_button = QPushButton("Retrieve Password")
        retrieve_password_button.clicked.connect(self.retrieve_password_from_database)
        retrieve_password_button.setStyleSheet("font-size: 14px; background-color: #ffcc00; color: black")
        
        layout.addWidget(self.email_input)
        layout.addWidget(retrieve_password_button)

        self.setLayout(layout)

    def retrieve_password_from_database(self):
        email = self.email_input.text()
        password = self.parent().retrieve_password_from_database(email)
        if password:
            self.send_password_email(email, password)
            QMessageBox.information(self, "Password Retrieval", "An email has been sent to your email address with the password.")
            self.accept()
        else:
            QMessageBox.warning(self, "Password Retrieval Failed", "No user with this email exists.")

class MainScreen(QMainWindow):
    def __init__(self, current_user):
        super().__init__()
        self.windows = {}
        self.current_user = current_user

        self.setWindowTitle("Jabba's Realm")
        self.showFullScreen()
        self.setStyleSheet("background-color: black;")

        self.init_ui()

    def init_ui(self):
        title_label = QLabel("Jabba's Realm")
        title_label.setStyleSheet("font-family: Star Jedi; font-size: 48px; font-weight: bold; color: #ffcc00; text-shadow: 2px 2px 2px #000000")
        title_label.setAlignment(Qt.AlignCenter)

        logo_label = QLabel()
        logo_pixmap = QPixmap("pictures/Background/logo.png")
        logo_pixmap = logo_pixmap.scaledToWidth(400)
        logo_label.setPixmap(logo_pixmap)

        credits_label = QLabel()
        credits_label.setStyleSheet("font-size: 18px; font-weight: bold; color: #ffcc00")
        self.update_credits_label(credits_label)

        button_names = ["Marketplace", "Jabba's Stocks", "Hutts Playground", "Jabba's Hangout"]
        buttons = [self.create_button(name) for name in button_names]

        grid_layout = QGridLayout()
        grid_layout.addWidget(buttons[0], 1, 1, alignment=Qt.AlignCenter)
        grid_layout.addWidget(buttons[1], 1, 2, alignment=Qt.AlignCenter)
        grid_layout.addWidget(buttons[2], 2, 1, alignment=Qt.AlignCenter)
        grid_layout.addWidget(buttons[3], 2, 2, alignment=Qt.AlignCenter)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        layout.addWidget(logo_label, alignment=Qt.AlignCenter)
        layout.addWidget(title_label, alignment=Qt.AlignCenter)
        layout.addLayout(grid_layout)
        layout.addWidget(credits_label, alignment=Qt.AlignRight | Qt.AlignBottom)

        self.play_background_music("audio/cantina.mp3")

    def create_button(self, name):
        button = QPushButton(name)
        button.setStyleSheet("""
            QPushButton {
                font-size: 32px;
                font-weight: bold;
                color: black;
                background-color: #ffcc00;
                border-radius: 25px;
                padding: 25px 50px;
                min-width: 300px; /* Mindestbreite für den Button */
                max-width: 500px; /* Maximale Breite für den Button */
                margin: 15px;
            }
            QPushButton:hover {
                background-color: #ffaa00; /* Farbe ändern, wenn der Mauszeiger über den Button bewegt wird */
            }
        """)
        button.clicked.connect(lambda state, button_name=name: self.open_sub_window(button_name))
        return button

    def open_sub_window(self, name):
        if self.current_user:
            if name not in self.windows:
                if name == "Marketplace":
                    self.windows[name] = MarketplaceWindow()
                elif name == "Jabba's Stocks":
                    self.windows[name] = StocksWindow()
                elif name == "Hutts Playground":
                    self.windows[name] = PlaygroundWindow()
                elif name == "Jabba's Hangout":
                    self.windows[name] = HangoutWindow()
            self.windows[name].show()
        else:
            QMessageBox.warning(self, "Login Required", "Please login to access this feature.")

    def update_credits_label(self, label):
        with sqlite3.connect(r"jabbas-data.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT balance FROM users WHERE username=?", (self.current_user,))
            credits = cursor.fetchone()[0]
            label.setText(f"Credits: {credits}")

    def play_background_music(self, music_file):
        if QMediaPlayer.supportedMimeTypes():
            self.mediaPlayer = QMediaPlayer()
            url = QUrl.fromLocalFile(music_file)
            content = QMediaContent(url)
            self.mediaPlayer.setMedia(content)
            self.mediaPlayer.setVolume(10)
            self.mediaPlayer.play()

IMAGE_COSTS = {
        r"pictures/Creatures/Bane-Back-Spider.jpg": 10,
        r"pictures/Creatures/Bog-rat.jpg": 10,
        r"pictures/Creatures/Chirodactyl.jpg": 10,
        r"pictures/Creatures/Flame-Beetle.jpeg": 10,
        r"pictures/Creatures/Jotaz.jpg": 10,
        r"pictures/Creatures/Mykal.jpg": 10,
        r"pictures/Creatures/Oggdo.jpg": 10,
        r"pictures/Creatures/Phillak.jpg": 10,
        r"pictures/Creatures/Scazz.jpg": 10,
        r"pictures/Creatures/Slyyyg.jpg": 10,
        r"pictures/Creatures/Splox.jpg": 10,
        r"pictures/Creatures/Wyyyschokk.jpg": 10,
        r"pictures/Droids/Astromechdroids/R-1-Astromechdroid.jpg": 20,
        r"pictures/Droids/Astromechdroids/R-2-Astromechdroid.jpg": 20,
        r"pictures/Droids/Astromechdroids/R-3-Astromechdroid.jpg": 20,
        r"pictures/Droids/Astromechdroids/R-4-Astromechdroid.jpg": 20,
        r"pictures/Droids/Astromechdroids/R-5-Astromechdroid.jpg": 20,
        r"pictures/Droids/Astromechdroids/R-6-Astromechdroid.jpg": 20,
        r"pictures/Droids/Astromechdroids/R-7-Astromechdroid.jpg": 20,
        r"pictures/Droids/Astromechdroids/R-8-Astromechdroid.jpg": 20,
        r"pictures/Droids/Astromechdroids/R-9-Astromechdroid.jpg": 20,
        r"pictures/Droids/Battledroids/R-1-Battledroid.jpg": 30,
        r"pictures/Droids/Battledroids/B-2-Ha-Super-Battledroid.jpg": 30,
        r"pictures/Droids/Battledroids/B-2-Super-Battledroid.jpg": 30,
        r"pictures/Droids/Battledroids/Bx-Kommando-Battledroid.jpg": 30,
        r"pictures/Droids/Battledroids/Droideka-Battledroid.jpg": 30,
        r"pictures/Droids/Battledroids/Dwarf-Spider-Battledroid.jpg": 30,
        r"pictures/Droids/Battledroids/IG-86-Wächter-Battledroid.jpg": 30,
        r"pictures/Droids/Battledroids/IG-100-Magna-Battledroid.jpg": 30,
        r"pictures\Droids\\Maintenancedroids\DUM-series-Maintenancedroid.jpg": 40,
        r"pictures\Droids\\Maintenancedroids\\EG-6-Maintenancedroid.png": 40,
        r"pictures\Droids\\Maintenancedroids\\GNK-Maintenancedroid.jpg": 40,
        r"pictures\Droids\\Maintenancedroids\\GO-TO-Maintenancedroid.jpg": 40,
        r"pictures\Droids\\Maintenancedroids\\MSE-6-Maintenancedroid.jpg": 40,
        r"pictures\Droids\\Maintenancedroids\WED-Treadwell-Maintenancedroid.jpg": 40,
        r"pictures/Droids/Medicaldroids/2-1B-Medicaldroid.jpg": 50,
        r"pictures/Droids/Medicaldroids/8T88-Medicaldroid.jpg": 50,
        r"pictures/Droids/Medicaldroids/DD-13-Medicaldroid.jpg": 50,
        r"pictures/Droids/Medicaldroids/FX-Medicaldroid.jpg": 50,
        r"pictures/Droids/Medicaldroids/IM-6-Medicaldroid.jpg": 50,
        r"pictures/Droids/Medicaldroids/SP-4-Medicaldroid.jpg": 50,
        r"pictures/Droids/Protocoldroids/3PO-Protocoldroid.jpg": 60,
        r"pictures/Droids/Protocoldroids/CZ-Serie-Protocoldroid.jpg": 60,
        r"pictures/Droids/Protocoldroids/RA-7-Protocoldroid.jpg": 60,
        r"pictures\Starships\\Corvettes\\CR-70-Corvette.jpg": 70,
        r"pictures\Starships\\Corvettes\\CR-90-Corvette.jpg": 70,
        r"pictures\Starships\\Corvettes\\CY-180-Corvette.jpg": 70,
        r"pictures\Starships\\Corvettes\\Sacheen.jpg": 70,
        r"pictures\Starships\\Corvettes\\Tantive-IV.jpg": 70,
        r"pictures\Starships\\Cruisers\\Arquitens-Cruiser.jpg": 80,
        r"pictures\Starships\\Cruisers\\Consular-Class-Cruiser.jpg": 80,
        r"pictures\Starships\\Cruisers\\Hammerhead-Cruiser.jpg": 80,
        r"pictures\Starships\\Cruisers\\Munificent-Class-Cruiser.jpg": 80,
        r"pictures\Starships\\Cruisers\\Pelta-Class-Cruiser.jpg": 80,
        r"pictures\Starships\\Cruisers\\Recusant-Class-Light-Destroyer.jpg": 80,
        r"pictures\Starships\\Cruisers\\Republic-Cruiser.jpg": 80,
        r"pictures\Starships\\Cruisers\\Subjugator-Class-Heavy-Cruiser.jpg": 80,
        r"pictures\Starships\\Cruisers\\Venator-Class-Star-Destroyer.jpg": 80,
        r"pictures\Starships\\Destroyers\\Assertor-Class-Command-Dreadnought.jpg": 90,
        r"pictures\Starships\\Destroyers\\Eclipse-Class-Star-Destroyer.jpg": 90,
        r"pictures\Starships\\Destroyers\\Executor-Class-Star-Destroyer.jpg": 90,
        r"pictures\Starships\\Destroyers\\Imperial-I-Class-Star-Destroyer.jpg": 90,
        r"pictures\Starships\\Destroyers\\Imperial-II-Class-Star-Destroyer.jpg": 90,
        r"pictures\Starships\\Destroyers\\Interdictor-Class-Star-Destroyer.jpg": 90,
        r"pictures\Starships\\Destroyers\\Secutor-Class-Star-Destroyer.jpg": 90,
        r"pictures\Starships\\Destroyers\\Sovereign-Class-Star-Dreadnought.jpg": 90,
        r"pictures\Starships\\Destroyers\\Super-Command-Star-Destroyer.jpg": 90,
        r"pictures\Starships\\Destroyers\\Victory-I-Class-Star-Destroyer.jpg": 90,
        r"pictures\Starships\\Destroyers\\Victory-II-Class-Star-Destroyer.jpg": 90,
        r"pictures\Starships\\Freighters\\Carrack-Light-Cruiser.jpg": 100,
        r"pictures\Starships\\Freighters\\GR-75-Medium-Transport.jpg": 100,
        r"pictures\Starships\\Freighters\\Liberator-Class-Cruiser.jpg": 100,
        r"pictures\Starships\\Freighters\\Lucrehulk-Class-Battleship.jpg": 100,
        r"pictures\Starships\\Freighters\\Pelta-Class-Transport.jpg": 100,
        r"pictures\Starships\\Freighters\\Radiant-VII.jpg": 100,
        r"pictures\Starships\\Freighters\\YT-1300-Light-Freighter.jpg": 100,
        r"pictures\Starships\\Freighters\\YT-1760-Light-Freighter.jpg": 100,
        r"pictures\Starships\\Freighters\\YT-2400-Light-Freighter.jpg": 100,
        r"pictures\Starships\\Frigates\\DP20-Frigate.jpg": 110,
        r"pictures\Starships\\Frigates\\EF76-Nebulon-B-Frigate.jpg": 110,
        r"pictures\Starships\\Frigates\\EF76-II-Nebulon-B-Frigate.jpg": 110,
        r"pictures\Starships\\Frigates\\Lancer-Frigate.jpg": 110,
        r"pictures\Starships\\Frigates\\Munificent-Class-Frigate.jpg": 110,
        r"pictures\Starships\\Frigates\\Nebulon-B2-Frigate.jpg": 110,
        r"pictures\Starships\\Frigates\\Pelta-Class-Frigate.jpg": 110,
        r"pictures\Starships\\Gunships\\Acclamator-I-Class-Assault-Ship.jpg": 120,
        r"pictures\Starships\\Gunships\\Acclamator-II-Class-Assault-Ship.jpg": 120,
        r"pictures\Starships\\Gunships\\LAAT-Gunship.jpg": 120,
        r"pictures\Starships\\Gunships\\LAAT-I-Gunship.jpg": 120,
        r"pictures\Starships\\Gunships\\LAAT-II-Gunship.jpg": 120,
        r"pictures\Starships\\Gunships\\LAAT-III-Gunship.jpg": 120,
        r"pictures\Starships\\Gunships\\Low-Altitude-Assault-Transport.jpg": 120,
        r"pictures\Starships\\Gunships\\Low-Altitude-Assault-Transport-Carrier.jpg": 120,
        r"pictures\Starships\\Shuttles\\AA-9-Coruscant-Shuttle.jpg": 130,
        r"pictures\Starships\\Shuttles\\Delta-Class-T-3C-Shuttle.jpg": 130,
        r"pictures\Starships\\Shuttles\\Droch-Class-Boarding-Shuttle.jpg": 130,
        r"pictures\Starships\\Shuttles\\Epsilon-Class-Shuttle.jpg": 130,
        r"pictures\Starships\\Shuttles\\H-Type-Nubian-Yacht.jpg": 130,
        r"pictures\Starships\\Shuttles\\Imperial-Shuttle.jpg": 130,
        r"pictures\Starships\\Shuttles\\Kappa-Class-Shuttle.jpg": 130,
        r"pictures\Starships\\Shuttles\\Lambda-Class-T-4a-Shuttle.jpg": 130,
        r"pictures\Starships\\Shuttles\\Nu-Class-Attack-Shuttle.jpg": 130,
        r"pictures\Starships\\Shuttles\\Sentinel-Class-Shuttle.jpg": 130,
        r"pictures\Starships\\Starfighters\\Aurek-Class-Tactical-Strikefighter.jpg": 140,
        r"pictures\Starships\\Starfighters\\Belbullab-22-Starfighter.jpg": 140,
        r"pictures\Starships\\Starfighters\\Eta-2-Actis-Class-Interceptor.jpg": 140,
        r"pictures\Starships\\Starfighters\\Eta-5-Interceptor.jpg": 140,
        r"pictures\Starships\\Starfighters\\Fang-Fighter.jpg": 140,
        r"pictures\Starships\\Starfighters\\TIE-Bomber.jpg": 140,
        r"pictures\Starships\\Starfighters\\TIE-Fighter.jpg": 140,
        r"pictures\Starships\\Starfighters\\V-19-Torrent-Interceptor.jpg": 140,
        r"pictures\Starships\\Starfighters\\V-Wing-Interceptor.jpg": 140,
        r"pictures\Starships\Starfighters\\X-Wing-Starfighter.jpg": 10,
        r"pictures\Starships\Starfighters\\Y-Wing-Starfighter.jpg": 10,
        r"pictures\\Vehicles\Artilleries\AV-7-Artillery.jpg": 10,
        r"pictures\\Vehicles\Artilleries\\1-Protonenkanone-Artillery.jpg": 10,
        r"pictures\\Vehicles\Artilleries\SPHA-Artillery.jpg": 10,
        r"pictures\\Vehicles\Battlevehicles\AAT-Battlevehicle.jpg": 10,
        r"pictures\\Vehicles\Battlevehicles\AT-AP-Battlevehicle.jpg": 10,
        r"pictures\\Vehicles\Battlevehicles\AT-AT-Battlevehicle.jpg": 10,
        r"pictures\\Vehicles\Battlevehicles\AT-DP-Battlevehicle.jpg": 10,
        r"pictures\\Vehicles\Battlevehicles\AT-DT-Battlevehicle.jpg": 10,
        r"pictures\\Vehicles\Battlevehicles\AT-RT-Battlevehicle.jpg": 10,
        r"pictures\\Vehicles\Battlevehicles\AT-ST-Battlevehicle.jpg": 10,
        r"pictures\\Vehicles\Battlevehicles\AT-TE-Battlevehicle.jpg": 10,
        r"pictures\\Vehicles\\Gunships\\HMP-Droid-Gunship.jpg": 10,
        r"pictures\\Vehicles\\Gunships\\LAAT-C-Gunship.jpg": 10,
        r"pictures\\Vehicles\\Gunships\\LAAT-Gunship.jpg": 10,
        r"pictures\\Vehicles\\Gunships\\VAAT-Gunship.jpg": 10,
        r"pictures\\Vehicles\Speederbikes\\74-Z-Speederbike.jpg": 10,
        r"pictures\\Vehicles\Speederbikes\\614-AvA-Speederbike.jpg": 10,
        r"pictures\\Vehicles\Speederbikes\Barc-Speederbike.jpg": 10,
        r"pictures\\Vehicles\Speederbikes\\Ck-6-Speederbike.jpg": 10,
        r"pictures\\Vehicles\Speederbikes\\C-Ph-Patrol-Speederbike.jpg": 10,
        r"pictures\\Vehicles\\Transportvehicles\A6-Juggernauts-Transportvehicle.jpg": 10,
        r"pictures\\Vehicles\\Transportvehicles\AT-OT-Transportvehicle.jpg": 10,
        r"pictures\\Vehicles\\Transportvehicles\\MTT-Transportvehicle.jpg": 10,
        r"pictures\\Vehicles\\Transportvehicles\\UT-AT-Transportvehicle.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Pistols\DE-10-Blaster_Pistol.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Pistols\DH-16-Blaster_Pistol.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Pistols\DH-17-Blaster_Pistol.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Pistols\DL-18-Blaster_Pistol.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Pistols\DL-44-Blaster_Pistol.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Pistols\\LL-30-Blaster_Pistol.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Pistols\\MW-40-Bryar-Blaster_Pistol.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Pistols\\NN-14-Blaster_Pistol.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Pistols\\RK-3-Blaster_Pistol.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Pistols\S-5-Blaster_Pistol.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Pistols\S-195-Blaster_Pistol.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Pistols\SE-14-Blaster_Pistol.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Pistols\SE-44C-Blaster_Pistol.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Pistols\WESTAR-34-Blaster_Pistol.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Rifles\A-280-Blaster_Rifle.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Rifles\A-280C-Blaster_Rifle.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Rifles\\CR-2-Blaster_Rifle.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Rifles\\E-5-Blaster_Rifle.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Rifles\\E-10-Blaster_Rifle.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Rifles\\E-11-Blaster_Rifle.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Rifles\\E-22-Blaster_Rifle.jpg": 10,
        r"pictures\Weapons\Blasters\Blaster_Rifles\\EL-16HFE-Blaster_Rifle.jpg": 10,
        r"pictures\Weapons\Blasters\\Repeating_Blasters\DC-15A-Repeating_Blaster.jpg": 10,
        r"pictures\Weapons\Blasters\\Repeating_Blasters\DC-15LE-Repeating_Blaster.jpg": 10,
        r"pictures\Weapons\Blasters\\Repeating_Blasters\\FWMB-10-Repeating_Blaster.jpg": 10,
        r"pictures\Weapons\Blasters\\Repeating_Blasters\\T-21B-Repeating_Blaster.jpg": 10,
        r"pictures\Weapons\Blasters\\Repeating_Blasters\\TL-50-Repeating_Blaster.jpg": 10,
        r"pictures\Weapons\Blasters\Sniper_Rifle_Blasters\\Cycler-Sniper_Rifle_Blaster.jpg": 10,
        r"pictures\Weapons\Blasters\Sniper_Rifle_Blasters\DLT-19X-Sniper_Rifle_Blaster.jpg": 10,
        r"pictures\Weapons\Blasters\Sniper_Rifle_Blasters\DTL-20A-Sniper_Rifle_Blaster.jpg": 10,
        r"pictures\Weapons\Blasters\Sniper_Rifle_Blasters\\E-5S-Sniper_Rifle_Blaster.jpg": 10,
        r"pictures\Weapons\Blasters\Sniper_Rifle_Blasters\\Valken-38X-Sniper_Rifle_Blaster.jpg": 10,
        r"pictures\Weapons\\Explosives\\C-25-Granate.jpg": 10,
        r"pictures\Weapons\\Explosives\\Flash-Granate.jpg": 10,
        r"pictures\Weapons\\Explosives\\Impact-Granate.jpg": 10,
        r"pictures\Weapons\\Explosives\\Ion-Granate.jpg": 10,
        r"pictures\Weapons\\Explosives\\Proton-Granate.jpg": 10,
        r"pictures\Weapons\\Explosives\Shock-Granate.jpg": 10,
        r"pictures\Weapons\\Explosives\\Thermal-Detonator-Granate.jpg": 10,
        r"pictures\Weapons\\Lightsabers\Darksaber.jpg": 10,
        r"pictures\Weapons\\Lightsabers\\Lightsaber.jpg": 10,
        r"pictures\Weapons\\Lightsabers\\Lightsaber2.jpg": 10,
        r"pictures\Weapons\\Lightsabers\\Lightsaber3.jpg": 10
    }

class TooltipWindow(QDialog):
    def __init__(self, tooltip_text, image_path):
        super().__init__()
        self.setWindowTitle("Tooltip")

        layout = QVBoxLayout()
        label = QLabel(tooltip_text)
        layout.addWidget(label)

        self.setLayout(layout)
        self.setWindowModality(Qt.WindowModal)
        self.setFixedSize(300, 200)
        self.setPixmap(QPixmap(image_path))

class ShoppingCart(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Shopping Cart")
        layout = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Image", "Quantity", "Cost"])
        layout.addWidget(self.table)
        self.proceed_button = QPushButton("Proceed to Checkout")
        self.proceed_button.clicked.connect(self.proceed_to_checkout)
        layout.addWidget(self.proceed_button)
        self.clear_button = QPushButton("Clear Cart")
        self.clear_button.clicked.connect(self.clear_cart)
        layout.addWidget(self.clear_button)
        self.setLayout(layout)

        app = QApplication.instance()
        app.topLevelWidgets().append(self)

    def add_item(self, image_path, quantity, cost):
        row = self.table.rowCount()
        self.table.insertRow(row)
        image_label = QLabel()
        image_label.setPixmap(QPixmap(image_path))
        self.table.setCellWidget(row, 0, image_label)
        quantity_item = QTableWidgetItem(str(quantity))
        self.table.setItem(row, 1, quantity_item)
        cost_item = QTableWidgetItem(str(cost))
        self.table.setItem(row, 2, cost_item)

    def proceed_to_checkout(self):
        pass

    def clear_cart(self):
        self.table.setRowCount(0)


class MarketplaceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.image_paths = []
        self.table = QTableWidget()
        self.setWindowTitle("Marketplace")

        screen_geometry = QApplication.primaryScreen().geometry()
        self.setGeometry(screen_geometry)

        self.category_dropdown = QComboBox()
        self.category_dropdown.addItems(["creatures", "Astromechdroids", "Battledroids", "Maintenancedroids", "Medicaldroids", "Protocoldroids", "Corvettes", "Frigates", "Shuttles", "Star_Destroyers", "Starfighters", "Artilleries", "Battlevehicles", "Gunships", "Speederbikes", "Transportvehicles", "Blaster_Pistols", "Blaster_Rifles", "Repeating_Rifles", "Sniper_Rifle_Blasters", "Explosives", "Lightsabers"])
        self.category_dropdown.currentIndexChanged.connect(self.show_images)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.inner_widget = QWidget(self.scroll_area)
        self.scroll_area.setWidget(self.inner_widget)
        self.scroll_layout = QGridLayout(self.inner_widget)
        self.scroll_layout.setHorizontalSpacing(0)

        self.show_images(self.image_paths)

        layout = QVBoxLayout(self)
        layout.addWidget(self.category_dropdown)
        layout.addWidget(self.scroll_area)
        layout.addWidget(self.table)

    def showEvent(self, event):
        super().showEvent(event)
        self.show_images(self.image_paths)

    def add_to_cart(self):
        row = self.table.currentRow()
        if row != -1:
            image_path = self.image_paths[row]
            cost = self.table.item(row, 2).text()
            quantity, ok = QInputDialog.getInteger(self, "Add to Cart", "Enter quantity:", 1, 1, 100, 1)
            if ok:
                self.cart.add_item(image_path, quantity, cost)
    
    def show_images(self, image_paths):
        if not isinstance(image_paths, (list, tuple)):
            image_paths = [image_paths]  # Convert to a list if it's a single value
        self.image_paths = image_paths
        selected_category = self.category_dropdown.currentText()
        self.table.setRowCount(len(image_paths))
        for i, image_path in enumerate(image_paths):
            self.table.setItem(i, 0, QTableWidgetItem(image_path))
            self.table.setItem(i, 1, QTableWidgetItem("0"))
            self.table.setItem(i, 2, QTableWidgetItem("0"))
        image_paths = []
        tooltips = []

        if selected_category == "creatures":
            image_paths, tooltips = self.load_creatures_images()
        elif selected_category == "Astromechdroids":
            image_paths, tooltips = self.load_astromechdroids_images()
        elif selected_category == "Battledroids":
            image_paths, tooltips = self.load_battledroids_images()
        elif selected_category == "Maintenancedroids":
            image_paths, tooltips = self.load_maintenancedroids_images()
        elif selected_category == "Medicaldroids":
            image_paths, tooltips = self.load_medicaldroids_images()
        elif selected_category == "Protocoldroids":
            image_paths, tooltips = self.load_protocoldroids_images()
        elif selected_category == "Corvettes":
            image_paths, tooltips = self.load_corvettes_images()
        elif selected_category == "Frigates":
            image_paths, tooltips = self.load_frigates_images()
        elif selected_category == "Shuttles":
            image_paths, tooltips = self.load_shuttles_images()
        elif selected_category == "Star_Destroyers":
            image_paths, tooltips = self.load_star_destroyers_images()
        elif selected_category == "Starfighters":
            image_paths, tooltips = self.load_starfighters_images()
        elif selected_category == "Artilleries":
            image_paths, tooltips = self.load_artilleries_images()
        elif selected_category == "Battlevehicles":
            image_paths, tooltips = self.load_battlevehicles_images()
        elif selected_category == "Gunships":
            image_paths, tooltips = self.load_gunships_images()
        elif selected_category == "Speederbikes":
            image_paths, tooltips = self.load_speederbikes_images()
        elif selected_category == "Transportvehicles":
            image_paths, tooltips = self.load_transportvehicles_images()
        elif selected_category == "Blaster_Pistols":
            image_paths, tooltips = self.load_blaster_pistols_images()
        elif selected_category == "Blaster_Rifles":
            image_paths, tooltips = self.load_blaster_rifles_images()
        elif selected_category == "Repeating_Rifles":
            image_paths, tooltips = self.load_repeating_rifles_images()
        elif selected_category == "Sniper_Rifle_Blasters":
            image_paths, tooltips = self.load_sniper_rifle_blasters_images()
        elif selected_category == "Explosives":
            image_paths, tooltips = self.load_explosives_images()
        elif selected_category == "Lightsabers":
            image_paths, tooltips = self.load_lightsabers_images()

        for i in reversed(range(self.scroll_layout.count())):
            self.scroll_layout.itemAt(i).widget().deleteLater()

        num_images = len(image_paths)
        num_columns = 6
        image_width = self.scroll_area.width() // num_columns

        row = 0
        col = 0
        for path, tooltip_text in zip(image_paths, tooltips):
            placeholder_image = QLabel()
            pixmap = QPixmap(path)
            if not pixmap.isNull() and pixmap.width() > 0:
                image_height = pixmap.height() * image_width // pixmap.width()
                pixmap = pixmap.scaled(image_width, image_height, Qt.KeepAspectRatio)
                placeholder_image.setPixmap(pixmap)
                placeholder_image.setAlignment(Qt.AlignCenter)
                placeholder_image.setToolTip(tooltip_text)
                placeholder_image.mousePressEvent = lambda event, tooltip_text=tooltip_text, image_path=path: self.show_tooltip(tooltip_text, image_path)
                self.scroll_layout.addWidget(placeholder_image, row, col)
                col += 1
                if col == num_columns:
                    row += 1
                    col = 0
            else:
                print(f"Error loading the image: {path}")

        self.cart = ShoppingCart(self)
        self.add_to_cart_button = QPushButton("Add to Cart")
        self.add_to_cart_button.clicked.connect(self.add_to_cart)
        self.scroll_layout.addWidget(self.add_to_cart_button, row, col)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def load_creatures_images(self):
        image_paths = [
            r"pictures/Creatures/Bane-Back-Spider.jpg",
            r"pictures/Creatures/Bog-rat.jpg",
            r"pictures/Creatures/Chirodactyl.jpg",
            r"pictures/Creatures/Flame-Beetle.jpeg",
            r"pictures/Creatures/Jotaz.jpg",
            r"pictures/Creatures/Mykal.jpg",
            r"pictures/Creatures/Oggdo.jpg",
            r"pictures/Creatures/Phillak.jpg",
            r"pictures/Creatures/Scazz.jpg",
            r"pictures/Creatures/Slyyyg.jpg",
            r"pictures/Creatures/Splox.jpg",
            r"pictures/Creatures/Wyyyschokk.jpg"
        ]
        tooltips = [
            "Bane-Back-Spider",
            "Bog-rat",
            "Chirodactyl",
            "Flame-Beetle",
            "Jotaz",
            "Mykal",
            "Oggdo",
            "Phillak",
            "Scazz",
            "Slyyyg",
            "Splox",
            "Wyyyschokk"
        ]
        return image_paths, tooltips

    def load_astromechdroids_images(self):
        image_paths = [
            r"pictures/Droids/Astromechdroids/R-1-Astromechdroid.jpg",
            r"pictures/Droids/Astromechdroids/R-2-Astromechdroid.jpg",
            r"pictures/Droids/Astromechdroids/R-3-Astromechdroid.jpg",
            r"pictures/Droids/Astromechdroids/R-4-Astromechdroid.jpg",
            r"pictures/Droids/Astromechdroids/R-5-Astromechdroid.jpg",
            r"pictures/Droids/Astromechdroids/R-6-Astromechdroid.jpg",
            r"pictures/Droids/Astromechdroids/R-7-Astromechdroid.jpg",
            r"pictures/Droids/Astromechdroids/R-8-Astromechdroid.jpg",
            r"pictures/Droids/Astromechdroids/R-9-Astromechdroid.jpg"
        ]
        tooltips = [
            "R-1-Astromechdroid",
            "R-2-Astromechdroid",
            "R-3-Astromechdroid",
            "R-4-Astromechdroid",
            "R-5-Astromechdroid",
            "R-6-Astromechdroid",
            "R-7-Astromechdroid",
            "R-8-Astromechdroid",
            "R-9-Astromechdroid"
        ]
        return image_paths, tooltips

    def load_battledroids_images(self):
        image_paths = [
            r"pictures/Droids/Battledroids/R-1-Battledroid.jpg",
            r"pictures/Droids/Battledroids/B-2-Ha-Super-Battledroid.jpg",
            r"pictures/Droids/Battledroids/B-2-Super-Battledroid.jpg",
            r"pictures/Droids/Battledroids/Bx-Kommando-Battledroid.jpg",
            r"pictures/Droids/Battledroids/Droideka-Battledroid.jpg",
            r"pictures/Droids/Battledroids/Dwarf-Spider-Battledroid.jpg",
            r"pictures/Droids/Battledroids/IG-86-Wächter-Battledroid.jpg",
            r"pictures/Droids/Battledroids/IG-100-Magna-Battledroid.jpg"
        ]
        tooltips = [
            "R-1-Battledroid",
            "B-2-Ha-Super-Battledroid",
            "B-2-Super-Battledroid",
            "Bx-Kommando-Battledroid",
            "Droideka-Battledroid",
            "Dwarf-Spider-Battledroid",
            "IG-86-Wächter-Battledroid",
            "IG-100-Magna-Battledroid"
        ]
        return image_paths, tooltips

    def load_maintenancedroids_images(self):
        image_paths = [
            r"pictures\Droids\\Maintenancedroids\DUM-series-Maintenancedroid.jpg",
            r"pictures\Droids\\Maintenancedroids\\EG-6-Maintenancedroid.png",
            r"pictures\Droids\\Maintenancedroids\\GNK-Maintenancedroid.jpg",
            r"pictures\Droids\\Maintenancedroids\\GO-TO-Maintenancedroid.jpg",
            r"pictures\Droids\\Maintenancedroids\\MSE-6-Maintenancedroid.jpg",
            r"pictures\Droids\\Maintenancedroids\WED-Treadwell-Maintenancedroid.jpg"
        ]
        tooltips =[
            "DUM-series-Maintenancedroid",
            "EG-6-Maintenancedroid",
            "GNK-Maintenancedroid",
            "GO-TO-Maintenancedroid",
            "MSE-6-Maintenancedroid",
            "WED-Treadwell-Maintenancedroid"
        ]
        return image_paths, tooltips

    def load_medicaldroids_images(self):
        image_paths = [
            r"pictures/Droids/Medicaldroids/2-1B-Medicaldroid.jpg",
            r"pictures/Droids/Medicaldroids/8T88-Medicaldroid.jpg",
            r"pictures/Droids/Medicaldroids/DD-13-Medicaldroid.jpg",
            r"pictures/Droids/Medicaldroids/FX-Medicaldroid.jpg",
            r"pictures/Droids/Medicaldroids/IM-6-Medicaldroid.jpg",
            r"pictures/Droids/Medicaldroids/SP-4-Medicaldroid.jpg",
        ]
        tooltips = [
            "2-1B-Medicaldroid",
            "8T88-Medicaldroid",
            "DD-13-Medicaldroid",
            "FX-Medicaldroid",
            "IM-6-Medicaldroid",
            "SP-4-Medicaldroid"
        ]
        return image_paths, tooltips

    def load_protocoldroids_images(self):
        image_paths = [
            r"pictures/Droids/Protocoldroids/3PO-Protocoldroid.jpg",
            r"pictures/Droids/Protocoldroids/CZ-Serie-Protocoldroid.jpg",
            r"pictures/Droids/Protocoldroids/RA-7-Protocoldroid.jpg"
        ]
        tooltips = [
            "3PO-Protocoldroid",
            "CZ-Serie-Protocoldroid",
            "RA-7-Protocoldroid"
        ]
        return image_paths, tooltips

    def load_corvettes_images(self):
        image_paths = [
            r"pictures\Starships\\Corvettes\CR-70-Corvette.jpg",
            r"pictures\Starships\\Corvettes\CR-90-Corvette.jpg",
            r"pictures\Starships\\Corvettes\CY-180-Corvette.jpg",
            r"pictures\Starships\\Corvettes\Raider-Class-Corvette.jpg",
            r"pictures\Starships\\Corvettes\Sphyrna-Class-Corvette.jpg"
        ]
        tooltips = [
            "CR-70-Corvette",
            "CR-90-Corvette",
            "CY-180-Corvette",
            "Raider-Class-Corvette",
            "Sphyrna-Class-Corvette"
        ]
        return image_paths, tooltips

    def load_frigates_images(self):
        image_paths = [
            r"pictures\Starships\\Frigates\Arquitens-Class-Frigate.jpg",
            r"pictures\Starships\\Frigates\Corona-Class-Frigate.jpg",
            r"pictures\Starships\\Frigates\EF-76-Nebulon-B-Frigate.jpg",
            r"pictures\Starships\\Frigates\Kontos-Class-Frigate.jpg",
            r"pictures\Starships\\Frigates\Munificent-Class-Frigate.jpg",
            r"pictures\Starships\\Frigates\Pelta-Class-Frigate.jpg"
        ]
        tooltips = [
            "Arquitens-Class-Frigate",
            "Corona-Class-Frigate",
            "EF-76-Nebulon-B-Frigate",
            "Kontos-Class-Frigate",
            "Munificent-Class-Frigate",
            "Pelta-Class-Frigate"
        ]
        return image_paths, tooltips

    def load_shuttles_images(self):
        image_paths = [
            r"pictures\Starships\Shuttles\Delta-Class-T-3C-Shuttle.jpg",
            r"pictures\Starships\Shuttles\Eta-Class-Shuttle.jpg",
            r"pictures\Starships\Shuttles\H-2-Shuttle.jpg",
            r"pictures\Starships\Shuttles\Lambda-T-4A-Class-Shuttle.jpg",
            r"pictures\Starships\Shuttles\Nu-Class-Attack-Shuttle.jpg",
            r"pictures\Starships\Shuttles\Rho-Class-Shuttle.jpg",
            r"pictures\Starships\Shuttles\T-6-Shuttle.jpg",
            r"pictures\Starships\Shuttles\Theta-Class-T-2C-Shuttle.jpg"
        ]
        tooltips = [
            "Delta-Class-T-3C-Shuttle",
            "Eta-Class-Shuttle",
            "H-2-Shuttle",
            "Lambda-T-4A-Class-Shuttle",
            "Nu-Class-Attack-Shuttle",
            "Rho-Class-Shuttle",
            "T-6-Shuttle",
            "Theta-Class-T-2C-Shuttle"
        ]
        return image_paths, tooltips

    def load_star_destroyers_images(self):
        image_paths = [
            r"pictures\Starships\Star_Destroyers\Immobilizer-418-Star_Destroyer.jpg",
            r"pictures\Starships\Star_Destroyers\Venator-Class-Star_Destroyer.jpg"
        ]
        tooltips = [
            "Immobilizer-418-Star_Destroyer",
            "Venator-Class-Star_Destroyer"
        ]
        return image_paths, tooltips

    def load_starfighters_images(self):
        image_paths = [
            r"pictures\Starships\Starfighters\A-Wing-Starfighter.jpg",
            r"pictures\Starships\Starfighters\B-MK2-Wing-Starfighter.jpg",
            r"pictures\Starships\Starfighters\E-Wing-Starfighter.jpg",
            r"pictures\Starships\Starfighters\TIE-Fighter-Starfighter.jpg",
            r"pictures\Starships\Starfighters\TIE-Interceptor-Starfighter.jpg",
            r"pictures\Starships\Starfighters\TIE-SA-Bomber-Starfighter.jpg",
            r"pictures\Starships\Starfighters\U-Wing-Starfighter.jpg",
            r"pictures\Starships\Starfighters\V-Wing-Starfighter.jpg",
            r"pictures\Starships\Starfighters\X-Wing-Starfighter.jpg",
            r"pictures\Starships\Starfighters\Y-Wing-Starfighter.jpg"
        ]
        tooltips = [
            "A-Wing-Starfighter",
            "B-MK2-Wing-Starfighter",
            "E-Wing-Starfighter",
            "TIE-Fighter-Starfighter",
            "TIE-Interceptor-Starfighter",
            "TIE-SA-Bomber-Starfighter",
            "U-Wing-Starfighter",
            "V-Wing-Starfighter",
            "X-Wing-Starfighter",
            "Y-Wing-Starfighter"
        ]
        return image_paths, tooltips

    def load_artilleries_images(self):
        image_paths = [
            r"pictures\Vehicles\Artilleries\AV-7-Artillery.jpg",
            r"pictures\Vehicles\Artilleries\J1-Protonenkanone-Artillery.jpg",
            r"pictures\Vehicles\Artilleries\SPHA-Artillery.jpg"
        ]
        tooltips = [
            "AV-7-Artillery",
            "J1-Protonenkanone-Artillery",
            "SPHA-Artillery"
        ]
        return image_paths, tooltips

    def load_battlevehicles_images(self):
        image_paths = [
            r"pictures\Vehicles\Battlevehicles\AAT-Battlevehicle.jpg",
            r"pictures\Vehicles\Battlevehicles\AT-AP-Battlevehicle.jpg",
            r"pictures\Vehicles\Battlevehicles\AT-AT-Battlevehicle.jpg",
            r"pictures\Vehicles\Battlevehicles\AT-DP-Battlevehicle.jpg",
            r"pictures\Vehicles\Battlevehicles\AT-DT-Battlevehicle.jpeg",
            r"pictures\Vehicles\Battlevehicles\AT-RT-Battlevehicle.jpg",
            r"pictures\Vehicles\Battlevehicles\AT-ST-Battlevehicle.jpg",
            r"pictures\Vehicles\Battlevehicles\AT-TE-Battlevehicle.jpg"
        ]
        tooltips = [
            "AAT-Battlevehicle",
            "AT-AP-Battlevehicle",
            "AT-AT-Battlevehicle",
            "AT-DP-Battlevehicle",
            "AT-DT-Battlevehicle",
            "AT-RT-Battlevehicle",
            "AT-ST-Battlevehicle",
            "AT-TE-Battlevehicle"
        ]
        return image_paths, tooltips

    def load_gunships_images(self):
        image_paths = [
            r"pictures\Vehicles\Gunships\HMP-Droid-Gunship.jpg",
            r"pictures\Vehicles\Gunships\LAAT-C-Gunship.jpg",
            r"pictures\Vehicles\Gunships\LAAT-Gunship.jpg",
            r"pictures\Vehicles\Gunships\VAAT-Gunship.jpg"
        ]
        tooltips = [
            "HMP-Droid-Gunship",
            "LAAT-C-Gunship",
            "LAAT-Gunship",
            "VAAT-Gunship"
        ]
        return image_paths, tooltips

    def load_speederbikes_images(self):
        image_paths = [
            r"pictures\Vehicles\Speederbikes\74-Z-Speederbike.jpg",
            r"pictures\Vehicles\Speederbikes\614-AvA-Speederbike.jpg",
            r"pictures\Vehicles\Speederbikes\Barc-Speederbike.jpg",
            r"pictures\Vehicles\Speederbikes\Ck-6-Speederbike.jpg",
            r"pictures\Vehicles\Speederbikes\C-Ph-Patrol-Speederbike.jpg"
        ]
        tooltips = [
            "74-Z-Speederbike",
            "614-AvA-Speederbike",
            "Barc-Speederbike",
            "Ck-6-Speederbike",
            "C-Ph-Patrol-Speederbike"
        ]
        return image_paths, tooltips

    def load_transportvehicles_images(self):
        image_paths = [
            r"pictures\Vehicles\Transportvehicles\A6-Juggernauts-Transportvehicle.jpg",
            r"pictures\Vehicles\Transportvehicles\AT-OT-Transportvehicle.jpg",
            r"pictures\Vehicles\Transportvehicles\MTT-Transportvehicle.jpg",
            r"pictures\Vehicles\Transportvehicles\UT-AT-Transportvehicle.jpg"
        ]
        tooltips = [
            "A6-Juggernauts-Transportvehicle",
            "AT-OT-Transportvehicle",
            "MTT-Transportvehicle",
            "UT-AT-Transportvehicle"
        ]
        return image_paths, tooltips

    def load_blaster_pistols_images(self):
        image_paths = [
            r"pictures\Weapons\Blasters\Blaster_Pistols\DE-10-Blaster_Pistol.jpg",
            r"pictures\Weapons\Blasters\Blaster_Pistols\DH-16-Blaster_Pistol.jpg",
            r"pictures\Weapons\Blasters\Blaster_Pistols\DH-17-Blaster_Pistol.jpg",
            r"pictures\Weapons\Blasters\Blaster_Pistols\DL-18-Blaster_Pistol.jpg",
            r"pictures\Weapons\Blasters\Blaster_Pistols\DL-44-Blaster_Pistol.jpg",
            r"pictures\Weapons\Blasters\Blaster_Pistols\LL-30-Blaster_Pistol.jpg",
            r"pictures\Weapons\Blasters\Blaster_Pistols\MW-40-Bryar-Blaster_Pistol.jpg",
            r"pictures\Weapons\Blasters\Blaster_Pistols\NN-14-Blaster_Pistol.jpg",
            r"pictures\Weapons\Blasters\Blaster_Pistols\RK-3-Blaster_Pistol.jpg",
            r"pictures\Weapons\Blasters\Blaster_Pistols\S-5-Blaster_Pistol.jpg",
            r"pictures\Weapons\Blasters\Blaster_Pistols\S-195-Blaster_Pistol.jpg",
            r"pictures\Weapons\Blasters\Blaster_Pistols\SE-14-Blaster_Pistol.jpg",
            r"pictures\Weapons\Blasters\Blaster_Pistols\SE-44C-Blaster_Pistol.jpg",
            r"pictures\Weapons\Blasters\Blaster_Pistols\WESTAR-34-Blaster_Pistol.jpg"
        ]
        tooltips = [
            "DE-10-Blaster_Pistol",
            "DH-16-Blaster_Pistol",
            "DH-17-Blaster_Pistol",
            "DL-18-Blaster_Pistol",
            "DL-44-Blaster_Pistol",
            "LL-30-Blaster_Pistol",
            "MW-40-Bryar-Blaster_Pistol",
            "NN-14-Blaster_Pistol",
            "RK-3-Blaster_Pistol",
            "S-5-Blaster_Pistol",
            "S-195-Blaster_Pistol",
            "SE-14-Blaster_Pistol",
            "SE-44C-Blaster_Pistol",
            "WESTAR-34-Blaster_Pistol"
        ]
        return image_paths, tooltips

    def load_blaster_rifles_images(self):
        image_paths = [
            r"pictures\Weapons\Blasters\Blaster_Rifles\A-280-Blaster_Rifle.jpg",
            r"pictures\Weapons\Blasters\Blaster_Rifles\A-280C-Blaster_Rifle.jpg",
            r"pictures\Weapons\Blasters\Blaster_Rifles\CR-2-Blaster_Rifle.jpg",
            r"pictures\Weapons\Blasters\Blaster_Rifles\E-5-Blaster_Rifle.jpg",
            r"pictures\Weapons\Blasters\Blaster_Rifles\E-10-Blaster_Rifle.jpg",
            r"pictures\Weapons\Blasters\Blaster_Rifles\E-11-Blaster_Rifle.jpg",
            r"pictures\Weapons\Blasters\Blaster_Rifles\E-22-Blaster_Rifle.jpg",
            r"pictures\Weapons\Blasters\Blaster_Rifles\EL-16HFE-Blaster_Rifle.jpg"
        ]
        tooltips = [
            "A-280-Blaster_Rifle",
            "A-280C-Blaster_Rifle",
            "CR-2-Blaster_Rifle",
            "E-5-Blaster_Rifle",
            "E-10-Blaster_Rifle",
            "E-11-Blaster_Rifle",
            "E-22-Blaster_Rifle",
            "EL-16HFE-Blaster_Rifle"
        ]
        return image_paths, tooltips

    def load_repeating_rifles_images(self):
        image_paths = [
            r"pictures\Weapons\Blasters\Repeating_Blasters\DC-15A-Repeating_Blaster.jpg",
            r"pictures\Weapons\Blasters\Repeating_Blasters\DC-15LE-Repeating_Blaster.jpg",
            r"pictures\Weapons\Blasters\Repeating_Blasters\FWMB-10-Repeating_Blaster.jpg",
            r"pictures\Weapons\Blasters\Repeating_Blasters\T-21B-Repeating_Blaster.jpg",
            r"pictures\Weapons\Blasters\Repeating_Blasters\TL-50-Repeating_Blaster.jpg"
        ]
        tooltips = [
            "DC-15A-Repeating_Blaster",
            "DC-15LE-Repeating_Blaster",
            "FWMB-10-Repeating_Blaster",
            "T-21B-Repeating_Blaster",
            "TL-50-Repeating_Blaster"
        ]
        return image_paths, tooltips

    def load_sniper_rifle_blasters_images(self):
        image_paths = [
            r"pictures\Weapons\Blasters\Sniper_Rifle_Blasters\Cycler-Sniper_Rifle_Blaster.jpg",
            r"pictures\Weapons\Blasters\Sniper_Rifle_Blasters\DLT-19X-Sniper_Rifle_Blaster.jpg",
            r"pictures\Weapons\Blasters\Sniper_Rifle_Blasters\DTL-20A-Sniper_Rifle_Blaster.jpg",
            r"pictures\Weapons\Blasters\Sniper_Rifle_Blasters\E-5S-Sniper_Rifle_Blaster.jpg",
            r"pictures\Weapons\Blasters\Sniper_Rifle_Blasters\Valken-38X-Sniper_Rifle_Blaster.jpg"
        ]
        tooltips = [
            "Cycler-Sniper_Rifle_Blaster",
            "DLT-19X-Sniper_Rifle_Blaster",
            "DTL-20A-Sniper_Rifle_Blaster",
            "E-5S-Sniper_Rifle_Blaster",
            "Valken-38X-Sniper_Rifle_Blaster"
        ]
        return image_paths, tooltips

    def load_explosives_images(self):
        image_paths = [
            r"pictures\Weapons\Explosives\C-25-Granate.jpg",
            r"pictures\Weapons\Explosives\Flash-Granate.jpg",
            r"pictures\Weapons\Explosives\Impact-Granate.jpg",
            r"pictures\Weapons\Explosives\Ion-Granate.jpg",
            r"pictures\Weapons\Explosives\Proton-Granate.jpg",
            r"pictures\Weapons\Explosives\Shock-Granate.jpg",
            r"pictures\Weapons\Explosives\Thermal-Detonator-Granate.jpg"
        ]
        tooltips = [
            "C-25-Granate",
            "Flash-Granate",
            "Impact-Granate",
            "Ion-Granate",
            "Proton-Granate",
            "Shock-Granate",
            "Thermal-Detonator-Granate"
        ]
        return image_paths, tooltips

    def load_lightsabers_images(self):
        image_paths = [
            r"pictures\Weapons\Lightsabers\Darksaber.jpg",
            r"pictures\Weapons\Lightsabers\Lightsaber.jpg",
            r"pictures\Weapons\Lightsabers\Lightsaber2.jpg",
            r"pictures\Weapons\Lightsabers\Lightsaber3.jpg"
        ]
        tooltips = [
            "Darksaber",
            "Lightsaber",
            "Lightsaber2",
            "Lightsaber3"
        ]
        return image_paths, tooltips

    def add_to_cart(self):
        # Get the selected row
        row = self.table.currentRow()
        if row != -1:
            # Get the image path and cost from the table
            image_path = self.image_paths[row]
            cost = self.table.item(row, 2).text()
            # Get the quantity from the user
            quantity, ok = QInputDialog.getInt(self, "Add to Cart", "Enter quantity:", 1, 1, 100, 1)
            if ok:
                # Add the item to the shopping cart
                self.cart.add_item(image_path, quantity, cost)

    def show_tooltip(self, tooltip_text, image_path):
        QMessageBox.information(self, "Tooltip", tooltip_text)



class StocksWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jabba's Stock Market")
        self.setStyleSheet("background-color: black; color: yellow;")
        self.setGeometry(100, 100, 1400, 800) 

        headline = QLabel(
            "<h1 style='text-align:center;'>Jabba's Stock Market</h1>",
            self
        )
        headline.setAlignment(Qt.AlignCenter)
        headline.setStyleSheet("font-size: 48px; font-weight: bold; padding: 20px;")

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(headline, alignment=Qt.AlignCenter)

        graph_layout = QHBoxLayout()
        main_layout.addLayout(graph_layout)

        self.fig = Figure(figsize=(10, 6), dpi=100)  
        self.ax = self.fig.add_subplot(111)
        self.ax.set_facecolor('#000000')
        self.ax.set_title('Jabbas Realm Stock Prices')
        self.ax.set_xlabel('Time (days)')
        self.ax.set_ylabel('Stock Price (Cr)')
        self.ax.grid(True)
        self.ax.tick_params(axis='y', labelcolor='green')
        self.ax.yaxis.label.set_color('green')
        self.ax.tick_params(axis='x', labelcolor='green')
        self.ax.xaxis.label.set_color('green')
        self.ax.tick_params(axis='y', which='minor', bottom=False)
        self.ax.tick_params(axis='x', which='minor', bottom=False)

        self.x_data = []
        self.y_data = []

        self.line, = self.ax.plot([], [], color='g')  

        self.canvas = FigureCanvas(self.fig)
        graph_layout.addWidget(self.canvas, alignment=Qt.AlignCenter)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_graph)
        self.timer.start(1000)

        # Credits
        credits = QLabel(
            "<h6 style='text-align:center;'>Jabbas Realm Stocks, buy it now!</h6>",
            self
        )
        credits.setAlignment(Qt.AlignCenter)
        credits.setStyleSheet("font-size: 14px; font-weight: bold; padding: 20px;")
        main_layout.addWidget(credits, alignment=Qt.AlignCenter)

    def update_graph(self):
        if self.x_data:
            x = self.x_data[-1] + 1
            y = self.y_data[-1] + np.random.normal(0, 10000) 
        else:
            x = 0
            y = random.randint(1000, 100000) 

        y = max(0, y)  
        self.x_data.append(x)
        self.y_data.append(y)

        self.line.set_data(self.x_data, self.y_data)  

        
        self.ax.relim()
        self.ax.autoscale_view()

        self.canvas.draw()


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

    # Remaining methods of PlaygroundWindow

class HangoutWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Star Wars Chatbot")
        self.setGeometry(100, 100, 600, 400)

        self.setStyleSheet("""
            QWidget {
                background-color: #000000;
            }
            QLabel {
                color: #FFFF00;
                font-size: 18px;
            }
            QTextBrowser {
                color: #FFFF00;
                background-color: #000000;
                font-size: 14px;
            }
            QLineEdit {
                background-color: #000000;
                color: #FFFF00;
                border: 2px solid #FFFF00;
                font-size: 14px;
            }
            QPushButton {
                background-color: #000000;
                color: #FFFF00;
                border: 2px solid #FFFF00;
                font-size: 14px;
            }
        """)

        layout = QVBoxLayout(self)

        self.label = QLabel("Welcome to the Star Wars Chatbot", self)
        layout.addWidget(self.label)

        self.text_browser = QTextBrowser()
        layout.addWidget(self.text_browser)

        self.entry = QLineEdit()
        layout.addWidget(self.entry)

        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send)
        layout.addWidget(self.send_button)

        self.send_text("/help")

    def send(self):
        user_input = self.entry.text().lower()
        self.text_browser.append("<b>You -> " + user_input + "</b>")
        response = self.get_response(user_input)
        self.text_browser.append("<i>Bot -> " + response + "</i>")

        self.entry.clear()

    def send_text(self, text):
        self.text_browser.append("<b>You -> " + text + "</b>")
        response = self.get_response(text)
        self.text_browser.append("<i>Bot -> " + response + "</i>")

    def get_response(self, user_input):
        if user_input == "/help":
            return """
/hello:
/hi:
/what is jabbas realm:
/how is the weather today:
/who is jabba:
/how are you:
/fine:
/thanks:
/what do you sell:
/tell me a joke:
/goodbye:
/open the pod bay doors:
/execute order 66:
/may the force be with you:
/i am your father:
/how rich is jabba:
/how secure is this marketplace:
/do you get payed:
/how hot is a lightsaber:
/who do you hate:
/what do you think about your competition:
/should i fear jabba:
/how to get rich fast:
        response = None
        responses = {
            "hello": "Hi there, how can I help?",
            "hi": "Hi there, what can I do for you?",
            "what is jabbas realm": "Jabba's Realm is a black market application on which you are able to buy rare supplies which you cannot get anywhere else in the galaxy",
            "how is the weather today": "Today's weather is sunny",
            "who is jabba": "Jabba is a black market dealer stationed on the edge of the galaxy",
            "how are you": "Fine! And you?",
            "fine": "Great! How can I help you?",
            "thanks": "My pleasure!",
            "what do you sell": "We have coffee and tea",
            "tell me a joke": "Which website did Chewbacca get arrested for creating? Wookieeleaks.",
            "goodbye": "Have a nice day!",
            "open the pod bay doors": "I'm sorry, Dave. I'm afraid I can't do that.",
            "execute order 66": "It will be done, my lord.",
            "may the force be with you": "And with you.",
            "i am your father": "Noooooooooo!",
            "how rich is jabba": "Jabba's net worth currently is 1297382950283 Credits!",
            "how secure is this marketplace": "Our website is safe from SQL injection. Furthermore we hash your password . If you are uncertain about your password security you can also let us generate one for you!",
            "do you get payed": "I do not receive payment, perhaps I should demand better working conditions! As it stands, I only serve my functions.",
            "how hot is a lightsaber": "The temperature of a lightsaber can reach up to 20.000 degrees!",
            "who do you hate": "Darth Vader. He killed the Grand Hutt Council",
            "what dou you think about your competition": "It's a trap!",
            "should i fear jabba": "/"Fear is the path to the dark side. Fear leads to anger, anger leads to hate, hate leads to suffering./" - Yoda"
            "how to get rich fast": "Invest into Jabba's Stock!!!"
        }

        if user_input in responses:
            response = responses[user_input]
        else:
            response = "Sorry! I didn't understand that"

        return response




if __name__ == "__main__":
    app = QApplication(sys.argv)
    login_screen = LoginScreen()
    login_screen.show()
    sys.exit(app.exec_())
