from estruturas import Fila, Pilha
from models import Entregador


class SistemaEntregas:
    def __init__(self):
        
        self.fila_normal = Fila()
        self.fila_prioridade = Fila()

        
        self.historico = Pilha()

        
        self.entregadores = [
            Entregador(1, "João"),
            Entregador(2, "Maria"),
            Entregador(3, "Carlos")
        ]

    def adicionar_pedido(self, pedido):
        if pedido.prioridade == "alta":
            self.fila_prioridade.enqueue(pedido)
            print(f"Pedido #{pedido.id_pedido} adicionado à fila de prioridade.")
        else:
            self.fila_normal.enqueue(pedido)
            print(f"Pedido #{pedido.id_pedido} adicionado à fila normal.")

    def listar_pedidos_pendentes(self):
        print("\n=== PEDIDOS PENDENTES ===")

        print("\n--- Fila de Prioridade ---")
        if self.fila_prioridade.is_empty():
            print("Nenhum pedido prioritário pendente.")
        else:
            for pedido in self.fila_prioridade.show():
                print(pedido)

        print("\n--- Fila Normal ---")
        if self.fila_normal.is_empty():
            print("Nenhum pedido normal pendente.")
        else:
            for pedido in self.fila_normal.show():
                print(pedido)

    def listar_entregadores(self):
        print("\n=== ENTREGADORES ===")
        for entregador in self.entregadores:
            print(entregador)

    def atribuir_pedidos(self):
        print("\n=== ATRIBUIÇÃO DE PEDIDOS ===")

        algum_pedido_atribuido = False

        for entregador in self.entregadores:
            if entregador.disponivel:
                pedido = None

                if not self.fila_prioridade.is_empty():
                    pedido = self.fila_prioridade.dequeue()
                elif not self.fila_normal.is_empty():
                    pedido = self.fila_normal.dequeue()

                if pedido is not None:
                    entregador.atribuir_pedido(pedido)
                    print(f"{entregador.nome} recebeu {pedido}")
                    algum_pedido_atribuido = True

        if not algum_pedido_atribuido:
            print("Nenhum pedido foi atribuído.")
            print("Motivo: ou não há pedidos pendentes, ou todos os entregadores estão ocupados.")

    def finalizar_entrega(self, id_entregador):
        for entregador in self.entregadores:
            if entregador.id_entregador == id_entregador:
                pedido_finalizado = entregador.finalizar_entrega()

                if pedido_finalizado is not None:
                    self.historico.push(pedido_finalizado)
                    print(f"\nEntrega finalizada com sucesso: {pedido_finalizado}")
                else:
                    print("\nEsse entregador não possui pedido em andamento.")
                return

        print("\nEntregador não encontrado.")

    def mostrar_historico(self):
        print("\n=== HISTÓRICO DE ENTREGAS ===")

        if self.historico.is_empty():
            print("Nenhuma entrega foi finalizada ainda.")
        else:
            for pedido in self.historico.show():
                print(pedido)