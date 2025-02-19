import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def contar_faixas_etarias(idades):
    faixas = {
        "0-18": 0, "19-23": 0, "24-28": 0, "29-33": 0, 
        "34-38": 0, "39-43": 0, "44-48": 0, "49-53": 0, 
        "54-58": 0, "59+": 0
    }
    for idade in idades:
        if 0 <= idade <= 18:
            faixas["0-18"] += 1
        elif 19 <= idade <= 23:
            faixas["19-23"] += 1
        elif 24 <= idade <= 28:
            faixas["24-28"] += 1
        elif 29 <= idade <= 33:
            faixas["29-33"] += 1
        elif 34 <= idade <= 38:
            faixas["34-38"] += 1
        elif 39 <= idade <= 43:
            faixas["39-43"] += 1
        elif 44 <= idade <= 48:
            faixas["44-48"] += 1
        elif 49 <= idade <= 53:
            faixas["49-53"] += 1
        elif 54 <= idade <= 58:
            faixas["54-58"] += 1
        else:
            faixas["59+"] += 1
    return faixas

@app.route('/contar-idades', methods=['POST'])
def contar_idades():
    data = request.json
    idades = data.get("idades", [])

    if not isinstance(idades, list) or not all(isinstance(i, int) for i in idades):
        return jsonify({"erro": "Envie uma lista de idades inteiras"}), 400

    resultado = contar_faixas_etarias(idades)
    resultado["Quantidade de Vidas"] = sum(resultado.values())

    return jsonify(resultado)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=False)
