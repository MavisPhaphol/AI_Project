import datetime
from tkinter import *

from music_selector import music_selector

#window setup
window = Tk()
window.geometry("1280x720")
window.title("AI Agent GUI")
window.config(background="#343940")

#calls the music selector to choose for user
selector = music_selector()

MOODS = ["Happy", "Sad", "Energetic", "Calm", "Focused"]
ACTIVITIES = ["Study", "Workout", "Relax", "Commute", "Sleep"]
TIMES_OF_DAY = ["Morning", "Afternoon", "Evening", "Night"]


#setting up time in military format
def default_time_of_day():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Morning"
    if 12 <= hour < 17:
        return "Afternoon"
    if 17 <= hour < 21:
        return "Evening"
    return "Night"

#setting up the page for user interaction
def build_section():
    heading = Label(window, text="Music Selector", font=("Arial", 20, "bold"), bg="#343940", fg="white")
    heading.pack(pady=(20, 10))

    frame = Frame(window, bg="#343940")
    frame.pack(pady=10)

    # Mood
    mood_label = Label(frame, text="Mood:", bg="#343940", fg="white", font=("Arial", 12))
    mood_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)
    mood_var = StringVar(value=MOODS[0])
    mood_menu = OptionMenu(frame, mood_var, *MOODS)
    mood_menu.config(width=16)
    mood_menu.grid(row=0, column=1, padx=10, pady=5)

    # Activity
    activity_label = Label(frame, text="Activity:", bg="#343940", fg="white", font=("Arial", 12))
    activity_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    activity_var = StringVar(value=ACTIVITIES[0])
    activity_menu = OptionMenu(frame, activity_var, *ACTIVITIES)
    activity_menu.config(width=16)
    activity_menu.grid(row=1, column=1, padx=10, pady=5)

    # Time of day
    time_label = Label(frame, text="Time of Day (24-HR format):", bg="#343940", fg="white", font=("Arial", 12))
    time_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    time_var = StringVar(value=default_time_of_day())
    time_menu = OptionMenu(frame, time_var, *TIMES_OF_DAY)
    time_menu.config(width=16)
    time_menu.grid(row=2, column=1, padx=10, pady=5)

    return mood_var, activity_var, time_var


def populate_results(music_items):
    listbox.delete(0, END)
    if not music_items:
        listbox.insert(END, "No recommendations found. Try different inputs.")
        return
    for idx, music in enumerate(music_items, start=1):
        listbox.insert(END, f"{idx}. {music}")

#main screen for GUI
mood_var, activity_var, time_var = build_section()

button = Button(window, text="Get Playlist", font=("Arial", 12, "bold"), bg="#5c7a97", fg="white", padx=10, pady=5)
button.pack(pady=(0, 10))

status_label = Label(window, text="Select mood, activity, and time of day, then click Get Playlist", bg="#343940", fg="white", font=("Arial", 11))
status_label.pack(pady=(0, 10))

listbox = Listbox(window, height=10, width=100, background="#495059", fg="white", font=("Arial", 11))
listbox.pack(pady=(0, 20))

#gets playlist from selector and put on screen as results
def on_get_playlist():
    mood = mood_var.get().strip()
    activity = activity_var.get().strip()
    time_of_day = time_var.get().strip()

    if not mood or not activity or not time_of_day:
        status_label.config(text="Please select mood, activity, and time of day.", fg="red")
        return

    recommendations = selector.select_music(mood, activity, time_of_day)
    populate_results(recommendations)
    status_label.config(text=f"Showing {len(recommendations)} recommendations for {mood}/{activity}/{time_of_day}.", fg="lightgreen")


button.config(command=on_get_playlist)

#gets default playlist based on input
populate_results(selector.select_music(mood_var.get(), activity_var.get(), time_var.get()))
status_label.config(text="Ready. Click Get Playlist to refresh.", fg="white")

window.mainloop()

