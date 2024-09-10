library = []

def add_book(library, title, author):
    library.append({
        'title': title,
        'author': author
    })

    print(f'O livro {title} foi cadastrado com sucesso!\n')

def list_books(library):
    if(len(library) == 0):
        print('Não há livros.\n')
        return

    for book in library:
        print(f'Livro "{book['title']}", Autor "{book['author']}"')
    
    print('\n')

def find_book_by_title(library, title):
    if(len(library) == 0):
        print('Não há livros.\n')
        return
    
    for book in library:
        if(book['title'] == title):
            print(f'Livro "{book['title']}", Autor "{book['author']}" \n')
            return

    print(f'Livro {title} não encontrado!\n')
    
def main():

    print('Seja bem-vindo(a) \n')

    while True:

        print('1. Adicionar um livro')
        print('2. Listar todos os livros')
        print('3. Buscar um livro por título')
        print('0. Sair')

        option = input('\nEscolha um opção: ')

        if(option == '0'):
            print('Até mais!')
            break
        elif(option == '1'):
            title = input('Digite o nome do livro: ')
            author = input(f'Digite o nome do author do livro {title}: ')

            add_book(library, title, author)
        elif(option == '2'):
            list_books(library)
        elif(option == '3'):
            title = input('Digite o nome do livro que deseja encontrar: ')

            find_book_by_title(library, title)
main()









### Lucca :)