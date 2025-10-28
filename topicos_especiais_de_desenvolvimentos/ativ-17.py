import json
import math
import random
from datetime import date

alunos = {
    0:{"nome": "zack", "nota1": random.randint(0, 10), "nota2": random.randint(0, 10), "data_avaliacao": "", "media": 0, "aprovado": "?"}, 
    1:{"nome": "maria", "nota1": random.randint(0, 10), "nota2": random.randint(0, 10), "data_avaliacao": "", "media": 0, "aprovado": "?"},
    2:{"nome": "carlos", "nota1": random.randint(0, 10), "nota2": random.randint(0, 10), "data_avaliacao": "", "media": 0, "aprovado": "?"},
    3:{"nome": "juvenal", "nota1": random.randint(0, 10), "nota2": random.randint(0, 10), "data_avaliacao": "", "media": 0, "aprovado": "?"},
    4:{"nome": "clara", "nota1": random.randint(0, 10), "nota2": random.randint(0, 10), "data_avaliacao": "", "media": 0, "aprovado": "?"},
    5:{"nome": "julia", "nota1": random.randint(0, 10), "nota2": random.randint(0, 10), "data_avaliacao": "", "media": 0, "aprovado": "?"}
    }

for i in range(0, 6):
    media = (alunos[i]["nota1"] + alunos[i]["nota2"]) / 2
    media = math.ceil(media)
    alunos[i]["media"] = media


    if media > 6.9:
        alunos[i]["data_avaliacao"] = f"{date.today()}"
        alunos[i]["aprovado"] = True
    else:
        alunos[i]["data_avaliacao"] = f"{date.today()}"
        alunos[i]["aprovado"] = False





alunos_json = json.dumps(alunos, indent=1)
print("\n"*2)
print(alunos_json)
print("\n"*3)

