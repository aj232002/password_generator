# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

# print(f"Your password is: {password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail:{email}"
                                   f"\nPassword:{password}\n Is it ok to save?")
    if is_ok:
        with open("data.txt","a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0,END)
            password_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *
window = Tk()

window.title("Password Manager")
window.config(pady=50 ,padx=50)
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = logo_img)
canvas.grid(row = 0, column=1 )


website_label = Label(text="Website:",)
website_label.grid(row=1, column =0)
# button_website = Button(width=35,)

email_label = Label(text="Email/Username: ")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column =1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row= 2,column = 1,columnspan=2)
email_entry.insert(0,"arorajasmol23@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row = 3, column = 1)

#Buttons

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column =2)
add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4, column=1,columnspan=2)












window.mainloop()