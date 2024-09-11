grades = []

while True:
    try:
        for i in range(0, 4):
            grade = int(input('Insira uma nota: '))
            grades.append(grade)
        
        break
    except ValueError:
        print('Você inseriu um valor inválido, tente novamente!')

average = sum(grades) / len(grades)

if(average >= 7):
    print('APROVADO')
else:
    print('Enviado para a prova final! \n')

    while True:
        try:
            grade = int(input('Insira a nota final: '))
            grades.append(grade)

            break
        except ValueError:
            print('Você inseriu um valor inválido, tente novamente!')
    
    average = sum(grades) / len(grades)

    if(average > 5):
        print('APROVADO')
    else:
        print('REPROVADO')








### Lucca :)