lista = ['frutas','ovos','leite',1,2,3,4,'macarrão']

# Buscar strings em uma lista
'''
for item in lista:
    if type(item) == str:
        print(item.upper())
'''    
lista_de_nomes = ['Ana Paula', 'ana', 'Elias', 'elias josé']
lista_de_nomes +=  ['José', 'Maria', 'Orlando', 'José', 'José Maria']
lista_de_nomes +=  ['Roberto Carlos', 'Mariana', 'Pedro', 'Pedro Antonio']
# Buscar nomes que comecem com vogais
'''
for nome in lista_de_nomes:
    if nome[0].upper() in 'AEIOU':
        print(nome)
    if nome[0].upper() in ['A','E','I','O','U']:
        print(nome.capitalize())
'''
# Buscar apenas os nomes compostos
for nome in lista_de_nomes:
    if ' ' in nome:
        print(nome)

# Buscar apenas os nomes compostos e armazenar em uma sublista
# chamada lista_nomes_compostos
lista_nomes_compostos = []
for nome in lista_de_nomes:
    if len(nome.split(' ')) > 1:
        print(nome.upper())
        lista_nomes_compostos.append(nome)


lista_nomes_idades = [] 
lista_nomes_idades.append(('José',20))
lista_nomes_idades.append(('José',20))
lista_nomes_idades.append(('Antonio',30))
lista_nomes_idades.append(('Carlos',25))
lista_nomes_idades.append(('Maria',25))  
lista_nomes_idades.append(('Maria Antonia',25))
lista_nomes_idades.append(('Maria',25))  
lista_nomes_idades.append(('Antonio',30))

# Remover as tuplas duplicadas na lista lista_nomes_idades

# Spoiler: tipo SET