import customtkinter
raise NotImplemented


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure(2, weight=8, pad=25)
        self.geometry("1000x600")
        self.frame = customtkinter.CTkFrame(self)
        self.button = customtkinter.CTkButton(self.frame, text="my button")
        self.button.pack(padx=25, pady=25)
        self.frame.grid(row=0, column=0, sticky=customtkinter.NSEW, padx=30, pady=10)
        self.workflowCanvasframe = customtkinter.CTkFrame(self,width=550,height=550)
        self.workflowCanvasframe.grid(row=0, column=1, sticky=customtkinter.NSEW, padx=30, pady=10)
        self.workflowCanvas = customtkinter.CTkCanvas(self.workflowCanvasframe, width=500, height=500, background="cyan" )
        self.workflowCanvas.pack()



app = App()
app.mainloop()
