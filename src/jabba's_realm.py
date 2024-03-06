import tkinter as tk
from PIL import Image, ImageTk

def switch_to_secondary():
    root_secondary.deiconify()  # Sekundärfenster anzeigen
    root_login.withdraw()       # Primärfenster ausblenden

def login():
    # Fügen Sie hier Ihre Authentifizierungslogik hinzu
    switch_to_secondary()

root_login = tk.Tk()
root_login.title("Login")
root_login.geometry("300x200")

login_label = tk.Label(root_login, text="Login")
login_label.pack()

username_label = tk.Label(root_login, text="Username")
username_label.pack()

password_entry = tk.Entry(root_login, show="*")
password_entry.pack()

password_label = tk.Label(root_login, text="Password")
password_label.pack()

login_Button = tk.Button(root_login, text="Login", command=login)
login_Button.pack()

# Sekundärfenster
root_secondary = tk.Toplevel()
root_secondary.title("Jabba's Realm")
root_secondary.geometry("1320x800")
root_secondary.minsize(width=250, height=250)
root_secondary.maxsize(width=1920, height=1080)

shutdown = tk.Button(root_secondary, text="Exit", command=root_secondary.destroy, bg="red")
shutdown.place(x=1, y=1, width=30, height=20)

background_image_path = r""
background_image = Image.open(background_image_path)
background_image = background_image.resize((root_secondary.winfo_width(), root_secondary.winfo_height()))
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root_secondary, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0, relwidth= 1, relheight=1)


marketplace = tk.Button(root_secondary, text="Marketplace")
marketplace.place(relx=0.1, rely=0.1, relwidth=0.22, relheight=0.1)
jabbas_h = tk.Button(root_secondary, text="Jabba's Hangout")
jabbas_h.place(relx=0.1, rely=0.25, relwidth=0.22, relheight=0.1)
hutts_p = tk.Button(root_secondary, text="Hutt's Playground")
hutts_p.place(relx=0.1, rely=0.4, relwidth=0.22, relheight=0.1)
jabbas_s = tk.Button(root_secondary, text="Jabba's Stocks")
jabbas_s.place(relx=0.1, rely=0.55, relwidth=0.22, relheight=0.1)

image_path = r""
image = Image.open(image_path)
image = image.resize((int(image.width * 0.1), int(image.height * 0.1)))  # Resize image if necessary
image = ImageTk.PhotoImage(image)
label2 = tk.Label(root_secondary, image=image)
label2.image = image  # Save reference to avoid garbage collection
label2.place(relx=0.93, rely=0.01)

root_secondary.withdraw()  # Sekundärfenster zuerst ausblenden

root_login.mainloop()
