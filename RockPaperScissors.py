from tkinter import *
import random
import tkinter

win = 0
lose = 0

def rps(win, lose, user):
    choices = ["Rock", "Paper", "Scissors"]
    computer = random.randrange(1, 4)
    if user == computer:
        var.set(f"It's a draw! \nBoth chose {choices[user - 1]}")  
    elif (user == 1 and computer == 3) or (user == 2 and computer == 1) or (user == 3 and computer == 2):
        var.set(f"You chose {choices[user - 1]}, I chose {choices[computer - 1]}. \nYou win! 🎉")
        wins.set(wins.get() + 1)
    else:
        var.set(f"You chose {choices[user - 1]}, I chose {choices[computer - 1]}. \nYou lose! 😢")
        wins.set(wins.get() - 1)

# GUI Setup
top = tkinter.Tk()
top.wm_title("Rock Paper Scissors - Fun Edition!")
top.state("zoomed")  # Maximize window
top.configure(bg="black")  # Set background to black

# Adding a background fill
top_canvas = Canvas(top, width=top.winfo_screenwidth(), height=top.winfo_screenheight(), bg="black")
top_canvas.pack(fill="both", expand=True)

# Creating a background pattern
top_canvas.create_text(top.winfo_screenwidth()//2, 50, text="Rock, Paper, Scissors!", font=("Arial", 30, "bold"), fill="white")
for i in range(0, top.winfo_screenwidth(), 200):
    for j in range(100, top.winfo_screenheight(), 150):
        top_canvas.create_text(i, j, text=random.choice(["✊", "✋", "✌️"]), font=("Arial", 40, "bold"), fill="gray")

# Buttons Frame
frame = Frame(top, bg="black")
frame.place(relx=0.5, rely=0.4, anchor=CENTER)

B1 = tkinter.Button(frame, text="Rock ✊", bg="pink", font=("Arial", 16, "bold"), command=lambda: rps(win, lose, 1))
B1.grid(row=0, column=0, padx=20, pady=10)
B2 = tkinter.Button(frame, text="Paper ✋", bg="pink", font=("Arial", 16, "bold"), command=lambda: rps(win, lose, 2))
B2.grid(row=0, column=1, padx=20, pady=10)
B3 = tkinter.Button(frame, text="Scissors ✌️", bg="pink", font=("Arial", 16, "bold"), command=lambda: rps(win, lose, 3))
B3.grid(row=0, column=2, padx=20, pady=10)

# Result Display
var = StringVar()
var.set('Welcome! Ready to play? 🎮')
result_label = Label(top, textvariable=var, font=("Arial", 18, "bold"), bg="black", fg="white")
result_label.place(relx=0.5, rely=0.55, anchor=CENTER)

# Score Display
score_frame = Frame(top, bg="black")
score_frame.place(relx=0.5, rely=0.65, anchor=CENTER)
labeled = Label(score_frame, text="Score:", font=("Arial", 16, "bold"), bg="black", fg="white")
labeled.grid(row=0, column=0)
wins = IntVar()
wins.set(win)
w = Label(score_frame, textvariable=wins, font=("Arial", 16, "bold"), bg="black", fg="white")
w.grid(row=0, column=1)

top.mainloop()
