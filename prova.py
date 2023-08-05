minhas_notas = []
notas = 0
continua = 's'

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
print(f'Situação do aluno{result}')