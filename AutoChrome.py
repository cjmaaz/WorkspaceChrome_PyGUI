# import the relevant modules
import pyautogui
from pywinauto import Application
import time

# Basics
# Prints the resolution of your screen
# print(pyautogui.size())

# Prints the current position of your mouse
# print(pyautogui.position())

# pyautogui.moveTo(965, 666, 3)  Args: x=965, y=666, 3 = time it takes to move (simulate mouse movement)
# pyautogui.moveRel()  Moves relative to the current position of the mouse

# Click
# pyautogui.click(100, 100, 3, 3, button='left')  X=100, Y=100, 3 = Number of clicks, 3 = duration, button = left

# Scroll
# pyautogui.scroll(500) Scroll Up
# pyautogui.scroll(-500) Scroll Down

# Keyboard
# pyautogui.write('Hello')

app = Application(backend='win32').start('C:\Program Files\Google\Chrome\Application\chrome.exe').connect(
    title='Google Chrome', timeout=10)
pyautogui.moveTo(965, 666)
time.sleep(1)
pyautogui.click()
time.sleep(2)
pyautogui.click(891,55, button='right')
pyautogui.click(988,271, button='left')
pyautogui.write('Workspace')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('mail.google.com/mail')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')
pyautogui.write('calendar.google.com')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 't')
pyautogui.write('www.docs.google.com/spreadsheets/')
pyautogui.press('enter')
pyautogui.hotkey('ctrl', 'n')
# pyautogui.click(27, 57, button='right')


# time.sleep(3)
# print(pyautogui.position())