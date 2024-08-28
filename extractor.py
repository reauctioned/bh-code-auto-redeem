import pyperclip
import pyautogui
import time

file_path = 'codex.txt'

def code_paster(file_path, pause_time=10):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            pyperclip.copy(line)
            time.sleep(pause_time)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            time.sleep(pause_time)
            pyautogui.press('enter')
            time.sleep(pause_time)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            time.sleep(pause_time)


code_paster('codes.txt')