from models import Pedido
from SistemaEntregas import SistemaEntregas


def mostrar_menu():
    print("\n=== SISTEMA DE ROTEAMENTO DE ENTREGAS ===")
    print("1 - Inserir novo pedido")
    print("2 - Listar pedidos pendentes")
    print("3 - Atribuir pedidos aos entregadores disponíveis")
    print("4 - Finalizar entrega")
    print("5 - Consultar histórico de entregas")
    print("6 - Ver entregadores")
    print("0 - Sair")


def main():
    sistema = SistemaEntregas()
    proximo_id = 1

    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            endereco = input("Digite o endereço de entrega: ")
            latitude = float(input("Digite a latitude: "))
            longitude = float(input("Digite a longitude: "))
            prioridade = input("Digite a prioridade (normal ou alta): ").strip().lower()

            if prioridade not in ["normal", "alta"]:
                print("Prioridade inválida. O pedido será cadastrado como normal.")
                prioridade = "normal"

            pedido = Pedido(
                proximo_id,
                endereco,
                (latitude, longitude),
                prioridade
            )

            sistema.adicionar_pedido(pedido)
            proximo_id += 1

        elif opcao == "2":
            sistema.listar_pedidos_pendentes()

        elif opcao == "3":
            sistema.atribuir_pedidos()

        elif opcao == "4":
            try:
                id_entregador = int(input("Digite o ID do entregador: "))
                sistema.finalizar_entrega(id_entregador)
            except ValueError:
                print("Digite um número válido para o ID do entregador.")

        elif opcao == "5":
            sistema.mostrar_historico()

        elif opcao == "6":
            sistema.listar_entregadores()

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()