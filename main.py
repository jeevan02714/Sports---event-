import csv
import os

FILE = "events.csv"

def init_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Sport", "Team/Player", "Venue", "Date", "Time"])

def add_event():
    sport = input("Enter Sport: ")
    player = input("Enter Team/Player: ")
    venue = input("Enter Venue: ")
    date = input("Enter Date (DD-MM-YYYY): ")
    time = input("Enter Time: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([sport, player, venue, date, time])

    print("✅ Event added successfully")

def view_events():
    print("\n--- All Events ---")
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def search_event():
    keyword = input("Search by sport or player: ").lower()

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if keyword in row[0].lower() or keyword in row[1].lower():
                print(row)

def filter_by_sport():
    sport_name = input("Enter sport name: ").lower()

    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if sport_name == row[0].lower():
                print(row)

def menu():
    init_file()

    while True:
        print("\n--- Sports Event Dashboard ---")
        print("1. Add Event")
        print("2. View Events")
        print("3. Search Event")
        print("4. Filter by Sport")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_event()
        elif choice == "2":
            view_events()
        elif choice == "3":
            search_event()
        elif choice == "4":
            filter_by_sport()
        elif choice == "5":
            break
        else:
            print("Invalid choice")

menu()
