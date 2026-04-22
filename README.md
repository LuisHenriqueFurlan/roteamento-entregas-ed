# Sistema de Roteamento de Entregas com Pilha e Fila

## Descrição do Projeto

Este projeto foi desenvolvido para a disciplina de Estrutura de Dados com o objetivo de simular um sistema de roteamento de entregas urbanas nas cidades de Cuiabá e Várzea Grande (MT).

O sistema recebe pedidos de entrega, organiza os pedidos pendentes utilizando filas e registra as entregas concluídas em uma pilha, permitindo o controle de entregadores, pedidos prioritários e histórico de entregas.

---

## Objetivo

Aplicar, na prática, os conceitos de Estrutura de Dados, com foco nas estruturas:

- **Fila (FIFO)** para o controle de pedidos pendentes
- **Pilha (LIFO)** para o histórico de entregas realizadas

Além disso, o projeto busca simular o funcionamento básico de uma empresa de entregas com três entregadores fixos.

---

## Funcionalidades

O sistema permite:

- inserir novos pedidos
- listar pedidos pendentes
- atribuir pedidos aos entregadores disponíveis
- finalizar entregas
- registrar entregas no histórico
- consultar histórico de entregas realizadas
- visualizar o status dos entregadores
- interface via terminal
- interface gráfica com Tkinter

---

## Estruturas de Dados Utilizadas

### Fila (FIFO)

A fila foi utilizada para armazenar os pedidos pendentes.

Foram implementadas duas filas:

- **fila de prioridade**
- **fila normal**

A lógica utilizada foi:

- pedidos de prioridade **alta** entram na fila de prioridade
- pedidos de prioridade **normal** entram na fila normal
- no momento da atribuição, a fila de prioridade é atendida primeiro

Assim, a ordem de chegada é mantida dentro de cada fila.

### Pilha (LIFO)

A pilha foi utilizada para armazenar o histórico de entregas concluídas.

Toda vez que uma entrega é finalizada, o pedido correspondente é empilhado no histórico. Dessa forma, a entrega mais recente aparece primeiro na consulta do histórico.

---

## Interface Gráfica (Tkinter)

O projeto também possui uma interface gráfica desenvolvida com a biblioteca **Tkinter**, permitindo uma interação mais visual com o sistema.

Por meio da interface é possível:

- cadastrar pedidos
- atribuir entregas
- finalizar entregas
- visualizar pedidos, entregadores e histórico

<<<<<<< HEAD
## Fluxo do Sistema

O funcionamento do sistema ocorre da seguinte forma:

1. o usuário escolhe uma opção no menu
2. ao cadastrar um pedido, o sistema cria um objeto `Pedido`
3. o pedido é enviado para a fila correta:
   - fila de prioridade
   - fila normal
4. quando a opção de atribuição é executada, os entregadores disponíveis recebem pedidos
5. pedidos prioritários são atendidos antes dos pedidos normais
6. ao finalizar uma entrega, o pedido é removido do entregador
7. o pedido finalizado é armazenado na pilha de histórico
8. o usuário pode consultar o histórico e o status dos entregadores a qualquer momento

---

## Tecnologias Utilizadas

- Python 3
- Programação Orientada a Objetos
- Estruturas de Dados: Fila e Pilha

---

## Como Executar

### 1. Clone o repositório

git clone https://github.com/LuisHenriqueFurlan/roteamento-entregas-ed

### 2. rodar a interface grafica
-python app_tkinter.py

### 3. rodar somente no terminal 
-python main.py



