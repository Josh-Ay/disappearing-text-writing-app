from tkinter import *

start_time, inactive_time = 0, 0
reset = None


def font(font_size):
    """ Accepts a font size and returns a tuple that can be used as font in the widgets """
    return "Roboto", font_size


def update_monitor():
    """ Updates the reset tracker variable """
    global reset
    reset = True


def reset_monitor():
    """ Resets the reset tracker variable """
    global reset
    reset = None


def count_mechanism(count):
    f""" Adds one to the {count} parameter passed in and updates the inactive time to the result """
    global inactive_time
    inactive_time = count

    if reset is not None:
        if reset:
            count = 0

    window.after(1000, count_mechanism, count + 1)


def start_writing():
    """ Configures the canvas and updates the window with a text box """
    global input_text_box

    canvas.config(height=36)
    canvas.delete(intro_text_section_1, intro_text_section_2, intro_text_section_3, bottom_intro_text)
    canvas.itemconfig(typing_text, text="Start typing...")

    start_btn.destroy()

    input_text_box = Text(width=50, height=15, padx=10, font=font(16), borderwidth=0, relief="groove", wrap=WORD)
    input_text_box.focus_set()

    input_text_box.bind("<KeyPress>", lambda *args: update_monitor())
    input_text_box.bind("<KeyRelease>", lambda *args: reset_monitor())

    input_text_box.pack()

    count_mechanism(0)

    check_inactivity()


def check_inactivity():
    difference = inactive_time - start_time
    if difference > 5:
        input_text_box.delete("1.0", END)

    window.after(5000, check_inactivity)


window = Tk()

# Configuring the window appearance
window.title("Disappearing Text Writing App")
window.iconbitmap("./icon/icon.ico")
window.minsize(width=400, height=300)
window.resizable(False, False)
window.config(bg="white")

# Creating a canvas
canvas = Canvas()
canvas.config(width=450, height=200, bg="white", highlightthickness=0)
canvas.pack()

# The introduction title text
intro_text_section_1 = canvas.create_text(70, 70, text="The Most", font=font(18))
intro_text_section_2 = canvas.create_text(187, 70, text="Dangerous", font=font(18), fill="red")
intro_text_section_3 = canvas.create_text(340, 70, text="Text Writing App", font=font(18))

# The supporting introduction text
bottom_intro_text = canvas.create_text(225, 100, text="Don’t stop writing, or all progress will be lost.❌",
                                       font=font(10))

# Start Button
start_btn = Button(text="Start writing", font=font(12), fg="white", bg="green", borderwidth=0, highlightthickness=0,
                   command=start_writing, padx=15, pady=5, cursor="hand2")
start_btn.pack()

# Typing text
typing_text = canvas.create_text(225, 18, text="", font=font(18), fill="green")

# Input text box where the user writes
input_text_box = None

window.mainloop()
