minhas_notas = []
notas = 0
continua = 's'
n = 0

while continua == 's':
    notas = float(input('Digite a nota do aluno: '))
    continua = input('Deseja continuar?')
    
def situacao_aluno(minhas_notas):
    media = (minhas_notas) / 4
    if(media < 6):
        return 'Aprovado!'
    else:
        return 'Reprovado!'
    
result = situacao_aluno
  
for notas in range(0,n):
    print(result)