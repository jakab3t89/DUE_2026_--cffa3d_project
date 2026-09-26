import os
from datetime import datetime
from class_JT import Trip_JT

FILE_NAME = "utak.txt"


def JT_today():
    return datetime.now().strftime("%Y-%m-%d")


def JT_check_date(text):
    try:
        datetime.strptime(text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def JT_load_trips():
    trips = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(";")
                if len(parts) == 3:
                    trips.append(Trip_JT(parts[0], parts[1], parts[2]))
    if not trips:
        trips = [
            Trip_JT("Budapest-Keleti", "Szombathely", "2026-09-05"),
            Trip_JT("Szombathely", "Budapest-Keleti", "2026-09-07"),
            Trip_JT("Budapest-Keleti", "Dunaújváros", "2026-09-12")
        ]
        JT_save_trips(trips)
    return trips


def JT_save_trips(trips):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for trip in trips:
            f.write(f"{trip.start};{trip.end};{trip.date}\n")


def JT_add_trip(trip, trips):
    trips.append(trip)
    JT_save_trips(trips)
    return trips


def JT_remove_trip(trip, trips):
    if trip in trips:
        trips.remove(trip)
        JT_save_trips(trips)
    return trips
