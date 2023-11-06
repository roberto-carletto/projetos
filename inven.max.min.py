import pyautogui
import pyperclip
from playwright.sync_api import sync_playwright
from datetime import datetime
import pandas
import time
import os

def realizar_login(page):
    page.goto("https://login-evcj-test-saasfaprod1.fa.ocs.oraclecloud.com")
    time.sleep(3)

    username_input = page.locator('xpath=/html/body/div[2]/div[3]/div/main/form/input[1]')
    username_input.fill("mariana.maciel@beepsaude.com.br")

    time.sleep(5)

    password_input = page.locator('xpath=/html/body/div[2]/div[3]/div/main/form/input[2]')
    password_input.fill("Za7yu8ma@")
    page.keyboard.press("Enter")
    time.sleep(3)

def acessar_contagens_ciclos(page):
    page.goto("https://fa-evcj-test-saasfaprod1.fa.ocs.oraclecloud.com/fscmUI/faces/FuseWelcome?_afrLoop=14629167889228257&fnd=%3B%3B%3B%3Bfalse%3B256%3B%3B%3B&_adf.ctrl-state=m8rxhn2th_736")
    time.sleep(3)


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
    #programar novo processo
    page.locator('xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/table/tbody/tr/td[2]/div/div[1]/div[1]/table/tbody/tr/td[1]/div').click()
    time.sleep(5)

    input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/span/input')

    # Preencha o campo de entrada com o texto desejado
    input_element.fill("Imprimir Relatório de Planejamento Mín-Máx")

    time.sleep(10)

    for _ in range(4):
        page.keyboard.press("Tab")
        time.sleep(3)

    # # Pressione 'Enter' para enviar o formulário
    page.keyboard.press('Enter')
    time.sleep(5)

    for _ in range(7):
        page.keyboard.press("Tab")
    time.sleep(5)

    
    page.keyboard.press("Enter")


def encontrar_e_digitar_hub(page, hub,tipo):
    # Realize ações específicas para o hub atual aqui
    print(f"Iniciando contagem do hub: {hub}")
    # Execute qualquer lógica que você desejar para este hub

    input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[2]/div/div/div/div/span/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/span/input')
    input_element.fill(hub)
    time.sleep(3)

    page.keyboard.press("Tab")

    for _ in range(3):
        page.keyboard.press("ArrowDown")
    time.sleep(3)

    for _ in range(5):
        page.keyboard.press("Tab")
    time.sleep(3)

    print(f"Iniciando contagem do tipo: {tipo}")
    # Execute qualquer lógica que você desejar para este hub

    input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[2]/div/div/div/div/span/div/table/tbody/tr/td/table/tbody/tr[8]/td[2]/span/input')
    input_element.fill(tipo)
    time.sleep(3)

    for _ in range(7):
        page.keyboard.press("Tab")
    time.sleep(3)

    for _ in range(1):
        page.keyboard.press("ArrowDown")


    time.sleep(3)

    for _ in range(16):
        page.keyboard.press("Tab")
    time.sleep(3)

    for _ in range(1):
        page.keyboard.press("ArrowUp")


    time.sleep(3)

    for _ in range(7):
        page.keyboard.press("Tab")
    time.sleep(3)

    print(f"Contagem concluída para o hub: {hub}")
    print(f"Contagem concluída para o tipo: {tipo}")

def processos_programados_segundo(page):
    programados_element =  page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[23]/div/div[2]/div[2]/div[5]/div')

    programados_element.click()

    time.sleep(5)
    #programar novo processo
    page.locator('xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/table/tbody/tr/td[2]/div/div[1]/div[1]/table/tbody/tr/td[1]/div').click()
    time.sleep(5)

    input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/span/input')

    # Preencha o campo de entrada com o texto desejado
    input_element.fill("Processar Interface de Orquestração da Cadeia de Suprimentos")

    time.sleep(10)    

    for _ in range(6):
        page.keyboard.press("Tab")
        time.sleep(3)



    page.locator('xpath=//html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[2]/div/div/div/div/span/div/div[1]/table/tbody/tr/td/table/tbody/tr[2]/td[2]/select')
    input_element.fill("Oracle Fusion Inventory Management")

    time.sleep(10)    

    for _ in range(2):
        page.keyboard.press("Tab")
        time.sleep(3)


    

    # Feche o navegador
    pyautogui.hotkey('ctrl', 'w')

    # Após concluir as ações específicas, você pode imprimir uma mensagem de conclusão

   










def controlador():
        lab = [
            'BARRA_RJ_0608',
            'SC_RJ_1256',
            'TATUAPE_SP_1337',
            'VL_OLIMPIA_SP_0446',
            'ALPHAVILLE_SP_1094',
            'SBERNARDO_SP_1175',
            'CAMPINAS_SP_1507',
            'BRASILIA_DF_0950'
        ]

        sv = [
            'BARRA_RJ_0608',
            'SC_RJ_1256',
            'TATUAPE_SP_1337',
            'VL_OLIMPIA_SP_0446',
            'ALPHAVILLE_SP_1094',
            'SBERNARDO_SP_1175',
            'CAMPINAS_SP_1507',
            'BRASILIA_DF_0950'
        ]
        hubs_lab = []
        hubs_sv = []

        for hub in lab:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                page = browser.new_page()

                realizar_login(page)
                acessar_contagens_ciclos(page)
                pagina_ferramenta(page)
                processos_programados(page)

                encontrar_e_digitar_hub(page, hub,"LAB")  # Realize ações para o hub
            
            print("Processo finalizado!")

        for hub in sv:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                page = browser.new_page()

                realizar_login(page)
                acessar_contagens_ciclos(page)
                pagina_ferramenta(page)
                processos_programados(page)

                encontrar_e_digitar_hub(page, hub,"SV")  # Realize ações para o hub
                processos_programados_segundo(page)

            print("Processo finalizado!")

# Chame a função controladora para iniciar o processo
controlador()