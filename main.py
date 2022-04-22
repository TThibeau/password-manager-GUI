from tkinter import *
from tkinter import messagebox
import os
from random import choice, randint,shuffle
import pyperclip

os.system('cls || clear')

FONT_NAME = "Courier"
FONT = (FONT_NAME,12,"bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= randint(8,10)
    nr_symbols = randint(2,4)
    nr_numbers = randint(2,4)

    pw_list = []
    [pw_list.append(choice(letters)) for i in range(nr_letters)]
    [pw_list.append(choice(numbers)) for i in range(nr_numbers)]
    [pw_list.append(choice(symbols)) for i in range(nr_symbols)]
    shuffle(pw_list)
    pw_hard = ''.join(pw_list)

    pyperclip.copy(pw_hard)
    password_entry.insert(END, string=pw_hard)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
 
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Entry missing",message="An entry is missing. Please fill in all entries.")
        
    else:
        okay = messagebox.askokcancel(title=website,message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nClick OK to save.")

        if okay:
            with open("data.txt",mode="a") as data:
                data.write(f"{website} | {email} | {password}\n")
            
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            email_entry.insert(END, string="example.name@email.com")
            password_entry.delete(0,END)  

            messagebox.showinfo(title="Password saved",message="Password has been saved.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password manager")
window.config(padx=50,pady=50)

logo_img = PhotoImage(file="logo.png")
logo_canvas = Canvas(width=200,height=200)
logo_canvas.create_image(100,100,image=logo_img)
logo_canvas.grid(row=0,column=1,sticky="w")
 
# Labels (Left column)
website_label = Label(text="Website:",font=FONT)
website_label.grid(row=1,column=0,sticky="e")

email_label = Label(text="Email/Username:",font=FONT)
email_label.grid(row=2,column=0,sticky="e")

password_label = Label(text="Password:",font=FONT)
password_label.grid(row=3,column=0,sticky="e")

# Entries (Mid column)
website_entry = Entry(width=52)
website_entry.grid(row=1,column=1,columnspan=2,sticky="w")
website_entry.focus()

email_entry = Entry(width=52)
email_entry.insert(END, string="example.name@email.com")
email_entry.grid(row=2,column=1,columnspan=2,sticky="w")

password_entry = Entry(width=31)
password_entry.grid(row=3,column=1,sticky="w")

# Buttons

save_button = Button(text="Save",width=44,command=save_password)
save_button.grid(row=4,column=1,columnspan=2,pady=5)

generate_button = Button(text="Generate Password",command=generate_password)
generate_button.grid(row=3,column=2,sticky="e")

window.mainloop()