# -*- coding: utf-8 -*-
"""media.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R1l_Lpl9qOIzE_HShOf7HXZIdS9P5fky
"""

# Função para calcular a média das 3 notas
def calcular_media():
    # Recebe as 3 notas do aluno
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    # Calcula a média aritmética
    media = (nota1 + nota2 + nota3) / 3

    # Exibe o resultado
    print(f"A média do aluno é: {media:.2f}")

     # Verifica se o aluno está aprovado ou reprovado
    if media >= 6:
        print("Aprovado")
    else:
        print("Reprovado")

# Chama a função
calcular_media()
