import os
import threading

import customtkinter
import pyautogui
import subprocess

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x240")


def button_function():
    print("button pressed")


def RunWebConf(port):
    RunWebpage = subprocess.run(f"streamlit run Generate.py --server.port {int(port)}", shell=True,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)
    print(RunWebpage.stdout)
    print(RunWebpage.stderr)


def MouseInfoThread():
    pyautogui.mouseInfo()


def MouseInfoStart():
    os.system("python ShowMouseInfo.py")
    # threading.Thread(target=MouseInfoThread).start()


Title = app.title("Welcome to Low code configurator")
PortLabel = customtkinter.CTkLabel(master=app, text="Select the port to run the web configurator")
PortLabel.place(relx=0.5, rely=0.15, anchor=customtkinter.CENTER)
PortEntry = customtkinter.CTkEntry(master=app)
PortEntry.place(relx=0.5, rely=0.25, anchor=customtkinter.CENTER)
StartWeb = customtkinter.CTkButton(master=app, text="Start web configurator",
                                   command=lambda: RunWebConf(PortEntry.get()))
StartWeb.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)
StartMouseInfo = customtkinter.CTkButton(master=app, text="Show mouse info", command=MouseInfoStart)
StartMouseInfo.place(relx=0.5, rely=0.75, anchor=customtkinter.CENTER)

app.mainloop()