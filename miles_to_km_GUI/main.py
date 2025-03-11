from tkinter import *

def calculator():
    new_text = float(input.get()) * 1.609
    result_label.config(text=new_text)

window = Tk()
window.title("Miles to Km converter")
window.minsize(width=500, height=300)
window.config(padx=80, pady=80)

###Labels
#is equal label
my_label = Label(text="is equal to", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=1)
my_label.config(padx=20, pady=20)

#result label
result_label = Label(text=0, font=("Arial", 24, "bold"))
result_label.grid(column=1, row=1)
result_label.config(padx=20, pady=20)

#Miles and KM
miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=3, row=0)
miles_label.config(padx=20, pady=20)

KM_label = Label(text="km", font=("Arial", 24, "bold"))
KM_label.grid(column=3, row=1)
KM_label.config(padx=20, pady=20)


#Entrys
input = Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

#Button
button_calculator = Button(text="Calculate", command=calculator)
button_calculator.grid(column=1, row=3)


window.mainloop()