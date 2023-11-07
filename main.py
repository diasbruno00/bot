from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import date


service = Service()
cardapio = []

options = webdriver.ChromeOptions()
options.add_argument("--headless")

driver = webdriver.Chrome(service= service, options= options)

def buscarCardapio():

    url = 'https://ufop.br/cardapio-do-ru'

    driver.get(url)

    table = driver.find_elements(By.TAG_NAME, 'table')

    for i in table:
        tr = i.find_elements(By.TAG_NAME, 'tr')
        for i in tr:
            td = i.find_elements(By.TAG_NAME, 'td')
            for i in td:
                cardapio.append(i.text)



def mostrarMenu():

    print(f'Cardapio Ru UFOP {date.today()}')
    print('1 - Ouro Preto e Mariana')
    print('2 - joão Monlevade')
    print('0 - para sair')


def motrarCardapio(opcao):
    if opcao == 1:
        print(almocoOuroPreto)
        print(jantarOuroPreto)
    elif opcao == 2: 
        print(almocoJoãoMonlevade)
        print(jantarJoãoMonlevade)
    elif opcao == 0:
        print('Programa finalizado...')
    else:
        print('Opcao invalida ...')



while True:
  
  try:

    buscarCardapio()
    mostrarMenu()
    escolha = int(input('Qual sua escolha: '))
    print('\n')
    almocoOuroPreto = cardapio[1]
    jantarOuroPreto = cardapio[2]
    almocoJoãoMonlevade = cardapio[4]
    jantarJoãoMonlevade = cardapio[5]
    motrarCardapio(escolha)
    if escolha == 0:
        break

  except Exception as error:
    print(error)

   