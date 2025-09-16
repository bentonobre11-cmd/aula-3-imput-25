print("Atividade: Operações Aritméticas")

# Solicita ao usuário que digite o primeiro número
numero1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário que digite o segundo número
numero2 = float(input("Digite o segundo número: "))

# Calcula a soma
soma = numero1 + numero2

# Calcula a subtração
subtracao = numero1 - numero2

# Calcula a multiplicação
multiplicacao = numero1 * numero2

# Calcula a divisão
# Verifica se o segundo número não é zero para evitar erro de divisão por zero
divisao = numero1 / numero2 if numero2 != 0 else "Divisão por zero não é permitida"

# Exibe os resultados
print(f"\nSoma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")


