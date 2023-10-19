import pyautogui
import pyperclip
from playwright.sync_api import sync_playwright
from datetime import datetime
import pandas
import time
import os



def fazer_login(page):
    page.goto("https://login-evcj-test-saasfaprod1.fa.ocs.oraclecloud.com")
    time.sleep(3)

    username_input = page.locator('xpath=/html/body/div[2]/div[3]/div/main/form/input[1]')
    username_input.fill("mariana.maciel@beepsaude.com.br")

    time.sleep(2)

    password_input = page.locator('xpath=/html/body/div[2]/div[3]/div/main/form/input[2]')
    password_input.fill("Za7yu8ma@")
    page.keyboard.press("Enter")
    time.sleep(3)

def acessar_contagens_de_ciclos(page):
    page.goto("https://fa-evcj-test-saasfaprod1.fa.ocs.oraclecloud.com/fscmUI/faces/FuseWelcome?_afrLoop=14629167889228257&fnd=%3B%3B%3B%3Bfalse%3B256%3B%3B%3B&_adf.ctrl-state=m8rxhn2th_736")
    time.sleep(3)

    page.keyboard.press("Enter")
    time.sleep(3)

    page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div[3]/div').click()
    time.sleep(5)

def mostrar_tarefas(page):
    page.locator('xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[6]/table/tbody/tr/td[1]/div/div[1]').click()
    time.sleep(5)

def acessar_gerenciar_contagens_ciclos(page):
    page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div/table/tbody/tr/td/div/table/tbody/tr/td[2]/div/div[1]/div/div/span/table/tbody/tr/td[1]/table').click()
    time.sleep(5)
    page.keyboard.press('ArrowDown')
    page.keyboard.press('Enter')
    time.sleep(5)

def acessar_organizacao(page):
    page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div/table/tbody/tr/td/div/table/tbody/tr/td[2]/div/div[1]/div/div/span/div/div[1]/div/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/div[2]/div/ul/li[2]/a').click()
    time.sleep(4)


def digitar_hub_com_base_no_dia_da_semana(page, hub):

    print(f'Digitando o hub: {hub}')
    input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/span/input')
    input_element.click()
    input_element.fill(hub)

    time.sleep(4)

    page.keyboard.press('Tab')
    time.sleep(3)
    # Pressione a tecla "Enter" usando o teclado virtual
    page.keyboard.press('Enter')
    time.sleep(20)



def clicar_elemento_por_dia(elemento,page):

    page.click(elemento)
    time.sleep(5)

    time.sleep(5)

def acessar_a_açao(page):

    page.locator('xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/span/div[1]/div[1]/div/div/table/tbody/tr/td[1]/div/div[1]/div[1]/table/tbody/tr/td[1]/div/div/table/tbody/tr/td[3]/div').click()

    time.sleep(5)

    for _ in range(5):
            page.keyboard.press('ArrowDown')
    time.sleep(10) # Espere 1 segundo entre as pressionadas de tecla de seta


    page.keyboard.press('Enter')

    time.sleep(6)

    page.keyboard.press('Enter')

    time.sleep(6)

def pagina_inicial_execuçao_de_cadeia_suprimento(page):
    # Navegue para a URL da página de execução de cadeia de suprimentos
    page.goto("https://fa-evcj-test-saasfaprod1.fa.ocs.oraclecloud.com/fscmUI/faces/FuseWelcome?_afrLoop=14629167889228257&fnd=%3B%3B%3B%3Bfalse%3B256%3B%3B%3B&_adf.ctrl-state=m8rxhn2th_736")
    time.sleep(6)

def pagina_ferramenta(page):
    # Localize o elemento da página usando o seletor XPath fornecido
    ferramenta_element = page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[12]')

    # Clique no elemento
    ferramenta_element.click()

    time.sleep(5)

def processos_programados(page):
    programados_element =  page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[23]/div/div[2]/div[2]/div[5]/div')

    programados_element.click()

    time.sleep(5)

def atualizar_processos(page):
    atualizar_element = page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/table/tbody/tr/td[2]/div/div[1]/div[1]/table/tbody/tr/td[10]/div')

    atualizar_element.click()
    time.sleep(10)

    page.keyboard.press('Enter')
    time.sleep(3)
    page.keyboard.press('Enter')

    time.sleep(3)
    page.keyboard.press('Enter')

    time.sleep(3)
    page.keyboard.press('Enter')
    time.sleep(20) #deixar 20

