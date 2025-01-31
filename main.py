import tkinter as tk
import pyperclip
from PIL import Image, ImageTk
import os
import webbrowser

class CodeCenterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kód Központ")
        self.root.geometry("800x600")
        self.root.configure(bg='#1e1e1e')  # Dark grey background

        # Set up data
        self.setup_data()
        self.setup_ui()

    def setup_data(self):
        self.data = {
            "Netflix": {"code": ".nf.", "icon": "netflix_logo.png"},
            "Amazon Prime Video": {"code": ".amzn.", "icon": "amazon_prime_video_logo.png"},
            "Disney Plus": {"code": ".dsnp.", "icon": "disney_logo.png"},
            "HBO Max": {"code": ".hmax.", "icon": "hbo_logo.png"},
            "Sky Show Time": {"code": ".skst.", "icon": "skyshowtime_logo.png"},
            "Hulu": {"code": ".hulu.", "icon": "hulu_logo.png"},
            "RTL Klub": {"code": ".rtlp.", "icon": "rtl_logo.png"},
            "TV2 Play": {"code": ".tv2.", "icon": "tv2_play_logo.png"},
        }
        self.oldalak_data = {
            "HunTorrent": {"url": "https://huntorrent.org/browse.php?korhatar=0&xyz=yes&c3=1&c5=1&c1=1&c17=1&c18=1&c25=1&c23=1&c38=1&c26=1&c20=1&c21=1&c9=1&c7=1&c12=1&c10=1&sort=7&type=desc"},
            "Estone": {"url": "https://estone.cc/bongeszo.php?nyitja_zene_resz=true&nyitja_filmek_resz=true&nyitja_konyv_resz=true&nyitja_sorozat_resz=true&nyitja_program_resz=true&nyitja_jatek_resz=true&nyitja_xxx_resz=true&kat%5B%5D=28&true&kat%5B%5D=44&kat%5B%5D=49&&kat%5B%5D=41&kat%5B%5D=30&kat%5B%5D=24&kat%5B%5D=51&kat%5B%5D=25&kat%5B%5D=42&kat%5B%5D=36&kat%5B%5D=35&kat%5B%5D=34&kat%5B%5D=39&kereses_nev=&miben=0&cimke=&cat=0&submit.x=36&submit.y=16&feltoltok=DESC"},
            "Majomparádé": {"url": "https://majomparade.net/letoltes.php?tipus=1&time1728375316&k=yes&hogyan=csokkeno&category%5B%5D=4&category%5B%5D=50&category%5B%5D=25&category%5B%5D=59&category%5B%5D=51&category%5B%5D=24&category%5B%5D=87&category%5B%5D=36&category%5B%5D=6&category%5B%5D=56&category%5B%5D=44&category%5B%5D=28&category%5B%5D=30&category%5B%5D=74&category%5B%5D=41&category%5B%5D=34&category%5B%5D=35&category%5B%5D=46&category%5B%5D=4&tipus=1&rendezes=feltoltok"},
            "1337x": {"url": "https://1337x.to/"},
            "Ncore": {"url": "https://ncore.pro/login.php?honnan=/torrents.php"},
            "RARBG": {"url": "https://en.rarbg-official.com/movies?keyword=&quality=&genre=&rating=0&year=0&language=hu&order_by=latest"},
        }
        self.locations_data = {
            "Filmek": {"location": "/Filmek", "icon": "images/Films_logo.png"},
            "Sorozatok": {"location": "/Sorozatok"},
            "Magazinok": {"location": "/Magazinok"},
            "Programok": {"location": "/Programok"},
        }

    def open_url(self, service):
        url = self.oldalak_data.get(service, {}).get("url")
        if url:
            webbrowser.open(url)

    def setup_ui(self):
        main_frame = tk.Frame(self.root, bg='#1e1e1e')
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = tk.Label(main_frame, text="Kód Központ", font=("Helvetica", 24, "bold"), fg='#00ff00', bg='#1e1e1e')
        title_label.pack(pady=20)

        buttons_frame = tk.Frame(main_frame, bg='#1e1e1e')
        buttons_frame.pack(pady=10)

        row_count = 0
        col_count = 0
        for service, info in self.data.items():
            icon_path = os.path.join("Images", info["icon"])
            icon_image = Image.open(icon_path)
            icon_photo = ImageTk.PhotoImage(icon_image)

            button = tk.Button(buttons_frame, text=service, command=lambda s=service, c=info["code"]: self.update_selected_service(s, c), bg='#2a2a2a', fg='#00ff00', bd=1, relief=tk.RAISED, font=("Helvetica", 12), image=icon_photo, compound="top")
            button.image = icon_photo
            button.grid(row=row_count, column=col_count, pady=5, padx=10)

            col_count += 1
            if col_count == 4:
                col_count = 0
                row_count += 1

        self.code_label = tk.Label(main_frame, text="", font=("Helvetica", 14), fg='#00ff00', bg='#1e1e1e')
        self.code_label.pack(pady=20)

        quit_button = tk.Button(main_frame, text="Kilépés", command=self.root.destroy, bg='#ff4444', fg='#ffffff', bd=0, padx=10, pady=5, font=("Helvetica", 12, "bold"))
        quit_button.place(relx=0.5, rely=0.95, anchor="s")

        url_buttons_frame = tk.Frame(main_frame, bg='#1e1e1e')
        url_buttons_frame.pack(pady=10)

        for oldal in self.oldalak_data.keys():
            open_url_button = tk.Button(url_buttons_frame, text=oldal, command=lambda s=oldal: self.open_url(s), bg='#00ff00', fg='#000000', bd=1, padx=10, pady=5, font=("Helvetica", 12, "bold"))
            open_url_button.pack(side=tk.LEFT, padx=5)

        locations_frame = tk.Frame(main_frame, bg='#1e1e1e')
        locations_frame.pack(pady=10)

        for col, (location, info) in enumerate(self.locations_data.items()):
            button = tk.Button(locations_frame, text=location, command=lambda loc=info["location"]: self.copy_location(loc), bg='#2a2a2a', fg='#00ff00', bd=1, relief=tk.RAISED, font=("Helvetica", 12))
            button.grid(row=0, column=col, padx=10)

    def update_selected_service(self, service, code):
        self.code_label.config(text=code)  # Display the code
        pyperclip.copy(code)  # Copy the code to clipboard
        self.show_message("Sikeres másolás", f"{code} másolva a vágólapra")

    def show_message(self, title, message):
        self.clear_status()
        self.code_label.config(text=message)
        self.timer = self.root.after(6000, self.clear_status)  # Shorter duration

    def clear_status(self):
        self.code_label.config(text="")

    def copy_location(self, location):
        pyperclip.copy(location)
        self.show_message("Sikeres másolás", f"{location} másolva a vágólapra")

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeCenterApp(root)
    root.mainloop()
