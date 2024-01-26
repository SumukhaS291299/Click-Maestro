from Mouseops import MoveMouse,LeftClick


class ScriptMaker:

    def __init__(self):
        pass

LC = LeftClick(200,200,2,0,0,False)
print(LC)
LC.clicks = 10
print(LC)
LC.Click()


# M1 = MoveMouse(100, 100, 10, True)
# M2 = MoveMouse(50, 50, 20, True)
#
# M3 = M1 - M2