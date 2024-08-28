import pyperclip
import pyautogui
import keyboard
import time

file_path = 'codes.txt'
verify_delay= 6

def code_paster(file_path, pause_time=5):
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            pyperclip.copy(line)
            time.sleep(1)  
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(3)
            keyboard.press('enter')
            keyboard.release('enter')
            time.sleep(verify_delay) 
            pyautogui.press('z')
            time.sleep(2)
            pyautogui.click()  
            pyautogui.click()  
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('backspace')
            time.sleep(2)  
      
      

code_paster(file_path)
