from tkinter import *
import math
import os
import sys

# if getattr(sys, 'frozen', False):
#     # If running in a PyInstaller bundle
#     base_path = sys._MEIPASS
# else:
#     # If running normally
#     base_path = os.path.abspath(".")

# PHOTO_FILE = os.path.join(base_path, "tomato.png")
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.01
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
PHOTO_FILE ="D:/Python/100 days Python Challenge/Intermediate/day_28/tomato.png"
#D:/Python/100 days Python Challenge/Intermediate/day 28/tomato.png

reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)

    print("Rest button")
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    completion_tick.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    
    global reps 
    reps +=1
    work_sec= WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", font=(FONT_NAME,  38, "bold"), fg=GREEN, bg=YELLOW)
    elif reps % 2 ==0:
        count_down(short_break_sec)
        title_label.config(text= "Break", font=(FONT_NAME,  38, "bold"), fg=PINK, bg=YELLOW)
    else: 
        count_down(work_sec)
        title_label.config(text= "Work", font=(FONT_NAME,  38, "bold"), fg=RED, bg=YELLOW)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minute = math.floor(count /60)
    count_second = count % 60
    if count_second==0:
        count_second ="00"
    elif count_second<10 :
        count_second = f"0{count_second}"
    elif count_minute < 10:
        count_minute = "0"+ str(count_minute)
    canvas.itemconfig(timer_text, text = f"{count_minute}:{count_second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks= ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
           marks+="✔"
        completion_tick.config(text= marks)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pamadora Timer")
window.config(padx=100, pady=50, bg=YELLOW)
#window.minsize(width=400, height=400)

title_label = Label(text="Timer", font=(FONT_NAME, 38, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness =0) # creating Canvas() object so that we can put things on top of another in a window
photo = PhotoImage(file = PHOTO_FILE) # Photo image Object so that later we can use the "photo"
canvas.create_image(100, 112, image = photo) # Canvas create_image() method taking coordinates, an image to display 
#canvas.create_text(103, 130, text="00:00", fill= "white", font=(FONT_NAME, 35, "bold")) #Canvas crea_text() method used to diplay a text with *args, **kw to modify the text
timer_text = canvas.create_text(103, 130, text="00:00", fill= "white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# ---------------------------- Buttons SETUP ------------------------------- #
start_button = Button(text="Start", width=10, command= start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", width=10, command=reset_timer)
reset_button.grid(column=2, row=2) 


# ---------------------------- Check Mark SETUP ------------------------------- #
completion_tick = Label(font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
completion_tick.grid(column=1, row=3)




window.mainloop()