def pagina_inicial_novamente(page):
    page.goto("https://fa-evcj-test-saasfaprod1.fa.ocs.oraclecloud.com/fscmUI/faces/FuseWelcome?_afrLoop=14629167889228257&fnd=%3B%3B%3B%3Bfalse%3B256%3B%3B%3B&_adf.ctrl-state=m8rxhn2th_736")
    time.sleep(10)

    pyautogui.press('ENTER')

def elemento_da_seta(page):
    seta_element = page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[12]')
    seta_element.click()

    time.sleep(10)


def localizar_elemento():
    # Pressiona a tecla de seta para a esquerda quatro vezes
    for _ in range(4):
        pyautogui.press('left')
        time.sleep(1)  # Opcional: adicione um atraso entre cada pressionamento de tecla

    # Pressiona a tecla ENTER
    pyautogui.press('ENTER')
    time.sleep(3)

def elemento_da_pagina(page):
    elemnto_da_pagina_element = page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div[1]')
    elemnto_da_pagina_element.click()  # Adicione parênteses aqui
    time.sleep(3)

def terceira_elemento(page):
    terceira_element = page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[7]')
    terceira_element.click()  # Adicione parênteses aqui
    time.sleep(3)
    pyautogui.press('ENTER')
    time.sleep(3)


def pressionar_tecla_seta_e_enter():
    for _ in range(2):
        pyautogui.press('left')
        time.sleep(3)

    pyautogui.press('ENTER')
    time.sleep(1)

def procurar_elemento(page):
    procurar_element = page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div[1]')
    procurar_element.click()
    time.sleep(3)

    pyautogui.press('ENTER')

def procurar_quarto_elemento(page):
    quarto_element = page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[4]')
    quarto_element.click()
    time.sleep(3)
    pyautogui.press('ENTER')

    time.sleep(3)


def colocar_seta_novamente(page):
    seta_element = page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div[1]')
    seta_element.click
    time.sleep(3)
    pyautogui.press('ENTER')

def procurar_o_inicio_da_pagina():
    for _ in range(3):
        pyautogui.press('left')
        time.sleep(3)

        pyautogui.press('ENTER')
    time.sleep(1)

def procurar_quinto_elemento(page):
    quinto_element = page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div[1]')
    quinto_element.click()
    time.sleep(3)
    pyautogui.press('ENTER')

    time.sleep(3)

def segunda_vez_gerenciamento_de_estoque(page):
    gerenciamento_element = page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[1]/div/div[2]/div[2]/div[3]/div')
    gerenciamento_element.click()
    time.sleep(3)
    pyautogui.press('ENTER')

def novamente_mostrar_tarefas(page):
    page.locator('xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[6]/table/tbody/tr/td[1]/div/div[1]').click()
    time.sleep(5)

def novamente_acessar_gerenciar_contagens_ciclos(page):
    page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div/table/tbody/tr/td/div/table/tbody/tr/td[2]/div/div[1]/div/div/span/table/tbody/tr/td[1]/table').click()
    time.sleep(5)
    page.keyboard.press('Enter')  # Pressione apenas a tecla Enter
    time.sleep(5)

def novamente_acessar_organizacao(page):
    page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div/table/tbody/tr/td/div/table/tbody/tr/td[2]/div/div[1]/div/div/span/div/div[1]/div/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/div/div[2]/div/ul/li[2]/a').click()
    time.sleep(4)


def novamente_clicar_elemento_por_dia(elemento,page):

    page.click(elemento)
    time.sleep(5)
    

    time.sleep(5)

def novamente_acessar_a_açao(page):

    page.locator('xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/span/div[1]/div[1]/div/div/table/tbody/tr/td[1]/div/div[1]/div[1]/table/tbody/tr/td[1]/div/div/table/tbody/tr/td[3]/div').click()

    time.sleep(5)

    for _ in range(6):
            page.keyboard.press('ArrowDown')
    time.sleep(10) # Espere 1 segundo entre as pressionadas de tecla de seta


    page.keyboard.press('Enter')

    time.sleep(6)

    page.keyboard.press('Enter')

    time.sleep(6)


def retornar_pagina_inicial_execuçao_de_cadeia_suprimento(page):
    # Navegue para a URL da página de execução de cadeia de suprimentos
    page.goto("https://fa-evcj-test-saasfaprod1.fa.ocs.oraclecloud.com/fscmUI/faces/FuseWelcome?_afrLoop=14629167889228257&fnd=%3B%3B%3B%3Bfalse%3B256%3B%3B%3B&_adf.ctrl-state=m8rxhn2th_736")
    time.sleep(6)

