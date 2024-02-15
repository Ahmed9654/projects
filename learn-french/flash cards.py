from tkinter import *
import pandas as pd
import random

from pandas.errors import EmptyDataError

#---------------------Reading Files-------------------#
equivalent_arabic = {}
current_card = []
try:
    data = pd.read_csv('F:\\100 days python\\100 projects\\day 31\\data\\words to learn.csv')

    all_french_words = data['0'].tolist()
    print(all_french_words)
    data2 = pd.read_csv('F:\\100 days python\\100 projects\\day 31\\data\\french_words.csv')
    for index,row in data2.iterrows():
        equivalent_arabic[row.French] = row.Arabic
except (FileNotFoundError,EmptyDataError):
    data = pd.read_csv('F:\\100 days python\\100 projects\\day 31\\data\\french_words.csv')
    all_french_words = data['French'].tolist()
    for index,row in data.iterrows():
        equivalent_arabic[row.French] = row.Arabic
#---------------------Functions-------------------#
def random_word():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card.append(random.choice(all_french_words))
    canvas.itemconfig(changing_word, text=current_card[-1],fill='black')
    canvas.itemconfig(changing_language, text='French',fill='black')
    canvas.itemconfig(card_back_image,image=card_front)
    flip_timer = window.after(3000, filp_card)

def known_card():
    all_french_words.remove(current_card[-1])
    random_word()
    words_to_learn = pd.DataFrame(all_french_words)
    words_to_learn.to_csv('data/words to learn.csv',index=False)

def filp_card():
    global current_card
    canvas.itemconfig(changing_word, text=equivalent_arabic[current_card[-1]],fill='white')
    canvas.itemconfig(changing_language, text='Arabic',fill='white')
    canvas.itemconfig(card_back_image, image=card_back)
#---------------------UI-------------------#

BACKGROUND_COLOR = '#B1DDC6'
window = Tk()
window.title('flashy')
window.config(bg=BACKGROUND_COLOR,pady=50,padx=50)

card_front = PhotoImage(file='F:\\100 days python\\100 projects\\day 31\\images\\card_front.png')
card_back = PhotoImage(file='F:\\100 days python\\100 projects\\day 31\\images\\card_back.png')
right_mark = PhotoImage(file='F:\\100 days python\\100 projects\\day 31\\images\\right.png')
wrong_mark = PhotoImage(file='F:\\100 days python\\100 projects\\day 31\\images\\wrong.png')



canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_back_image = canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0,row=0,columnspan=2)
changing_language = canvas.create_text(400,150,text='French',font=('arial',40,'bold'))
changing_word = canvas.create_text(400, 263, text='Word', font=('arial', 60, 'bold'))


correct_button = Button(image=right_mark,highlightthickness=0,bg=BACKGROUND_COLOR,command=known_card)
correct_button.grid(row=1,column=0)

wrong_button = Button(image=wrong_mark,highlightthickness=0,bg=BACKGROUND_COLOR,command=random_word)
wrong_button.grid(row=1,column=1)
flip_timer = window.after(3000,filp_card)
random_word()
window.mainloop()