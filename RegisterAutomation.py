# code explanation
## comment
### change suggestion
#### needs to be implemented
##### error

# from google sheets acess data and store in datraframe
# call functions register

import gspread
from oauth2client.service_account import ServiceAccountCredentials

import pandas as pd
# from b2w import b2wRegister
from magazineLuiza import magazineLuizaRegister,  magazineLuizaRegisterSelenium
from B2w import b2wRegister

# sheets authentication
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('devbot.json', scope)
client = gspread.authorize(creds)

# sheets acess datas client
sheet = client.open('Register Automation').sheet1
dataCustomer = sheet.get_all_records()

# convert to dataframe
dfCustomer = pd.DataFrame(dataCustomer)

# convert mei status
meiStatus = {'Sim': True, 'Não': False}
dfCustomer.replace({'MEI': meiStatus}, inplace=True)

for index, row in dfCustomer.iterrows():
    #check B2W
    # if row['B2W'] == 'Pronto para iniciar cadastro':
    #     # captura dados do dataframe para variaveis
    #     cnpj = row['CNPJ']
    #     loginEmail = row['Tribo Email']
    #     customerName = row['Cliente Nome']
    #     customerCpf = row['Cliente CPF']
    #     customerPhone = row['Cliente Telefone']
    #     customerPosition = row['Cliente Cargo']
    #     site = row['Site']
    #     mei = row['MEI']
    #     registrationState = row['Inscrição Estadual']
    #
    #     b2wRegister(cnpj, loginEmail, customerName, customerCpf, customerPhone, customerPosition, site, mei, registrationState)

    # check Magazine Luiza
    if row['Magazine Luiza'] == 'Pronto para iniciar cadastro':
        displayName = row['Nome Fantasia']
        platform = row['Plataforma']
        cnpj = row['CNPJ']
        companyName = row['Razão Social']
        tradeName = row['Nome Fantasia']
        site = row['Site']
        cep = row['CEP']

        ## by standard: same name by custumer
        officerCommercialName = row['Cliente Nome']
        officerCommercialEmail = row['Cliente Email']
        officerCommercialPhone = row['Cliente Telefone']
        officerSacName = row['Cliente Nome']
        officerSacEmail = row['Cliente Email']
        officerSacPhone = row['Cliente Telefone']
        officerFinancialName = row['Cliente Nome']
        officerFinancialEmail = row['Cliente Email']
        officerFinancialPhone = row['Cliente Telefone']
        officerLegalName = row['Cliente Nome']
        officerLegalEmail = row['Cliente Email']
        officerLegalPhone = row['Cliente Telefone']
        ## not required: responsavelTi = False
        officerTiName = None
        officerTiEmail = None
        officerTiPhone = None

        bank = row['Banco']
        agency = row['Agencia']
        agencyDigit = row['Digito Agencia']
        currentAccount = row['Conta Corrente']
        currentAccountDigit = row['Digito Conta Corrente']

        magazineLuizaRegister(displayName, platform, cnpj, companyName, tradeName, site, cep,
                              officerCommercialName, officerCommercialEmail, officerCommercialPhone,
                              officerSacName, officerSacEmail, officerSacPhone,
                              officerFinancialName, officerFinancialEmail, officerFinancialPhone,
                              officerLegalName, officerLegalEmail, officerLegalPhone,
                              officerTiName, officerTiEmail, officerTiPhone,
                              bank, agency, agencyDigit, currentAccount, currentAccountDigit)
