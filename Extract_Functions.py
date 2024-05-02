import requests
from bs4 import BeautifulSoup

# Dicionário de capitais e suas respectivas cidades metropolitanas
capitais_e_metropolitanas = {
    'AC': {'capital': 'Rio Branco', 'metropolitanas': ['Brasiléia', 'Senador Guiomard']},
    'AL': {'capital': 'Maceió', 'metropolitanas': ['Arapiraca', 'São Miguel dos Campos']},
    'AP': {'capital': 'Macapá', 'metropolitanas': ['Santana', 'Mazagão']},
    'AM': {'capital': 'Manaus', 'metropolitanas': ['Itacoatiara', 'Manacapuru']},
    'BA': {'capital': 'Salvador', 'metropolitanas': ['Camaçari', 'Lauro de Freitas']},
    'CE': {'capital': 'Fortaleza', 'metropolitanas': ['Caucaia', 'Maracanaú']},
    'DF': {'capital': 'Brasília', 'metropolitanas': ['Gama', 'Taguatinga']},
    'ES': {'capital': 'Vitória', 'metropolitanas': ['Vila Velha', 'Serra']},
    'GO': {'capital': 'Goiânia', 'metropolitanas': ['Aparecida de Goiânia', 'Anápolis']},
    'MA': {'capital': 'São Luís', 'metropolitanas': ['São José de Ribamar', 'Paço do Lumiar']},
    'MT': {'capital': 'Cuiabá', 'metropolitanas': ['Várzea Grande', 'Rondonópolis']},
    'MS': {'capital': 'Campo Grande', 'metropolitanas': ['Dourados', 'Três Lagoas']},
    'MG': {'capital': 'Belo Horizonte', 'metropolitanas': ['Contagem', 'Betim']},
    'PA': {'capital': 'Belém', 'metropolitanas': ['Ananindeua', 'Marituba']},
    'PB': {'capital': 'João Pessoa', 'metropolitanas': ['Santa Rita', 'Bayeux']},
    'PR': {'capital': 'Curitiba', 'metropolitanas': ['São José dos Pinhais', 'Colombo']},
    'PE': {'capital': 'Recife', 'metropolitanas': ['Jaboatão dos Guararapes', 'Olinda']},
    'PI': {'capital': 'Teresina', 'metropolitanas': ['Parnaíba', 'Picos']},
    'RJ': {'capital': 'Rio de Janeiro', 'metropolitanas': ['São Gonçalo', 'Duque de Caxias']},
    'RN': {'capital': 'Natal', 'metropolitanas': ['Mossoró', 'Parnamirim']},
    'RS': {'capital': 'Porto Alegre', 'metropolitanas': ['Canoas', 'Caxias do Sul']},
    'RO': {'capital': 'Porto Velho', 'metropolitanas': ['Ji-Paraná', 'Ariquemes']},
    'RR': {'capital': 'Boa Vista', 'metropolitanas': ['Alto Alegre', 'Caracaraí']},
    'SC': {'capital': 'Florianópolis', 'metropolitanas': ['Joinville', 'São José']},
    'SP': {'capital': 'São Paulo', 'metropolitanas': ['Guarulhos', 'São Bernardo do Campo']},
    'SE': {'capital': 'Aracaju', 'metropolitanas': ['Nossa Senhora do Socorro', 'São Cristóvão']},
    'TO': {'capital': 'Palmas', 'metropolitanas': ['Porto Nacional', 'Paraíso do Tocantins']}
}


def extrair_municipios_brasil():
    # Definindo a URL da página da Wikipedia que contém a lista de municípios do Brasil
    url = "https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil"
    # Fazendo uma requisição GET para obter o conteúdo HTML da página
    response = requests.get(url)
    

    # Verificando se a requisição foi bem-sucedida (status code 200)
    if response.status_code != 200:
        print("Falha ao acessar a página da Wikipedia.")
        return []
    
    # Criando um objeto BeautifulSoup para fazer o parsing do conteúdo HTML
    soup = BeautifulSoup(response.content, "html.parser")
    

    # Encontrando todas as listas de municípios divididas por letras do alfabeto
    listas_municipios = soup.find_all("ul")

    # Lista para armazenar os municípios e estados extraídos
    municipios_estados = []

    # Iterando sobre as listas de municípios
    for lista in listas_municipios:
        # Obtendo a letra correspondente à lista de municípios
        letra = lista.find_previous("span", class_="mw-headline")
        if letra:
            letra = letra.text.strip()
        
        # Extraindo os municípios e estados da lista
        itens_lista = lista.find_all("li")
        for item in itens_lista:
            # Dividindo o texto do item em município e estado
            municipio_estado = item.text.strip().split(" (")
            if len(municipio_estado) >= 2:  # Verifica se a lista contém pelo menos 2 elementos
                municipio = municipio_estado[0] # O primeiro elemento é o nome do município
                estado = municipio_estado[1][:-1]  # Removendo o parêntese fechado do estado

                localidade = "Interior" #Define a localidade Padrão para todos os municípios

                #Verifica se o município é uma capital ou cidade metropolitana
                for estado, info in capitais_e_metropolitanas.items():
                    capital = info["capital"]
                    metropolitanas = info['metropolitanas']
                    if municipio == capital:
                        localidade = "Capital"
                        break
                    elif municipio in metropolitanas:
                        localidade = 'Metropolitana'
                        break

                #Verifica se o Municipio é Brasília, pois atribui o Distrito Federal 
                if estado == 'DF' and municipio == 'Brasília':
                    localidade = "Distrito Federal"

                municipios_estados.append((municipio, estado, localidade)) # Adiciona à lista de municípios e estados
    
    return municipios_estados

if __name__ == "__main__":
    # Chamando a função extrair_municipios_brasil() e armazenando o resultado em municipios_brasil
    municipios_brasil = extrair_municipios_brasil()

    # Exibindo n municípios e estados do Brasil como exemplo
    print(municipios_brasil[:5569])  