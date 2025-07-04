import pyautogui
from pynput import keyboard
import time

# Nome do arquivo onde as ações serão salvas
output_file = "recorded_actions.txt"

# Lista para armazenar as ações
actions = []

print("--- Gravador de Ações ---")
print("Pressione 's' para salvar a posição atual do mouse e adicionar um rótulo.")
print("Pressione 'esc' para parar a gravação e salvar o arquivo.")
print("-------------------------")

def on_press(key):
    try:
        if key.char == 's':
            x, y = pyautogui.position()
            label = input(f"[{x},{y}] Digite um rótulo para esta ação (ex: 'clicar_camada_texto', 'caixa_texto_nome_arquivo'): ")
            actions.append(f"POINT: {x},{y} LABEL: {label}")
            print(f"Ponto salvo: {x},{y} - {label}")
    except AttributeError:
        # Teclas especiais (como esc) não têm .char
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Para o listener
        return False

# Configura o listener de teclado
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Mantém o script rodando até 'esc' ser pressionado
listener.join()

# Salva as ações no arquivo
with open(output_file, "w") as f:
    for action in actions:
        f.write(action + "\n")

print(f"Gravação concluída. Ações salvas em {output_file}")
