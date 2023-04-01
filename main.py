from tkinter import *

#-----------------functions-----------------

"""Resets the number of seconds. Starts the timer"""
def start_timer():

  global seconds
  seconds = 60
  global isPauseTimer 
  isPauseTimer = False
  countdown()


"""Disables the start button to avoid bugs. 
     Counts down in seconds.
     Enables the button again when the time is up"""


def countdown():
  global seconds
  timerbutton.config(state=DISABLED)
  if seconds > 0 and not isPauseTimer:
    print(isPauseTimer)
    seconds -= 1
    root.after(1000, countdown)
    timerlabel.config(text=seconds)

  else:
    timerlabel.config(text="time's up!",
                      font=("bold", "24"),
                      bg="black",
                      fg="white")
    timerbutton.config(state=NORMAL)


def words_per_minute():
  wpm = Label(root, )


def show_info():
  wordsperminute = Label(root, )
  accuracy = Label(root, )
  time_taken = Label(root, )

def pause_timer():
  global isPauseTimer
  isPauseTimer = True
  
 #---------------function ends-----------------
  
#----------------Main menu starts here----------------

# load window
root = Tk()
root.title("typing game")
root.geometry("1000x1000")
root.configure(bg="lightblue")

# read file, display text
f = open("paragraphs", "r")
paragraph = Label(root, text=f.read(), font=("bold", "10"))
paragraph.grid(row=0, column=2)

seconds = 60

# set up screen
field = Entry(root, width=50, font=('Arial 10'))
field.grid(row=3, column=2)

timerlabel = Label(root,
                   text=seconds,
                   font=("bold", "24"),
                   bg="black",
                   fg="white")
timerbutton = Button(root, text="start", command=start_timer)
timerlabel.grid(row=1, column=2)
timerbutton.grid(row=2, column=2)

submit_button = Button(
  root,
  text="submit",
  font=("bold", "10"),
  command=lambda: [pause_timer(), show_info()])
submit_button.grid(row=6, column=2)

root.mainloop()
