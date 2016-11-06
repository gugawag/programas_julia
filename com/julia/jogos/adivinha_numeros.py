import random

print('=== Olá. Meu primeiro programa: adivinhe um número entre 0 e 100 ===')
print('Programadora: Júlia Vinagre Mendes')

numero = random.randrange(0, 101)

numero_digitado = int(input('Diga um número: '))
tentativas = 1

while (True):
    if numero_digitado == numero:
        print('Está certo. Você acertou depois de', tentativas, 'tentativas')
        break

    if numero_digitado < numero:
        print('O número é maior\n')

    if numero_digitado > numero:
        print('O número é menor\n')

    numero_digitado = int(input('Diga um número: '))
    tentativas += 1

