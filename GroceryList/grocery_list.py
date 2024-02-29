from tkinter import *
import customtkinter
from int_spinbox import int_spinbox

    
grocery_button_list = []
grocery_button_tracker = []

def grocery_button_switch(r):
            if(grocery_button_tracker[r]):
                grocery_button_list[r].configure(fg_color="grey")
                grocery_button_tracker[r] = False
            else:
                grocery_button_list[r].configure(fg_color="#4a7dcf")
                grocery_button_tracker[r] = True

class App(customtkinter.CTk):
    

    def __init__(self):
        super().__init__()

        customtkinter.set_appearance_mode("dark")
        self.title("Grocery List")
        self.geometry("400x600")
        self.grid_columnconfigure((0, 2), weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0,1,3), weight=0)
        self.grid_rowconfigure(2, weight=1)

        self.entry_text = customtkinter.CTkEntry(self, placeholder_text="Enter item")
        self.entry_text.grid(row=0, column=1, padx=10, pady=0, sticky="ew", columnspan=1)

        self.spinbox_1 = int_spinbox(self, "Number")
        self.spinbox_1.grid(row=0, column=2, padx=10, pady=0, sticky="ew", columnspan=1)

        self.spinbox_1.set(1)

        self.button = customtkinter.CTkButton(self, fg_color="#4a7dcf", text="Add To List", command=self.button_callback)
        self.button.grid(row=1, column=1, padx=10, pady=10, columnspan=1)

        self.delete_button = customtkinter.CTkButton(self, fg_color="#ba2116", text="Delete all items", command=self.delete_button_callback)
        self.delete_button.grid(row=3, column=2, padx=10, pady=10, columnspan=1)

        self.item_frame = customtkinter.CTkScrollableFrame(self)
        self.item_frame.grid(row=2, column=1, sticky="nsew", columnspan=2)
        self.item_frame.grid_rowconfigure((0,1,2,3), weight=1)

        
            
  

    def button_callback(self):
        if self.entry_text.get() != "":
            number_item_text = str(self.spinbox_1.get()) + " " + self.entry_text.get()
            btn = customtkinter.CTkButton(self.item_frame, fg_color="#4a7dcf", text= number_item_text, command= lambda r=len(grocery_button_list): grocery_button_switch(r))
            btn.grid(row=len(grocery_button_list) + 1, column=1, padx=10, pady=10)
            grocery_button_list.append(btn)
            grocery_button_tracker.append(True)
            self.entry_text.delete(0, len(self.entry_text.get()))
            self.spinbox_1.set(1)

    def delete_button_callback(self):
        grocery_button_list.clear()
        grocery_button_tracker.clear()
        self.item_frame.destroy()
        self.item_frame = customtkinter.CTkScrollableFrame(self)
        self.item_frame.grid(row=2, column=1, sticky="nsew", columnspan=2)
        self.item_frame.grid_rowconfigure((0,1,2,3), weight=1)



app = App()
app.mainloop()