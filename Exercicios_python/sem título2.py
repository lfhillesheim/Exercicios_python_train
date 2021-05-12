"""
Dados n e n seqüências de números inteiros não-nulos,
cada qual seguida por um 0,
calcular a soma dos números pares de cada seqüência.
"""

n = int(input("Digite o número de sequências: "))

for cont in range(n):
    n2 = int(input("Digite o tamanho desa sequência ")) 
    soma = 0
    soma_aux = soma
    for cont2 in range(n2):
        num=int (input("Digite o número de sequências: "))
        if num % 2 == 0:
            soma+= num
    print("A soma dessa sesquencias é", soma)
    print("E o soma de todas as sequencias é igual a: ")
    cont += 1
    
    