import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Grade Calculator")
root.geometry("500x400")

# Function to perform grade calculation
def calculation():
    try:
        english = int(englishvalue.get())
        speech_processing = int(speech_processingvalue.get())
        mathematics = int(mathematicsvalue.get())
        dbms = int(dbmsvalue.get())
        crt = int(crtvalue.get())

        total = english + speech_processing + mathematics + dbms + crt
        average = total / 5

        total_label.config(text=f"{total}")
        average_label.config(text=f"{average:.2f}")

        if average >= 90:
            grade = "A+"
        elif average >= 80:
            grade = "A"
        elif average >= 70:
            grade = "B+"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        else:
            grade = "F"

        grade_label.config(text=grade)
    except ValueError:
        total_label.config(text="Invalid")
        average_label.config(text="Input")
        grade_label.config(text="Error")

# Labels for subjects
Label(root, text="English:", font="arial 10").place(x=50, y=20)
Label(root, text="Speech Processing:", font="arial 10").place(x=50, y=70)
Label(root, text="Mathematics:", font="arial 10").place(x=50, y=120)
Label(root, text="DBMS:", font="arial 10").place(x=50, y=170)
Label(root, text="CRT:", font="arial 10").place(x=50, y=220)
Label(root, text="Total:", font="arial 10").place(x=50, y=270)
Label(root, text="Average:", font="arial 10").place(x=50, y=300)
Label(root, text="Grade:", font="arial 10").place(x=50, y=330)

# Entry fields
englishvalue = StringVar()
speech_processingvalue = StringVar()
mathematicsvalue = StringVar()
dbmsvalue = StringVar()
crtvalue = StringVar()

Entry(root, textvariable=englishvalue, font="arial 15", width=15).place(x=250, y=20)
Entry(root, textvariable=speech_processingvalue, font="arial 15", width=15).place(x=250, y=70)
Entry(root, textvariable=mathematicsvalue, font="arial 15", width=15).place(x=250, y=120)
Entry(root, textvariable=dbmsvalue, font="arial 15", width=15).place(x=250, y=170)
Entry(root, textvariable=crtvalue, font="arial 15", width=15).place(x=250, y=220)

# Dynamic output labels
total_label = Label(root, text="", font="Arial 15 bold")
total_label.place(x=250, y=270)

average_label = Label(root, text="", font="Arial 15 bold")
average_label.place(x=250, y=300)

grade_label = Label(root, text="", font="Arial 15 bold")
grade_label.place(x=250, y=330)

# Buttons
Button(text="Calculate", font="arial 15", bg="white", bd=5, command=calculation).place(x=50, y=360)
Button(text="Exit", font="arial 15", bg="white", bd=5, command=root.destroy).place(x=200, y=360)

root.mainloop()
