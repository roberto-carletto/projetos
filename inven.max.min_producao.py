import os
try:
    import pyautogui
    import pyperclip
    import clipboard
    from playwright.sync_api import sync_playwright
    from datetime import datetime
    import pandas
    import time
    from zipfile import ZipFile
    from drive import google_drive
except:
    path = os.getcwd()
    os.chdir(path)
    cmd = 'pip install -r requirements.txt'
    os.system(cmd)
    os.system('playwright install')
    import pyautogui
    import pyperclip
    from playwright.sync_api import sync_playwright
    from datetime import datetime
    import pandas
    import time

def realizar_login(page):
    page.goto("https://login-evcj-saasfaprod1.fa.ocs.oraclecloud.com")
    time.sleep(1)

    username_input = page.locator('xpath=/html/body/div[2]/div[3]/div/main/form/input[1]')
    username_input.fill("mariana.maciel@beepsaude.com.br")

    time.sleep(0.3)

    password_input = page.locator('xpath=/html/body/div[2]/div[3]/div/main/form/input[2]')
    password_input.fill("Za7yu8ma@")
    page.keyboard.press("Enter")
    time.sleep(2)

def acessar_contagens_ciclos(page):
    page.goto("https://fa-evcj-saasfaprod1.fa.ocs.oraclecloud.com/fscmUI/faces/FuseWelcome?_afrLoop=14629167889228257&fnd=%3B%3B%3B%3Bfalse%3B256%3B%3B%3B&_adf.ctrl-state=m8rxhn2th_736")
    time.sleep(2)
    print("Finalizado login")


def pagina_ferramenta(page):
    # Localize o elemento da página usando o seletor XPath fornecido
   #ferramenta_element = page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[12]')
    ferramenta_element = page.locator('xpath=/html/body/div[1]/form/div/div/div/div[1]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[1]/div[2]/div/div[12]')
    # Clique no elemento
    ferramenta_element.click()

    time.sleep(2)
    print("Página de Ferramenta")

def processos_programados(page):
   #programados_element =  page.locator('xpath=/html/body/div[1]/form/div/div/div/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[23]/div/div[2]/div[2]/div[5]/div')
    programados_element = page.locator ('xpath=/html/body/div[1]/form/div/div/div/div[1]/div/div/div/div[3]/div/div[1]/div/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/span/div/div/div[1]/div/div[1]/div[2]/div/div[1]/div/div[1]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div[23]/div/div[2]/div[2]/div[5]/div')
    programados_element.click()

    time.sleep(5)
#     #programar novo processo
   #page.locator('xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/table/tbody/tr/td[2]/div/div[1]/div[1]/table/tbody/tr/td[1]/div').click()
    page.locator('xpath=/html/body/div[1]/form/div[1]/div/div/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/table/tbody/tr/td[2]/div/div[1]/div[1]/table/tbody/tr/td[1]/div').click()
    time.sleep(5)

   #input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/span/input')
    input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/span/input')

    # Preencha o campo de entrada com o texto desejado
    input_element.fill("Imprimir Relatório de Planejamento Mín-Máx")

    time.sleep(5)


    for _ in range(4):
        page.keyboard.press("Tab")
        time.sleep(2)

    # Pressione 'Enter' para enviar o formulário
    page.keyboard.press('Enter')
    time.sleep(2)

    for _ in range(7):
        page.keyboard.press("Tab")
    time.sleep(2)

    page.keyboard.press("Enter")
    print("Processos programados")


def encontrar_e_digitar_hub(page, hub, tipo):
    # Realize ações específicas para o hub atual aqui
    print(f"Iniciando contagem do hub: {hub}")
    # Execute qualquer lógica que você desejar para este hub

   #input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[2]/div/div/div/div/span/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/span/input')
    input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[2]/div/div/div/div/span/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/span/input')
    input_element.fill(hub)
    time.sleep(5)

    page.keyboard.press("Tab")

    for _ in range(3):
        page.keyboard.press("ArrowDown")
    time.sleep(2)

    for _ in range(5):
        page.keyboard.press("Tab")

    print(f"Iniciando contagem do tipo: {tipo}")
    # Execute qualquer lógica que você desejar para este hub

   #input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[2]/div/div/div/div/span/div/table/tbody/tr/td/table/tbody/tr[8]/td[2]/span/input')
    input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[2]/div/div/div/div/span/div/table/tbody/tr/td/table/tbody/tr[8]/td[2]/span/input')

    input_element.fill(tipo)

    for _ in range(7):
        page.keyboard.press("Tab")

    for _ in range(2):
        page.keyboard.press("ArrowDown")
    time.sleep(2)



    for _ in range(16):
        page.keyboard.press("Tab")
    time.sleep(2)

    for _ in range(2):
        page.keyboard.press("ArrowUp")
    time.sleep(2)


    for _ in range(7):
        page.keyboard.press("Tab")

    page.keyboard.press("Enter")
    time.sleep(2)
    # Após concluir as ações específicas, você pode imprimir uma mensagem de conclusão

    print(f"Contagem concluída para o hub: {hub}")
    print(f"Contagem concluída para o tipo: {tipo}")
    print("Finalizado o primeiro processo")

