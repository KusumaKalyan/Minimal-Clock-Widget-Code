from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import datetime

main_window = Tk()
main_window.overrideredirect(True)# to hide window bar
main_window.geometry("230x230+%d+3" %(main_window.winfo_screenwidth()-232))# sets window geometry
main_window.wm_attributes("-transparentcolor", "#555")

main_window.canvas = Canvas(main_window,
                width=230,
                height=230,
                borderwidth=0,
                bg='#555',
                highlightthickness=0)

raw_time = str(datetime.datetime.now()).split(' ')[1].split(":")
hour = int(raw_time[0])
min = int(raw_time[1])

rotation_hour = -(hour/12.0) * 360
rotation_min = -(min/60.0) * 360

dot_centers = [
               [0, 96, 21],
               [1, 134, 32],
               [2, 161, 59],
               [3, 171, 96],
               [4, 161, 134],
               [5, 134, 161],
               [6, 96, 171],
               [7, 59, 162],
               [8, 31, 134],
               [9, 21, 96],
               [10, 31, 59],
               [11, 58, 31],
               [12, 96, 21],
               [13, 134, 32],
               [14, 161, 59],
               [15, 171, 96],
               [16, 161, 134],
               [17, 134, 161],
               [18, 96, 171],
               [19, 59, 162],
               [20, 31, 134],
               [21, 21, 96],
               [22, 31, 59],
               [23, 58, 31],
              ]

background = Image.open('assets/background.png')
background = background.resize((230, 230))
main_window.background = ImageTk.PhotoImage(background)

sun = Image.open('assets/sun.png')
sun = sun.resize((50, 50), Image.ANTIALIAS)
main_window.sun = ImageTk.PhotoImage(sun)

moon = Image.open('assets/moon.png')
moon = moon.resize((50, 50), Image.ANTIALIAS)
main_window.moon = ImageTk.PhotoImage(moon)

background_top = Image.open('assets/background_top.png')
background_top = background_top.resize((190, 190), Image.ANTIALIAS)
main_window.background_top = ImageTk.PhotoImage(background_top)

hour_circle = Image.open('assets/hour_circle.png')
hour_circle = hour_circle.resize((190, 190), Image.ANTIALIAS)
main_window.hour_circle = ImageTk.PhotoImage(hour_circle.rotate(rotation_hour))

dot = Image.open('assets/dot.png')
dot = dot.resize((40, 40), Image.ANTIALIAS)
main_window.dot = ImageTk.PhotoImage(dot.rotate(rotation_min))

main_window.canvas.create_image(0, 0, image=main_window.background, anchor=NW)
main_window.canvas.create_image(21, 21, image=main_window.background_top, anchor=NW)
main_window.canvas.create_image(21, 21, image=main_window.hour_circle, anchor=NW)
main_window.canvas.create_image(dot_centers[hour][1], dot_centers[hour][2], image=main_window.dot, anchor=NW)
if hour < 6 or hour >= 18:
    main_window.canvas.create_image(92, 92, image=main_window.moon, anchor=NW)
else:
    main_window.canvas.create_image(92, 92, image=main_window.sun, anchor=NW)

main_window.canvas.pack()
main_window.mainloop()
