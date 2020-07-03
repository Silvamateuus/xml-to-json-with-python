import xmltodict
import json
import os
import os.path


if not os.path.exists('folder_json'):
    
    os.mkdir('folder_json')
    
funcionalidades = ['TESTS-login','TESTS-parametro_de _volatilidade_correlacao']

for x in funcionalidades:
    
    resultado = x

    with open('folder_xmls/' + resultado + '.xml') as in_file:
        
        xml = in_file.read()
        
        with open('folder_json/'+ resultado + '.json', 'w') as out_file:
        
            json.dump(xmltodict.parse(xml), out_file)
        
        with open('folder_json/' + resultado +'.json', 'r') as out_file:
        
            dir = './json' 
        
            data = json.load(out_file)

    j = (data['testsuite'])
    

    # Exibição dos reports das features através do arquivo json gerado
    print ('|--------------------------')

    nome = j['@name']
    print (f'|Feature: {nome}')
    print ('|--------------------------')

    qnt_cenario = j['@tests']
    print (f'|Scenarios: {qnt_cenario}' )
    print ('|--------------------------')

    erros =  j['@errors']
    print (f'|Errors: {erros}')
    print ('|--------------------------')

    nao_passou = j['@skipped']
    print (f'|Skipped: {nao_passou}')
    print ('|--------------------------')

    falhou = j['@failures']
    print (f'|Failures: {falhou}')
    print ('|--------------------------')

    browser = 'Google Chrome'
    print (f'|Browser: {browser}'       )
    print ('|--------------------------')

    data_exe = j['@timestamp']
    print ('|Execution Date: {data_exe}')
    print ('|--------------------------')



