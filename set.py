lista1 = [('aluno1',10), ('aluno2',20), ('aluno3',30)]   
lista2 = [('aluno4',40), ('aluno2',20), ('aluno3',30)] 
lista3 = [('aluno4',40), ('aluno2',20), ('aluno5',50)] 

#quais são os registros comuns a todas as listas ?

set1 = set(lista1)
set2 = set(lista2)
set3 = set(lista3)

set1.intersection(set2, set3) 

set1.intersection(set2).intersection(set3) 