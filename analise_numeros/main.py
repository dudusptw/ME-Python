# Lista fornecida de números
numeros = [10, 23, 5, 8, 12, 33, 42, 7, 19, 28, 3, 16, 9, 50, 21]

# Função que calcula e exibe as estatísticas
def estatisticas(lista):
    # Cálculo da média
    media = sum(lista) / len(lista)
    
    # Identificação do maior e menor número
    maior = max(lista)
    menor = min(lista)
    
    # Contagem de números pares
    pares = len([num for num in lista if num % 2 == 0])

    # Exibindo os resultados
    print(f'Média: {media}')
    print(f'Maior número: {maior}')
    print(f'Menor número: {menor}')
    print(f'Quantidade de números pares: {pares}')

# Chamando a função com a lista fornecida
estatisticas(numeros)
