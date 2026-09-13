import time
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
ARQUIVO_JSON = BASE_DIR / 'produtos.json'

def carregar_produtos():

    try:
        with open(ARQUIVO_JSON, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

def salvar_produtos(lista):
     
     with open(ARQUIVO_JSON, 'w', encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)

lista = carregar_produtos()

def menu():
    print(
        '\n========================================='
        '\n     Sistema de controle de estoque      '
        '\n========================================='
        '\n1 - Adicionar novo produto'
        '\n2 - Remover produto do estoque'
        '\n3 - Editar produto em estoque'
        '\n4 - Buscar produto em estoque'
        '\n5 - Listar estoque'
        '\n6 - Sair'
    )

    while True:
        try:
            opcao = int(input('\nDigite uma opção: '))
            break
        except ValueError:
            print('\nERRO: Digite uma opção válida!')

    return opcao


def adicionar(lista):
    produtos = {}

    produtos['nome'] = input('\nNome do novo produto: ').strip()

    while True:
        try:
            produtos['valor'] = float(input('\nDigite o valor do produto: R$').replace(',','.'))
            break
        except ValueError:
            print('\nDigite um valor válido!')

    while True:
        try:
            produtos['quantidade'] = int(input('\nQuantidade: '))
            break
        except ValueError:
            print('\nDigite um valor válido!')

    lista.append(produtos)
    salvar_produtos(lista)


def remover(lista):
    while True:
        produto = input('\nNome do produto que deseja remover: ').strip().lower()
   
        for item in lista:
            if item['nome'].lower() == produto:
                lista.remove(item)
                salvar_produtos(lista)

                print('\nremovendo..')
                time.sleep(2)
                print('\nProduto removido com sucesso!')
                return
            
        print('\nProduto não encontrado!')
        print('\nTente novamente!')


def editar(lista):
    while True:
        encontrou = False

        produto = input('\nProduto que deseja editar: ').strip().lower()

        for item in lista:
            if item['nome'].lower() == produto:
                encontrou = True

                novo_nome = input('\nNovo nome: ')

                while True:
                    try:
                        novo_valor = float(input('Novo valor: R$'))
                        break
                    except ValueError:
                        print('\nDigite um valor válido!')

                while True:
                    try:
                        nova_quantidade = int(input('Nova quantidade: '))
                        break
                    except ValueError:
                        print('\nDigite uma quantidade válida!')
                    
                item['nome'] = novo_nome
                item['valor'] = novo_valor
                item['quantidade'] = nova_quantidade
                salvar_produtos(lista)

                print('Produto editado com sucesso!')
                return
                
        if not encontrou:
            print('\nERRO: Produto não encontrado!')


def buscar(lista):
        encontrou = False

        produto = input('\nBuscar produto: ').strip().lower()

        for item in lista:
            if item['nome'].lower() == produto:
                print(f'{item["nome"]} | R${item["valor"]:.2f} | {item["quantidade"]} itens')
                encontrou = True
                break

        if not encontrou:
            print('Produto não encontrado!')


def listar(lista):
    for i, item in enumerate(lista):
        print(f'{i + 1} - {item["nome"]} | R${item["valor"]:.2f} | {item["quantidade"]} itens')
        print('------------------------------')

