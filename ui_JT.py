import tkinter as tk
from tkinter import messagebox
from class_JT import Trip_JT
from trip_JT import JT_load_trips, JT_add_trip, JT_remove_trip, JT_today, JT_check_date


class App_JT:
    def __init__(self, root):
        self.root = root
        self.root.title("Vonatút-napló JT")
        self.root.geometry("380x500")

        self.trips = JT_load_trips()

        tk.Label(root, text="Honnan:").pack(anchor="w", padx=10, pady=(10, 0))
        self.entry_start = tk.Entry(root)
        self.entry_start.pack(fill="x", padx=10, pady=5)

        tk.Label(root, text="Hova:").pack(anchor="w", padx=10)
        self.entry_end = tk.Entry(root)
        self.entry_end.pack(fill="x", padx=10, pady=5)

        tk.Label(root, text="Dátum (pl. 2026-09-25):").pack(anchor="w", padx=10)
        self.entry_date = tk.Entry(root)
        self.entry_date.pack(fill="x", padx=10, pady=5)
        self.entry_date.insert(0, JT_today())

        tk.Button(root, text="Hozzáadás", command=self.add_trip).pack(pady=(10, 5))
        tk.Button(root, text="Törlés", command=self.remove_trip).pack(pady=5)

        self.listbox = tk.Listbox(root)
        self.listbox.pack(fill="both", expand=True, padx=10, pady=10)

        self.label_count = tk.Label(root, text="")
        self.label_count.pack(pady=(0, 10))

        self.root.bind("<Return>", self.on_enter)

        self.refresh_list()

    def on_enter(self, event):
        self.add_trip()

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for trip in self.trips:
            self.listbox.insert(tk.END, trip.get_info())
        self.label_count.config(text=f"Utak száma: {len(self.trips)}")

    def add_trip(self):
        start = self.entry_start.get().strip()
        end = self.entry_end.get().strip()
        date = self.entry_date.get().strip()

        if not start or not end:
            messagebox.showwarning("Figyelem", "Add meg, honnan és hova utaztál!")
            return
        if not JT_check_date(date):
            messagebox.showwarning("Figyelem", "Rossz dátum! Helyes forma: 2026-09-25")
            return

        new_trip = Trip_JT(start, end, date)
        self.trips = JT_add_trip(new_trip, self.trips)
        self.refresh_list()
        self.entry_start.delete(0, tk.END)
        self.entry_end.delete(0, tk.END)
        self.entry_start.focus_set()

    def remove_trip(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showwarning("Figyelem", "Előbb jelölj ki egy utat a listában!")
            return
        trip = self.trips[selected[0]]
        self.trips = JT_remove_trip(trip, self.trips)
        self.refresh_list()
