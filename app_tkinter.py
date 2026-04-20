import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText

from SistemaEntregas import SistemaEntregas
from models import Pedido


class AppEntregas:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Roteamento de Entregas")
        self.root.geometry("900x650")
        self.root.resizable(False, False)

        self.sistema = SistemaEntregas()
        self.proximo_id = 1

        self.configurar_estilo()
        self.criar_interface()

    def configurar_estilo(self):
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.style.configure(
            "Titulo.TLabel",
            font=("Segoe UI", 18, "bold")
        )

        self.style.configure(
            "Subtitulo.TLabelframe.Label",
            font=("Segoe UI", 11, "bold")
        )

        self.style.configure(
            "TLabel",
            font=("Segoe UI", 10)
        )

        self.style.configure(
            "TButton",
            font=("Segoe UI", 10),
            padding=6
        )

        self.style.configure(
            "TEntry",
            padding=4
        )

        self.style.configure(
            "TCombobox",
            padding=4
        )

    def criar_interface(self):
        frame_principal = ttk.Frame(self.root, padding=15)
        frame_principal.pack(fill="both", expand=True)

        titulo = ttk.Label(
            frame_principal,
            text="Sistema de Roteamento de Entregas",
            style="Titulo.TLabel"
        )
        titulo.pack(pady=(0, 15))

        frame_topo = ttk.Frame(frame_principal)
        frame_topo.pack(fill="x")

        self.criar_frame_cadastro(frame_topo)
        self.criar_frame_acoes(frame_topo)
        self.criar_frame_saida(frame_principal)

    def criar_frame_cadastro(self, parent):
        frame_cadastro = ttk.LabelFrame(
            parent,
            text="Cadastro de Pedido",
            style="Subtitulo.TLabelframe"
        )
        frame_cadastro.pack(side="left", fill="both", expand=True, padx=(0, 10))

        ttk.Label(frame_cadastro, text="Endereço:").grid(row=0, column=0, sticky="w", padx=8, pady=8)
        self.entry_endereco = ttk.Entry(frame_cadastro, width=35)
        self.entry_endereco.grid(row=0, column=1, padx=8, pady=8)

        ttk.Label(frame_cadastro, text="Latitude:").grid(row=1, column=0, sticky="w", padx=8, pady=8)
        self.entry_latitude = ttk.Entry(frame_cadastro, width=20)
        self.entry_latitude.grid(row=1, column=1, sticky="w", padx=8, pady=8)

        ttk.Label(frame_cadastro, text="Longitude:").grid(row=2, column=0, sticky="w", padx=8, pady=8)
        self.entry_longitude = ttk.Entry(frame_cadastro, width=20)
        self.entry_longitude.grid(row=2, column=1, sticky="w", padx=8, pady=8)

        ttk.Label(frame_cadastro, text="Prioridade:").grid(row=3, column=0, sticky="w", padx=8, pady=8)
        self.combo_prioridade = ttk.Combobox(
            frame_cadastro,
            values=["normal", "alta"],
            state="readonly",
            width=18
        )
        self.combo_prioridade.grid(row=3, column=1, sticky="w", padx=8, pady=8)
        self.combo_prioridade.set("normal")

        btn_cadastrar = ttk.Button(
            frame_cadastro,
            text="Cadastrar Pedido",
            command=self.cadastrar_pedido
        )
        btn_cadastrar.grid(row=4, column=0, columnspan=2, pady=12)

    def criar_frame_acoes(self, parent):
        frame_acoes = ttk.LabelFrame(
            parent,
            text="Ações do Sistema",
            style="Subtitulo.TLabelframe"
        )
        frame_acoes.pack(side="right", fill="y")

        ttk.Button(
            frame_acoes,
            text="Atribuir Pedidos",
            width=25,
            command=self.atribuir_pedidos
        ).pack(padx=12, pady=(12, 6))

        ttk.Label(frame_acoes, text="ID do entregador:").pack(anchor="w", padx=12, pady=(10, 4))
        self.entry_id_entregador = ttk.Entry(frame_acoes, width=10)
        self.entry_id_entregador.pack(anchor="w", padx=12, pady=(0, 8))

        ttk.Button(
            frame_acoes,
            text="Finalizar Entrega",
            width=25,
            command=self.finalizar_entrega
        ).pack(padx=12, pady=6)

        ttk.Separator(frame_acoes, orient="horizontal").pack(fill="x", padx=12, pady=12)

        ttk.Button(
            frame_acoes,
            text="Ver Pedidos Pendentes",
            width=25,
            command=self.ver_pedidos
        ).pack(padx=12, pady=6)

        ttk.Button(
            frame_acoes,
            text="Ver Entregadores",
            width=25,
            command=self.ver_entregadores
        ).pack(padx=12, pady=6)

        ttk.Button(
            frame_acoes,
            text="Ver Histórico",
            width=25,
            command=self.ver_historico
        ).pack(padx=12, pady=6)

        ttk.Button(
            frame_acoes,
            text="Limpar Saída",
            width=25,
            command=self.limpar_saida
        ).pack(padx=12, pady=(20, 12))

    def criar_frame_saida(self, parent):
        frame_saida = ttk.LabelFrame(
            parent,
            text="Saída do Sistema",
            style="Subtitulo.TLabelframe"
        )
        frame_saida.pack(fill="both", expand=True, pady=(15, 0))

        self.area_saida = ScrolledText(
            frame_saida,
            wrap="word",
            font=("Consolas", 10),
            width=100,
            height=20
        )
        self.area_saida.pack(fill="both", expand=True, padx=10, pady=10)

    def escrever_saida(self, texto):
        self.area_saida.insert(tk.END, texto + "\n")
        self.area_saida.see(tk.END)

    def limpar_saida(self):
        self.area_saida.delete("1.0", tk.END)

    def cadastrar_pedido(self):
        endereco = self.entry_endereco.get().strip()
        prioridade = self.combo_prioridade.get().strip().lower()

        if not endereco:
            messagebox.showwarning("Atenção", "Informe o endereço do pedido.")
            return

        try:
            latitude = float(self.entry_latitude.get())
            longitude = float(self.entry_longitude.get())
        except ValueError:
            messagebox.showerror("Erro", "Latitude e longitude devem ser números válidos.")
            return

        pedido = Pedido(
            self.proximo_id,
            endereco,
            (latitude, longitude),
            prioridade
        )

        self.sistema.adicionar_pedido(pedido)
        self.escrever_saida(f"Pedido #{self.proximo_id} cadastrado com sucesso.")
        self.proximo_id += 1

        self.entry_endereco.delete(0, tk.END)
        self.entry_latitude.delete(0, tk.END)
        self.entry_longitude.delete(0, tk.END)
        self.combo_prioridade.set("normal")

    def atribuir_pedidos(self):
        self.sistema.atribuir_pedidos()
        self.escrever_saida("Atribuição de pedidos executada.")

    def finalizar_entrega(self):
        try:
            id_entregador = int(self.entry_id_entregador.get())
        except ValueError:
            messagebox.showerror("Erro", "Digite um ID de entregador válido.")
            return

        self.sistema.finalizar_entrega(id_entregador)
        self.escrever_saida(f"Tentativa de finalização da entrega do entregador #{id_entregador}.")

        self.entry_id_entregador.delete(0, tk.END)

    def ver_pedidos(self):
        self.escrever_saida("\n=== PEDIDOS PENDENTES ===")

        self.escrever_saida("\n--- Fila de Prioridade ---")
        fila_prioridade = self.sistema.fila_prioridade.show()
        if not fila_prioridade:
            self.escrever_saida("Nenhum pedido prioritário pendente.")
        else:
            for pedido in fila_prioridade:
                self.escrever_saida(str(pedido))

        self.escrever_saida("\n--- Fila Normal ---")
        fila_normal = self.sistema.fila_normal.show()
        if not fila_normal:
            self.escrever_saida("Nenhum pedido normal pendente.")
        else:
            for pedido in fila_normal:
                self.escrever_saida(str(pedido))

    def ver_entregadores(self):
        self.escrever_saida("\n=== ENTREGADORES ===")
        for entregador in self.sistema.entregadores:
            self.escrever_saida(str(entregador))

    def ver_historico(self):
        self.escrever_saida("\n=== HISTÓRICO DE ENTREGAS ===")
        historico = self.sistema.historico.show()

        if not historico:
            self.escrever_saida("Nenhuma entrega foi finalizada ainda.")
            return

        for pedido in historico:
            self.escrever_saida(str(pedido))


if __name__ == "__main__":
    root = tk.Tk()
    app = AppEntregas(root)
    root.mainloop()