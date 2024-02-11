import Mouseops


def RunOnce(worflow: dict):
    taskList: list = worflow.get("Tasks")
    for task in taskList:
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
