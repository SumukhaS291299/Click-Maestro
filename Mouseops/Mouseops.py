import json

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
        return f"Left Click\nX= {self.X} px\nY= {self.Y} px\nNumber of Clicks = {self.clicks} click(s)\nInterval between Clicks = {self.interval} s\nDefault duration for movement= {self.duration} s\nLog Screenshort= {self.logSS}"

    def Click(self):
        pyautogui.click(x=self.X, y=self.Y, button=self.button, clicks=self.clicks, interval=self.interval,
                        duration=self.duration,
                        logScreenshot=self.logSS)


class RightClick(Mouse):
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
        self.button = "RIGHT"
        self.X = X
        self.Y = Y
        self.clicks = clicks
        self.interval = interval
        self.duration = duration
        self.logSS = logSS

    def __str__(self):
        return f"Mouse Pointer Right clicks with:\nX= {self.X} px\nY= {self.Y} px\nNumber of Clicks = {self.clicks} click(s)\nInterval between Clicks = {self.interval} s\nDefault duration for movement= {self.duration} s\nLog Screenshort= {self.logSS}"

    def __repr__(self):
        return f"Right Click\nX= {self.X} px\nY= {self.Y} px\nNumber of Clicks = {self.clicks} click(s)\nInterval between Clicks = {self.interval} s\nDefault duration for movement= {self.duration} s\nLog Screenshort= {self.logSS}"

    def Click(self):
        pyautogui.click(x=self.X, y=self.Y, button=self.button, clicks=self.clicks, interval=self.interval,
                        duration=self.duration,
                        logScreenshot=self.logSS)


# MIDDLE
class ScrollWheelClick(Mouse):
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
        self.button = "MIDDLE"
        self.X = X
        self.Y = Y
        self.clicks = clicks
        self.interval = interval
        self.duration = duration
        self.logSS = logSS

    def __str__(self):
        return f"Mouse Pointer Right clicks with:\nX= {self.X} px\nY= {self.Y} px\nNumber of Clicks = {self.clicks} click(s)\nInterval between Clicks = {self.interval} s\nDefault duration for movement= {self.duration} s\nLog Screenshort= {self.logSS}"

    def __repr__(self):
        return f"Right Click\nX= {self.X} px\nY= {self.Y} px\nNumber of Clicks = {self.clicks} click(s)\nInterval between Clicks = {self.interval} s\nDefault duration for movement= {self.duration} s\nLog Screenshort= {self.logSS}"

    def Click(self):
        pyautogui.click(x=self.X, y=self.Y, button=self.button, clicks=self.clicks, interval=self.interval,
                        duration=self.duration,
                        logScreenshot=self.logSS)


class Scroll(Mouse):

    def __init__(self, noOfscroll: float, x: int, y: int, logSS=False):
        super().__init__()
        self.x = x
        self.y = y
        self.clicks = noOfscroll
        self.logSS = logSS

    def Scroll(self):
        pyautogui.scroll(clicks=self.clicks, x=self.x, y=self.y, logScreenshot=self.logSS)


class MiddleClick(ScrollWheelClick):

    def __init__(self, X: int, Y: int, clicks: int, interval: float, duration: float):
        super().__init__(X, Y, clicks, interval, duration)


class Region:

    def __init__(self, fromx=0, fromy=0, tox=pyautogui.size().width, toy=pyautogui.size().height):
        self.fromx = int(fromx)
        self.fromy = int(fromy)
        self.tox = int(tox)
        self.toy = int(toy)

    def __str__(self):
        return json.dumps({"From X": self.fromx, "From Y": self.fromy, "To X": self.tox, "To Y": self.toy})


class Locate(Mouse):

    def __init__(self, img: str, grayscale=False, minSearchTime=1):
        super().__init__()
        self.img = img
        self.grayscale = grayscale
        self.minSearchTime = minSearchTime
        raise FutureWarning

    def Locate(self):
        return pyautogui.locateCenterOnScreen(self.img, grayscale=self.grayscale, minSearchTime=self.minSearchTime)

    def LocateOnScreen(self):
        return pyautogui.locateOnScreen(self.img, grayscale=self.grayscale, minSearchTime=self.minSearchTime)

    def LocateAllOnScreen(self, regionSerach: Region):
        return pyautogui.locateAllOnScreen(image=self.img, grayscale=self.grayscale,
                                           region=(regionSerach.fromx, regionSerach.fromy, regionSerach.tox,
                                                   regionSerach.toy))
