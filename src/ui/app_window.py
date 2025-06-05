from tkinter import Label, Button, Entry, Frame
from utils.helpers import process_input

class AppWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Andersen Lab QA Task")
        self.master.geometry("600x500")
        self.setup_layout()

    def setup_layout(self):
        # Center frame for all widgets
        center_frame = Frame(self.master)
        center_frame.place(relx=0.5, rely=0.3, anchor='center')
        self.label = Label(center_frame, text="Enter a number, a name, or a list of numbers (space/comma separated):")
        self.label.pack(pady=10)
        self.entry = Entry(center_frame, width=50)
        self.entry.pack(pady=10)
        self.button = Button(center_frame, text="Submit", command=self.handle_submit)
        self.button.pack(pady=10)
        self.output_label = Label(center_frame, text="", fg="blue", wraplength=450, justify="left")
        self.output_label.pack(pady=20)

    def handle_submit(self):
        user_input = self.entry.get().strip()
        output = process_input(user_input)
        self.output_label.config(text=output)