def numero_processo(page):
   #texto = page.query_selector("xpath=/html/body/div[1]/form/div[2]/div[2]/div[3]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/div[2]/span/label").inner_text()
    texto = page.query_selector("xpath=/html/body/div[1]/form/div[2]/div[2]/div[3]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/div[2]/span/label").inner_text()

    num = texto[11:18]
    num_proc = 'MINMAX' + num
    return num_proc

def atualizar(page):

    time.sleep(2)
    page.keyboard.press("Enter")
    time.sleep(1)
    page.keyboard.press("Tab")
    time.sleep(2)
    for _ in range(5):
        page.keyboard.press("Enter")
        time.sleep(5)


def processos_programados_segundo(page):
    for _ in range(21):
        page.keyboard.press("Tab")
        time.sleep(1)

    page.keyboard.press("Enter")

    time.sleep(2)
    #programar novo processo
   #page.locator('xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/table/tbody/tr/td[2]/div/div[1]/div[1]/table/tbody/tr/td[1]/div').click()
    page.locator('xpath=/html/body/div[1]/form/div[1]/div/div/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/table/tbody/tr/td[2]/div/div[1]/div[1]/table/tbody/tr/td[1]/div').click()
    time.sleep(5)

   #input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/span/input')
    input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/span/input')

    # Preencha o campo de entrada com o texto desejado
    input_element.fill("Processar Interface de Orquestração da Cadeia de Suprimentos")

    time.sleep(5)

    for _ in range(1):
        page.keyboard.press("Tab")
        time.sleep(5)

    time.sleep(5)
    # # Pressione 'Enter' para enviar o formulário
    page.keyboard.press('Enter')
    time.sleep(5)
    print("Iniciando primeiro processo")


def encontrar_segundo(page, num_proc):
    for _ in range(6):
        page.keyboard.press("Tab")
    time.sleep(3)

    for _ in range(4):
        page.keyboard.press("ArrowDown")

    for _ in range(2):
        page.keyboard.press("Tab")
    time.sleep(3)

    for letra in num_proc:
        page.keyboard.press(letra)
        time.sleep(0.05)
    time.sleep(1)

    page.keyboard.press("Tab")

    for letra in num_proc:
        page.keyboard.press(letra)
        time.sleep(0.05)
    time.sleep(1)

    for _ in range(7):
        page.keyboard.press("Tab")
    time.sleep(1)

    page.keyboard.press('Enter')
    time.sleep(3)
    page.keyboard.press('Enter')
    time.sleep(3)
    print ("Finalizado o segundo processo")


def processos_programados_terceito(page):
    time.sleep(5)
    #programar novo processo
   #page.locator('xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/table/tbody/tr/td[2]/div/div[1]/div[1]/table/tbody/tr/td[1]/div').click()
    page.locator('xpath=/html/body/div[1]/form/div[1]/div/div/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[1]/div/div/table/tbody/tr/td[2]/div/div[1]/div[1]/table/tbody/tr/td[1]/div').click()

    time.sleep(5)

   #input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/span/input')
    input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr/td/table/tbody/tr[4]/td[2]/span/input')

    # Preencha o campo de entrada com o texto desejado
    input_element.fill("Imprimir Relatório de Slip de Separação de Solicitação de Movimento")

    time.sleep(5)

    for _ in range(1):
        page.keyboard.press("Tab")
        time.sleep(5)

    time.sleep(5)
    # # Pressione 'Enter' para enviar o formulário
    page.keyboard.press('Enter')
    time.sleep(5)
    print("Iniciando o terceiro processo")

def encontrar_e_digitar_hub_terceiro(page, hub, tipo):
    # Realize ações específicas para o hub atual aqui
    print(f"Iniciando contagem do hub: {hub}")
    # Execute qualquer lógica que você desejar para este hub

   #input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[2]/div/div/div/div/span/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/span/input')
    input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[2]/div/div/div/div/span/div/table/tbody/tr/td/table/tbody/tr[2]/td[2]/span/input')
    input_element.fill(hub)
    time.sleep(3)

    # # Pressione 'Enter' para enviar o formulário
    page.keyboard.press('Enter')
    time.sleep(3)

    for _ in range(7):
        page.keyboard.press("Tab")
        time.sleep(0.02)
    time.sleep(5)

    input_element = page.locator('xpath=/html/body/div[1]/form/div[2]/div[2]/div[1]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[2]/div/div/div/div/span/div/table/tbody/tr/td/table/tbody/tr[9]/td[2]/span/input')
    input_element.fill(tipo)
    time.sleep(3)

    for _ in range(3):
        page.keyboard.press("Tab")
        time.sleep(0.02)
    time.sleep(5)

    page.keyboard.press("ArrowDown")
    time.sleep(1)

    for _ in range(4):
        page.keyboard.press("Tab")
        time.sleep(0.02)
    time.sleep(1)

    page.keyboard.press('Enter')
    time.sleep(1)

    page.keyboard.press("Tab")
    time.sleep(1)

    page.keyboard.press("ArrowDown")
    time.sleep(1)

    for _ in range(4):
        page.keyboard.press("Tab")
        time.sleep(0.02)
    time.sleep(1)

    page.keyboard.press('Enter')
    time.sleep(1)

    for _ in range(7):
        page.keyboard.press("Tab")
        time.sleep(0.02)
    time.sleep(1)

    for _ in range(2):
        page.keyboard.press("ArrowDown")

    for _ in range(8):
        page.keyboard.press("Tab")
        time.sleep(0.02)
    time.sleep(3)

    page.keyboard.press('Enter')
    time.sleep(3)
    page.keyboard.press('Enter')
    time.sleep(5)
    print("FInalizado o terceiro processo")

