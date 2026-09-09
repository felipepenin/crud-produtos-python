import time

def menu():
    print('=== SUPERMERCADOS BZ ===')
    print()
    print('1 - Adicionar')
    print('2 - Remover')
    print('3 - Editar')
    print('4 - Buscar')
    print('5 - Listar')
    print('6 - Sair')
    print()

    while True:
        try:
            opcao = int(input('Digite uma opção: '))
            print()
            break
        except ValueError:
            print('ERRO: Digite uma opção válida!')

    return opcao


def adicionar(lista):
    produtos = {}

    produtos['nome'] = input('Nome: ')
    produtos['valor'] = float(input('Valor: '))
    produtos['quantidade'] = int(input('Quantidade: '))

    lista.append(produtos)


def remover(lista):
    while True:
        produto = input('Nome: ')
   
        for item in lista:
            if item['nome'] == produto:
                lista.remove(item)

                print('removendo..')
                time.sleep(2)
                print('Produto removido com sucesso!')
                return
            
        print('Produto não encontrado!')
        print('Tente novamente!')
        print()


def editar(lista):
    while True:
        encontrou = False

        produto = input('Nome: ')

        for item in lista:
            if item['nome'] == produto:
                encontrou = True

                novo_nome = input('Nome: ')

                while True:
                    try:
                        novo_valor = float(input('Valor: '))
                        break
                    except ValueError:
                        print('Digite um valor válido!')

                while True:
                    try:
                        nova_quantidade = int(input('Quantidade: '))
                        break
                    except ValueError:
                        print('Digite uma quantidade válida!')
                    
                item['nome'] = novo_nome
                item['valor'] = novo_valor
                item['quantidade'] = nova_quantidade

                print('Produto editado com sucesso!')
                return
                
        if not encontrou:
            print('ERRO: Produto não encontrado!')


def buscar(lista):
        encontrou = False

        produto = input('Nome: ').strip()

        for item in lista:
            if item['nome'] == produto:
                print(f'{item["nome"]} | R${item["valor"]:.2f} | {item["quantidade"]} itens')
                encontrou = True
                break

        if not encontrou:
            print('Produto não encontrado!')


def listar(lista):
    for i, item in enumerate(lista):
        print(f'{i + 1} - {item["nome"]} | R${item["valor"]:.2f} | {item["quantidade"]} itens')

        
            

            

