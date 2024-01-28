import pyautogui

import Mouseops

# LC = Mouseops.LeftClick(100, 200, 1, 1, 1, False)
# LC.Click()

loc = pyautogui.locateAll("img.png", "img.png", grayscale=False)
# pyautogui.moveTo(loc)
print(list(loc))


class ScriptMaker:

    def __init__(self):
        pass
#
# LC = LeftClick(200,200,2,0,0,False)
# print(LC)
# LC.clicks = 10
# print(LC)
# LC.Click()

# RC = RightClick(200,200,1,0,0,False)
# RC.Click()

# M1 = MoveMouse(100, 100, 10, True)
# M2 = MoveMouse(50, 50, 20, True)
#
# M3 = M1 - M2
