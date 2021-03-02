from tkinter import *
from tkinter import messagebox
import random
import pyperclip

BG_COLOR = "#fce8e9"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(LETTERS) for x in range(nr_letters)] + [random.choice(NUMBERS) for x in range(nr_numbers)] + [random.choice(SYMBOLS) for x in range(nr_symbols)]
    random.shuffle(password_list)
    password = "".join(password_list)

    entry_3.delete(0, END)
    entry_3.insert(END, password)

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_data():
    website = entry_1.get()
    user = entry_2.get()
    password = entry_3.get()
    if website == "" or user == "" or password == "":
        error_label.config(text="Wrong/empty field", font=("Arial", 12, "bold"), fg="#b82828")
    else:
        try:
            with open("data.txt", "a") as file:
                if messagebox.askokcancel(title="Confirm data", message=f"Are those details correct?\nWebsite: {website}\nEmail/Username: {user}\nPassword: {password}"):
                    file.write(f"{website} | {user} | {password}\n")
                    file.close()
                    entry_1.delete(0, END)
                    entry_3.delete(0, END)
                    messagebox.showinfo("Success!", "Password saved.")
        except:
            error_label.config(text="Somethind goes wrong", font=("Arial", 12, "bold"), fg="#b82828")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=80, pady=80, bg = BG_COLOR)
window.title("Password Manager")

canvas = Canvas(width=300, height=200, bg=BG_COLOR, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(150, 100, image=logo)
canvas.grid(row=0, columnspan=3)



label_1 = Label(text = "Website:", bg=BG_COLOR, font=("Arial", 12))
entry_1 = Entry(width=40, font=("Arial", 12))
entry_1.focus()
label_1.grid(row=1, column=0)
entry_1.grid(row=1, column=1, columnspan=2)

label_2 = Label(text = "Email/Username:", bg=BG_COLOR, pady=6, font=("Arial", 12))
entry_2 = Entry(width=40, font=("Arial", 12))
entry_2.insert(END, "jakub@bartnyk.pl")
label_2.grid(row=2, column=0)
entry_2.grid(row=2,column=1, columnspan=2)

label_3 = Label(text = "Password:", bg=BG_COLOR, font=("Arial", 12))
entry_3 = Entry(font=("Arial", 12), width=22)
label_3.grid(row=3, column=0)
entry_3.grid(row=3, column=1, pady=(0,6))

generate_button = Button(text="Generate Password", font=("Arial", 12), command=generate_password)
generate_button.grid(row=3, column=2, pady=(0,6), sticky="E")

confirm_button = Button(text="Add", font=("Arial", 12), width=40, command=get_data)
confirm_button.grid(row=4, column=1, columnspan=2)

error_label = Label(text="", bg=BG_COLOR, pady=6)
error_label.grid(row=5, column=1, columnspan=2)

window.mainloop()
