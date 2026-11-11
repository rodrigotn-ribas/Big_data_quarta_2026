# TODO 0: funcao filtrar_pares(numeros : list[int])
# TODO 1: percorrer a lista de numeros e criar uma lista com o numeros pares

def filtrar_pares(numeros : list[int]) -> list[int]:
    pares_list = []
    # for num in numeros:
    #     if num % 2 == 0:
    #         pares_list.append(num)
    pares_list = [num for num in numeros if num % 2 == 0]

    return pares_list

list_num = [1,2,3,4,5,6,7,8,9,10]

print(filtrar_pares(list_num))