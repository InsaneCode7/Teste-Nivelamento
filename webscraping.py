import os
import time
import zipfile
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Configurar opções do navegador
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": os.getcwd(),  # Define o diretório de download
    "download.prompt_for_download": False,      # Impede que o Chrome exiba a janela de confirmação de download.
    "plugins.always_open_pdf_externally": True  # Evita abertura do PDF no navegador
})

# Inicializar o WebDriver
service = Service(ChromeDriverManager().install())
navegador= webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

try:
   
    navegador.get(url) #Requisição para acessar a pagina 
    time.sleep(5)  # Aguarda carregar a página

    #Aceita os cookies da página
    cookies = navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div[2]/button[3]')
    cookies.click()

    #Procura e baixa o primeiro arquivo
    anexo1 = navegador.find_element(By.XPATH, '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[1]/a[1]')
    anexo1.click()
    time.sleep(10) #Garante que o navegador não feche antes do download
    
    #Procura e baixa o segundo arquivo
    anexo2 = navegador.find_element(By.XPATH, '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[2]/a')
    anexo2.click()
    time.sleep(10) #Garante que o navegador não feche antes do download

    print("DOWNLOADS BEM SUCEDIDOS!!")

finally:
    navegador.quit() #Encerra o navegador 
    
    # Compactar os arquivos baixados
zip_filename = "anexos_kayke.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for file in os.listdir(os.getcwd()):
        if file.endswith(".pdf"):
            zipf.write(file, os.path.basename(file))
           
            print(f"Arquivo {file} adicionado ao ZIP.")
    

