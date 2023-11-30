from __future__ import print_function


import os
try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    from googleapiclient.http import MediaFileUpload
    from google.oauth2 import service_account
except ImportError:
    print("Algumas biblioteca não estão instaladas. Instalando as dependências...")
    os.system("pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib")
    print("Dependências instaladas com sucesso.")

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
        self.service_account_json_key = "credentials.json"
        self.credentials = service_account.Credentials.from_service_account_file(
                                    filename=self.service_account_json_key,
                                    scopes=self.scope)
        self.service = build('drive', 'v3', credentials=self.credentials)


    def salvar_arquivo(self, nome, arquivo, tipo):

        if tipo =="BARRA":
            pasta_id = "1YKUjRtRjYuJK0KJcihSQReCVumw-9jvY"
        elif tipo =="SC":
            pasta_id = "1NZ95WW1ht2BQxOKn8PC6KXIyd5w_7Q3A"
        elif tipo =="TATUAPÉ":
            pasta_id = "1s3y8lA99TZ3EU0x6ZbK_Qr18bWzM32SG"
        elif tipo =="OLÍMPIA":
            pasta_id = "1ip05OGxp0cmcSMYpQ92CGE6df_bloQPM"
        elif tipo =="ALPHAVILLE":
            pasta_id = "1tbCtw-CQx-omuN2PlKPC7y-AHm5Fi9Fs"
        elif tipo =="S.BERNARDO":
            pasta_id = "1otOJwTXw30iHO_0F9qmcV_7y7jsIKpQq"
        elif tipo =="CAMPINAS":
            pasta_id = "1zBeS_ZBJ4X5jQ3XkgwTSpqQL_xMfB_xl"
        elif tipo =="BRASÍLIA":
            pasta_id = "1mFGK86BPKsrnCIiyI9lPd5wPpGflegUl"


        # Upload do arquivo
        file_path = f'{arquivo}'  # Usando uma raw string
        media = MediaFileUpload(file_path)
        file_metadata = {'name': nome, 'parents': [pasta_id]}
        uploaded_file = self.service.files().create(body=file_metadata, media_body=media).execute()
        return print(f'File uploaded com sucesso no ID: {uploaded_file.get("id")}')

