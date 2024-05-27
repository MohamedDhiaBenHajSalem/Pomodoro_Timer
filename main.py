from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN =25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps=0
initial_timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(initial_timer)
    canvas.itemconfig(Titel_mode, text="Timer", fill=GREEN)
    canvas.itemconfig(timer_text,text="00:00")
    check_marks.config(text="")
    global reps
    reps=0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_Break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    mark = "✔"
    if reps % 8==0:

        counttdown(long_break_sec)
        canvas.itemconfig(Titel_mode, text="Break", fill=GREEN)


    elif  reps % 2==0 :
        canvas.itemconfig(Titel_mode, text="Break",fill=PINK)
        counttdown(short_Break_sec)

    else :
        counttdown(work_sec)
        canvas.itemconfig(Titel_mode, text="Working", fill=RED)

    for _ in range (math.floor(reps/2)):
        mark+="✔"

    check_marks.config(text=mark)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counttdown(count):

    minute=math.floor(count/60)
    second=count % 60
    if second <10:
        second=f"0{second}"
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count >0:
        global initial_timer
        initial_timer= window.after(1000,counttdown,count-1)
    else : start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)




canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

Titel_mode=canvas.create_text(100,20,text="Timer",fill=GREEN,font=(FONT_NAME,35,"bold"))
canvas.grid(row=0,column=1)



#calls action() when pressed
button_Start = Button(text="Start", command=start_timer)
button_Start.grid(row=2,column=0)
button_Reset=Button(text="reset",command=reset_timer)
button_Reset.grid(row=2,column=2)

check_marks=Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)

window.mainloop()
