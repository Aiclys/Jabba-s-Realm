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
        self.current_user = None  # Hinzufügen einer Instanzvariable für den aktuellen Benutzer

        # Set window title and size
        self.setWindowTitle("Login Screen")
        self.setFixedSize(500, 300)

        # Create and set the background image directly on the central widget
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # Set background image using Stylesheet
        background_image_path = r"pictures\Background_stern.png"  # Replace "background_image.jpg" with the path to your image
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
        layout.addWidget(title_label, alignment=Qt.AlignCenter)
        layout.addWidget(self.username_input, alignment=Qt.AlignCenter)
        layout.addWidget(self.password_input, alignment=Qt.AlignCenter)
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.register_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.forgot_password_button, alignment=Qt.AlignCenter)

        # Play background music for login screen
        self.play_background_music(r"Audio\\Login.mp3")

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
    
        # Check if username or password fields are empty
        if not username or not password:
            QMessageBox.warning(self, "Login Failed", "Please enter both username and password.")
            return

        # Check credentials against the database
        conn = sqlite3.connect("jabbas-data.db")
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
            region = dialog.region_dropdown.currentText()  # Get the selected region from the dropdown

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
        conn = sqlite3.connect("jabbas-data.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users(username, password, email, region, balance) VALUES (?, ?, ?, ?, ?)", (username, password, email, region, 99999999999999999999))
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


