import time
import pyautogui
from pynput import keyboard
from spellchecker import SpellChecker
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import openai
from threading import Thread
import os

# Configuración de OpenAI (necesitas una API key)
openai.api_key = os.getenv("Osk-proj-cHOEX_IpOuO42iMeDpYeJFQOFvTnlEo-D1D4Fl95XEL3VpXEIqTXkhxYqXwsuNxq8aEj0Na9-PT3BlbkFJLgvPGmmKoDWGwz-z5ORgSbxsqt20cDLVYK3ew7AKll_x2uqEDgro1blG7OdFfxkjP0au8u1R0A")  # Reemplaza con una variable de entorno

# Descargar recursos de NLTK (solo la primera vez)
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

print("Corrector automático en español iniciado...")
texto_actual = ""
spell = SpellChecker(language='es')
stop_words = set(stopwords.words('spanish'))
palabras_correctas = {"quiero", "hacerlo", "rapido"}  # Diccionario personalizado

# Función para corregir palabras mal escritas
def corregir_palabras(texto):
    palabras = word_tokenize(texto, language='spanish')
    texto_corregido = []
    
    for palabra in palabras:
        if palabra.lower() in stop_words or not palabra.isalpha() or palabra.lower() in palabras_correctas:
            texto_corregido.append(palabra)
        else:
            palabra_corregida = spell.correction(palabra)
            if palabra_corregida and palabra_corregida != palabra:
                texto_corregido.append(palabra_corregida)
            else:
                texto_corregido.append(palabra)
    
    return " ".join(texto_corregido)

# Función para corregir texto usando GPT
def corregir_con_ia(texto):
    try:
        respuesta = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Corrige el siguiente texto en español:\n{texto}\n\nTexto corregido:",
            max_tokens=500,
            temperature=0.5
        )
        return respuesta.choices[0].text.strip()
    except Exception as e:
        print(f"Error al conectar con OpenAI: {e}")
        return texto

# Función para escuchar las pulsaciones del teclado
def on_press(tecla):
    global texto_actual
    
    try:
        if tecla == keyboard.Key.space or tecla == keyboard.Key.enter:
            texto_corregido = corregir_palabras(texto_actual)
            if texto_actual != texto_corregido:
                for _ in range(len(texto_actual) + 1):  # +1 para borrar el espacio o Enter
                    pyautogui.press('backspace')
                time.sleep(0.1)
                pyautogui.write(texto_corregido)
                pyautogui.press('space' if tecla == keyboard.Key.space else 'enter')
            texto_actual = ""
        
        elif tecla == keyboard.Key.backspace:
            texto_actual = texto_actual[:-1]
        
        elif hasattr(tecla, 'char') and tecla.char is not None:
            texto_actual += tecla.char
    
    except Exception as e:
        print(f"Error: {e}")

# Iniciar la escucha del teclado en un hilo separado
def iniciar_corrector():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    # Iniciar el corrector en un hilo separado para no bloquear la ejecución
    corrector_thread = Thread(target=iniciar_corrector)
    corrector_thread.start()
    corrector_thread.join()