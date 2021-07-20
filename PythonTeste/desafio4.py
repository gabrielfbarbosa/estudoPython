algo = input('Digite algo: ')

print('Tipo:', type(algo))
print('Apenas letras? ', algo.isalpha())
print('Apenas numeros? ', algo.isnumeric())
print('Letras e numeros? ', algo.isalnum())
