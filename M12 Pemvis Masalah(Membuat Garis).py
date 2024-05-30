import tkinter as tk
from tkinter import ttk

class Garis:
    def __init__(self, root):
        self.root = root
        self.root.title("Menggambar Garis Bersama Dapa")

        # Frame untuk kontrol
        control_frame = ttk.Frame(self.root)
        control_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

        # Frame untuk kanvas
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

        # Kontrol untuk input variabel
        self.create_controls(control_frame)

    def create_controls(self, frame):
        # Koor titik awal
        ttk.Label(frame, text="Koordinat Titik Awal (x1, y1):").pack(pady=5)
        self.x1_entry = ttk.Entry(frame)
        self.x1_entry.pack(pady=5)
        self.y1_entry = ttk.Entry(frame)
        self.y1_entry.pack(pady=5)

        # Koor titik akhir
        ttk.Label(frame, text="Koordinat Titik Akhir (x2, y2):").pack(pady=5)
        self.x2_entry = ttk.Entry(frame)
        self.x2_entry.pack(pady=5)
        self.y2_entry = ttk.Entry(frame)
        self.y2_entry.pack(pady=5)

        # Ketebalan Garis
        ttk.Label(frame, text="Tebal Garis:").pack(pady=5)
        self.line_thickness_entry = ttk.Entry(frame)
        self.line_thickness_entry.pack(pady=5)

        # Kontrol untuk warna garis
        ttk.Label(frame, text="Warna Garis:").pack(pady=5)
        self.color_var = tk.StringVar(value="black") #Warna dasar
        color_options = ["merah", "hijau", "biru", "kuning", "magenta", "putih"] #Pemilihan warna
        self.color_menu = ttk.Combobox(frame, textvariable=self.color_var, values=color_options)
        self.color_menu.pack(pady=5)

        # Button untuk menggambar garis
        self.draw_button = ttk.Button(frame, text="Gambar Garis", command=self.draw_line)
        self.draw_button.pack(pady=5)

    def draw_line(self):
        # Mengambil nilai input
        x1 = int(self.x1_entry.get())
        y1 = int(self.y1_entry.get())
        x2 = int(self.x2_entry.get())
        y2 = int(self.y2_entry.get())
        thickness = int(self.line_thickness_entry.get())
        color = self.get_color_code(self.color_var.get())

        # Menggambar garis di kanvas
        self.canvas.create_line(x1, y1, x2, y2, width=thickness, fill=color)

    def get_color_code(self, color_name):
        # Kode Warna
        color_codes = {
            "merah": "red",
            "hijau": "green",
            "biru": "blue",
            "kuning": "yellow",
            "magenta": "magenta",
            "putih": "white"
        }
        return color_codes.get(color_name, "black")

if __name__ == "__main__":
    root = tk.Tk()
    app = Garis(root)
    root.mainloop()


