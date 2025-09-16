# ATIVIDADE JSON 1

import json

dados_json = '{ "nome":"Ana", "idade":25, "cidade":"São Paulo" }'

dados_python = json.loads(dados_json)

print(dados_python["nome"])
print(dados_python["idade"])
print(dados_python["cidade"])
