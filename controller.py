import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle

class Main():
    def __init__(self,master):
        master.geometry('500x500')
        master.title('DioCar Controller')
        self.button_1 = ttk.Button(root,text='Start Car !',takefocus = False,command=self.start_car).grid(row=0,column=0)
        self.button_2 = ttk.Button(root,text='Call Car!',takefocus=False,command=self.call_car).grid(padx=10,row=0,column=1)

    def start_car(self):
        start_label = ttk.Entry(root)
        start_label.insert(0,'Car started!')
        start_label.config(state="disabled")
        start_label.grid(padx=10,row=1,column=0)

    def call_car(self):
        call_label = ttk.Entry(root)
        call_label.insert(0,'Car called!')
        call_label.config(state="disabled")
        call_label.grid(row=1,column=1)


root = tk.Tk()
style = ThemedStyle(root)
style.set_theme("yaru")
app = Main(root)
root.mainloop()
