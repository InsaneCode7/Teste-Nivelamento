import pdfplumber
import pandas as pd
import zipfile

pdf_path = "anexo1.pdf"
csv_path = "Rol_de_Procedimentos.csv"
zip_path = "Teste_{kayke}.zip"  

# Dicionário para substituir abreviações
descricao_substituicao = {
    "OD": "Procedimentos Odontológicos",
    "AMB": "Procedimentos Ambulatoriais"
}


def extrair_dados_do_pdf(pdf_path): # Função para extrair dados das tabela presentes no pdf 
    
    ''' tirar todos os comentarios e colocar 1 comentario so aqui sobre a função '''
    dados_extraidos = []   # Lista vazia para armazenar os dados que serão extraidos 
    with pdfplumber.open(pdf_path) as pdf: # Abre o pdf 
        for page in pdf.pages: # Percorre as paginas do pdf
            tables = page.extract_table() # Tenta extrair tabelas dessas páginas
            if tables:  # Se houver tabelas então:
                for row in tables: # Percorre as linhas das tabelas 
                    dados_extraidos.append(row) # Adiciona os dados extraídos na lista criada inicialmente 
    return dados_extraidos

def salvar_como_csv(dados, csv_path): # Função para transformar os dados em um arquivo csv
    df = pd.DataFrame(dados) # Transforma os dados em um DataFrame
    df.columns = df.iloc[0]  # Define a primeira linha como cabeçalho
    df = df[1:].reset_index(drop=True)  # Remove a linha de cabeçalho duplicada

    df.replace({"OD": descricao_substituicao, "AMB": descricao_substituicao}, inplace=True) # Substitue as abreviações pelos valores citados no dicionário anteriormente 
    
    df.to_csv(csv_path, index=False, encoding='utf-8') # Conversão do DataFrame para um arquivo csv

def compactar_csv(csv_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:  # Cria um novo zip e diminue o tamanho do csv dentro do zip
        zipf.write(csv_path, arcname=csv_path)  # Adiciona o csv dentro do zip, mantendo seu nome original 

# Executando as funções
dados = extrair_dados_do_pdf(pdf_path)
salvar_como_csv(dados, csv_path)
compactar_csv(csv_path, zip_path)

print(f"Processo concluído! Arquivo salvo como {zip_path}")

