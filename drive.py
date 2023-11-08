from __future__ import print_function

import os.path
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

# If modifying these scopes, delete the file token.json.

class google_drive():
    def __init__(self):
        self.scope = ['https://www.googleapis.com/auth/drive']
        self.service_account_json_key = r"C:\Users\Beep Saude\Documents\projetos\credentials.json"
        self.credentials = service_account.Credentials.from_service_account_file(
                                    filename=self.service_account_json_key,
                                    scopes=self.scope)
        self.service = build('drive', 'v3', credentials=self.credentials)

    def id_pasta(self, nome):

        filtro = f"'{nome}' in parents and mimeType='application/vnd.google-apps.folder'"

        try:
            resultado = self.service.files().list(q=filtro).execute()
            pastas = resultado.get('files', [])

            pasta_certa = [pasta for pasta in pastas if pasta['name'] == nome]
            print(resultado)
            print(pastas)

            if pasta_certa:
                return pasta_certa[0]['id']

        except:
            dados = {
                'name': nome,
                'mimeType': 'application/vnd.google-apps.folder',
            }
            pasta_final = self.service.files().create(body=dados, fields='id').execute()
            print(pasta_final)
            return pasta_final.get('id')

    def salvar_arquivo(self, nome, arquivo, tipo):

        pasta_id = self.id_pasta(tipo)

        # Upload do arquivo
        file_path = f'{arquivo}'  # Usando uma raw string
        media = MediaFileUpload(file_path)
        file_metadata = {'name': nome, 'parents': [pasta_id]}
        uploaded_file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return print(f'File uploaded com sucesso no ID: {uploaded_file.get("id")}')


    def teste(self):

        filtro = f"'{'13HYmQmcqx2Met81tnv-xJIIj2yJRGMcn'}' in parents and mimeType='application/vnd.google-apps.folder'"

        try:
            resultado = self.service.files().list(q=filtro, includeItemsFromAllDrives=True, supportsAllDrives=True).execute()
            print(resultado)
            pastas = resultado.get('files', [])
            pasta_certa = [pasta for pasta in pastas if pasta['name'] == 'pasta teste']

        except:
            print('erro')

        file_path = r'C:\Users\Beep Saude\Documents\projetos\requirements.txt'
        media = MediaFileUpload(file_path)
        file_metadata = {'name': 'teste', 'parents': '13HYmQmcqx2Met81tnv-xJIIj2yJRGMcn'}
        uploaded_file = self.service.files().create(body=file_metadata, media_body=media, supportsAllDrives=True, ignoreDefaultVisibility=True).execute()
        resultado = self.service.files().list(q=filtro).execute()
        pastas = resultado
        print(pastas)
        return print(uploaded_file)

google_drive().teste()

