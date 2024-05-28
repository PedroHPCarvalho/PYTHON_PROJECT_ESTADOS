import requests
import openpyxl

capitais = [
    {'UF': 'RO', 'Capital': 'Porto Velho'},
    {'UF': 'AC', 'Capital': 'Rio Branco'},
    {'UF': 'AM', 'Capital': 'Manaus'},
    {'UF': 'RR', 'Capital': 'Boa Vista'},
    {'UF': 'PA', 'Capital': 'Belém'},
    {'UF': 'AP', 'Capital': 'Macapá'},
    {'UF': 'TO', 'Capital': 'Palmas'},
    {'UF': 'MA', 'Capital': 'São Luís'},
    {'UF': 'PI', 'Capital': 'Teresina'},
    {'UF': 'CE', 'Capital': 'Fortaleza'},
    {'UF': 'RN', 'Capital': 'Natal'},
    {'UF': 'PB', 'Capital': 'João Pessoa'},
    {'UF': 'PE', 'Capital': 'Recife'},
    {'UF': 'AL', 'Capital': 'Maceió'},
    {'UF': 'SE', 'Capital': 'Aracaju'},
    {'UF': 'BA', 'Capital': 'Salvador'},
    {'UF': 'MG', 'Capital': 'Belo Horizonte'},
    {'UF': 'ES', 'Capital': 'Vitória'},
    {'UF': 'RJ', 'Capital': 'Rio de Janeiro'},
    {'UF': 'SP', 'Capital': 'São Paulo'},
    {'UF': 'PR', 'Capital': 'Curitiba'},
    {'UF': 'SC', 'Capital': 'Florianópolis'},
    {'UF': 'RS', 'Capital': 'Porto Alegre'},
    {'UF': 'MS', 'Capital': 'Campo Grande'},
    {'UF': 'MT', 'Capital': 'Cuiabá'},
    {'UF': 'GO', 'Capital': 'Goiânia'},
    {'UF': 'DF', 'Capital': 'Brasília'}
]

