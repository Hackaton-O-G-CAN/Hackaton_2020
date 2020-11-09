## Decrypting the blind test
company = {}
department = {}
municipality = {}
field = {}
contract = {}



################ YEAR 2018 ########################

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
field.update({'c728bf96':'CAÑO RONDÓN',
    'febb6cf6':'CARICARE'})

#missing from CHIPIRÓN
field.update({ '13276557':'ARAGUATO',
    '1ab355bf':'JIBA UNIFICADO',
    '254d7db5':'MATANEGRA OESTE',
    '9ac1420f':'GALEMBO',
    '9b395bc9':'MACANA',
    'c220f014':'BAYONERO'})

#Filtrating in CASANARE by 3 or more appearences in contracts and companies, and discarding the already identified cities
# turns out that there is only one field which stops production from March to June, what can be matched in the blind dataset

municipality.update({'16b873c5':'OROCUE'})
company.update({'2fe52430':'VETRA EXPLORACION Y PRODUCCION COLOMBIA S.A.S.'})
contract.update({'0191a2e4':'CDNDI LA PUNTA'})
field.update({'7eb34927':'JUAPE',
              '4f4a249f':'SANTO DOMINGO',
              '8ba362f3':'SANTO DOMINGO NORTE',})

#Finally, once the last company was identified, the following information can be found:

department.update({'0fa93c9b':'PUTUMAYO'})
municipality.update({'756c486f':'PUERTO ASIS'})
contract.update({'4b05ae15':'SURORIENTE'})
field.update({
    '48670499':'COHEMBI',
    '373ebdec':'QUILLACINGA',
    'e32e23a1':'QUINDE'})
###################################################

################ YEAR 2017 ########################

# Replacing known keys, looking for OCCIDENTAL DE COLOMBIA, and removing already known contracts,
# it is straightforward to identify two new mappings in the 2017 year

contract.update({'76a16657':'CHIPIRON',
                 'ab8c6300':'RONDON'})

#from RONDON

field.update({'c728bf96':'CAÑO RONDÓN',
              'febb6cf6':'CARICARE'})

#from CHIPIRÓN
field.update({'1f d2689f':'CHIPIRÓN'})


#Once OCCIDENTAL was completed, following company, PAREX, has only one municipality missing
municipality.update({'e1745f70':'VILLANUEVA'})
contract.update({'796c2e32':'CABRESTERO PAREX'})
field.update({'82edafb9':'AKIRA',
              '8dd7c41b':'BACANO',
              'b111ec69':'KITARO'})
#other contracts in known municipalities
contract.update({'5f512199':'E&P LLANOS 26',
                'e068232a':'E&P LLANOS 40',
                '1ef80899':'E&P Llanos 16 Contrato # 45',
                'af29b5ed':'E&P LLANOS 30',
                'e753d35d':'E&P LOS OCARROS PAREX'})

# from missing departments for PAREX (2 entries)
department.update({'5f559ecb':'BOYACA',
                   'eccb9ef1':'META'})
municipality.update({'95c9d783':'PUERTO BOYACA',
                     '870c4a0b':'CABUYARO'})
contract.update({'6e6815e2':'VMM-11',
                 'a3d02126':'CERRERO'})
field.update({'c6ba0174':'GLAUCA',
              '27cb99a2':'KATMANDÚ NORTE'})

#Finally, from VETRA, only an already identified city was missing (PUERTO ASIS)
contract.update({'b4dad5fa':'CPI SUR ORIENTE'})
field.update({'48670499':'COHEMBI',
              '373ebdec':'QUILLACINGA',
              'e32e23a1':'QUINDE'})

###################################################

################ YEAR 2019 ########################

contract.update({'1f d2689f':'CHIPIRÓN'})

#after assigning known values, a contract associated to VETRA was missing

contract.update({'23980b82':'LA PUNTA'})
field.update({'7eb34927':'JUAPE',
              '4f4a249f':'SANTO DOMINGO',
              '8ba362f3':'SANTO DOMINGO NORTE'})

# CHIPIRÓN contract has a new entry
field.update({'649eeafb':'JIBA'})

#CAPACHOS contract has a new entry
field.update({'d56beadb':'ANDINA NORTE'})

# Finally, there are two deparments with not assignment, but belonging to PAREX
# No filtrating by ARAUCA or CASANARE, a department with a single municipality
department.update({'ec12ad00':'CESAR'}) 
municipality.update({'dfb943a1':'RIO DE ORO'})
contract.update({'68f1a111':'FORTUNA'})
field.update({'85c1a0e5':'HABANERO',
              '5558f26e':'PIMIENTO',
              '44502c89':'TOTUMAL'})

#The last department
department.update({'657b6154':'SANTANDER'}) 

#Repeated city: RIO NEGRO
municipality.update({'a6b36c07':'RIO NEGRO',
                     '28b6a6a0':'SIMACOTA'})
contract.update({'38c31ea1':'CONVENIO BORANDA',
                 '8568d01e':'AGUAS BLANCAS'})
field.update({'11e586b4':'BORANDA',
              '8568d01e':'AGUAS BLANCAS'})


###################################################

print('\nDepartamento\n', department)
print('\nMunicipio\n', municipality)
print('\nOperadora\n', company)
print('\nContrato\n', contract)
print('\nCampo\n', field)



