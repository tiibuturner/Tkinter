
from tkinter import *
from datetime import date

## Luodan ikkuna
timerWindow=Tk()
timerWindow.geometry("500x500")
timerWindow.title("About today and days left in this year")
timerWindow.configure(background='royal blue')

today = date.today()
f_today = today.strftime("%A | %B %d, %Y")
today_label = Label(timerWindow, text=f'Today is\n {f_today}')
today_label.pack(pady=20)

days_in_year = 365
todays_day_number = int(today.strftime("%j"))
days_left = days_in_year - todays_day_number
countdown_label = Label(timerWindow, text=f'Days left in this year {days_left}')
countdown_label.pack(pady=20)


## Loop loop!
timerWindow.mainloop()