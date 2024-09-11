def calculate_sum_of_squares(vetor):
    
    new_list = []

    for x in vetor:
        new_list.append(x * x)

    return sum(new_list) 

def main():
    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = calculate_sum_of_squares(vetor)

    print(f'O resultado da soma dos quadrados dos elementos do vetor é: {result}')

main()










### Lucca :)