import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x150")
        self.frame = customtkinter.CTkFrame(self)
        self.button = customtkinter.CTkButton(self.frame, text="my button", command=self.button_callbck)
        self.button.pack(padx=20, pady=20)
        self.frame.pack(padx=20, pady=20)

    def button_callbck(self):
        print("button clicked")

app = App()
app.mainloop()