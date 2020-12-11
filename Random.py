from random import randint

num = randint(0, 100)

if (num % 2):
    print(f'É Impar: {num}')
else:
    print(f'É Par: {num}')

fatorial = 1
i = 1

#não consegui fazer com For
while i <= num:
    fatorial = fatorial*i
    i = i + 1

print("O valor de %d! eh =" %num, fatorial)

dif0 = 0 + num
dif100 = 100 - num

print(f"A diferença de {num} para 0 é de {dif0}")
print(f"A diferença de {num} para 100 é de {dif100}")
