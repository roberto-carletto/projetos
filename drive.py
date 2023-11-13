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


    def salvar_arquivo(self, nome, arquivo, tipo):

        if tipo =="BARRA":
            pasta_id = "1fr2iHrqbyFjWK7M1BUzlafPCYhvfLg95"
        elif tipo =="SC":
            pasta_id = "1qCa9YMPyh21Z5tcQxoEOZLhuVPCDMBYs"
        elif tipo =="TATUAPE":
            pasta_id = "1NIgoo6T64HSzOzy_EYH96tahG_ld4Odr"
        elif tipo =="VL_OLIMPIA":
            pasta_id = "1WirHVwqJDPyJP_FHiL2twhOLKtXkldya"
        elif tipo =="ALPHAVILLE":
            pasta_id = "1Z_T4bBH1atlBYHaIvJvnbY0ABthkihk0"
        elif tipo =="SBERNARDO":
            pasta_id = "1pRaer4j5VjVvhs9MqctBmxx4k8SqElY5"
        elif tipo =="CAMPINAS":
            pasta_id = "1-IQWQEkJ__dHtfCJH2-CF2Ct1Ao0_ouT"
        elif tipo =="BRASILIA":
            pasta_id = "1OrcyfAtFWuhnKSBOIq31x1cepWjhOkYx"


        # Upload do arquivo
        file_path = f'{arquivo}'  # Usando uma raw string
        media = MediaFileUpload(file_path)
        file_metadata = {'name': nome, 'parents': [pasta_id]}
        uploaded_file = self.service.files().create(body=file_metadata, media_body=media).execute()
        return print(f'File uploaded com sucesso no ID: {uploaded_file.get("id")}')

