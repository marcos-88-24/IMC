def calcular_imc(peso, altura):
    if altura <= 0:
        raise ValueError("A altura precisa ser um valor positivo, maior que zero.")
    if altura > 2.40:
        raise ValueError("Digite uma altura aceitável, menor ou igual a 2.40 metros.")
    if peso <= 0:14
    if peso > 200:
        raise ValueError("Digite um peso aceitável, menor ou igual a 200 kg.")
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Baixo peso", "É recomendado procurar um médico para avaliação."
    elif 18.5 <= imc <= 24.9:
        return "Peso adequado", "Tudo indica que está tudo bem."
    elif 25.0 <= imc <= 29.9:
        return "Sobrepeso", "O sobrepeso está associado ao risco de doenças como diabetes e hipertensão."
    elif 30.0 <= imc <= 34.9:
        return "Obesidade grau I", "É importante buscar orientação médica e nutricional."
    elif 35.0 <= imc <= 39.9:
        return "Obesidade grau II", "Indica um quadro de obesidade mais evoluído, deve buscar por orientação médica."
    else:
        return "Obesidade grau III", "É fundamental buscar orientação médica."

while True:
    try:
        peso_input = input("Digite seu peso em kg (ex: 70.5): ").replace(',', '.')
        altura_input = input("Digite sua altura em metros (ex: 1.75): ").replace(',', '.')

        peso = float(peso_input)
        altura = float(altura_input)

        imc_final = calcular_imc(peso, altura)
        categoria_imc, recomendacao_imc = classificar_imc(imc_final)

        print(f"\nSeu IMC é: {imc_final:.2f} kg/m²")
        print(f"Classificação: {categoria_imc}")
        print(f"Recomendação: {recomendacao_imc}")
        break

    except ValueError as e:
        print(f"Erro de entrada: {e}. Por favor, tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