litoral = [
    {"UF": "RJ", "Litoral": "Rio de Janeiro"},
    {"UF": "BA", "Litoral": "Salvador"},
    {"UF": "CE", "Litoral": "Fortaleza"},
    {"UF": "PE", "Litoral": "Recife"},
    {"UF": "MA", "Litoral": "São Luís"},
    {"UF": "RJ", "Litoral": "São Gonçalo"},
    {"UF": "AL", "Litoral": "Maceió"},
    {"UF": "RJ", "Litoral": "Duque de Caxias"},
    {"UF": "RN", "Litoral": "Natal"},
    {"UF": "PB", "Litoral": "João Pessoa"},
    {"UF": "PE", "Litoral": "Jaboatão dos Guararapes"},
    {"UF": "SE", "Litoral": "Aracaju"},
    {"UF": "ES", "Litoral": "Serra"},
    {"UF": "RJ", "Litoral": "Niterói"},
    {"UF": "RJ", "Litoral": "Campos dos Goytacazes"},
    {"UF": "AP", "Litoral": "Macapá"},
    {"UF": "SC", "Litoral": "Florianópolis"},
    {"UF": "ES", "Litoral": "Vila Velha"},
    {"UF": "SP", "Litoral": "Santos"},
    {"UF": "PE", "Litoral": "Olinda"},
    {"UF": "SP", "Litoral": "São Vicente"},
    {"UF": "ES", "Litoral": "Vitória"},
    {"UF": "CE", "Litoral": "Caucaia"},
    {"UF": "PE", "Litoral": "Paulista"},
    {"UF": "SP", "Litoral": "Praia Grande"},
    {"UF": "SP", "Litoral": "Guarujá"},
    {"UF": "BA", "Litoral": "Camaçari"},
    {"UF": "RN", "Litoral": "Parnamirim"},
    {"UF": "RJ", "Litoral": "Macaé"},
    {"UF": "RJ", "Litoral": "Magé"},
    {"UF": "RJ", "Litoral": "Itaboraí"},
    {"UF": "RJ", "Litoral": "Cabo Frio"},
    {"UF": "SC", "Litoral": "Itajaí"},
    {"UF": "RS", "Litoral": "Rio Grande"},
    {"UF": "PE", "Litoral": "Cabo de Santo Agostinho"},
    {"UF": "RJ", "Litoral": "Angra dos Reis"},
    {"UF": "BA", "Litoral": "Lauro de Freitas"},
    {"UF": "MA", "Litoral": "São José de Ribamar"},
    {"UF": "ES", "Litoral": "Linhares"},
    {"UF": "SC", "Litoral": "Palhoça"},
    {"UF": "BA", "Litoral": "Ilhéus"},
    {"UF": "RJ", "Litoral": "Maricá"},
    {"UF": "PR", "Litoral": "Paranaguá"},
    {"UF": "PI", "Litoral": "Parnaíba"},
    {"UF": "RJ", "Litoral": "Rio das Ostras"},
    {"UF": "BA", "Litoral": "Porto Seguro"},
    {"UF": "SC", "Litoral": "Balneário Camboriú"},
    {"UF": "PB", "Litoral": "Santa Rita"},
    {"UF": "RJ", "Litoral": "Itaguaí"},
    {"UF": "RJ", "Litoral": "Araruama"},
    {"UF": "ES", "Litoral": "São Mateus"},
    {"UF": "CE", "Litoral": "Itapipoca"},
    {"UF": "PA", "Litoral": "Bragança"},
    {"UF": "ES", "Litoral": "Guarapari"},
    {"UF": "MA", "Litoral": "Paço do Lumiar"},
    {"UF": "SP", "Litoral": "Caraguatatuba"},
    {"UF": "PE", "Litoral": "Igarassu"},
    {"UF": "SP", "Litoral": "Itanhaém"},
    {"UF": "ES", "Litoral": "Aracruz"},
    {"UF": "BA", "Litoral": "Valença"},
    {"UF": "PE", "Litoral": "Ipojuca"},
    {"UF": "SP", "Litoral": "Ubatuba"},
    {"UF": "RJ", "Litoral": "Saquarema"},
    {"UF": "SP", "Litoral": "São Sebastião"},
    {"UF": "SC", "Litoral": "Navegantes"},
    {"UF": "CE", "Litoral": "Aquiraz"},
    {"UF": "PE", "Litoral": "Goiana"},
    {"UF": "CE", "Litoral": "Aracati"},
    {"UF": "RN", "Litoral": "Ceará-Mirim"},
    {"UF": "CE", "Litoral": "Cascavel"},
    {"UF": "SE", "Litoral": "Estância"},
    {"UF": "SP", "Litoral": "Peruíbe"},
    {"UF": "SC", "Litoral": "Araranguá"},
    {"UF": "PB", "Litoral": "Cabedelo"},
    {"UF": "SC", "Litoral": "Itapema"},
    {"UF": "CE", "Litoral": "Camocim"},
    {"UF": "SP", "Litoral": "Bertioga"},
    {"UF": "CE", "Litoral": "Acaraú"},
    {"UF": "MA", "Litoral": "Barreirinhas"},
    {"UF": "PA", "Litoral": "Viseu"},
    {"UF": "RJ", "Litoral": "Guapimirim"},
    {"UF": "MA", "Litoral": "Tutóia"},
    {"UF": "AL", "Litoral": "Coruripe"},
    {"UF": "SP", "Litoral": "Mongaguá"},
    {"UF": "CE", "Litoral": "Trairi"},
    {"UF": "PA", "Litoral": "Vigia"},
    {"UF": "CE", "Litoral": "Beberibe"},
    {"UF": "RS", "Litoral": "Capão da Canoa"},
    {"UF": "SC", "Litoral": "São Francisco do Sul"},
    {"UF": "AL", "Litoral": "Marechal Deodoro"},
    {"UF": "RS", "Litoral": "Tramandaí"},
    {"UF": "RN", "Litoral": "São Gonçalo do Amarante"},
    {"UF": "BA", "Litoral": "Mata de São João"},
    {"UF": "MA", "Litoral": "Araioses"},
    {"UF": "PA", "Litoral": "Augusto Corrêa"},
    {"UF": "RS", "Litoral": "Osório"},
    {"UF": "PE", "Litoral": "Sirinhaém"},
    {"UF": "SC", "Litoral": "Laguna"},
    {"UF": "SC", "Litoral": "Imbituba"},
    {"UF": "RJ", "Litoral": "Mangaratiba"},
    {"UF": "RJ", "Litoral": "Casimiro de Abreu"},
    {"UF": "CE", "Litoral": "Amontada"},
    {"UF": "BA", "Litoral": "Nova Viçosa"},
    {"UF": "BA", "Litoral": "Vera Cruz"},
    {"UF": "RJ", "Litoral": "Paraty"},
    {"UF": "MA", "Litoral": "Rosário"},
    {"UF": "PE", "Litoral": "Barreiros"},
    {"UF": "RJ", "Litoral": "São Francisco de Itabapoana"},
    {"UF": "CE", "Litoral": "Itarema"},
    {"UF": "BA", "Litoral": "Entre Rios"},
    {"UF": "BA", "Litoral": "Mucuri"},
    {"UF": "PA", "Litoral": "Salinópolis"},
    {"UF": "RJ", "Litoral": "Armação dos Búzios"},
    {"UF": "PA", "Litoral": "Curuçá"},
    {"UF": "RS", "Litoral": "Torres"},
    {"UF": "ES", "Litoral": "Marataízes"},
    {"UF": "SC", "Litoral": "Tijucas"},
    {"UF": "SC", "Litoral": "Araquari"},
    {"UF": "PB", "Litoral": "Santa Rita"},
    {"UF": "BA", "Litoral": "Esplanada"},
    {"UF": "PR", "Litoral": "Guaratuba"},
    {"UF": "RJ", "Litoral": "São João da Barra"},
    {"UF": "MA", "Litoral": "Turiaçu"},
    {"UF": "BA", "Litoral": "Camamu"},
    {"UF": "CE", "Litoral": "Paracuru"},
    {"UF": "SP", "Litoral": "Ilhabela"},
    {"UF": "PR", "Litoral": "Matinhos"},
    {"UF": "SE", "Litoral": "Itaporanga d'Ajuda"},
    {"UF": "ES", "Litoral": "Itapemirim"},
    {"UF": "RN", "Litoral": "Canguaretama"},
    {"UF": "RN", "Litoral": "Touros"},
    {"UF": "CE", "Litoral": "Paraipaba"},
    {"UF": "AL", "Litoral": "Maragogi"},
    {"UF": "MA", "Litoral": "Cururupu"},
    {"UF": "SC", "Litoral": "Penha"},
    {"UF": "RN", "Litoral": "Macau"},
    {"UF": "BA", "Litoral": "Canavieiras"},
    {"UF": "ES", "Litoral": "Conceição da Barra"},
    {"UF": "PA", "Litoral": "Tracuateua"},
    {"UF": "SP", "Litoral": "Iguape"},
    {"UF": "MA", "Litoral": "Raposa"},
    {"UF": "SE", "Litoral": "Barra dos Coqueiros"},
    {"UF": "RJ", "Litoral": "Arraial do Cabo"},
    {"UF": "PI", "Litoral": "Luís Correia"},
    {"UF": "MA", "Litoral": "Santa Vitória do Palmar"},
    {"UF": "PA", "Litoral": "Maracanã"},
    {"UF": "ES", "Litoral": "Anchieta"},
    {"UF": "SC", "Litoral": "Barra Velha"},
    {"UF": "MA", "Litoral": "Humberto de Campos"},
    {"UF": "BA", "Litoral": "Ituberá"},
    {"UF": "RN", "Litoral": "Extremoz"},
    {"UF": "PA", "Litoral": "Marapanim"},
    {"UF": "BA", "Litoral": "Itacaré"},
    {"UF": "BA", "Litoral": "Prado"},
    {"UF": "BA", "Litoral": "Santa Cruz Cabrália"},
    {"UF": "RN", "Litoral": "Areia Branca"},
    {"UF": "RS", "Litoral": "Nísia Floresta"},
    {"UF": "PR", "Litoral": "Pontal do Paraná"},
    {"UF": "AP", "Litoral": "Oiapoque"},
    {"UF": "MA", "Litoral": "Icatu"},
    {"UF": "PE", "Litoral": "Ilha de Itamaracá"},
    {"UF": "PB", "Litoral": "Conde"},
    {"UF": "PA", "Litoral": "Soure"},
    {"UF": "CE", "Litoral": "Cruz"},
    {"UF": "RJ", "Litoral": "Quissamã"},
    {"UF": "PB", "Litoral": "Rio Tinto"},
    {"UF": "MA", "Litoral": "Carutapera"},
    {"UF": "PA", "Litoral": "Salvaterra"},
    {"UF": "PA", "Litoral": "Chaves"},
    {"UF": "PE", "Litoral": "Tamandaré"},
    {"UF": "BA", "Litoral": "Belmonte"},
    {"UF": "SC", "Litoral": "Balneário Piçarras"},
    {"UF": "SC", "Litoral": "Garopaba"},
    {"UF": "PA", "Litoral": "São João de Pirabas"},
    {"UF": "RS", "Litoral": "Imbé"},
    {"UF": "BA", "Litoral": "Alcobaça"},
    {"UF": "MA", "Litoral": "Alcântara"},
    {"UF": "BA", "Litoral": "Caravelas"},
    {"UF": "ES", "Litoral": "Piúma"},
    {"UF": "ES", "Litoral": "Fundão"},
    {"UF": "SC", "Litoral": "Porto Belo"},
    {"UF": "PE", "Litoral": "São José da Coroa Grande"},
    {"UF": "MA", "Litoral": "Bequimão"},
    {"UF": "MA", "Litoral": "São João Batista"},
    {"UF": "SC", "Litoral": "Itapoá"},
    {"UF": "BA", "Litoral": "Maraú"},
    {"UF": "BA", "Litoral": "Uruçuca"},
    {"UF": "MA", "Litoral": "Cândido Mendes"},
    {"UF": "SC", "Litoral": "Jaguaruna"},
    {"UF": "CE", "Litoral": "Icapuí"},
    {"UF": "CE", "Litoral": "Jijoca de Jericoacoara"},
    {"UF": "SC", "Litoral": "Bombinhas"},
    {"UF": "PB", "Litoral": "Pitimbu"},
    {"UF": "BA", "Litoral": "Una"},
    {"UF": "BA", "Litoral": "Jaguaripe"},
    {"UF": "MA", "Litoral": "Bacuri"},
    {"UF": "BA", "Litoral": "Cairu"},
    {"UF": "PA", "Litoral": "São Caetano de Odivelas"},
    {"UF": "AL", "Litoral": "Piaçabuçu"},
    {"UF": "MA", "Litoral": "Apicum-Açu"},
    {"UF": "MA", "Litoral": "Bacabeira"},
    {"UF": "CE", "Litoral": "Fortim"},
    {"UF": "RS", "Litoral": "Xangri-Lá"},
    {"UF": "RJ", "Litoral": "Carapebus"},
    {"UF": "RS", "Litoral": "Cidreira"},
    {"UF": "MA", "Litoral": "Paulino Neves"},
    {"UF": "AL", "Litoral": "Barra de Santo Antônio"},
    {"UF": "MA", "Litoral": "Santo Amaro do Maranhão"},
    {"UF": "RN", "Litoral": "Guamaré"},
    {"UF": "MA", "Litoral": "Primeira Cruz"},
    {"UF": "AL", "Litoral": "Passo de Camaragibe"},
    {"UF": "CE", "Litoral": "Barroquinha"},
    {"UF": "SC", "Litoral": "Governador Celso Ramos"},
    {"UF": "CE", "Litoral": "Pacatuba"},
    {"UF": "RN", "Litoral": "Tibau do Sul"},
    {"UF": "RS", "Litoral": "Balneário Pinhal"},
    {"UF": "BA", "Litoral": "Nilo Peçanha"},
    {"UF": "BA", "Litoral": "Quatipuru"},
    {"UF": "BA", "Litoral": "Igrapiúna"},
    {"UF": "AL", "Litoral": "Paripueira"},
    {"UF": "PB", "Litoral": "Lucena"},
    {"UF": "SC", "Litoral": "Balneário Arroio do Silva"},
    {"UF": "RS", "Litoral": "Mostardas"},
    {"UF": "SC", "Litoral": "Balneário Rincão"},
    {"UF": "SP", "Litoral": "Cananéia"},
    {"UF": "RN", "Litoral": "Maxaranguape"},
    {"UF": "MA", "Litoral": "Axixá"},
    {"UF": "PA", "Litoral": "Colares"},
    {"UF": "MA", "Litoral": "Guimarães"},
    {"UF": "MA", "Litoral": "Godofredo Viana"},
    {"UF": "AL", "Litoral": "Jequiá da Praia"},
    {"UF": "ES", "Litoral": "Presidente Kennedy"},
    {"UF": "RS", "Litoral": "Palmares do Sul"},
    {"UF": "RS", "Litoral": "Terra de Areia"},
    {"UF": "MA", "Litoral": "Cajapió"},
    {"UF": "SP", "Litoral": "Ilha Comprida"},
    {"UF": "AP", "Litoral": "Calçoene"},
    {"UF": "SC", "Litoral": "Balneário Gaivota"},
    {"UF": "RN", "Litoral": "Rio do Fogo"},
    {"UF": "SC", "Litoral": "Balneário Barra do Sul"},
    {"UF": "RN", "Litoral": "Jandaíra"},
    {"UF": "MA", "Litoral": "Cedral"},
    {"UF": "RN", "Litoral": "Grossos"},
    {"UF": "RN", "Litoral": "São Miguel do Gostoso"},
    {"UF": "MA", "Litoral": "Serrano do Maranhão"},
    {"UF": "RS", "Litoral": "Arroio do Sal"},
    {"UF": "RJ", "Litoral": "Ilha Grande"},
    {"UF": "SE", "Litoral": "Pirambu"},
    {"UF": "RN", "Litoral": "Baía Formosa"},
    {"UF": "AP", "Litoral": "Amapá"},
    {"UF": "PB", "Litoral": "Baía da Traição"},
    {"UF": "SC", "Litoral": "Passo de Torres"},
    {"UF": "PB", "Litoral": "Marcação"},
    {"UF": "PA", "Litoral": "Magalhães Barata"},
    {"UF": "PB", "Litoral": "Mataraca"},
    {"UF": "AL", "Litoral": "Japaratinga"},
    {"UF": "AL", "Litoral": "Barra de São Miguel"},
    {"UF": "SE", "Litoral": "Brejo Grande"},
    {"UF": "AL", "Litoral": "São Miguel dos Milagres"},
    {"UF": "AL", "Litoral": "Porto de Pedras"},
    {"UF": "PI", "Litoral": "Cajueiro da Praia"},
    {"UF": "PR", "Litoral": "Guaraqueçaba"},
    {"UF": "SC", "Litoral": "Paulo Lopes"},
    {"UF": "MA", "Litoral": "Luís Domingues"},
    {"UF": "AL", "Litoral": "Roteiro"},
    {"UF": "RN", "Litoral": "Caiçara do Norte"},
    {"UF": "RN", "Litoral": "Porto do Mangue"},
    {"UF": "MA", "Litoral": "Porto Rico do Maranhão"},
    {"UF": "MA", "Litoral": "Bacurituba"},
    {"UF": "PB", "Litoral": "Tavares"},
    {"UF": "AL", "Litoral": "Feliz Deserto"},
    {"UF": "RN", "Litoral": "Senador Georgino Avelino"},
    {"UF": "RN", "Litoral": "Tibau"},
    {"UF": "RN", "Litoral": "Pedra Grande"},
    {"UF": "PE", "Litoral": "Fernando de Noronha"},
    {"UF": "RN", "Litoral": "Galinhos"},
    {"UF": "RN", "Litoral": "São Bento do Norte"}
    
]

