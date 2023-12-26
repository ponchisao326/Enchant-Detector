import pyautogui
import time
import win32api
import threading
import win32con
from attempts import attempts


# Variable de bandera para indicar a los hilos que deben detenerse
stop_threads = threading.Event()

def locate(path):
    location = pyautogui.locateOnScreen(path, confidence=0.99, region=(500,300,900,250))
    return location is not None, location

def loop_locate(path, stop_event):
    try:
        while not stop_event.is_set():
            if stop_event.is_set():
                break  # Sal del bucle si la bandera de detención se establece
            found, location = locate(path)
            if found:
                print(f"[+] Encantamiento encontrado")

                print("---------------------------------------------------")
                print("")
                print(f'Code created by PonchisaoHosting')
                print("")
                print("---------------------------------------------------")
                
                stop_event.set()  # Establece la bandera de detención
            if not stop_event.is_set():
                print("[-] Encantamiento no encontrado, sigo buscando... ")
    except KeyboardInterrupt:
        print("[+] Programa detenido")

        print("---------------------------------------------------")
        print("")
        print(f'Code created by PonchisaoHosting')
        print("")
        print("---------------------------------------------------")

def move_mouse(x, y):
    win32api.SetCursorPos((x, y))

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def mouse_movement(repetitions, stop_event):
    try:
        count = 0
        while count < repetitions:
            move_mouse(785, 423)
            time.sleep(0.3)
            move_mouse(787, 366)
            time.sleep(0.3)
            if stop_event.is_set():
                exit()
            click(888, 323)
            attempts(count)
            count += 1
    except KeyboardInterrupt:
        print("[+] Programa detenido")

        print("---------------------------------------------------")
        print("")
        print(f'Code created by PonchisaoHosting')
        print("")
        print("---------------------------------------------------")

    stop_event.set() # Establece la bandera de detención
    print("[+] El numero de intentos han sido probados y no se ha encontrado el encantamiento, vuelva a iniciar el programa si desea seguir intentandolo")

    print("---------------------------------------------------")
    print("")
    print(f'Code created by PonchisaoHosting')
    print("")
    print("---------------------------------------------------")

def main(path, stop_event):
    loop_locate(path, stop_event)