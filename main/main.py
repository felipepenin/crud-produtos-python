from funcoes import menu, adicionar, remover, editar, buscar, listar
import time

lista = []

while True:
    opcao = menu()

    match opcao:
        case 1:
            adicionar(lista)
        case 2:
            remover(lista)
        case 3:
            editar(lista)
        case 4:
            buscar(lista)
        case 5:
            listar(lista)
        case 6:
            print('Finalizando...')
            time.sleep(3)
            break
print('Finalizado! Volte sempre.')
