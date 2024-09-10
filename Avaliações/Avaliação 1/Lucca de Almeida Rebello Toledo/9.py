fibonacci_sequence = []

def generate_fibonacci_sequence(length):
    for i in range(0, length):
        if(i == 0):
            fibonacci_sequence.append(0)
        elif(i == 1):
            fibonacci_sequence.append(1)
        else:
            element_one = fibonacci_sequence[i - 1]
            element_two = fibonacci_sequence[i - 2]

            fibonacci_sequence.append(element_one + element_two)


def main():

    while True:
        try:
            length = int(input('Qual o tamanho da sequência de fibonnaci você deseja? '))
            break
        except ValueError:  
            print('Você inseriu um valor inválido, tente novamente!')

    generate_fibonacci_sequence(length)

    print(f'A sequência de Fibonacci com {length} termos é: {fibonacci_sequence}')

main()










### Lucca :)