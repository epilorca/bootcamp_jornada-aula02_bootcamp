# #### try-except e if

# 21: Conversor de Temperatura

try:
    temperatura = input("Digite qual a temperatura usar para conversão: C (Celsius), F (Farenheit), K (Kelvin): ").upper()

    if temperatura not in ["C", "F", "K"]:
        print("Você deve digitar C, F ou K")
        exit()

    if temperatura == "C":
        celsius = float(input("Digite a temperatura desejada: "))

        farenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15

        print(f"Conversão de Celsius para Farenheit é {farenheit:.2f}")
        print(f"Conversão de Celsius para Kelvin é {kelvin:.2f}")

    elif temperatura == "F":
        farenheit = float(input("Digite a temperatura desejada: "))

        kelvin = (farenheit - 32) / 1.8 + 273.15
        celsius = (farenheit - 32) * 5/9

        print(f"A conversão de Farenheit para Kelvin é {kelvin:.2f}")
        print(f"A conversão de Farenheit para Celsius é {celsius:.2f}")

    elif temperatura == "K":
        kelvin = float(input("Digite a temperatura desejada: "))

        celsius = kelvin - 273.15
        farenheit = (kelvin - 273.15) * 9/5 + 32

        print(f"A conversão de Farenheit para Kelvin é {farenheit:.2f}")
        print(f"A conversão de Kelvin para Celsius é {celsius:.2f}")

except ValueError as e:
    print(e)

# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação