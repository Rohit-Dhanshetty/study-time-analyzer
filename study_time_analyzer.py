import time
import datetime
import os

LOG_FILE = "study_log.txt"


def start_session():
    print("📚 Study session started...")
    return time.time()


def end_session(start_time):
    end_time = time.time()
    duration = end_time - start_time
    minutes = int(duration // 60)
    hours = minutes // 60
    minutes = minutes % 60

    today = datetime.date.today().isoformat()
    entry = f"{today} - {hours} hours {minutes} minutes\n"

    with open(LOG_FILE, "a") as file:
        file.write(entry)

    print("📝 Session saved:", entry)


def view_history():
    if not os.path.exists(LOG_FILE):
        print("No history found.")
        return

    print("\n📖 Study History:")
    with open(LOG_FILE, "r") as file:
        print(file.read())


def weekly_summary():
    if not os.path.exists(LOG_FILE):
        print("No history available.")
        return

    total_minutes = 0
    today = datetime.date.today()
    week_ago = today - datetime.timedelta(days=7)

    with open(LOG_FILE, "r") as file:
        for line in file:
            date_str, data = line.split(" - ")
            date = datetime.date.fromisoformat(date_str)
            if date >= week_ago:
                parts = data.split()
                hrs = int(parts[0])
                mins = int(parts[2])
                total_minutes += hrs * 60 + mins

    hours = total_minutes // 60
    minutes = total_minutes % 60

    print(f"\n📊 Weekly Study Summary: {hours} hours {minutes} minutes\n")


def main():
    start_time = None

    while True:
        print("\n======= Study Time Analyzer =======")
        print("1. Start Study Session")
        print("2. End Study Session")
        print("3. View History")
        print("4. Weekly Summary")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            start_time = start_session()

        elif choice == "2":
            if start_time is None:
                print("Start a session first!")
            else:
                end_session(start_time)
                start_time = None

        elif choice == "3":
            view_history()

        elif choice == "4":
            weekly_summary()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


main()