def retornar_pagina_ferramenta(page):
    # Localize o elemento da página usando o seletor XPath fornecido
    retornar_ferramenta_element = page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[12]')

    # Clique no elemento
    retornar_ferramenta_element.click()

    time.sleep(5)

def retornar_processos_programados(page):
    retornar_programados_element =  page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[23]/div/div[2]/div[2]/div[5]/div')

    retornar_programados_element.click()

    time.sleep(5)

def retornar_atualizar_processos(page):
    retornar_atualizar_element = page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/table/tbody/tr/td[2]/div/div[1]/div[1]/table/tbody/tr/td[10]/div')

    retornar_atualizar_element.click()
    time.sleep(10)

    page.keyboard.press('Enter')
    time.sleep(3)
    page.keyboard.press('Enter')

    time.sleep(3)
    page.keyboard.press('Enter')

    time.sleep(3)
    page.keyboard.press('Enter')

    time.sleep(20) #deixar 20

def press_tab_and_enter(num_tabs=23, tab_delay=0.1, enter_delay=5):
    # Pressiona a tecla 'Tab' várias vezes
    for _ in range(num_tabs):
        pyautogui.press('Tab')
        time.sleep(tab_delay)

    # Aguarda um período de tempo
    time.sleep(enter_delay)

    # Pressiona a tecla 'Enter'
    pyautogui.press('Enter')

def preencher_e_submeter_formulario(page):
    # Localize o campo de entrada
    input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/span/input')

    # Preencha o campo de entrada com o texto desejado
    input_element.fill("Imprimir Relatório da Listagem da Contagem Cíclica")

    # Pressione 'Tab' para navegar para o próximo elemento
    page.keyboard.press('Tab')
    time.sleep(3)

    # Pressione 'Tab' algumas vezes (no exemplo, 3 vezes) para navegar para o próximo elemento
    for _ in range(3):
        pyautogui.press('Tab')
        time.sleep(3)

    # Pressione 'Enter' para enviar o formulário
    page.keyboard.press('Enter')
    time.sleep(5)


def encontrar_e_digitar_hub(hub):
    # Pressiona 'Tab' várias vezes (no exemplo, 7 vezes)
    for _ in range(7):
        pyautogui.press('Tab')
    time.sleep(5)


    print(f'Digitando o hub: {hub}')

    # Simular a inserção do hub (neste caso, simulamos pressionando as teclas)
    pyautogui.typewrite(hub)



    time.sleep(3)
    pyautogui.press('Tab')
    time.sleep(3)


def combinar_e_digitar_informacoes(registro_contagem_ciclica, hub):


    if registro_contagem_ciclica == "descartaveis":
        registro_contagem_ciclica = "Descartáveis"

    if registro_contagem_ciclica == "duraveis":
        registro_contagem_ciclica = "Duráveis"

    if registro_contagem_ciclica == "lab_vacina":
        registro_contagem_ciclica = "LAB/VAC"


    if hub == "SBERNARDO_SP_1175":
        hub_semana = "S.BERNARDO"

    elif hub == "BRASILIA_DF_0950":
        hub_semana = "BRASÍLIA"

    elif hub == "VL_OLIMPIA_SP_0446":
        hub_semana = "VL OLÍMPIA"

    else:
        hub_semana = hub[:-8]

    if registro_contagem_ciclica == "Descartáveis" or registro_contagem_ciclica == "Duráveis":
        info = f'LAB - {registro_contagem_ciclica} {hub_semana}'


    elif registro_contagem_ciclica == "insumos":
        info =  f'{registro_contagem_ciclica} - {hub_semana}'

    else:
        info = f'ALMOX - {registro_contagem_ciclica} - {hub_semana}'


    print(f'Digitando o hub:')
    print(info)
    pyperclip.copy(info)


    # Simular a inserção das informações (neste caso, simulamos pressionando as teclas)
    pyautogui.hotkey("ctrl", "v")

    time.sleep(15)
    for _ in range(14):
        pyautogui.press('Tab')
    time.sleep(2)
    pyautogui.press('ENTER')
    time.sleep(2)

    for _ in range(13):
        pyautogui.press('Tab')
    time.sleep(2)
    pyautogui.press('ENTER')
    time.sleep(10)

    # Feche o navegador
    pyautogui.hotkey('ctrl', 'w')
    print("Hub finalizado!")
    print("Iniciando próximo ciclo")








