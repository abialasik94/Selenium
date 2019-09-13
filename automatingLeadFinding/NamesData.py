from Google import Create_Service
import pandas as pd

def getName():

    CLIENT_SECRET_FILE = 'client_secret.json'
    API_SERVICE_NAME = 'sheets'
    API_VERSION = 'v4'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    gsheetId = '1H3KBMR6J5UBxQStSi1GGUbnHiG5MMSsVBO1if2MsKQk'

    s = Create_Service(CLIENT_SECRET_FILE, API_SERVICE_NAME, API_VERSION, SCOPES)
    gs = s.spreadsheets()
    rows = gs.values().get(spreadsheetId=gsheetId, range='Local Government').execute()
    data = rows.get('values')
    df = pd.DataFrame(data)
    return(df[0] + ' ' + df[1])

names = getName()
print(names)