metropolitanas = [
    {'UF': 'AC', 'Capital': 'Rio Branco', 'Metropolitana': ['Bujari', 'Rio Branco']},
    {'UF': 'AL', 'Capital': 'Maceió', 'Metropolitana': ['Atalaia', 'Barra de Santo Antônio', 'Barra de São Miguel', 'Capela', 'Coqueiro Seco', 'Flexeiras', 'Jequiá da Praia', 'Maceió', 'Marechal Deodoro', 'Messias', 'Murici', 'Paripueira', 'Pilar', 'Rio Largo', 'Roteiro', 'Santa Luzia do Norte', 'São Luís do Quitunde', 'São Miguel dos Campos', 'Satuba']},
    {'UF': 'AP', 'Capital': 'Macapá', 'Metropolitana': ['Macapá', 'Mazagão', 'Santana']},
    {'UF': 'AM', 'Capital': 'Manaus', 'Metropolitana': ['Careiro da Várzea', 'Iranduba', 'Manaus']},
    {'UF': 'BA', 'Capital': 'Salvador', 'Metropolitana': ['Camaçari', 'Candeias', 'Dias dÁvila', 'Itaparica', 'Jaguaripe', 'Lauro de Freitas', 'Madre de Deus', 'Salinas da Margarida', 'Salvador', 'Santa Terezinha', 'São Francisco do Conde', 'Saubara', 'Simões Filho', 'Vera Cruz']},
    {'UF': 'CE', 'Capital': 'Fortaleza', 'Metropolitana': ['Aquiraz', 'Caucaia', 'Eusébio', 'Fortaleza', 'Guaiúba', 'Horizonte', 'Itaitinga', 'Maracanaú', 'Maranguape', 'Pacatuba', 'Pindoretama']},
    {'UF': 'DF', 'Capital': 'Brasília', 'Metropolitana': ['Brasília']},
    {'UF': 'ES', 'Capital': 'Vitória', 'Metropolitana': ['Cariacica', 'Domingos Martins', 'Fundão', 'Guarapari', 'Marechal Floriano', 'Santa Leopoldina', 'Serra', 'Viana', 'Vila Velha', 'Vitória']},
    {'UF': 'GO', 'Capital': 'Goiânia', 'Metropolitana': ['Abadia de Goiás', 'Aparecida de Goiânia', 'Aragoiânia', 'Bela Vista de Goiás', 'Bonfinópolis', 'Brazabrantes', 'Caldazinha', 'Campestre de Goiás', 'Campo Limpo de Goiás', 'Caturaí', 'Damolândia', 'Goianápolis', 'Goiânia', 'Goianira', 'Guapó', 'Hidrolândia', 'Inhumas', 'Nerópolis', 'Nova Veneza', 'Santa Bárbara de Goiás', 'Santo Antônio de Goiás', 'Senador Canedo', 'Terezópolis de Goiás', 'Trindade']},
    {'UF': 'MA', 'Capital': 'São Luís', 'Metropolitana': ['Alcântara', 'Axixá', 'Bacabeira', 'Icatu', 'Morros', 'Paço do Lumiar', 'Presidente Juscelino', 'Raposa', 'Rosário', 'São José de Ribamar', 'São Luís']},
    {'UF': 'MT', 'Capital': 'Cuiabá', 'Metropolitana': ['Chapada dos Guimarães', 'Cuiabá', 'Nossa Senhora do Livramento', 'Santo Antônio de Leverger', 'Várzea Grande']},
    {'UF': 'MS', 'Capital': 'Campo Grande', 'Metropolitana': ['Campo Grande', 'Jaraguari', 'Terenos']},
    {'UF': 'MG', 'Capital': 'Belo Horizonte', 'Metropolitana': ['Barão de Cocais', 'Belo Horizonte', 'Betim', 'Brumadinho', 'Caeté', 'Capim Branco', 'Confins', 'Contagem', 'Esmeraldas', 'Ibirité', 'Igarapé', 'Itabirito', 'Jaboticatubas', 'Nova União', 'Juatuba', 'Lagoa Santa', 'Mário Campos', 'Matozinhos', 'Moeda', 'Nova Lima', 'Pedro Leopoldo', 'Raposos', 'Ribeirão das Neves', 'Rio Acima', 'Sabará', 'Santa Luzia', 'São Joaquim de Bicas', 'São José da Lapa', 'Sarzedo', 'Taquaraçu de Minas', 'Vespasiano']},
    {'UF': 'PA', 'Capital': 'Belém', 'Metropolitana': ['Ananindeua', 'Barcarena', 'Belém', 'Benevides', 'Marituba', 'Ponta de Pedras', 'Santa Bárbara do Pará', 'Santa Izabel do Pará']},
    {'UF': 'PB', 'Capital': 'João Pessoa', 'Metropolitana': ['Alhandra', 'Baía da Traição', 'Bayeux', 'Caaporã', 'Cabedelo', 'Capim', 'Conde', 'Cruz do Espírito Santo', 'Cuité de Mamanguape', 'João Pessoa', 'Lucena', 'Mamanguape', 'Marcação', 'Pedras de Fogo', 'Pilar', 'Pitimbu', 'Riachão do Poço', 'Rio Tinto', 'Santa Rita', 'São Miguel de Taipu', 'Sapé', 'Sobrado']},
    {'UF': 'PR', 'Capital': 'Curitiba', 'Metropolitana': ['Almirante Tamandaré', 'Araucária', 'Balsa Nova', 'Bocaiúva do Sul', 'Campina Grande do Sul', 'Campo Largo', 'Campo Magro', 'Colombo', 'Contenda', 'Curitiba', 'Fazenda Rio Grande', 'Itaperuçu', 'Mandirituba', 'Morretes', 'Pinhais', 'Piraquara', 'Quatro Barras', 'Rio Branco do Sul', 'São José dos Pinhais']},
    {'UF': 'PE', 'Capital': 'Recife', 'Metropolitana': ['Abreu e Lima', 'Araçoiaba', 'Cabo de Santo Agostinho', 'Camaragibe', 'Carpina', 'Chã de Alegria', 'Glória do Goitá', 'Igarassu', 'Ipojuca', 'Ilha de Itamaracá', 'Itapissuma', 'Itaquitinga', 'Jaboatão dos Guararapes', 'Lagoa de Itaenga', 'Moreno', 'Olinda', 'Paudalho', 'Paulista', 'Recife', 'São Lourenço da Mata', 'Tracunhaém', 'Vitória de Santo Antão']},
    {'UF': 'PI', 'Capital': 'Teresina', 'Metropolitana': ['Altos', 'Demerval Lobão', 'José de Freitas', 'Lagoa do Piauí', 'Nazária', 'Pau DArco do Piauí', 'Teresina']},
    {'UF': 'RJ', 'Capital': 'Rio de Janeiro', 'Metropolitana': ['Belford Roxo', 'Duque de Caxias', 'Guapimirim', 'Itaboraí', 'Magé', 'Maricá', 'Mesquita', 'Nilópolis', 'Niterói', 'Nova Iguaçu', 'Petrópolis', 'Queimados', 'Rio de Janeiro', 'São Gonçalo', 'São João de Meriti']},
    {'UF': 'RN', 'Capital': 'Natal', 'Metropolitana': ['Arês', 'Bom Jesus', 'Brejinho', 'Ceará-Mirim', 'Parnamirim', 'Extremoz', 'Ielmo Marinho', 'Lagoa de Pedras', 'Lagoa Salgada', 'Macaíba', 'Maxaranguape', 'Monte Alegre', 'Natal', 'Nísia Floresta', 'São Gonçalo do Amarante', 'São José de Mipibu', 'São Pedro', 'Senador Georgino Avelino', 'Taipu', 'Tibau do Sul', 'Vera Cruz']},
    {'UF': 'RS', 'Capital': 'Porto Alegre', 'Metropolitana': ['Alvorada', 'Arroio dos Ratos', 'Barra do Ribeiro', 'Cachoeirinha', 'Campo Bom', 'Canoas', 'Capela de Santana', 'Charqueadas', 'Eldorado do Sul', 'Estância Velha', 'Esteio', 'Glorinha', 'Gravataí', 'Guaíba', 'Ivoti', 'Lindolfo Collor', 'Mariana Pimentel', 'Montenegro', 'Nova Santa Rita', 'Novo Hamburgo', 'Pareci Novo', 'Portão', 'Porto Alegre', 'São Jerônimo', 'São Leopoldo', 'Sapiranga', 'Sapucaia do Sul', 'Triunfo', 'Viamão']},
    {'UF': 'RO', 'Capital': 'Porto Velho', 'Metropolitana': ['Porto Velho', 'Candeias do Jamari']},
    {'UF': 'RR', 'Capital': 'Boa Vista', 'Metropolitana': ['Boa Vista', 'Cantá', 'Mucajaí']},
    {'UF': 'SC', 'Capital': 'Florianópolis', 'Metropolitana': ['Águas Mornas', 'Angelina', 'Antônio Carlos', 'Biguaçu', 'Bombinhas', 'Canelinha', 'Florianópolis', 'Garopaba', 'Governador Celso Ramos', 'Major Gercino', 'Palhoça', 'Paulo Lopes', 'Porto Belo', 'Rancho Queimado', 'Santo Amaro da Imperatriz', 'São João Batista', 'São José', 'São Pedro de Alcântara', 'Tijucas']},
    {'UF': 'SE', 'Capital': 'Aracaju', 'Metropolitana': ['Aracaju', 'Areia Branca', 'Barra dos Coqueiros', 'Capela', 'Carmópolis', 'Divina Pastora', 'General Maynard', 'Itabaiana', 'Itaporanga dAjuda', 'Japaratuba', 'Laranjeiras', 'Malhador', 'Maruim', 'Nossa Senhora do Socorro', 'Pirambu', 'Riachuelo', 'Rosário do Catete', 'Salgado', 'Santa Rosa de Lima', 'Santo Amaro das Brotas', 'São Cristóvão', 'Siriri']},
    {'UF': 'TO', 'Capital': 'Palmas', 'Metropolitana': ['Aparecida do Rio Negro', 'Lajeado', 'Palmas']},
    {'UF': 'SP', 'Capital': 'São Paulo', 'Metropolitana': ['Araçariguama', 'Arujá', 'Atibaia', 'Barueri', 'Bom Jesus dos Perdões', 'Caieiras', 'Cajamar', 'Campo Limpo Paulista', 'Carapicuíba', 'Cotia', 'Cubatão', 'Diadema', 'Embu das Artes', 'Embu-Guaçu', 'Ferraz de Vasconcelos', 'Francisco Morato', 'Franco da Rocha', 'Guarulhos', 'Itapecerica da Serra', 'Itapevi', 'Itaquaquecetuba', 'Jandira', 'José Bonifácio', 'Jundiaí', 'Mairiporã', 'Mauá', 'Mogi das Cruzes', 'Nazaré Paulista', 'Osasco', 'Pirapora do Bom Jesus', 'Poá', 'Ribeirão Pires', 'Rio Grande da Serra', 'Santa Isabel', 'Santana de Parnaíba', 'Santo André', 'São Bernardo do Campo', 'São Caetano do Sul', 'São Lourenço da Serra', 'São Paulo', 'Suzano', 'Taboão da Serra', 'Vargem Grande Paulista', 'Várzea Paulista']}

]