def contagem_inventario(hub, registro_contagem_ciclica, elemento):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()



        fazer_login(page)
        acessar_contagens_de_ciclos(page)
        mostrar_tarefas(page)
        acessar_gerenciar_contagens_ciclos(page)
        acessar_organizacao(page)


        # Chame a função para digitar o hub com base no dia da semana
        digitar_hub_com_base_no_dia_da_semana(page, hub)

        clicar_elemento_por_dia(elemento,page)
        acessar_a_açao(page)


        pagina_inicial_execuçao_de_cadeia_suprimento(page)
        pagina_ferramenta(page)
        processos_programados(page)
        atualizar_processos(page)




        pagina_inicial_novamente(page)
        elemento_da_seta(page)
        quantidade_de_pressionadas = 4
        localizar_elemento()
        elemento_da_pagina(page)
        terceira_elemento(page)
        quantidade_de_pressionadas = 2  
        pressionar_tecla_seta_e_enter()
        procurar_elemento(page)
        procurar_quarto_elemento(page)
        colocar_seta_novamente(page)
        procurar_o_inicio_da_pagina()
        procurar_quinto_elemento(page)
        segunda_vez_gerenciamento_de_estoque(page)
        novamente_mostrar_tarefas(page)
        novamente_acessar_gerenciar_contagens_ciclos(page)
        novamente_acessar_organizacao(page)
        novamente_clicar_elemento_por_dia(elemento,page)
        novamente_acessar_a_açao(page)
        retornar_pagina_inicial_execuçao_de_cadeia_suprimento(page)
        retornar_pagina_ferramenta(page)
        retornar_processos_programados(page)
        retornar_atualizar_processos(page)
        press_tab_and_enter()
        preencher_e_submeter_formulario(page)


        encontrar_e_digitar_hub(hub)

        # Chame a função para combinar e digitar as informações

        combinar_e_digitar_informacoes(registro_contagem_ciclica, hub)






