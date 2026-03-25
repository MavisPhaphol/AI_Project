import datetime
from tkinter import *

from music_selector import music_selector

#use reference from youtube video: https://www.youtube.com/watch?v=lyoyTlltFVU
window = Tk()
window.geometry("1280x720") #the window size
window.title("AI Agent GUI") #the title for the window screen
window.config(background="#343940") #background of window

#use reference from GeeksForGeeks: https://www.geeksforgeeks.org/python/python-tkinter-listbox-widget/
listbox = Listbox(window, height = 10, width = 100, background="#495059",fg="white") #displays the assignments w/ due dates and priority in this list box
boxTitle = Label(window, text="Music Selector") #title with listed box listing genres of music to listen to
boxTitle.pack() #this will display the title for the list box
listbox.pack() #this will display the list box on the window

