##Suponha que você queira garantir que um conjunto de valores não seja modificado. Crie uma tupla contendo três coordenadas (x, y, z) 
# e tente alterar a coordenada y, 
## exibindo uma mensagem informativa caso ocorra erro.

tupla = ("x","y","z")

try:

    tupla[1] = "W"

except TypeError:

    print("A tupla é uma estrutura de dado imutável!!!")
    print(tupla)


