print('')
print('{:=^80}'.format(' Exercício Python 77'))
print('Crie um programa que tenha uma tupla com várias palavras (não usar acentos).')
print('Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais')
print()


lista =(
        'APREENDER','PROGRAMAR','LINGUAGEM',
        'PYTHON','CURSO','GRATIS',
        'ESTUDAR','PRATICAR','TRABALHAR',
        'MERCADO','PROGAMADOR','FUTURO')


for i in lista:
        tamanho = len(i)
        print(i[0:tamanho])
