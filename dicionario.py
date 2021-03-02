agenda_telefonica = {}
agenda_telefonica['orlando'] = '9999-99999' 
agenda_telefonica['gabriel'] = '8888-888888'
agenda_telefonica['ricardo'] = ('Ricardo','8888-888888')
agenda_telefonica['sheila'] = ('Sheila',(123,456)) 
registro = agenda_telefonica.get('sheila','')   

chave = 'ricardo'
if chave in agenda_telefonica:
    registro2 = agenda_telefonica[chave]

# Caso busque uma chave inexistente, gera-se um KeyError
chave = 'julia'
try:
    agenda_telefonica[chave]
except KeyError:
    print('Chave não encontrada')