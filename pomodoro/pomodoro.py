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
check = '✔'
reps = 0
pomodoro_timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global pomodoro_timer,reps
    window.after_cancel(pomodoro_timer)
    timer_label.config(text='Timer')
    check_label.config(text='')
    canvas.itemconfig(timer_counter,text='00:00')
    reps=0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    if reps % 8 ==0:
        count = 20 * 60
        timer_label.config(text='Long break',fg=RED)
        count_down(count)

    if reps%2==0:
        count = 5*60
        timer_label.config(text='Short break',fg=PINK)
        count_down(count)
    else:
        count = 25 * 60
        timer_label.config(text='Work',fg=GREEN)
        count_down(count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps
    count_min = count//60
    count_second = count % 60
    if count_second < 10:
        count_second = f"0{count_second}"

    canvas.itemconfig(timer_counter,text=f"{count_min}:{count_second}")
    if count > 0:
        global pomodoro_timer
        pomodoro_timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        if reps%2==0:
            check_label.config(text=check*(reps//2))

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100,pady=60,bg=YELLOW)
window.title('Pomodoro')
canvas = Canvas(width=202,height=224,bg=YELLOW,highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(102,112,image=img)
timer_counter = canvas.create_text(102,130,text='00:00',fill='white',font=(FONT_NAME,25,'bold'))
canvas.grid(column= 1,row= 1)

timer_label = Label(text='Timer',font=(FONT_NAME,30,'bold'),fg=GREEN,bg=YELLOW)
timer_label.grid(column= 1,row= 0)

start_button = Button(text='start',width=7,command=start_timer)
start_button.grid(column= 0,row= 2)

reset_button = Button(text='reset',width=7,command=reset)
reset_button.grid(column= 2,row= 2)

check_label = Label(fg=GREEN)
check_label.grid(column=1,row=3)


window.mainloop()