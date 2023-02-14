#Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
maioridade = 0
homens = 0
mulheres = 0
while True:
    pergunta_cadastro = 'CADASTRE UMA PESSOA'
    print('-' * len(pergunta_cadastro))
    print(pergunta_cadastro)
    print('-' * len(pergunta_cadastro))

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    print('-' * 30)
    repeat = ' '
    while repeat not in 'SN':
        repeat = str(input('Quer continuar [s/n]? ')) .upper() .strip()[0]
    if idade > 18:
        maioridade +=1
    if sexo in 'M':
        homens += 1
    if sexo in 'F' and idade < 20:
        mulheres += 1
    if repeat == 'N':
        break

print(f'Temos {maioridade} pessoas tem mais de 18 anos.')
print(f'O total de homens cadastrados foi {homens}.')
print(f'Das mulheres cadastradas, {mulheres} têm menos de 20 anos.')
print('FIM DO PROGRAMA!!')