import os
try:
    import requests
    import json
    import pandas as pd
    import urllib.parse
    from datetime import datetime
    import pytz
except:
    print("Algumas biblioteca não estão instaladas. Instalando as dependências...")
    path = os.getcwd()
    os.chdir(path)
    os.system('pip install requests')
    os.system('pip install pandas')
    os.system('pip install pytz')
    os.system('pip install urllib')
    os.system('pip install openpyxl')
    print("Dependências instaladas com sucesso.")

import requests
import json
import pandas as pd
import urllib.parse
from datetime import datetime
import pytz
from drive_inventario import google_drive

user_banco = 'mariana_maciel'
senha_banco = '2qSM21thGDbof2H'

def time_print(text):
    now = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%H:%M:%S')
    print(f'[{now}] {text}')

headers = {
    'Content-Type': 'application/vnd.oracle.adf.resourceitem+json'
}

def create_auth():
    auth = ('rafael.fernandes@beepsaude.com.br', 'Beep7792')
    return auth

def upload_drive(path, nome, cycle_count_name):

    name = nome
    path = path
    list = cycle_count_name.split()
    type = list[-1]
    google_drive().salvar_arquivo(name, path, type)

def create_engine():
    import sqlalchemy
    engine_bi = sqlalchemy.create_engine(f"postgresql://{user_banco}:{senha_banco}@data-services.beepapp.com.br/beepsaude", echo=False)
    return engine_bi

server_url = 'https://fa-evcj-saasfaprod1.fa.ocs.oraclecloud.com'
auth = create_auth()
engine_bi = create_engine()
df_total = pd.DataFrame()
df_inv = pd.read_excel('./Listagens de Inventário.xlsx', engine='openpyxl')


def exec():

    for index, row in df_inv.iterrows():

        offset = 0
        limit = 100
        terminou = False

        df = pd.DataFrame()

        cycle_count_name = row['Nome da Contagem'] #'ALMOX - LAB - TATUAPÉ'
        encoded_cycle_count_name = urllib.parse.quote(cycle_count_name)

        organization_name = row['Organização de Estoque'] #'TATUAPE_SP_1337'
        encoded_organization_name = urllib.parse.quote(organization_name)

        time_print(f'{organization_name.replace("/", "-")} - {cycle_count_name.replace("/", "-")}')

        while not terminou:

            path_url = f'''/fscmRestApi/resources/11.13.18.05/cycleCountSequenceDetails?offset={offset}&limit={limit}&q=OrganizationName={encoded_organization_name};CycleCountName={encoded_cycle_count_name};CountSequenceStatus={urllib.parse.quote("Pending count")}+or+{urllib.parse.quote("Recount")}'''

            url = server_url + path_url

            response = requests.get(url, headers=headers, auth=auth)
            response_json = json.loads(response.text)

            if response_json['hasMore'] == False:
                terminou = True
            else:
                offset += response_json['limit']

            df = pd.concat([
                df,
                pd.DataFrame(response_json['items'])
            ])

        if len(df.index) > 0:

            df = df[[
                'CycleCountName',
                'OrganizationName',
                'CountSequence',
                'ItemNumber',
                'ItemDescription',
                'Subinventory',
                'LotNumber',
                'CountQuantity',
                'CountUOM'
            ]].rename(columns={
                'CycleCountName': 'Nome da Contagem',
                'OrganizationName': 'Organização',
                'CountSequence': 'Sequência de Contagem',
                'ItemNumber': 'Item',
                'ItemDescription': 'Descrição',
                'Subinventory': 'Subinventário',
                'LotNumber': 'Lote',
                'CountQuantity': 'Quantidade da Contagem',
                'CountUOM': 'Unidade de Medida',
            }).sort_values(
                by=['Item'],
                ascending=[True]
            )

            df.to_excel(f'./Listagens de Inventário/{organization_name.replace("/", "-")} - {cycle_count_name.replace("/", "-")}.xlsx', index=False)

            path = f'./Listagens de Inventário/{organization_name.replace("/", "-")} - {cycle_count_name.replace("/", "-")}.xlsx'
            nome = cycle_count_name.replace("/", "-")
            upload_drive(path, nome, cycle_count_name)
