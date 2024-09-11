def calculate_cpf(cpf):
    formatted_cpf = cpf.replace('.', '').replace('-', '')

    if(len(formatted_cpf) != 11):
        print('CPF Inválido!')
        return

    list_cpf = []

    for i in formatted_cpf:
        list_cpf.append(int(i))

    total_sum = sum(list_cpf)

    if(total_sum % 2 == 0):
        print(f'O CPF {cpf} é Par!')
    else:
        print(f'O CPF {cpf} é Impar!')


try:
    cpf = input('Digite seu CPF (000.000.000-00): ')

    calculate_cpf(cpf)
except ValueError:
    print('Você inseriu um valor inválido!')










### Lucca :)