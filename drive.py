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


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())


if __name__ == '__main__':
    main()

class google_drive():
    def __init__(self):
        self.scope = ['https://www.googleapis.com/auth/drive']
        self.service_account_json_key = 'credentials.json'
        self.credentials = service_account.Credentials.from_service_account_file(
                                    filename=self.service_account_json_key, 
                                    scopes=self.scope)
        self.service = build('drive', 'v3', credentials=self.credentials)

    def id_pasta(self, nome):

        filtro = f"'{nome}' in parents and mimeType='application/vnd.google-apps.folder'"
        resultado = self.service.files().list(q=filtro).execute()
        pastas = resultado.get('files', [])

        pasta_certa = [pasta for pasta in pastas if pasta['name'] == nome]

        if pasta_certa:
            # Já existe uma pasta com a data de hoje, use-a
            return pasta_certa[0]['id']


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

