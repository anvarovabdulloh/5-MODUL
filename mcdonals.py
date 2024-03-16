
from tkinter import Tk, Label, Frame, LabelFrame, Button, Spinbox
from PIL import ImageTk
from basa import Database

window = Tk()
window.geometry("1000x1000")
window.configure(bg="yellow")

frame = Frame(window)
frame.grid(padx=80, pady=70)
db = Database()

label_frame = LabelFrame(frame, bg="brown")
label_frame.grid()
# ======================================================
# YOZUV ================================================
e_label = Label(window, text="MCDONAL'S KAFESI",
                fg="yellow", bg="red",
                font=("Arial", 30))
e_label.place(x=250, y=10)

# BURGER =================================================
burger_photo = ImageTk.PhotoImage(file="burgers_2 (1).jpg")
burger_label = Label(label_frame, image=burger_photo)
burger_label.grid(row=1, column=0)

burger_label = Label(label_frame, text="burgerlar",
                     font=("Verdana", 20),
                     fg="red", bg="yellow")
burger_label.grid(row=2, column=0)

burger_label2 = Label(label_frame, text="25,000 so'm",
                      font=("Verdana", 20),
                      fg="red", bg="yellow")
burger_label2.grid(row=3, column=0)

burger_spinbox = Spinbox(label_frame, from_=1, to=100)
burger_spinbox.grid(row=4, column=0)
# LAVASH ==================================================
lavash_photo = ImageTk.PhotoImage(file="burgers_3 (1).jpg")
lavsh_label = Label(label_frame, image=lavash_photo)
lavsh_label.grid(row=1, column=1)

lavsh_label = Label(label_frame, text="bugerlar",
                    font=("Verdana", 20),
                    fg="red", bg="yellow")
lavsh_label.grid(row=2, column=1)

lavsh_label2 = Label(label_frame, text="28,000 so'm",
                     font=("Verdana", 20),
                     fg="red", bg="yellow")
lavsh_label2.grid(row=3, column=1)

lavash_spinbox = Spinbox(label_frame, from_=1, to=100)
lavash_spinbox.grid(row=4, column=1)
# Shaurma ===================================================

shaurma_photo = ImageTk.PhotoImage(file="coffee_2 (1).jpg")
shaurma_label = Label(label_frame, image=shaurma_photo)
shaurma_label.grid(row=1, column=2)

shaurma_label = Label(label_frame, text="koffee",
                      font=("Verdana", 20),
                      fg="red", bg="yellow")
shaurma_label.grid(row=2, column=2)

shaurma_label2 = Label(label_frame, text="25,000 so'm",
                       font=("Verdana", 20),
                       fg="red", bg="yellow")
shaurma_label2.grid(row=3, column=2)

shaurma_spinbox = Spinbox(label_frame, from_=1, to=100)
shaurma_spinbox.grid(row=4, column=2)
# HOT DOG ===============================================
Hot_dog_photo = ImageTk.PhotoImage(file="combo (1).jpg")
Hot_dog_label = Label(label_frame, image=Hot_dog_photo)
Hot_dog_label.grid(row=1, column=3)

Hot_dog_label = Label(label_frame, text="combo",
                      font=("Verdana", 20),
                      fg="red", bg="yellow")
Hot_dog_label.grid(row=2, column=3)

Hot_dog_label2 = Label(label_frame, text="15,000 so'm",
                       font=("Verdana", 20),
                       fg="red", bg="yellow")
Hot_dog_label2.grid(row=3, column=3)

hotdog_spinbox = Spinbox(label_frame, from_=1, to=100)
hotdog_spinbox.grid(row=4, column=3)
# FRIES====================================================
fries_photo = ImageTk.PhotoImage(file="gazli ichimliklar 1 (1).jpg")
fries_label = Label(label_frame, image=fries_photo)
fries_label.grid(row=5, column=0)

fries_label = Label(label_frame, text="ichimliklar",
                    font=("Verdana", 20),
                    fg="red", bg="yellow")
fries_label.grid(row=6, column=0)


fries_label2 = Label(label_frame, text="14,000 so'm",
                     font=("Verdana", 20),
                     fg="red", bg="yellow")
fries_label2.grid(row=7, column=0)

fries_spinbox = Spinbox(label_frame, from_=1, to=100)
fries_spinbox.grid(row=8, column=0)
# SNACKS ================================================
snacks_photo = ImageTk.PhotoImage(file="marojniy 1 (1).jpg")
snacks_label = Label(label_frame, image=snacks_photo)
snacks_label.grid(row=5, column=1)

snacks_label = Label(label_frame, text="marojniy",
                     font=("Verdana", 20),
                     fg="red", bg="yellow")
snacks_label.grid(row=6, column=1)

snacks_label2 = Label(label_frame, text="9,000 so'm",
                      font=("Verdana", 20),
                      fg="red", bg="yellow")
snacks_label2.grid(row=7, column=1)

snack_spinbox = Spinbox(label_frame, from_=1, to=100)
snack_spinbox.grid(row=8, column=1)
# HOT DOG ===============================================
combo_photo = ImageTk.PhotoImage(file="sandwich_2 (1).jpg")
combo_label = Label(label_frame, image=combo_photo)
combo_label.grid(row=5, column=2)

combo_label = Label(label_frame, text="sandvich",
                    font=("Verdana", 20),
                    fg="red", bg="yellow")