def controlador():


    vacina = {
            "SC_RJ_1256": 0, # Segunda-feira
            "BARRA_RJ_0608": 0, # Segunda-feira
            "TATUAPE_SP_1337": 4, # Segunda-feira
            "VL_OLIMPIA_SP_0446": 4, # Terça-feira
            "ALPHAVILLE_SP_1094": 4, # Terça-feira
            "SBERNARDO_SP_1175": 4, # Terça-feira
            "CAMPINAS_SP_1507": 4 # Terça-feira
    }

    lab_vacina = {
            "SC_RJ_1256": 0, # Terça-feira
            "BARRA_RJ_0608": 0, # Terça-feira
            "VL_OLIMPIA_SP_0446": 0, # Terça-feira
            "ALPHAVILLE_SP_1094": 0, # Terça-feira
            "SBERNARDO_SP_1175": 0, # Terça-feira
            "CAMPINAS_SP_1507": 4, # Terça-feira
            "TATUAPE_SP_1337": 4 # Quarta-feira

    }

    lab = {
            "RECIFE_PE_1760":4,
            "CURITIBA_PR_0870":4,
            "SC_RJ_1256": 0, # Quarta-feira
            "BARRA": 0, # Quarta-feira
            "VL_OLIMPIA_SP_0446": 0, # Quinta-feira
            "ALPHAVILLE_SP_1094": 1, # Quinta-feira
            "SBERNARDO_SP_1175": 0, # Quinta-feira
            "CAMPINAS_SP_1507": 1, # Quinta-feira
            "TATUAPE_SP_1337": 1  # Sexta-feira

    }

    duraveis = {
            "SC_RJ_1256": 0, # Terça-feira
            "BARRA": 0, # Terça-feira
            "VL_OLIMPIA_SP_0446": 0, # Terça-feira
            "ALPHAVILLE_SP_1094": 0, # Terça-feira
            "SBERNARDO_SP_1175": 0, # Terça-feira
            "TATUAPE_SP_1337": 0, # Terça-feira
            "CAMPINAS_SP_1507": 0, # Terça-feira
            "BRASILIA": 4 # Terça-feira
    }

    # descartaveis["descartáveis"]
    descartaveis = {
            "RECIFE_PE_1760":4,
            "CURITIBA_PR_0870":4,
            "SC_RJ_1256": 4, # Sexta-feira
            "BARRA": 4, # Sexta-feira
            "VL_OLIMPIA_SP_0446": 4, # Sexta-feira
            "ALPHAVILLE_SP_1094": 4, # Sexta-feira
            "SBERNARDO_SP_1175": 4, # Sexta-feira
            "TATUAPE_SP_1337": 4, # Sexta-feira
            "CAMPINAS_SP_1507": 4, # Sexta-feira
            "BRASÍLIA": 4 # Sexta-feira
    }

    insumos = {
        "BRASILIA_DF_0950": 3,
        "RECIFE_PE_1760":4
    }

    elementos = ['xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/span/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/div',
                'xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/span/div[1]/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/div',
                'xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/span/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/div',
                'xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/span/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[2]/div',
                'xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/span/div[1]/div[2]/div/div[2]/table/tbody/tr[6]/td[2]/div',
                'xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/span/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/div'
                ]

    hubs_vacina = []
    hubs_lab_vacina = []
    hubs_lab = []
    hubs_duraveis = []
    hubs_descartaveis = []
    hubs_insumos = []

    dia_da_semana = datetime.now().date().weekday()
    dia_mes = datetime.now().date().day


    # Inicia a contagem para Vacina

    print("Iniciando a contagem para Vacina")

    for hub, dias_semana in vacina.items():
        if dia_da_semana == dias_semana:
            hubs_vacina.append(hub)

    for hub in hubs_vacina:
        print("Iniciando contagem do hub ", end='')
        print(hub)
        contagem_inventario(hub, "vacina", elementos[3])

    print("Processo finalizado!")
    print("------------------------------------------------")


    # Inicia a contagem para Lab Vacina

    print("Iniciando a contagem para Lab Vacina")

    for hub, dias_semana in lab_vacina.items():
        if dia_da_semana == dias_semana:
            hubs_lab_vacina.append(hub)

    for hub in hubs_lab_vacina:
        print("Iniciando contagem do hub ", end='')
        print(hub)
        contagem_inventario(hub, "lab_vacina", elementos[2])

    print("Processo finalizado!")
    print("------------------------------------------------")


    # Inicia a contagem para Lab

    print("Iniciando a contagem para Lab")

    for hub, dias_semana in lab.items():
        if dia_da_semana == dias_semana:
            hubs_lab.append(hub)

    for hub in hubs_lab:
        print("Iniciando contagem do hub ", end='')
        print(hub)
        contagem_inventario(hub, "lab", elementos[1])

    print("Processo finalizado!")
    print("------------------------------------------------")

    # Inicia a contagem para Duráveis

    print("Iniciando a contagem para Duráveis")

    for hub, dias_semana in duraveis.items():
        if dia_da_semana == dias_semana:
            if (dia_mes < 8) or (14 < dia_mes < 22):
                hubs_duraveis.append(hub)

    for hub in hubs_duraveis:
        print("Iniciando contagem do hub ", end='')
        print(hub)
        contagem_inventario(hub, "duraveis", elementos[4])


    print("Processo finalizado!")
    print("------------------------------------------------")

     # Inicia a contagem para insumos

    print("Iniciando a contagem para insumos")

    for hub, dias_semana in insumos.items():
        if dia_da_semana == dias_semana:
            hubs_insumos.append(hub)

    for hub in hubs_insumos:
        print("Iniciando contagem do hub ", end='')
        print(hub)
        contagem_inventario(hub,  "insumos", elementos[5])

    print("Processo finalizado!")
    print("------------------------------------------------")

    # Inicia a contagem para Descartáveis

    print("Iniciando a contagem para Descartáveis")

    for hub, dias_semana in descartaveis.items():
        if dia_da_semana == dias_semana:
            hubs_descartaveis.append(hub)


    for hub in hubs_descartaveis:
        print("Iniciando contagem do hub ", end='')
        print(hub)
        contagem_inventario(hub,  "descartaveis", elementos[0])

    print("Processo finalizado!")
    print("------------------------------------------------")


    print("Fim da execução")

controlador()










#subinventario

#  Lab descartaveis   'xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/span/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[2]/div',
#  Almox. Lab         'xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/span/div[1]/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/div',
# Almox lab/vac       'xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/span/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/div',      
# Almox vac           'xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/span/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[2]/div', 
# # Almox DURAVEIS           'xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/span/div[1]/div[2]/div/div[2]/table/tbody/tr[6]/td[2]/div',
# Insumos             'xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div/div/div/div/div/div/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div/span/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[2]/div',