import json

with open("bd.json", "r") as arq_json:
    dicionario = json.load(arq_json)
    for chave, dados in dicionario.items():
        print(chave + " " + str(dados))

dicionariodois = {
    "CHAVES": ["CHAVES DO 8", "26/01/2023", "RECEPÇÃO"],
    "QUICO": ["QUICO FLORES", "26/01/2022", "SALA"]
}

with open("bd1.json", "w") as json_file:
    json.dump(dicionariodois, json_file)