combo_label.grid(row=6, column=2)

combo_label2 = Label(label_frame, text="30,000 so'm",
                     font=("Verdana", 20),
                     fg="red", bg="yellow")
combo_label2.grid(row=7, column=2)

combo_spinbox = Spinbox(label_frame, from_=1, to=100)
combo_spinbox.grid(row=8, column=2)
# COFFEE ===========================================
coffee_photo = ImageTk.PhotoImage(file="sandwichlar_1 (1).jpg")
coffee_label = Label(label_frame, image=coffee_photo)
coffee_label.grid(row=5, column=3)

coffee_label = Label(label_frame, text="sandvich",
                     font=("Verdana", 20),
                     fg="red", bg="yellow")
coffee_label.grid(row=6, column=3)

coffee_label2 = Label(label_frame, text="12,000 so'm",
                      font=("Verdana", 20),
                      fg="red", bg="yellow")
coffee_label2.grid(row=7, column=3)

coffee_spinbox = Spinbox(label_frame, from_=1, to=100)
coffee_spinbox.grid(row=8, column=3)


# KNOPKA=================================================
def button_count():
    burger_total = int(burger_spinbox.get()) * 55_000
    lavash_total = int(lavash_spinbox.get()) * 28_000
    shaurma_total = int(shaurma_spinbox.get()) * 15_000
    hot_dog_total = int(hotdog_spinbox.get()) * 95_000
    fries_total = int(fries_spinbox.get()) * 26_000
    snack_total = int(snack_spinbox.get()) * 30_000
    combo_total = int(combo_spinbox.get()) * 10_000
    coffee_total = int(coffee_spinbox.get()) * 52_000
    total_bills = sum([burger_total, lavash_total, shaurma_total, hot_dog_total,
                       fries_total, snack_total, combo_total, coffee_total])
    bills = Label(text=f"Sizning hisobingiz {total_bills} so'm bo'ldi",
                  bg="#279340", fg="red", font=("Arial", 20, "bold"))
    bills.place(x=140, y=685)


buyur_button = Button(window, text="Buyurtma berish",
                      font=("Verdana", 25),
                      fg="yellow", bg="red", command=button_count)
buyur_button.place(x=310, y=680)

# =====================================================

for widget in label_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
from tkinter import Menu, filedialog

my_menu = Menu(window)
window.config(menu=my_menu)

file_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)


def open_file():
    filedialog.askopenfilename()


file_menu.add_command(label="javascript", command=window)
file_menu.add_separator()
file_menu.add_command(label="python", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=window.quit)
file_menu.add_separator()


sub_menu = Menu(file_menu, tearoff=0)
sub_menu.add_command(label="Plugins")
sub_menu.add_command(label="copy")
file_menu.add_cascade(label="Settings", menu=sub_menu)

sub_menu2 = Menu(file_menu, tearoff=0)
sub_menu2.add_command(label="plugin1")
sub_menu2.add_command(label="plugin2")
sub_menu.add_cascade(label="Settings", menu=sub_menu2)
# -------------------------------------------
# def button_count():
#     burger_total = int(spinbox_burger.get()) * 25_000
#     lavash_total = int(spinbox_lavash.get()) * 28_000
#     shaurma_total = int(spinbox_shaurma.get()) * 25_000
#     hot_dog_total = int(spinbox_hotdog.get()) * 15_000
#     fries_total = int(spinbox_fries.get()) * 14_000
#     snack_total = int(spinbox_snack.get()) * 9_000
#     combo_total = int(spinbox_combo.get()) * 30_000
#     coffee_total = int(spinbox_coffee.get()) * 12_000
#     total_bills = sum([burger_total, lavash_total, shaurma_total, hot_dog_total,
#                        fries_total, snack_total, combo_total, coffee_total])
#
#     database_evos = db.insert_food(fast_food_name="Burger", price=25_000, how_much=spinbox_burger.get(), total=burger_total)
#     database_evos1 = db.insert_food(fast_food_name="Lavash", price=28_000, how_much=spinbox_lavash.get(), total=lavash_total)
#     database_evos2 = db.insert_food(fast_food_name="Shaurma", price=25_000, how_much=spinbox_shaurma.get(), total=shaurma_total)
#     database_evos3 = db.insert_food(fast_food_name="Hot dog", price=15_000, how_much=spinbox_hotdog.get(), total=hot_dog_total)
#     database_evos4 = db.insert_food(fast_food_name="Fries", price=14_000, how_much=spinbox_fries.get(), total=fries_total)
#     database_evos5 = db.insert_food(fast_food_name="Snack", price=9_000, how_much=spinbox_snack.get(), total=snack_total)
#     database_evos6 = db.insert_food(fast_food_name="Combo", price=30_000, how_much=spinbox_combo.get(), total=combo_total)
#     database_evos7 = db.insert_food(fast_food_name="Coffee", price=12_000, how_much=spinbox_coffee.get(), total=coffee_total)
#     if database_evos:
#         messagebox.showinfo(title="Success",
#                             message="Successfully order")
#     if total_bills != 0:
#         bills = Label(label_frame, text=f"Sizning hisobingiz {total_bills} so'm bo'ldi",
#                       bg="#279340", fg="white", font=("Arial", 20, "bold"))
#         bills.grid(row=9, column=0, columnspan=4, pady=10, padx=10)

#     --------------------------------------------
window.mainloop()
window.mainloop()