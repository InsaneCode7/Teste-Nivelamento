from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS 


app = Flask(__name__)
CORS(app, resources={r"/buscar": {"origins": "http://localhost:8080"}})

# Carregar o arquivo CSV
df = pd.read_csv("C:/Users/kayke/OneDrive/Documentos/dados/Relatorio_cadop.csv", delimiter=";")



@app.route('/buscar', methods=['GET'])
def buscar():
    '''necessita que o usuário utilize "/buscar?termo=" na url'''
    termo = request.args.get('termo', default='', type=str)
    print(f"Termo de busca: {termo}")
    if not termo:
        return jsonify({"erro": "É necessário fornecer um termo de busca."}), 400

    # Convertendo a coluna 'Registro_ANS' para string
    df['Registro_ANS'] = df['Registro_ANS'].astype(str)
    
    # Filtrando os dados do CSV
    resultados = df[df['Registro_ANS'].str.contains(termo, case=False, na=False)]
    
    # Retornar os resultados como JSON
    return jsonify(resultados.to_dict(orient="records"))

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)
