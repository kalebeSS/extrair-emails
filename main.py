from selenium import webdriver
import time
import pyautogui
import pyperclip

#importa a função extrair_emails do outro arquivo
from extratorDeEmail import extrair_emails

# URL do site de exemplo, ou pode ser varios dentro da lista.
urls = ["http://www.ndk-tour.com.br"]

for i in urls:
	
	# Inicializa o driver do navegador / falta o caminho do webdriver
	driver = webdriver.Chrome()

	# Abre a URL no navegador da lista
	driver.get(i)

	# Aguarda um pouco para garantir que a página seja carregada completamente
	time.sleep(2)

	pyautogui.hotkey("ctrl", "a")
	pyautogui.hotkey("ctrl", "c")

	# Aguarda um pouco para ver o texto selecionado
	time.sleep(2)

	# Fecha o navegador
	driver.quit()

	text = pyperclip.paste()

	#cria uma variavel que utiliza a função extrair_emails
	emails = extrair_emails(text)
	print(emails)