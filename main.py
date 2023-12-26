from screenshot import main
from screenshot import mouse_movement
import threading
import time

def obtener_encantamiento(seleccion):
    switch_encantamientos = {
        1: 'protection',
        2: 'feather',
        3: 'unbreaking',
        4: 'mending',
        5: 'efficiency',
        6: 'fortune',
        7: 'silk',
        8: 'looting',
        9: 'sharpness',
        10: 'smite',
        11: 'sweeping',
        12: 'power'
    }

    return switch_encantamientos.get(seleccion, 'Selección no válida. Por favor, elige un número válido.')

# Variable de bandera para indicar a los hilos que deben detenerse
stop_threads = threading.Event()
ASCII = '''
 _______    ______   __    __   ______   __    __  ______   ______    ______    ______  
|       \  /      \ |  \  |  \ /      \ |  \  |  \|      \ /      \  /      \  /      \ 
| $$$$$$$\|  $$$$$$\| $$\ | $$|  $$$$$$\| $$  | $$ \$$$$$$|  $$$$$$\|  $$$$$$\|  $$$$$$|
| $$__/ $$| $$  | $$| $$$\| $$| $$   \$$| $$__| $$  | $$  | $$___\$$| $$__| $$| $$  | $$
| $$    $$| $$  | $$| $$$$\ $$| $$      | $$    $$  | $$   \$$    \ | $$    $$| $$  | $$
| $$$$$$$ | $$  | $$| $$\$$ $$| $$   __ | $$$$$$$$  | $$   _\$$$$$$\| $$$$$$$$| $$  | $$
| $$      | $$__/ $$| $$ \$$$$| $$__/  \| $$  | $$ _| $$_ |  \__| $$| $$  | $$| $$__/ $$
| $$       \$$    $$| $$  \$$$ \$$    $$| $$  | $$|   $$ \ \$$    $$| $$  | $$ \$$    $$
 \$$        \$$$$$$  \$$   \$$  \$$$$$$  \$$   \$$ \$$$$$$  \$$$$$$  \$$   \$$  \$$$$$$ 
                                                                                                                                                                      
                                                                                        
'''

encantamientos_str = """Armadura:
1. Protección 
2. Feather Falling 

Herramientas:
3. Unbreaking 
4. Mending 
5. Efficiency 
6. Fortune 
7. Silk Touch 

Armas:
8. Looting 
9. Sharpness 
10. Smite 
11. Sweeping Edge 

Arcos:
12. Power """


if __name__ == "__main__":
    # Copyright (c) PonchisaoHosting
    print(ASCII)

    print('¿Qué encantamiento deseas obtener?')
    print(" ")
    print(encantamientos_str)
    print(" ")
    selection = int(input())

    img_name = obtener_encantamiento(selection)
    print(f'Has seleccionado: {img_name}')

    print("[?] ¿Cuantas veces quieres ejecutar el ciclo?")
    repetitions = int(input())
    reference_pattern_path = f'screenshots/{img_name}.png'

    # Crea dos threads
    thread_1 = threading.Thread(target=lambda: main(reference_pattern_path, stop_threads))
    thread_2 = threading.Thread(target=mouse_movement, args=(repetitions, stop_threads))

    # Inicia los threads
    thread_1.start()
    thread_2.start()

    # Espera a que ambos threads terminen
    thread_1.join()
    thread_2.join()

    time.sleep(3)
