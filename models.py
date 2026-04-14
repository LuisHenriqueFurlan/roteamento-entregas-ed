from datetime import datetime


class Pedido:
    def __init__(self, id_pedido, endereco, coordenadas, prioridade="normal"):
        self.id_pedido = id_pedido
        self.endereco = endereco
        self.coordenadas = coordenadas
        self.horario_solicitacao = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.prioridade = prioridade.lower()

    def __str__(self):
        return (
            f"Pedido #{self.id_pedido} | "
            f"Endereço: {self.endereco} | "
            f"Coordenadas: {self.coordenadas} | "
            f"Horário: {self.horario_solicitacao} | "
            f"Prioridade: {self.prioridade}"
        )


class Entregador:
    def __init__(self, id_entregador, nome):
        self.id_entregador = id_entregador
        self.nome = nome
        self.disponivel = True
        self.pedido_atual = None

    def atribuir_pedido(self, pedido):
        if self.disponivel:
            self.pedido_atual = pedido
            self.disponivel = False
            return True
        return False

    def finalizar_entrega(self):
        if self.pedido_atual is not None:
            pedido_finalizado = self.pedido_atual
            self.pedido_atual = None
            self.disponivel = True
            return pedido_finalizado
        return None

    def __str__(self):
        status = "Disponível" if self.disponivel else "Ocupado"
        pedido_info = (
            "Nenhum pedido"
            if self.pedido_atual is None
            else f"Pedido #{self.pedido_atual.id_pedido}"
        )

        return (
            f"Entregador #{self.id_entregador} - {self.nome} | "
            f"Status: {status} | "
            f"Pedido atual: {pedido_info}"
        )