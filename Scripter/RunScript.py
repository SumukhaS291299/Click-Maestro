import Mouseops
import customtkinter


def RunOnce(worflow: dict):
    taskList: list = worflow.get("Tasks")
    app = customtkinter.CTk()
    app.geometry("400x150")
    taskListLength = len(taskList)
    label = customtkinter.CTkLabel(app, text="Progress of current workflow....", fg_color="transparent")
    label.pack(padx=20, pady=20)
    progressbar = customtkinter.CTkProgressBar(app, orientation="horizontal")
    progressbar.pack(padx=20, pady=20)
    for i, task in enumerate(taskList):
        progressbar.set((i + 1) / taskListLength)
        if task.get("Task") == "move_mouse":
            # {"X": X, "Y": Y, "Duration": Duration, "LogSS": LogSS}
            X = task.get("args").get('X')
            Y = task.get("args").get('Y')
            Duration = task.get("args").get('Duration')
            LogSS = task.get("args").get('LogSS')
            moveMouse = Mouseops.MoveMouse(X, Y, Duration, LogSS)
            moveMouse.MoveMouse()

        if task.get("Task") == "left_click":
            #     {"X": X, "Y": Y, "Clicks": Clicks, "Interval": Interval,
            #     "Duration": Duration,"LogSS": LogSS}
            print(task)
            X = task.get("args").get('X')
            Y = task.get("args").get('Y')
            Clicks = task.get("args").get("Clicks")
            Interval = task.get("args").get("Interval")
            Duration = task.get("args").get('Duration')
            LogSS = task.get("args").get('LogSS')
            print(X, Y, Clicks, Interval, Duration, LogSS)
            LC = Mouseops.LeftClick(X, Y, Clicks, Interval, Duration, LogSS)
            LC.Click()

        if task.get("Task") == "right_click":
            X = task.get("args").get('X')
            Y = task.get("args").get('Y')
            Clicks = task.get("args").get("Clicks")
            Interval = task.get("args").get("Interval")
            Duration = task.get("args").get('Duration')
            LogSS = task.get("args").get('LogSS')
            RC = Mouseops.LeftClick(X, Y, Clicks, Interval, Duration, LogSS)
            RC.Click()

        if task.get("Task") == "Scroll":
            X = task.get("args").get('X')
            Y = task.get("args").get('Y')
            Clicks = task.get("args").get("Clicks")
            LogSS = task.get("args").get('LogSS')
            scroll = Mouseops.Scroll(Clicks, X, Y, LogSS)
            scroll.Scroll()

        if task.get("Task") == "middle_click":
            X = task.get("args").get('X')
            Y = task.get("args").get('Y')
            Clicks = task.get("args").get("Clicks")
            Interval = task.get("args").get("Interval")
            Duration = task.get("args").get('Duration')
            LogSS = task.get("args").get('LogSS')
            MC = Mouseops.ScrollWheelClick(X, Y, Clicks, Interval, Duration, LogSS)
            MC.Click()

    app.mainloop()
