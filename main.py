import time
import pyautogui

import subprocess

RunWebpage = subprocess.run("streamlit run Generate.py", shell=True, stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE)

print(RunWebpage.stdout)
print(RunWebpage.stderr)
