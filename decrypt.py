## Decrypting the blind test
company = {}
department = {}
municipality = {}
field = {}
contract = {}

#Step zero: Count appearances of companies, contracts, and fields in 2018 file

#First step: Selecting companies with 23 or more contracts 
company_possible = ['ECOPETROL S.A.','Frontera Energy Colombia Corp Sucursal Colombia',
    'HOCOL S.A.','OCCIDENTAL DE COLOMBIA LLC', 'PERENCO COLOMBIA LIMITED']

#Second step: Which companies have a contract with 8 or more appearences? Contract: '1f-d2689f'
company_possible = ['ECOPETROL S.A.','Frontera Energy Colombia Corp Sucursal Colombia'
    ,'OCCIDENTAL DE COLOMBIA LLC', 'PERENCO COLOMBIA LIMITED']

#Third step: Which entries have the same contract and field name?
company_possible = ['ECOPETROL S.A.','OCCIDENTAL DE COLOMBIA LLC']

#Fourth step: Which entry have more than 1 appeareance (two different municipalities)
company.update({'d5580f74': "OCCIDENTAL DE COLOMBIA LLC"})

department.update({'cf33cb8a':'ARAUCA'})

municipality.update({'cf33cb8a':'ARAUCA',
                     '102a28a6':'ARAUQUITA'})

field.update({'1f-d2689f':'CHIPIRÓN',
              '1fd2689f' :'CHIPIRÓN'})

contract.update({'1f-d2689f':'CHIPIRÓN'})

#Filling with the new findings, in ARAUCA department, there are only two municipalities in the dataframe:
# TAME and SARAVENA. However, only TAME appears twice, as in the blind test
municipality.update({'5abe4339':'TAME'})
company.update({'ffd6d24d':'PAREX RESOURCES COLOMBIA LTD. SUCURSAL'})
contract.update({'876a64fe':'CAPACHOS'})
field.update({'fd6f6562':'ANDINA',
              '876a64fe':'CAPACHOS'})

# PAREX has operations in ARAUCA and CASANARE, what gives the next key
department.update({'f7fd2c4f':'CASANARE'})

#Looking for PAREX, this company has two entries appearing twice, one of them in the same contract. Then:
municipality.update({'76acd11e':'VILLA NUEVA'})
contract.update({'81c9dc26':'CABRESTERO'})
field.update({'8dd7c41b':'BACANO',
              '82edafb9':'AKIRA'})

# and
municipality.update({'6feb5887':'SAN LUIS DE PALENQUE'})
contract.update({'73dec126':'LOS OCARROS',
                 'f67a6350':'LLA 30'})
field.update({'c98bd9dd':'ADALIA',
              '51cbb05d':'LAS MARACAS'})

#The missing entries for PAREX
municipality.update({
    '1218f7fa':'PORE',
    '21d4886b':'PAZ DE ARIPORO',
    '48399655':'AGUAZUL'})

contract.update({
    '2d2fa4e7':'LLA 16',
    'b93bf597':'LLA 40',
    '0602f724':'LLA 26'})

field.update({
    '741abe20':'KONA',
    '4d0fb45e':'BEGONIA',
    '58a0d8ca':'RUMBA' })

# Following the logic with OCCIDENTAL, apart from CHIPIRÓN, the company
# has other 3 contracts with counts of 2, 6, and 7. Accordingly, we have:

contract.update({
    '29ded6f4':'CRAVO NORTE',
    'a1fdefb8':'COSECHA',
    'ea18fc5d':'RONDÓN'})
# Comparing production between fields in a single contract:
field.update({
    '043b305e':'CAÑO YARUMAL',
    '1d31fa4e':'REDONDO ESTE',
    '2f614c0b':'CAÑO LIMÓN',
    '3f67010a':'REDONDO',
    'fca93f9e':'TONINA'})

# From COSECHA
field.update({
    '0e01f88f':'MORROCOY',
    '124207de':'FINN',
    '241d3779':'REX',
    '3f10a1f5':'CANAGUEY',
    '5559f8d7':'REX NE',
    '5dd16431':'TERECAY',
    'c6da2541':'GOLONDRINA'})

#from RONDÓN
field.update({
    'c728bf96':'CAÑO RONDÓN',
    'febb6cf6':'CARICARE',




print(contract)