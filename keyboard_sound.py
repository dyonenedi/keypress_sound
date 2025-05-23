import sys
import os
import pygame
import keyboard
import threading
import winsound
from pystray import Icon, MenuItem, Menu
from PIL import Image, ImageDraw

pygame.mixer.init()

icon = None  # Variável global para o ícone

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def play_sound():
    sound_path = resource_path("relax_key.wav")
    sound = pygame.mixer.Sound(sound_path)
    sound.play()

def beep_start():
    winsound.MessageBeep(winsound.MB_ICONASTERISK)

def beep_exit():
    winsound.MessageBeep(winsound.MB_ICONHAND)

def start_keyboard_listener():
    keyboard.on_press(lambda e: play_sound())
    keyboard.add_hotkey('shift+esc', on_exit)

def create_image():
    # Cria uma imagem branca
    img = Image.new("RGB", (64, 64), "white")
    draw = ImageDraw.Draw(img)

    # Desenha o círculo externo
    draw.ellipse((4, 4, 60, 60), outline="black", width=3)

    # Parâmetros para desenhar as teclas
    key_width = 6
    key_height = 6
    key_spacing_x = 2
    key_spacing_y = 2
    offset_x = 14
    offset_y = 20

    # Linha superior de teclas
    for i in range(10):
        x = offset_x + i * (key_width + key_spacing_x)
        y = offset_y
        draw.rectangle([x, y, x + key_width, y + key_height], fill="black")

    # Linha do meio de teclas
    for i in range(9):
        x = offset_x + i * (key_width + key_spacing_x) + (key_width + key_spacing_x) / 2
        y = offset_y + key_height + key_spacing_y
        draw.rectangle([x, y, x + key_width, y + key_height], fill="black")

    # Barra de espaço
    spacebar_width = (key_width + key_spacing_x) * 6 - key_spacing_x
    x = (64 - spacebar_width) // 2
    y = offset_y + 2 * (key_height + key_spacing_y)
    draw.rectangle([x, y, x + spacebar_width, y + key_height], fill="black")

    return img

def on_exit(icon_item=None, item=None):
    beep_exit()
    global icon
    if icon:
        icon.stop()
    os._exit(0)

def main():
    global icon
    beep_start()

    # Configura ícone na bandeja
    menu = Menu(MenuItem('Sair', on_exit))
    icon = Icon("TecladoSom", create_image(), menu=menu)

    # Inicia listener do teclado em thread separada
    listener_thread = threading.Thread(target=start_keyboard_listener, daemon=True)
    listener_thread.start()

    icon.run()

if __name__ == "__main__":
    main()
