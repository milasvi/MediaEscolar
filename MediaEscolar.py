
from tkinter import N


print('-' * 23)
print('Escola Santa paciência')
print('-' * 23)

print('A média da Escola é 7.')
nota1 = int(input('Digite a primeira nota:'))
nota2 = int(input('Digite a segunda nota'))
media = (nota1 + nota2) / 2

if media > 7:
    print(f'A média foi de {media}. O alune foi aprovado, parabéns!')
else:
    print(f'A média foi de {media}. O alune ficou de recuperação, que pena!')