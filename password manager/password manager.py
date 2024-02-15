from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
FONT = ('arial',8,'bold')
# ---------------------------- Search File ------------------------------- #
def search_file():
    website = website_entry.get().title()
    try:
        with open('data file.json') as file:
            data = json.load(file)
        if website in data.keys():
            messagebox.showinfo(website.title(),f'Email: {data[website]["Email"]}\nPassword: {data[website]["Password"]}')
        else:
            messagebox.showinfo('Sorry','No details for the website :(')
    except FileNotFoundError:
        messagebox.showinfo('Sorry', 'No data file found')
    except JSONDecodeError:
        messagebox.showinfo('Sorry', 'Your file is empty')

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generated_password():
    password_entry.delete(0,END)
    password_list = [random.choice(letters) for letter in range(random.randint(8, 10))]
    password_list += [random.choice(symbols) for symb in range(random.randint(2, 4))]
    password_list += [random.choice(numbers) for num in range(random.randint(2, 4))]
    random.shuffle(password_list)
    new_password = ''.join(password_list)
    password_entry.insert(0,new_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    WEB = website_entry.get()
    EMAIL = email_entry.get()
    PASS = password_entry.get()

    if not WEB or not EMAIL or not PASS:
        messagebox.showinfo('notice','Please fill all fields')
    else:
        is_ok = messagebox.askokcancel(WEB,f'Do you want to save these details\nEmail: {EMAIL}\nPassword: {PASS}')

        if is_ok:
            new_data = {WEB.title(): {
                'Email': EMAIL,
                'Password': PASS
            }
                        }
            try:
                with open('data file.json','r') as file:
                    data = json.load(file)

            except (FileNotFoundError , JSONDecodeError):
                with open('data file.json', 'w') as file:
                    json.dump(new_data,file,indent=4)
            else:
                data.update(new_data)
                with open('data file.json', 'w') as file:
                    json.dump(data, file,indent=4)
            finally:
                answer = messagebox.askokcancel('all done','Do you want to save password to clipboard')
                if answer:
                    pyperclip.copy(PASS)
                website_entry.delete(0,END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50,pady=50)

canvas = Canvas(height=200,width=200)
image = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=image)
canvas.grid(column=1,row=0)
#website
website_label = Label(text='Website',font=FONT)
website_label.grid(column=0,row=1)
website_entry = Entry(width=32)
website_entry.focus()
website_entry.grid(column=1,row=1,columnspan=2,sticky='w',padx=20)
website_search = Button(text='Search',width=15,font=FONT,command=search_file)
website_search.grid(column=2,row=1)
#email
email_label = Label(text='Email/Username',font=FONT)
email_label.grid(column=0,row=2,columnspan=1)
email_entry = Entry(width=34)
email_entry.grid(column=1,row=2,columnspan=2,sticky='w',padx=20,pady=5)
#password
password_label = Label(text='Password',font=FONT)
password_label.grid(column=0,row=3,columnspan=1)
password_entry = Entry(width=32)
password_entry.grid(column=1,row=3,columnspan=1,sticky='w',padx=20)

generate_password = Button(text='Generate Password',width=16,font=FONT,height=1,command=generated_password)
generate_password.grid(column=2,row=3,columnspan=1,sticky='w',pady=2)

add_button = Button(text='Add',width=36,font=FONT,command=save_data)
add_button.grid(column=1,row=4,columnspan=2,pady=5)


window.mainloop()