def obter_municipios():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'
    response = requests.get(url)

    if response.status_code == 200:
        municipios = response.json()
        return municipios
    else:
        print("Falha ao obter os estados da API do IBGE.")
        return None

def verificar_tipo_municipio(municipio, metropolitanas, litoral, capitais):
    nome_municipio = municipio['nome']
    uf_municipio = municipio['microrregiao']['mesorregiao']['UF']['sigla']

    for capital in capitais:
        if uf_municipio == 'DF':
            return 'Distrito Federal'
        if nome_municipio == capital['Capital'] and uf_municipio == capital['UF']:
            return 'Capital'
    for item in metropolitanas:
            if nome_municipio in item['Metropolitana'] and uf_municipio == item['UF']:
                return 'Metropolitana'
    for item in litoral:
        if nome_municipio == item['Litoral'] and uf_municipio == item['UF']:
            return 'Litoral'      
    return 'Interior'


def salvar_municipios_em_excel(municipios, metropolitanas, litoral, capitais):
    workbook = openpyxl.Workbook()
    sheet = workbook.active

    sheet['A1'] = 'Nome do Município'
    sheet['B1'] = 'UF'
    sheet['C1'] = 'Nome da UF'
    sheet['D1'] = 'Região'
    sheet['E1'] = 'Tipo de Município'

    for index, municipio in enumerate(municipios, start=2):
        sheet[f'A{index}'] = municipio['nome']
        sheet[f'B{index}'] = municipio['microrregiao']['mesorregiao']['UF']['sigla']
        sheet[f'C{index}'] = municipio['microrregiao']['mesorregiao']['UF']['nome']
        sheet[f'D{index}'] = municipio['microrregiao']['mesorregiao']['UF']['regiao']['nome']
        sheet[f'E{index}'] = verificar_tipo_municipio(municipio, metropolitanas, litoral, capitais)

    workbook.save('Base_Geográfica.xlsx')

def obter_teste():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/regioes-metropolitanas'
    response = requests.get(url)

    if response.status_code == 200:
        municipios = response.json()
        return municipios
    else:
        print("Falha ao obter os estados da API do IBGE.")
        return None


      
municipios = obter_municipios()
if municipios:
    salvar_municipios_em_excel(municipios, metropolitanas, litoral, capitais)
else:
    print("Não foi possível obter a lista de municípios.")

