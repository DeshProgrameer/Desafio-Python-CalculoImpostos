def calcular_imposto(salario):
    aliquota = 0.0
    if 0 <= salario <= 1100:
        aliquota = 0.00
    elif 1100.01 <= salario <= 2500.00:
        aliquota = 0.10
    else:
        aliquota = 0.15

    return aliquota * salario

valor_salario = float(input("Digite o valor do salário: "))
valor_beneficios = float(input("Digite o valor dos benefícios: "))

valor_imposto = calcular_imposto(valor_salario)

saida = valor_salario - valor_imposto + valor_beneficios
print(f'O valor líquido é: R${saida:.2f}')