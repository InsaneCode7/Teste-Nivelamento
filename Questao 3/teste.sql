--3.3 Criação das tabelas

CREATE table operadora_teste(

REGISTRO_OPERADORA VARCHAR (6) PRIMARY KEY,
CNPJ VARCHAR (14),
Razao_Social VARCHAR (140),
Nome_Fantasia VARCHAR (140),
Modalidade VARCHAR (140),
Logradouro VARCHAR (40),
Número VARCHAR (20),
Complemento VARCHAR (40),
Bairro VARCHAR  (30),
Cidade VARCHAR  (30),
UF CHAR (2),
CEP CHAR (8),
DDD CHAR (4),
Telefone VARCHAR (20),
Fax VARCHAR (20),
Endereco_eletronico VARCHAR (255),
Representante VARCHAR (50),
Cargo_Representante VARCHAR(40),
Regiao_de_Comercializacao CHAR  (1),
data_registro_ans DATE
);

CREATE table DADOS_TESTE (
DATA_DADO DATE,
REG_ANS VARCHAR (6),
CD_CONTA_CONTABIL NUMERIC (10, 0),
DESCRICAO VARCHAR (150),
VL_SALDO_INICIAL NUMERIC (20, 2),
VL_SALDO_FINAL NUMERIC (20, 2)
);

--3.4 Importando arquivos csv

--Preenchendo dados com informações do CSV DADOS
COPY DADOS_TESTE (DATA_DADO, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL)
FROM '/home/kayke/Área de Trabalho/dados2324/1T2023V2.csv' --Substituir o nome do arquivo para cadastrar os dados de todos os trimestres Ex: 2T2023, 3T2023 e assim por diante.
WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8');

-- Preenchendo dados com informações do CSV OPERADORA
COPY operadora_teste --(REGISTRO_OPERADORA, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Número, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico , Representante, Cargo_Representante, Regiao_de_Comercializacao)
FROM '/home/kayke/Área de Trabalho/dados2324/Relatorio_cadop.csv'
WITH (FORMAT csv, DELIMITER ';', HEADER true, ENCODING 'UTF8', NULL '');

--3.5 Listando as 10 operadoras com maiores despesas no ultimo trimestre e as 10 com maiores despesas no ano.

-- TOP 10 MAIORES DESPESAS NOS ULTIMOS 3 MESES POR OPERADORA
SELECT 
    o.Razao_Social,
    SUM(d.VL_SALDO_INICIAL - d.VL_SALDO_FINAL) AS despesa_total
FROM 
    operadora o
JOIN 
    dados d ON o.REGISTRO_OPERADORA = d.REG_ANS
WHERE 
    UPPER(d.DESCRICAO) LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND d.DATA_DADO BETWEEN '2024-10-01' AND '2024-12-31'  -- Filtra para o último trimestre
GROUP BY 
    o.Razao_Social
ORDER BY 
    despesa_total DESC
LIMIT 10;

-- TOP 10 DESPESAS POR OPERADORA NO ANO
SELECT 
    o.Razao_Social,
    SUM(d.VL_SALDO_INICIAL - d.VL_SALDO_FINAL) AS despesa_total
FROM 
    operadora o
JOIN 
    dados d ON o.REGISTRO_OPERADORA = d.REG_ANS
WHERE 
    UPPER(d.DESCRICAO) LIKE '%EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR%'
    AND d.DATA_DADO >= '2024-01-01' -- Filtra para o último trimestre
GROUP BY 
    o.Razao_Social
ORDER BY 
    despesa_total DESC
LIMIT 10;