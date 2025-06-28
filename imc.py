def calcular_imc(peso, altura):
    """
    Calcula o Índice de Massa Corporal (IMC) de uma pessoa.

    Parâmetros:
        peso (float): O peso da pessoa em quilogramas (kg).
        altura (float): A altura da pessoa em metros (m).

    Retorna:
        float: O valor do IMC.

    Levanta:
        ValueError: Se a altura for menor ou igual a zero, ou maior que 2.50 metros.
    """
    if altura <= 0:
        raise ValueError("A altura precisa ser um valor positivo, maior que zero.")
    if altura > 2.50:
        raise ValueError("Digite uma altura aceitável, menor ou igual a 2.50 metros.")
    return peso / (altura ** 2)

def classificar_imc(imc):
    """
    Classifica o IMC de acordo com as diretrizes da Organização Mundial da Saúde (OMS).

    Parâmetros:
        imc (float): O valor do IMC a ser classificado.

    Retorna:
        tuple: Uma tupla contendo a categoria do IMC e uma recomendação.
    """
    if imc < 18.5:
        categoria = "Baixo peso"
        recomendacao = "É recomendado procurar um médico para avaliação."
    elif 18.5 <= imc <= 24.9:
        categoria = "Peso adequado"
        recomendacao = "Tudo indica que está tudo bem."
    elif 25.0 <= imc <= 29.9:
        categoria = "Sobrepeso"
        recomendacao = "O sobrepeso está associado ao risco de doenças como diabetes e hipertensão."
    elif 30.0 <= imc <= 34.9:
        categoria = "Obesidade grau I"
        recomendacao = "É importante buscar orientação médica e nutricional para entender melhor o seu caso."
    elif 35.0 <= imc <= 39.9:
        categoria = "Obesidade grau II"
        recomendacao = "Indica um quadro de obesidade mais evoluído, deve busca por orientação médica e nutricional."
    else:
        categoria = "Obesidade grau III"
        recomendacao = "Nesse ponto, a chance de já estarmos diante de outras doenças associadas é mais elevada. É fundamental buscar orientação médica."
    return categoria, recomendacao

if __name__ == "__main__":
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

    except ValueError as e:
        print(f"Erro de entrada: {e}. Por favor, verifique os valores digitados para peso e altura.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")