def linha():
    print('-' * 30)


for a in range (0,5):
    aluno = str(input('Nome do aluno: '))
    nota1 = float(input('Informe a primeira nota: '))
    nota2 = float(input('Informe a segunda nota: '))


media = (nota1 + nota2) /2 

print("Média aritmética: ", media)
linha()
print('Abaixo de 4,0 = Reprovado')
linha()
print('De 4,0 até menor que 7,0 = Recuperação')
linha()
print('De 7,0 para cima = Aprovado')
linha()

qntd_aprovados = 0
qntd_reprovados = 0
recuperação = 0
media_turma = (nota1 + nota2) / 5

if media >= 7 :
        qntd_aprovados += 1
elif media >= 4:
        recuperação += 1
else:
        qntd_reprovados += 1

print("Quantidade de alunos APROVADOS: ", qntd_aprovados)
print("Quantidade de alunos em RECUPERAÇÃO: ", recuperação)
print("Quantidade de alunos REPROVADOS: ", qntd_reprovados)
print('média da turma: ', media_turma)




