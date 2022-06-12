import requests
import json
from time import sleep

dispositivos = [
    {
        "id": 1,
        "cidade": "Uberlandia",
        "bairro": "Jardim Karaíba",
        "estado": "MG",
        "rua": "Alameda Marília de Dirceu",
        "latitude": "-23.564",
        "longitude": "-46.654",
        "mapa": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3773.886442456692!2d-48.2728233995356!3d-18.936419895463242!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94a445185efb2751%3A0xdd6b545a66b2a96f!2sAlameda%20Mar%C3%ADlia%20de%20Dirceu%2C%20230%20-%20Jardim%20Kara%C3%ADba%2C%20Uberl%C3%A2ndia%20-%20MG%2C%2038411-276!5e0!3m2!1spt-BR!2sbr!4v1654982050576!5m2!1spt-BR!2sbr"
    },
    {
        "id": 2,
        "cidade": "Uberaba",
        "bairro": "Nossa Sra. da Abadia",
        "estado": "MG",
        "rua": "Castro Alves",
        "latitude": "-23.564",
        "longitude": "-46.654",
        "mapa": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3755.0026744051083!2d-47.92992238554853!3d-19.755040986701978!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94bad025c05b7423%3A0xb60a9d45ec1191ba!2sR.%20Castro%20Alves%2C%20231%20-%20Nossa%20Sra.%20da%20Abadia%2C%20Uberaba%20-%20MG%2C%2038025-380!5e0!3m2!1spt-BR!2sbr!4v1654982262527!5m2!1spt-BR!2sbr"
    },
    {
        "id": 3,
        "cidade": "PLanura",
        "bairro": "",
        "estado": "MG",
        "rua": "Tupaciguara",
        "latitude": "-23.564",
        "longitude": "-46.654",
        "mapa": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3745.9018132400797!2d-48.70627788554117!3d-20.138143486487532!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x94bb5f94a01b9139%3A0x4b6bc50501c04a2d!2sR.%20Tupaciguara%2C%20380-394%2C%20Planura%20-%20MG%2C%2038220-000!5e0!3m2!1spt-BR!2sbr!4v1654982389362!5m2!1spt-BR!2sbr"
    }, 
    {
        "id": 5,
        "cidade": "Campo grande",
        "bairro": "Guanandi",
        "estado": "MS",
        "rua": "Gabriel Cardoso Ramalho",
        "latitude": "-23.564",
        "longitude": "-46.654",
        "mapa": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3737.0979829371827!2d-54.6484385855341!3d-20.502209186285945!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9486e5d1c230c1a3%3A0x97db1ed2ff44ae5!2sR.%20Gabriel%20Cardoso%20Ramalho%2C%20555-467%20-%20Guanandi%2C%20Campo%20Grande%20-%20MS%2C%2079086-200!5e0!3m2!1spt-BR!2sbr!4v1654982522852!5m2!1spt-BR!2sbr"
    },{
        "id": 6,
        "cidade": "Campo grande",
        "bairro": "Guanandi",
        "estado": "MS",
        "rua": "Gabriel Cardoso Ramalho",
        "latitude": "-23.564",
        "longitude": "-46.654",
        "mapa": "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3737.0979829371827!2d-54.6484385855341!3d-20.502209186285945!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x9486e5d1c230c1a3%3A0x97db1ed2ff44ae5!2sR.%20Gabriel%20Cardoso%20Ramalho%2C%20555-467%20-%20Guanandi%2C%20Campo%20Grande%20-%20MS%2C%2079086-200!5e0!3m2!1spt-BR!2sbr!4v1654982522852!5m2!1spt-BR!2sbr"
    },

]


def readValues():
    file = open("./sensor.sor", "r")
    lines = file.readlines()
    file.close()
    return lines


def parserFile():
    lines = readValues()
    ret = []
    for line in lines:
        ret.append(line.split(";"))
    return ret


def completeData(dados):
    ret = []
    for i in dados:
        for j in dispositivos:
            if str(i[0]) == str(j["id"]):
                ret.append(
                    {
                        "id": i[0],
                        "cidade": j["cidade"],
                        "bairro": j["bairro"],
                        "estado": j["estado"],
                        "rua": j["rua"],
                        "distancia": i[1],
                        "perda": float(i[2]),
                        "latitude": j["latitude"],
                        "longitude": j["longitude"],
                        "mapa": j["mapa"]
                    }
                )
    return ret

def insert():
        dados = completeData(parserFile())
        for i in dados:
            requests.post("http://localhost:5000/add", json=i)

def main():
    #insert()
    while True:
        dados = completeData(parserFile())
        for i in dados:
            requests.put("http://localhost:5000/update", json=i)
        print("executou")
        sleep(100)
    
main()
