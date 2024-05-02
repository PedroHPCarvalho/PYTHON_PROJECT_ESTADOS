import requests

def obter_estado():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados'
    response = requests.get(url)

    if response.status_code == 200:
        estados = response.json()
        return estados
    else:
        print("Falha ao obter os estados da API do IBGE.")
        return None
    
def obter_municipios():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'
    response = requests.get(url)

    if response.status_code == 200:
        municipios = response.json()
        return municipios
    else:
        print("Falha ao obter os estados da API do IBGE.")
        return None
    
def obter_distritos():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/distritos'
    response = requests.get(url)

    if response.status_code == 200:
        distritos = response.json()
        return distritos
    else:
        print("Falha ao obter os estados da API do IBGE.")
        return None











#TESTE AREA
estados = obter_estado()
municipios = obter_municipios()
distritos = obter_distritos()

# if municipios:
#     for municipio in municipios:
#         print(f"Município: {municipio["nome"]}")

if distritos:
    for distrito in distritos:
        print(f"Distritos: {distrito["nome"]}")

# if estados:
#     for estado in estados:
#         print(f"Estado: {estado['nome']} - Sigla: {estado['sigla']}")

