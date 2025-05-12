numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]

def estatisticas(lista):

    media = sum(lista) / len(lista)
    
    maior = max(lista)
    menor = min(lista)
    
    pares = len([num for num in lista if num % 2 == 0])

    print(f'Média: {media}')
    print(f'Maior número: {maior}')
    print(f'Menor número: {menor}')
    print(f'Quantidade de números pares: {pares}')

estatisticas(numeros)
