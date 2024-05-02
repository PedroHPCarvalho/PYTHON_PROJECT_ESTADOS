import requests
from bs4 import BeautifulSoup

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
                municipios_estados.append((municipio, estado)) # Adiciona à lista de municípios e estados
    
    return municipios_estados

if __name__ == "__main__":
    # Chamando a função extrair_municipios_brasil() e armazenando o resultado em municipios_brasil
    municipios_brasil = extrair_municipios_brasil()

    # Exibindo n municípios e estados do Brasil como exemplo
    print(municipios_brasil[:5569])  