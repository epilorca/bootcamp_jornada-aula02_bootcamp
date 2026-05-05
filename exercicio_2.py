# #### try-except e if

# 21: Conversor de Temperatura

# try:
#     temperatura = input("Digite qual a temperatura usar para conversão: C (Celsius), F (Farenheit), K (Kelvin): ").upper()

#     if temperatura not in ["C", "F", "K"]:
#         print("Você deve digitar C, F ou K")
#         exit()
    
#     if temperatura == "C":
#         celsius = float(input("Digite a temperatura desejada: "))

#         farenheit = (celsius * 9/5) + 32
#         kelvin = celsius + 273.15

#         print(f"Conversão de Celsius para Farenheit é {farenheit:.2f}")
#         print(f"Conversão de Celsius para Kelvin é {kelvin:.2f}")

#     elif temperatura == "F":
#         farenheit = float(input("Digite a temperatura desejada: "))

#         kelvin = (farenheit - 32) / 1.8 + 273.15
#         celsius = (farenheit - 32) * 5/9

#         print(f"A conversão de Farenheit para Kelvin é {kelvin:.2f}")
#         print(f"A conversão de Farenheit para Celsius é {celsius:.2f}")

#     elif temperatura == "K":
#         kelvin = float(input("Digite a temperatura desejada: "))

#         celsius = kelvin - 273.15
#         farenheit = (kelvin - 273.15) * 9/5 + 32

#         print(f"A conversão de Farenheit para Kelvin é {farenheit:.2f}")
#         print(f"A conversão de Kelvin para Celsius é {celsius:.2f}")

# except ValueError:
#     print("Digite um número válido para a temperatura.")

# 22: Verificador de Palíndromo

# entrada = input("Digite uma palavra ou frase: ")
# limpa = entrada.replace(" ", "")

# if limpa.isalpha():
#     formatado = limpa.lower()

#     if formatado == formatado[::-1]:
#         print("É um palíndromo!")
#     else:
#         print("Não é um palíndromo!")
# else:
#     print("Entrada inválida! Digite apenas letra.")
# 23: Calculadora Simples

# try:
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))

#     operador = input("Digite o operador desejado: +, -, /, *: ")

#     if operador == "+":
#         resultado = num1 + num2
#     elif operador == "-":
#         resultado = num1 - num2
#     elif operador == "/":
#         resultado = num1 / num2
#     elif operador == "*":
#         resultado = num1 * num2
#     else:
#         print("Operador inválido!")
#         exit()

#     print("Resultado:", resultado)

# except ValueError:
#     print("Erro: entrada inválida.")
# except ZeroDivisionError:
#     print("Erro: divisão por zero não é permitida.")

# 24: Classificador de Números
# try:
#     num = int(input("Digite um número inteiro: "))
#     print(f"Número digitado: {num}")
#     if num < 0:
#         print("Número negativo.")
#     elif num > 0:
#         print("Número positivo!")
#     else:
#         print("Zero!")
#     if num % 2 == 0:
#         print("Número PAR.")
#     else:
#         print("Número IMPAR.")

# except ValueError:
#     print("Erro. Digite um número inteiro.")

# 25: Conversão de Tipo com Validação

entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numero_str = entrada_lista.split(",")
numero_int = []
try:
    for num in numero_str:
        numero_int.append(int(num.strip()))
    print("Lista de inteiros:", numero_int)
except ValueError:
    print("Erro. Certifique-se de que todos os elementos são números inteiros válidos.")