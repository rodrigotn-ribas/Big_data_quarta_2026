# TODO 0: Crie um dicionario chamado estoque com 3 produtos
# TODO 1: Crie uma função adiciona_produto(produto, quatidade)
# TODO 1: DESCRIÇÃO -> se o produto já existir, some a quatidade

dict_produto = {
    "arroz": 2,
    "feijão": 3,
    "leite": 1,
                }
                
def adiciona_produto(produto, quatidade):

    if produto in dict_produto:
        dict_produto[produto] += quatidade
    else:
        dict_produto[produto] = quatidade
    
    

adiciona_produto("banana", 3)

for key, value in dict_produto.items():
        print(key, value)

new_list = [keys for keys in dict_produto]


print(new_list)