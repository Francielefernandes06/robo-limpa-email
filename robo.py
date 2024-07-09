import pyautogui
import time

# Pausar entre os comandos
pyautogui.PAUSE = 1

def move_and_click(x, y):
    # Mover o mouse para a posição (x, y)
    pyautogui.moveTo(x, y, duration=1)
    # Clicar na posição atual do mouse
    pyautogui.click()



time.sleep(5)

for _ in range(50):
    # Move e clica na posição (190, 290)
    move_and_click(190, 290)

    # Espera 2 segundos
    time.sleep(2)

    # Move e clica na posição (350, 290)
    move_and_click(350, 290)

    # Espera 2 segundos
    time.sleep(2)