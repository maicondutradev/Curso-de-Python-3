def valida_cpf(cpf):
    # Remove caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verifica se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 11 - resto if resto > 1 else 0

    # Verifica o primeiro dígito verificador
    if digito1 != int(cpf[9]):
        return False

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 11 - resto if resto > 1 else 0

    # Verifica o segundo dígito verificador
    if digito2 != int(cpf[10]):
        return False

    # Se chegou até aqui, o CPF é válido
    return True

# Exemplo de uso
cpf_input = input("Digite o CPF (apenas números): ")
if valida_cpf(cpf_input):
    print("CPF válido!")
else:
    print("CPF inválido.")
