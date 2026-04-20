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
        fila_destino = self.fila_prioridade if pedido.prioridade == "alta" else self.fila_normal
        fila_destino.enqueue(pedido)
        print(f"Pedido #{pedido.id_pedido} adicionado com sucesso.")

    def exibir_fila(self, titulo, fila, mensagem_vazia):
        print(f"\n--- {titulo} ---")

        if fila.is_empty():
            print(mensagem_vazia)
            return

        for pedido in fila.show():
            print(pedido)

    def listar_pedidos_pendentes(self):
        print("\n=== PEDIDOS PENDENTES ===")

        self.exibir_fila(
            "Fila de Prioridade",
            self.fila_prioridade,
            "Nenhum pedido prioritário pendente."
        )

        self.exibir_fila(
            "Fila Normal",
            self.fila_normal,
            "Nenhum pedido normal pendente."
        )

    def listar_entregadores(self):
        print("\n=== ENTREGADORES ===")
        for entregador in self.entregadores:
            print(entregador)

    def obter_proximo_pedido(self):
        if not self.fila_prioridade.is_empty():
            return self.fila_prioridade.dequeue()

        if not self.fila_normal.is_empty():
            return self.fila_normal.dequeue()

        return None

    def atribuir_pedidos(self):
        print("\n=== ATRIBUIÇÃO DE PEDIDOS ===")
        algum_pedido_atribuido = False

        for entregador in self.entregadores:
            if entregador.disponivel:
                pedido = self.obter_proximo_pedido()

                if pedido is not None:
                    entregador.atribuir_pedido(pedido)
                    print(f"{entregador.nome} recebeu {pedido}")
                    algum_pedido_atribuido = True

        if not algum_pedido_atribuido:
            print("Nenhum pedido foi atribuído. Verifique se há pedidos pendentes ou entregadores disponíveis.")

    def buscar_entregador_por_id(self, id_entregador):
        for entregador in self.entregadores:
            if entregador.id_entregador == id_entregador:
                return entregador
        return None

    def finalizar_entrega(self, id_entregador):
        entregador = self.buscar_entregador_por_id(id_entregador)

        if entregador is None:
            print("\nEntregador não encontrado.")
            return

        pedido_finalizado = entregador.finalizar_entrega()

        if pedido_finalizado is None:
            print("\nEsse entregador não possui pedido em andamento.")
            return

        self.historico.push(pedido_finalizado)
        print(f"\nEntrega finalizada com sucesso: {pedido_finalizado}")

    def mostrar_historico(self):
        print("\n=== HISTÓRICO DE ENTREGAS ===")

        if self.historico.is_empty():
            print("Nenhuma entrega foi finalizada ainda.")
            return

        for pedido in self.historico.show():
            print(pedido)