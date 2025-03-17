#Crie um programa que solicite três números do tipo float e, utilizando as funções built-in max() e min(), exiba qual deles é o maior e qual é o menor.
n1 = float(input("Digite um número: "))
n2 = float(input("Digite um número: "))
n3 = float(input("Digite um número: "))

lista = [n1,n2,n3]

maximo = max(lista)
minimo = min(lista)

print(f"Da lista {lista} o valor mínimo é {minimo} e o máximo é {maximo}.")
