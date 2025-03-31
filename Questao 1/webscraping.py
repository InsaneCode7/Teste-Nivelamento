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
    "download.default_directory": os.getcwd(),  
    "download.prompt_for_download": False,      
    "plugins.always_open_pdf_externally": True  
})

# Inicializar o WebDriver
service = Service(ChromeDriverManager().install())
navegador= webdriver.Chrome(service=service, options=chrome_options)

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

#Script para abrir o navegador baixar os arquivos necessários e fechar o navegador 
try:
  
    navegador.get(url)  
    time.sleep(5) 

    
    cookies = navegador.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div/div[2]/button[3]')
    cookies.click()

   
    anexo1 = navegador.find_element(By.XPATH, '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[1]/a[1]')
    anexo1.click()
    time.sleep(10) 
    
    
    anexo2 = navegador.find_element(By.XPATH, '//*[@id="cfec435d-6921-461f-b85a-b425bc3cb4a5"]/div/ol/li[2]/a')
    anexo2.click()
    time.sleep(10) 

    print("DOWNLOADS BEM SUCEDIDOS!!")

finally:
    navegador.quit() 
    
    # Compactar os arquivos baixados
zip_filename = "anexos_kayke.zip"
with zipfile.ZipFile(zip_filename, "w") as zipf:
    for file in os.listdir(os.getcwd()):
        if file.endswith(".pdf"):
            zipf.write(file, os.path.basename(file))
           
            print(f"Arquivo {file} adicionado ao ZIP.")
    

