def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True

lista_numeos = [3, 4, 8, 5, 5, 22, 13]
primos = list(filter(es_primo, lista_numeos))
print(primos)