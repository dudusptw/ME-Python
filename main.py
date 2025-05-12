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
