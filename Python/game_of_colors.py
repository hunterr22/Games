
import tkinter
import random

colors = ['white', 'blue', 'green', 'yellow', 'red', 'purple', 'black']
score = 0
time = 20


def start(e):
    if time == 20:
        count()
    next()


def next():
    global score
    global time
    if time > 0:
        word.focus_set()
        if word.get().lower() == colors[1].lower():
            score += 1
        word.delete(0, tkinter.END)
        random.shuffle(colors)
        colorWord.config(fg=str(colors[1]), text=str(colors[0]))
        score_sen.config(text="Score: " + str(score), font=('Times New Roman', 12))


def count():
    global time
    if time > 0:
        time -= 1
        timer.config(text="Time left: " + str(time), font=('Times New Roman', 12))
        timer.after(1000, count)


pic = tkinter.Tk()
pic.title("Game of Colors")
pic.geometry("500x250")

first_sen = tkinter.Label(pic, text="To answer correctly, type color of words! Press Enter to begin!",
                          font=('Times New Roman', 12))
first_sen.pack()
score_sen = tkinter.Label(pic)
score_sen.pack()
timer = tkinter.Label(pic, text="Time left: " + str(time), font=('Times New Roman', 12))
timer.pack()
colorWord = tkinter.Label(pic, font=('Times New Roman', 16))
colorWord.pack()

word = tkinter.Entry(pic)
pic.bind('<Return>', start)
word.pack()
word.focus_set()
pic.mainloop()
