import pyautogui


class Mouse:

    def __init__(self):
        self.W, self.H = pyautogui.size()
        self.x = int(self.W / 2)
        self.y = int(self.H / 2)

    def ShowMouseInfo(self):
        pyautogui.moveTo(100, 100, duration=10)
        pyautogui.mouseInfo()

    def ParseLogFile(self):
        pass


class MoveMouse(Mouse):
    """
    Move mouse to specific location
    X - Integer value to move the mouse to a specfic location X with-in the width of the screen
    Y - Integer value to move the mouse to a specfic location Y with-in the height of the screen
    duration -  float value which defines the intentional added linear lag to the mouse movement
    logSS - bool value If True takes a Scrrenshot after execution
    """

    def __init__(self, X: int, Y: int, duration=1, logSS=False):
        super().__init__()
        self.newx = int(X)
        self.newy = int(Y)
        self.duration = float(duration)
        self.logSS = logSS

    def __str__(self):
        return f"Mouse Pointer with:\nX= {self.newx} px\nY= {self.newy} px\nDefault duration for movement= {self.duration} s\nLog Screenshort= {self.logSS}"

    def __repr__(self):
        return f"MoveMouse\nX= {self.newx} px\nY= {self.newy} px\nDefault duration for movement= {self.duration} s\nLog Screenshort= {self.logSS}"

    def __add__(self, other):
        return MoveMouse(self.newx + other.newx, self.newy + other.newy,
                         duration=min(int(self.duration), int(other.duration)),
                         logSS=(self.logSS or other.logSS))

    def __sub__(self, other):
        return MoveMouse(self.newx - other.newx, self.newy - other.newy,
                         duration=min(int(self.duration), int(other.duration)),
                         logSS=(self.logSS or other.logSS))

    def MoveMouse(self):
        pyautogui.moveTo(self.newx, self.newy, duration=self.duration, logScreenshot=self.logSS)


class LeftClick(Mouse):
    """
    X - Integer value to move the mouse to a specfic location X with-in the width of the screen
    Y - Integer value to move the mouse to a specfic location Y with-in the height of the screen
    clicks - The number of clicks
    interval - The added delay in-between the clicks
    duration - float value which defines the intentional added linear lag to the mouse movement
    logSS - bool value If True takes a Scrrenshot after execution
    """

    def __init__(self, X: int, Y: int, clicks: int, interval: float, duration: float, logSS=False):
        super().__init__()
        self.button = "LEFT"
        self.X = X
        self.Y = Y
        self.clicks = clicks
        self.interval = interval
        self.duration = duration
        self.logSS = logSS

    def __str__(self):
        return f"Mouse Pointer Left clicks with:\nX= {self.X} px\nY= {self.Y} px\nNumber of Clicks = {self.clicks} click(s)\nInterval between Clicks = {self.interval} s\nDefault duration for movement= {self.duration} s\nLog Screenshort= {self.logSS}"

    def __repr__(self):
        return f"MoveMouse\nX= {self.X} px\nY= {self.Y} px\nNumber of Clicks = {self.clicks} click(s)\nInterval between Clicks = {self.interval} s\nDefault duration for movement= {self.duration} s\nLog Screenshort= {self.logSS}"

    def Click(self):
        pyautogui.click(x=self.X, y=self.Y, button=self.button, clicks=self.clicks, interval=self.interval,
                        duration=self.duration,
                        logScreenshot=self.logSS)
