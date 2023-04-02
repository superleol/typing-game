from tkinter import *

#-----------------functions for timer-----------------
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

#------------------- functions for timer ends ----------------------

#----------------------- functions for information ---------------------------

def number_of_words():
  #get words from textbox
  words = field.get()
  words_counter = len(words.split())
  total_num_of_words = Label(root, text="Number of words: " + str(words_counter), font=("bold","10"))
  total_num_of_words.grid(row=8, column=0)
  return words_counter


def words_per_minute():
  word_counter = number_of_words()

  #word_counter / time
  wpm = word_counter / seconds * 60 
  show_wpm = Label(root, text="Words per minute: " +str(round(wpm)), font=("bold","10"))
  show_wpm.grid(row=9, column=0)
  

def timetaken():
  time_taken = Label(root, text="Time taken: " +str(seconds) + " seconds", font=("bold","10"))
  time_taken.grid(row=7, column=0)


def pause_timer():
  global isPauseTimer
  isPauseTimer = True

#---------------------functions for information ends---------------------

#---------------functions ends-----------------


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
  command=lambda: [pause_timer(), number_of_words(),words_per_minute(), timetaken()])
submit_button.grid(row=6, column=2)

root.mainloop()
