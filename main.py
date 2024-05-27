from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)



canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

canvas.create_text(100,20,text="Timer",fill=GREEN,font=(FONT_NAME,35,"bold"))
canvas.grid(row=0,column=1)

def action():
    print("Do something")

#calls action() when pressed
button_Start = Button(text="Start", command=action)
button_Start.grid(row=2,column=0)
button_Reset=Button(text="reset",command=action)
button_Reset.grid(row=2,column=2)

check_marks=Label(text="✔",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)

window.mainloop()
