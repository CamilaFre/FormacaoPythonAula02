#Crie um programa que solicite uma palavra e, utilizando as funções built-in len() e upper(), exiba o tamanho da palavra e a palavra em letras maiúsculas.

palavra = input("Digite uma palavra: ")

tamanho = len(palavra)

print(f"A palavra {palavra.upper()} tem {tamanho} letras.")