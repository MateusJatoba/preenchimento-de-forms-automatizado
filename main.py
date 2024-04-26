import webbrowser
import pyautogui
from time import sleep
i = 0

while i < 3:

    sleep(2)
    webbrowser.open('https://docs.google.com/forms/d/e/1FAIpQLSdVq09bHQj19L6OMzCHiLnp8-_0ciVK4chIcgGx75Vz1Qqd7Q/viewform?usp=sf_link')

    sleep(2)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')

    pyautogui.hotkey('space') #clicou resp 1
    sleep(1.5)
    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab') # chegou resp 2
    pyautogui.hotkey('down') # clicou resp 2

    sleep(1.5)

    #pyautogui.hotkey('space')

    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab') # chegu resp 3
    pyautogui.hotkey('down')
    pyautogui.hotkey('down') # clicou resp 3
    sleep(1.5)

    pyautogui.hotkey('tab')
    pyautogui.hotkey('tab')
    pyautogui.hotkey('space') # enviou

    sleep(1.5)
    pyautogui.hotkey('ctrl' , 'w')

    i += 1