def atualizar2(page):

    time.sleep(2)
    page.keyboard.press("Tab")
    time.sleep(0.5)
    for _ in range(5):
        page.keyboard.press("Enter")
        time.sleep(5)

def encontrar_arquivo_download(page):

    with page.expect_download() as download_info:

       #element = page.locator("xpath=/html/body/div[1]/form/div[1]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/div/table/tbody")
        element = page.locator("xpath=/html/body/div[1]/form/div[1]/div/div/div[1]/div/div/div/div[3]/div/div[2]/div/div/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div/div/div[1]/div/div[1]/table/tbody/tr/td[1]/div/div/div/div/div[2]/div/div/div[1]/div/div[1]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/div/table/tbody")
        element.click()
        page.keyboard.press("Enter")
        time.sleep(5)
        for _ in range(9):
            page.keyboard.press("Tab")
            time.sleep(0.2)
        time.sleep(1)
        page.keyboard.press("Enter")

    download = download_info.value
    path = 'C:\\Users\\Beep Saude\\Downloads\\' + download.suggested_filename
    download.save_as(path)
    time.sleep(5)
    return path

def get_data():

    data = datetime.now()
    d = data.strftime("%d")
    m = data.strftime("%m")
    a = data.strftime("%Y")
    data = d+'-'+m+'-'+a
    return data

def upload_drive(nome, path, tipo):

    data = get_data()
    name = nome + '_' + data
    type = tipo
    google_drive().salvar_arquivo(name, path, type)

def upload_drive_min_max(nome, path, tipo):

    data = get_data()
    name = 'Min-Max ' + nome + '_' + data
    type = tipo
    google_drive().salvar_arquivo(name, path, type)

def controlador():
        lab = [
            'RECIFE_PE_1760',
            #'BARRA_RJ_0608',
            #'SC_RJ_1256',
            #'TATUAPE_SP_1337',
            #'VL_OLIMPIA_SP_0446',
            #'ALPHAVILLE_SP_1094',
            #'SBERNARDO_SP_1175',
            #'CAMPINAS_SP_1507',
            #'BRASILIA_DF_0950'
        ]

        sv = [
            'RECIFE_PE_1760',
            #'BARRA_RJ_0608',
            #'SC_RJ_1256',
            #'TATUAPE_SP_1337',
            #'VL_OLIMPIA_SP_0446',
            #'ALPHAVILLE_SP_1094',
            #'SBERNARDO_SP_1175',
            #'CAMPINAS_SP_1507',
            #'BRASILIA_DF_0950'
        ]
        hubs_lab = []
        hubs_sv = []

        for hub in lab:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                realizar_login(page)
                acessar_contagens_ciclos(page)
                pagina_ferramenta(page)
                processos_programados(page)
                encontrar_e_digitar_hub(page, hub,"LAB")  # Realize ações para o hub
                num_proc = numero_processo(page)
                atualizar(page)
                path = encontrar_arquivo_download(page)
                nome_hub = hub[:-8]
                upload_drive_min_max('lab', path, nome_hub)
                processos_programados_segundo(page)
                encontrar_segundo(page, num_proc)
                atualizar2(page)
                processos_programados_terceito(page)
                encontrar_e_digitar_hub_terceiro(page, hub,"LAB")
                atualizar2(page)
                path = encontrar_arquivo_download(page)
                nome_hub = hub[:-8]
                upload_drive('lab', path, nome_hub)

            print("Processo finalizado!")

        for hub in sv:
            with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)
                page = browser.new_page()

                realizar_login(page)
                acessar_contagens_ciclos(page)
                pagina_ferramenta(page)
                processos_programados(page)
                encontrar_e_digitar_hub(page, hub,"SV")  # Realize ações para o hub
                num_proc = numero_processo(page)
                atualizar(page)
                path = encontrar_arquivo_download(page)
                nome_hub = hub[:-8]
                upload_drive_min_max('sv', path, nome_hub)
                processos_programados_segundo(page)
                encontrar_segundo(page, num_proc)
                atualizar2(page)
                processos_programados_terceito(page)
                encontrar_e_digitar_hub_terceiro(page, hub,"SV")
                atualizar2(page)
                path = encontrar_arquivo_download(page)
                nome_hub = hub[:-8]
                upload_drive('sv', path, nome_hub)

            print("Processo finalizado!")

# Chame a função controladora para iniciar o processo
controlador()