class MainScreen(QMainWindow):
    def __init__(self, current_user):
        super().__init__()

        self.current_user = current_user  # Store the current user

        # Set window title and size
        self.setWindowTitle("Main Screen")
        self.setGeometry(100, 100, 500, 500)

        # Set background color
        self.setStyleSheet("background-color: black;")

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
            button.setStyleSheet("font-size: 24px; font-weight: bold; background-color: #ffcc00; color: black")
            self.button_widgets.append(button)

        # Add image in the top right corner
        self.logo_label = QLabel()
        self.logo_label.setScaledContents(True)
        self.set_background_image(self.logo_label, "pictures/credits.png")

        # Label to display credits
        self.credits_label = QLabel()
        self.credits_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #ffcc00")
        self.update_credits_label()  # Update credits label initially

        # Layout setup
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(title_label, alignment=Qt.AlignCenter)
        for button in self.button_widgets:
            layout.addWidget(button, alignment=Qt.AlignCenter)
        layout.addWidget(self.credits_label, alignment=Qt.AlignRight)  # Add credits label
        layout.addStretch(1)

        # Horizontal layout for logo
        h_layout = QHBoxLayout()
        h_layout.addStretch(1)
        h_layout.addWidget(self.logo_label)
        layout.addLayout(h_layout)

        #Play background music for main screen
        self.play_background_music(r"Audio\cantina.mp3")

    def update_credits_label(self):
        # Fetch credits from the database for the current user
        username = self.current_user
        conn = sqlite3.connect(r"H:\Desktop\App_Programming\jabbas-data.db")
        cursor = conn.cursor()
        cursor.execute("SELECT balance FROM users WHERE username=?", (username,))
        credits = cursor.fetchone()[0]  # Fetch the first column of the first row (assuming there's only one row)
        conn.close()

        self.credits_label.setText(f"Credits: {credits}")

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

    def set_background_image(self, widget, image_path):
        pixmap = QPixmap(image_path)
        widget.setPixmap(pixmap)

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
        self.category_dropdown.addItems(["creatures", "Astromechdroids", "Battledroids", "Maintenancedroids", "Medicaldroids", "Protocoldroids", "Corvettes", "Frigates", "Shuttles", "Star_Destroyers", "Starfighters", "Artilleries", "Battlevehicles", "Gunships", "Speederbikes", "Transportvehicles", "Blaster_Pistols", "Blaster_Rifles", "Repeating_Rifles", "Sniper_Rifle_Blasters", "Explosives", "Lightsabers"]) 
        self.category_dropdown.currentIndexChanged.connect(self.show_images)

        # Dropdown menu for subcategories
        self.subcategory_dropdown = QComboBox()

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
        layout.addWidget(self.subcategory_dropdown)
        layout.addWidget(self.scroll_area)

    def show_images(self):
        selected_category = self.category_dropdown.currentText()
        selected_subcategory = self.subcategory_dropdown.currentText()
        image_paths = []
        tooltips = []

        if selected_category == "creatures":
            image_paths = [
                r"Pictures/Creatures/Bane-Back-Spider.jpg",
                r"Pictures/Creatures/Bog-rat.jpg",
                r"Pictures/Creatures/Chirodactyl.jpg",
                r"Pictures/Creatures/Flame-Beetle.jpeg",
                r"Pictures/Creatures/Jotaz.jpg",
                r"Pictures/Creatures/Mykal.jpg",
                r"Pictures/Creatures/Oggdo.jpg",
                r"Pictures/Creatures/Phillak.jpg",
                r"Pictures/Creatures/Scazz.jpg",
                r"Pictures/Creatures/Slyyyg.jpg",
                r"Pictures/Creatures/Splox.jpg",
                r"Pictures/Creatures/Wyyyschokk.jpg"
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
            pass
        elif selected_category == "Astromechdroids":
            image_paths = [
                r"Pictures/Droids/Astromechdroids/R-1-Astromechdroid.jpg",
                r"Pictures/Droids/Astromechdroids/R-2-Astromechdroid.jpg",
                r"Pictures/Droids/Astromechdroids/R-3-Astromechdroid.jpg",
                r"Pictures/Droids/Astromechdroids/R-4-Astromechdroid.jpg",
                r"Pictures/Droids/Astromechdroids/R-5-Astromechdroid.jpg",
                r"Pictures/Droids/Astromechdroids/R-6-Astromechdroid.jpg",
                r"Pictures/Droids/Astromechdroids/R-7-Astromechdroid.jpg",
                r"Pictures/Droids/Astromechdroids/R-8-Astromechdroid.jpg",
                r"Pictures/Droids/Astromechdroids/R-9-Astromechdroid.jpg"
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
            pass
        elif selected_category == "Battledroids":
            image_paths = [
                r"Pictures/Droids/Battledroids/R-1-Battledroid.jpg",
                r"Pictures/Droids/Battledroids/B-2-Ha-Super-Battledroid.jpg",
                r"Pictures/Droids/Battledroids/B-2-Super-Battledroid.jpg",
                r"Pictures/Droids/Battledroids/Bx-Kommando-Battledroid.jpg",
                r"Pictures/Droids/Battledroids/Droideka-Battledroid.jpg",
                r"Pictures/Droids/Battledroids/Dwarf-Spider-Battledroid.jpg",
                r"Pictures/Droids/Battledroids/IG-86-Wächter-Battledroid.jpg",
                r"Pictures/Droids/Battledroids/IG-100-Magna-Battledroid.jpg"
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
            pass
        elif selected_category == "Maintenancedroids":
            image_paths = [
                r"Pictures\Droids\Astromechdroids\\R-1-Astromechdroid.jpg",
                r"Pictures\Droids\Astromechdroids\\R-2-Astromechdroid.jpg",
                r"Pictures\Droids\Astromechdroids\\R-3-Astromechdroid.jpg",
                r"Pictures\Droids\Astromechdroids\\R-4-Astromechdroid.jpg",
                r"Pictures\Droids\Astromechdroids\\R-5-Astromechdroid.jpg",
                r"Pictures\Droids\Astromechdroids\\R-6-Astromechdroid.jpg",
                r"Pictures\Droids\Astromechdroids\\R-7-Astromechdroid.jpg",
                r"Pictures\Droids\Astromechdroids\\R-8-Astromechdroid.jpg",
                r"Pictures\Droids\Astromechdroids\\R-9-Astromechdroid.jpg"
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
            pass
        elif selected_category == "Medicaldroids":
            image_paths = [
                r"Pictures/Droids/Medicaldroids/2-1B-Medicaldroid.jpg",
                r"Pictures/Droids/Medicaldroids/8T88-Medicaldroid.jpg",
                r"Pictures/Droids/Medicaldroids/DD-13-Medicaldroid.jpg",
                r"Pictures/Droids/Medicaldroids/FX-Medicaldroid.jpg",
                r"Pictures/Droids/Medicaldroids/IM-6-Medicaldroid.jpg",
                r"Pictures/Droids/Medicaldroids/SP-4-Medicaldroid.jpg",
            ]
            tooltips = [
                "2-1B-Medicaldroid",
                "8T88-Medicaldroid",
                "DD-13-Medicaldroid",
                "FX-Medicaldroid",
                "IM-6-Medicaldroid",
                "SP-4-Medicaldroid"
            ]
            pass
        elif selected_category == "Protocoldroids":
            image_paths = [
                r"Pictures/Droids/Protocoldroids/3PO-Protocoldroid.jpg",
                r"Pictures/Droids/Protocoldroids/CZ-Serie-Protocoldroid.jpg",
                r"Pictures/Droids/Protocoldroids/RA-7-Protocoldroid.jpg"
            ]
            tooltips = [
                "3PO-Protocoldroid",
                "CZ-Serie-Protocoldroid",
                "RA-7-Protocoldroid"
            ]
            pass
        elif selected_category == "Corvettes":
            image_paths = [
                r"Pictures\Starships\\Corvettes\\CR-70-Corvette.jpg",
                r"Pictures\Starships\\Corvettes\\CR-90-Corvette.jpg",
                r"Pictures\Starships\\Corvettes\\CY-180-Corvette.jpg",
                r"Pictures\Starships\\Corvettes\\Raider-Class-Corvette.jpg",
                r"Pictures\Starships\\Corvettes\Sphyrna-Class-Corvette.jpg"
            ]
            tooltips = [
                "CR-70-Corvette",
                "CR-90-Corvette",
                "CY-180-Corvette",
                "Raider-Class-Corvette",
                "Sphyrna-Class-Cor"
            ]
            pass
        elif selected_category == "Frigates":
            image_paths = [
                r"Pictures\Starships\\Frigates\Arquitens-Class-Frigate.jpg",
                r"Pictures\Starships\\Frigates\\Corona-Class-Frigate.jpg",
                r"Pictures\Starships\\Frigates\\EF-76-Nebulon-B-Frigate.jpg",
                r"Pictures\Starships\\Frigates\\Kontos-Class-Frigate.jpg",
                r"Pictures\Starships\\Frigates\\Munificent-Class-Frigate.jpg",
                r"Pictures\Starships\\Frigates\\Pelta-Class-Frigate.jpg"
            ]
            tooltips = [
                "Arquitens-Class-Frigate",
                "Corona-Class-Frigate",
                "EF-76-Nebulon-B-Frigate",
                "Kontos-Class-Frigate",
                "Munificent-Class-Frigate",
                "Pelta-Class-Frigate"
            ]
            pass
        elif selected_category == "Shuttles":
            image_paths = [
                r"Pictures\Starships\Shuttles\Delta-Class-T-3C-Shuttle.jpg",
                r"Pictures\Starships\Shuttles\\Eta-Class-Shuttle.jpg",
                r"Pictures\Starships\Shuttles\\H-2-Shuttle.jpg",
                r"Pictures\Starships\Shuttles\\Lambda-T-4A-Class-Shuttle.jpg",
                r"Pictures\Starships\Shuttles\\Nu-Class-Attack-Shuttle.jpg",
                r"Pictures\Starships\Shuttles\\Rho-Class-Shuttle.jpg",
                r"Pictures\Starships\Shuttles\\T-6-Shuttle.jpg",
                r"Pictures\Starships\Shuttles\\Theta-Class-T-2C-Shuttle.jpg"
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
            pass
        elif selected_category == "Star_Destroyers":
            image_paths = [
                "Pictures\Starships\Star_Destroyers\Immobilizer-418-Star_Destroyer.jpg",
                "Pictures\Starships\Star_Destroyers\Venator-Class-Star_Destroyer.jpg"
            ]
            tooltips = [
                "Immobilizer-418-Star_Destroyer",
                "Venator-Class-Star_Destroyer"
            ]
            pass
        elif selected_category == "Starfighters":
            image_paths = [
                r"Pictures\Starships\Starfighters\A-Wing-Starfighter.jpg",
                r"Pictures\Starships\Starfighters\B-MK2-Wing-Starfighter.jpg",
                r"Pictures\Starships\Starfighters\\E-Wing-Starfighter.jpg",
                r"Pictures\Starships\Starfighters\\TIE-Fighter-Starfighter.jpg",
                r"Pictures\Starships\Starfighters\\TIE-Interceptor-Starfighter.jpg",
                r"Pictures\Starships\Starfighters\\TIE-SA-Bomber-Starfighter.jpg",
                r"Pictures\Starships\Starfighters\\U-Wing-Starfighter.jpg",
                r"Pictures\Starships\Starfighters\\V-Wing-Starfighter.jpg",
                r"Pictures\Starships\Starfighters\\X-Wing-Starfighter.jpg",
                r"Pictures\Starships\Starfighters\\Y-Wing-Starfighter.jpg"
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
            pass
        elif selected_category == "Artilleries":
            image_paths = [
                r"Pictures\Vehicles\Artilleries\AV-7-Artillery.jpg",
                r"Pictures\Vehicles\Artilleries\\J1-Protonenkanone-Artillery.jpg",
                r"Pictures\Vehicles\Artilleries\SPHA-Artillery.jpg"
            ]
            tooltips = [
                "AV-7-Artillery",
                "J1-Protonenkanone-Artillery",
                "SPHA-Artillery"
            ]
            pass
        elif selected_category == "Battlevehicles":
            image_paths = [
                r"Pictures\\Vehicles\Battlevehicles\AAT-Battlevehicle.jpg",
                r"Pictures\\Vehicles\Battlevehicles\AT-AP-Battlevehicle.jpg",
                r"Pictures\\Vehicles\Battlevehicles\AT-AT-Battlevehicle.jpg",
                r"Pictures\\Vehicles\Battlevehicles\AT-DP-Battlevehicle.jpg",
                r"Pictures\\Vehicles\Battlevehicles\AT-DT-Battlevehicle.jpeg",
                r"Pictures\\Vehicles\Battlevehicles\AT-RT-Battlevehicle.jpg",
                r"Pictures\\Vehicles\Battlevehicles\AT-ST-Battlevehicle.jpg",
                r"Pictures\\Vehicles\Battlevehicles\AT-TE-Battlevehicle.jpg"
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
            pass
        elif selected_category == "Gunships":
            image_paths = [
                r"Pictures\\Vehicles\\Gunships\\HMP-Droid-Gunship.jpg",
                r"Pictures\\Vehicles\\Gunships\\LAAT-C-Gunship.jpg",
                r"Pictures\\Vehicles\\Gunships\\LAAT-Gunship.jpg",
                r"Pictures\\Vehicles\\Gunships\\VAAT-Gunship.jpg"
            ]
            tooltips = [
                "HMP-Droid-Gunship",
                "LAAT-C-Gunship",
                "LAAT-Gunship",
                "VAAT-Gunship"
            ]
            pass
        elif selected_category == "Speederbikes":
            image_paths = [
                r"Pictures\\Vehicles\Speederbikes\\74-Z-Speederbike.jpg",
                r"Pictures\\Vehicles\Speederbikes\\614-AvA-Speederbike.jpg",
                r"Pictures\\Vehicles\Speederbikes\Barc-Speederbike.jpg",
                r"Pictures\\Vehicles\Speederbikes\\Ck-6-Speederbike.jpg",
                r"Pictures\\Vehicles\Speederbikes\\C-Ph-Patrol-Speederbike.jpg"
            ]
            tooltips = [
                "74-Z-Speederbike",
                "614-AvA-Speederbike",
                "Barc-Speederbike",
                "Ck-6-Speederbike",
                "C-Ph-Patrol-Speederbike"
            ]
            pass
        elif selected_category == "Transportvehicles":
            image_paths = [
                r"Pictures\\Vehicles\\Transportvehicles\A6-Juggernauts-Transportvehicle.jpg",
                r"Pictures\\Vehicles\\Transportvehicles\AT-OT-Transportvehicle.jpg",
                r"Pictures\\Vehicles\\Transportvehicles\\MTT-Transportvehicle.jpg",
                r"Pictures\\Vehicles\\Transportvehicles\\UT-AT-Transportvehicle.jpg"
            ]
            tooltips = [
                "A6-Juggernauts-Transportvehicle",
                "AT-OT-Transportvehicle",
                "MTT-Transportvehicle",
                "UT-AT-Transportvehicle"
            ]
            pass
        elif selected_category == "Blaster_Pistols":
            image_paths = [
                r"Pictures\Weapons\Blasters\Blaster_Pistols\DE-10-Blaster_Pistol.jpg",
                r"Pictures\Weapons\Blasters\Blaster_Pistols\DH-16-Blaster_Pistol.jpg",
                r"Pictures\Weapons\Blasters\Blaster_Pistols\DH-17-Blaster_Pistol.jpg",
                r"Pictures\Weapons\Blasters\Blaster_Pistols\DL-18-Blaster_Pistol.jpg",
                r"Pictures\Weapons\Blasters\Blaster_Pistols\DL-44-Blaster_Pistol.jpg",
                r"Pictures\Weapons\Blasters\Blaster_Pistols\\LL-30-Blaster_Pistol.jpg",
                r"Pictures\Weapons\Blasters\Blaster_Pistols\\MW-40-Bryar-Blaster_Pistol.jpg",
                r"Pictures\Weapons\Blasters\Blaster_Pistols\\NN-14-Blaster_Pistol.jpg",
                r"Pictures\Weapons\Blasters\Blaster_Pistols\\RK-3-Blaster_Pistol.jpg",
                r"Pictures\Weapons\Blasters\Blaster_Pistols\S-5-Blaster_Pistol.jpg",
                r"Pictures\Weapons\Blasters\Blaster_Pistols\S-195-Blaster_Pistol.jpg",
                r"Pictures\Weapons\Blasters\Blaster_Pistols\SE-14-Blaster_Pistol.jpg",
                r"Pictures\Weapons\Blasters\Blaster_Pistols\SE-44C-Blaster_Pistol.jpg",
                r"Pictures\Weapons\Blasters\Blaster_Pistols\WESTAR-34-Blaster_Pistol.jpg"
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
            pass
        elif selected_category == "Blaster_Rifles":
            image_paths = [
            r"Pictures\Weapons\Blasters\Blaster_Rifles\A-280-Blaster_Rifle.jpg",
            r"Pictures\Weapons\Blasters\Blaster_Rifles\A-280C-Blaster_Rifle.jpg",
            r"Pictures\Weapons\Blasters\Blaster_Rifles\\CR-2-Blaster_Rifle.jpg",
            r"Pictures\Weapons\Blasters\Blaster_Rifles\\E-5-Blaster_Rifle.jpg",
            r"Pictures\Weapons\Blasters\Blaster_Rifles\\E-10-Blaster_Rifle.jpg",
            r"Pictures\Weapons\Blasters\Blaster_Rifles\\E-11-Blaster_Rifle.jpg",
            r"Pictures\Weapons\Blasters\Blaster_Rifles\\E-22-Blaster_Rifle.jpg",
            r"Pictures\Weapons\Blasters\Blaster_Rifles\\EL-16HFE-Blaster_Rifle.jpg"
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
            pass
        elif selected_category == "Repeating_Rifles":
            image_paths = [
                r"Pictures\Weapons\Blasters\\Repeating_Blasters\DC-15A-Repeating_Blaster.jpg",
                r"Pictures\Weapons\Blasters\\Repeating_Blasters\DC-15LE-Repeating_Blaster.jpg",
                r"Pictures\Weapons\Blasters\\Repeating_Blasters\\FWMB-10-Repeating_Blaster.jpg",
                r"Pictures\Weapons\Blasters\\Repeating_Blasters\\T-21B-Repeating_Blaster.jpg",
                r"Pictures\Weapons\Blasters\\Repeating_Blasters\\TL-50-Repeating_Blaster.jpg"
            ]
            tooltips = [
                "DC-15A-Repeating_Blaster",
                "DC-15LE-Repeating_Blaster",
                "FWMB-10-Repeating_Blaster",
                "T-21B-Repeating_Blaster",
                "TL-50-Repeating_Blaster"
            ]
            pass
        elif selected_category == "Sniper_Rifle_Blasters":
            image_paths = [
                r"Pictures\Weapons\Blasters\Sniper_Rifle_Blasters\\Cycler-Sniper_Rifle_Blaster.jpg",
                r"Pictures\Weapons\Blasters\Sniper_Rifle_Blasters\DLT-19X-Sniper_Rifle_Blaster.jpg",
                r"Pictures\Weapons\Blasters\Sniper_Rifle_Blasters\DTL-20A-Sniper_Rifle_Blaster.jpg",
                r"Pictures\Weapons\Blasters\Sniper_Rifle_Blasters\\E-5S-Sniper_Rifle_Blaster.jpg",
                r"Pictures\Weapons\Blasters\Sniper_Rifle_Blasters\\Valken-38X-Sniper_Rifle_Blaster.jpg"
            ]
            tooltips = [
                "Cycler-Sniper_Rifle_Blaster",
                "DLT-19X-Sniper_Rifle_Blaster",
                "DTL-20A-Sniper_Rifle_Blaster",
                "E-5S-Sniper_Rifle_Blaster",
                "Valken-38X-Sniper_Rifle_Blaster"
            ]
            pass
        elif selected_category == "Explosives":
            image_paths = [
                r"Pictures\Weapons\\Explosives\\C-25-Granate.jpg",
                r"Pictures\Weapons\\Explosives\\Flash-Granate.jpg",
                r"Pictures\Weapons\\Explosives\\Impact-Granate.jpg",
                r"Pictures\Weapons\\Explosives\\Ion-Granate.jpg",
                r"Pictures\Weapons\\Explosives\\Proton-Granate.jpg",
                r"Pictures\Weapons\\Explosives\Shock-Granate.jpg",
                r"Pictures\Weapons\\Explosives\\Thermal-Detonator-Granate.jpg"
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
            pass
        elif selected_category == "Lightsabers":
            image_paths = [
                r"Pictures\Weapons\\Lightsabers\Darksaber.jpg",
                r"Pictures\Weapons\\Lightsabers\\Lightsaber.jpg",
                r"Pictures\Weapons\\Lightsabers\\Lightsaber2.jpg",
                r"Pictures\Weapons\\Lightsabers\\Lightsaber3.jpg"
            ]
            tooltips = [
                "Darksaber",
                "Lightsaber",
                "Lightsaber2",
                "Lightsaber3"
            ]
            pass

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

    # Remaining methods of PlaygroundWindow

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
