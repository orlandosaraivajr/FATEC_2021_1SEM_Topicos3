idade = input("Digite a idade: ")
idade = int(idade)
if idade < 18:
    print("Não pode beber")
else:
    print("Pode beber, beba com moderação")

if idade < 14:
    print("Não pode entrar sem os pais.")
elif idade < 18:
    print("Pode entrar na matinê, mas não pode consumir bebidas")
else:
    print("Pode beber, beba com moderação")
