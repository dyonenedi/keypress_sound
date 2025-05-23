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
    """
    Cria um ícone de teclado baseado em uma imagem de referência,
    com um fundo branco, contornos pretos e proporções ajustadas.
    O ícone tem 64x64 pixels.
    """
    # Define o tamanho da imagem e cores
    img_width, img_height = 64, 64
    background_color = (255, 255, 255)  # Branco
    line_color = (0, 0, 0)  # Preto
    line_width = 2  # Espessura da linha para todos os elementos

    # Cria a imagem
    image = Image.new('RGB', (img_width, img_height), color=background_color)
    draw = ImageDraw.Draw(image)

    # Parâmetros do corpo do teclado (coordenadas para o centro da linha de contorno)
    # Baseado em uma análise visual da imagem de referência e escalonado para 64x64
    # Largura visual desejada: 48px, Altura visual desejada: 22px
    kb_visual_width = 48
    kb_visual_height = 22
    
    # Coordenadas do centro da linha para o desenho
    kb_center_line_width = kb_visual_width - line_width
    kb_center_line_height = kb_visual_height - line_width
    
    # Ajuste para centralização geral do ícone
    # O ícone (cabo + teclado) tem uma altura visual total de aprox. 30px
    # (64 - 30) / 2 = 17 (offset superior para o elemento mais alto)
    # O elemento mais alto é o topo do cabo (y_visual = 17)
    # O topo visual do teclado estará em y = 17 + (altura_cabo_vertical = 8) = 25
    kb_visual_y0 = 17 + 8 # y_visual_topo_cabo + altura_visual_cabo_vertical

    kb_x0_center = (img_width - kb_visual_width) / 2 + line_width / 2
    kb_y0_center = kb_visual_y0 + line_width / 2
    kb_x1_center = kb_x0_center + kb_center_line_width
    kb_y1_center = kb_y0_center + kb_center_line_height
    kb_corner_radius = 3 # Raio para o centro da linha

    # Desenha o corpo do teclado
    draw.rounded_rectangle(
        (kb_x0_center, kb_y0_center, kb_x1_center, kb_y1_center),
        radius=kb_corner_radius,
        outline=line_color,
        width=line_width
    )

    # Parâmetros das teclas
    num_rows = 3
    num_cols = 5
    key_visual_size = 4  # Tamanho visual de cada tecla (largura/altura)
    key_visual_spacing = 2  # Espaçamento visual entre as teclas

    # Dimensão de desenho para cada tecla (centro da linha)
    key_draw_dim = key_visual_size - line_width

    # Bloco total de teclas (dimensões visuais)
    key_block_visual_width = num_cols * key_visual_size + (num_cols - 1) * key_visual_spacing
    key_block_visual_height = num_rows * key_visual_size + (num_rows - 1) * key_visual_spacing

    # Área interna visual do corpo do teclado (onde as teclas se encaixam)
    kb_inner_visual_x0 = kb_x0_center - line_width / 2 + line_width # Borda visual esquerda + espessura da linha
    kb_inner_visual_y0 = kb_y0_center - line_width / 2 + line_width # Borda visual superior + espessura da linha
    kb_inner_visual_width = kb_center_line_width - line_width # Largura da linha central - espessura da linha
    kb_inner_visual_height = kb_center_line_height - line_width # Altura da linha central - espessura da linha
    
    # Padding do bloco de teclas dentro da área interna visual do teclado
    key_block_padding_x = (kb_inner_visual_width - key_block_visual_width) / 2
    key_block_padding_y = (kb_inner_visual_height - key_block_visual_height) / 2

    # Coordenada visual do canto superior esquerdo da primeira tecla
    first_key_visual_x0 = kb_inner_visual_x0 + key_block_padding_x
    first_key_visual_y0 = kb_inner_visual_y0 + key_block_padding_y
    
    # Passo entre teclas (visual)
    key_step_x = key_visual_size + key_visual_spacing
    key_step_y = key_visual_size + key_visual_spacing

    # Desenha as teclas
    for row in range(num_rows):
        for col in range(num_cols):
            # Canto superior esquerdo visual da tecla atual
            key_tl_visual_x = first_key_visual_x0 + col * key_step_x
            key_tl_visual_y = first_key_visual_y0 + row * key_step_y

            # Coordenadas de desenho (centro da linha)
            k_x0 = key_tl_visual_x + line_width / 2
            k_y0 = key_tl_visual_y + line_width / 2
            k_x1 = k_x0 + key_draw_dim
            k_y1 = k_y0 + key_draw_dim
            
            draw.rectangle((k_x0, k_y0, k_x1, k_y1), outline=line_color, width=line_width)

    # Parâmetros do cabo (coordenadas para o centro da linha)
    cable_mid_x = kb_x0_center + kb_center_line_width / 2
    
    # Segmento vertical do cabo
    cable_v_start_y = kb_y0_center # Sai do centro da linha superior do teclado
    cable_v_end_y = kb_y0_center - 8 # Comprimento visual de 8px para cima
    
    # Segmento horizontal do cabo
    cable_h_start_x = cable_mid_x
    cable_h_end_x = cable_mid_x + 10 # Comprimento visual de 10px para a direita
    cable_h_y = cable_v_end_y

    # Desenha o cabo
    # Linha vertical
    draw.line(
        (cable_mid_x, cable_v_start_y, cable_mid_x, cable_v_end_y),
        fill=line_color,
        width=line_width
    )
    # Linha horizontal
    draw.line(
        (cable_h_start_x, cable_h_y, cable_h_end_x, cable_h_y),
        fill=line_color,
        width=line_width
    )
    
    return image

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
