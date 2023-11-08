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
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
CURR_DIR = os.path.dirname(os.path.realpath(__file__))

class google_drive():
    def __init__(self):
        SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    r"C:\Users\Beep Saude\Documents\projetos\credentials.json", SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
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

            if pasta_certa:
                return pasta_certa[0]['id']

        except:
            dados = {
                'name': nome,
                'mimeType': 'application/vnd.google-apps.folder',
            }
            pasta_final = self.service.files().create(body=dados, fields='id').execute()
            return pasta_final.get('id')

    def salvar_arquivo(self, nome, arquivo, tipo):

        pasta_id = self.id_pasta(tipo)

        # Upload do arquivo
        file_path = f'{arquivo}'  # Usando uma raw string
        media = MediaFileUpload(file_path)
        file_metadata = {'name': nome, 'parents': [pasta_id]}
        uploaded_file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return print(f'File uploaded com sucesso no ID: {uploaded_file.get("id")}')

