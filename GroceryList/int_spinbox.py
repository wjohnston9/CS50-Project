from tkinter import *
import customtkinter

#IntSpinbox modified from Tom Schimanky's code at https://github.com/TomSchimansky/CustomTkinter/wiki/Create-new-widgets-(Spinbox)
class int_spinbox(customtkinter.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)

        self.step_size = 1
        self.command = None

        self.configure(fg_color=("gray78", "gray28"))

        self.grid_columnconfigure((0, 2), weight=0)  
        self.grid_columnconfigure(1, weight=1)  

        self.subtract_button = customtkinter.CTkButton(self, fg_color="#4a7dcf", text="-", width=10, height=10,
                                                       command=self.subtract_button_callback)
        self.subtract_button.grid(row=0, column=0, padx=(3, 0), pady=3)

        self.entry = customtkinter.CTkEntry(self, width=35, height=10, border_width=0)
        self.entry.grid(row=0, column=1, columnspan=1, padx=3, pady=3, sticky="ew")

        self.add_button = customtkinter.CTkButton(self, fg_color="#4a7dcf", text="+", width=10, height=10,
                                                  command=self.add_button_callback)
        self.add_button.grid(row=0, column=2, padx=(0, 3), pady=3)
        

        # default value
        self.entry.insert(0, "0")

    def add_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) + self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def subtract_button_callback(self):
        if self.command is not None:
            self.command()
        try:
            value = int(self.entry.get()) - self.step_size
            self.entry.delete(0, "end")
            self.entry.insert(0, value)
        except ValueError:
            return

    def get(self):
        try:
            return int(self.entry.get())
        except ValueError:
            return None

    def set(self, value: int):
        self.entry.delete(0, "end")
        self.entry.insert(0, str(int(value)))