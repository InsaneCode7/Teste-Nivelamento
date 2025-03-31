import pdfplumber
import pandas as pd
import zipfile

pdf_path = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
csv_path = "Rol_de_Procedimentos.csv"
zip_path = "Teste_{kayke}.zip"  

# Dicionário para substituir abreviações
descricao_substituicao = {
    "OD": "Procedimentos Odontológicos",
    "AMB": "Procedimentos Ambulatoriais"
}


def extrair_dados_do_pdf(pdf_path): 
    ''' Função para percorrer todo o pdfs extraindo os dados das tabelas '''
    
    dados_extraidos = []   
    with pdfplumber.open(pdf_path) as pdf: 
        for page in pdf.pages: 
            tables = page.extract_table() 
            if tables:  
                for row in tables: 
                    dados_extraidos.append(row) 
    return dados_extraidos

def salvar_como_csv(dados, csv_path): 
    ''' Função para transformar os dados em um arquivo csv e trocar as abreviações pelas descrições completas '''
    
    df = pd.DataFrame(dados) 
    df.columns = df.iloc[0]  
    df = df[1:].reset_index(drop=True)  

    df.replace({"OD": descricao_substituicao, "AMB": descricao_substituicao}, inplace=True) 
    df.to_csv(csv_path, index=False, encoding='utf-8') 

def compactar_csv(csv_path, zip_path):
    ''' Função para zipar o arquivo csv'''
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:  
        zipf.write(csv_path, arcname=csv_path) 

# Executando as funções
dados = extrair_dados_do_pdf(pdf_path)
salvar_como_csv(dados, csv_path)
compactar_csv(csv_path, zip_path)

print(f"Processo concluído! Arquivo salvo como {zip_path}")

