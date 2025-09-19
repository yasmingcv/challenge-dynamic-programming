# 🔬 Sistema de Gerenciamento de Estoque Laboratorial

Este projeto foi desenvolvido como parte da disciplina de **Dynamic Programming** do curso de **Engenharia de Software** da **FIAP**, sendo a solução proposta para o **Challenge 2025**, em colaboração com a **DASA**.

Nosso sistema simula o **controle de estoque em laboratórios**, otimizando a gestão de suprimentos e materiais. A aplicação utiliza **busca binária** para diversas funcionalidades, como adicionar novos itens e ordenar o estoque, garantindo eficiência e precisão nas operações.


---

## 🚀 Como Utilizar

1. Clone este repositório:

    ```bash
    git clone https://github.com/yasmingcv/challenge-dynamic-programming.git
    ```

2. Acesse a pasta do projeto:

    ```bash
    cd challenge-dynamic-programming
    ```

3. Execute o programa principal:

    ```bash
    py ./app.py
    ```

---

## 🛠️ Funcionalidades

Explore as principais capacidades do nosso sistema:


* **Cadastro de itens:** Adicione novos materiais e suprimentos ao seu estoque com facilidade.
* **Ordenação alfabética:** Mantenha seu estoque sempre organizado, facilitando a visualização e a busca.
* **Listagem de itens críticos:** Identifique rapidamente os itens com estoque abaixo do ideal, garantindo que você nunca fique sem o essencial.
* **Busca inteligente:** Encontre qualquer item no estoque pelo nome de forma rápida e eficiente (busca binária e busca sequencial).
* **Fila de reposição:** Visualize os itens que precisam ser repostos, em ordem de chegada, facilitando o planejamento de compras.
* **Pilha de validade:** Veja os itens ordenados por data de validade, do que vence primeiro ao que vence por último, auxiliando no controle de vencimentos.
* **Busca sequencial:** Alternativa à busca binária, permite encontrar itens mesmo em listas não ordenadas.
* **Ordenação por Merge Sort:** Ordene o estoque por nome utilizando o algoritmo Merge Sort, garantindo estabilidade e eficiência.
* **Ordenação por Quick Sort:** Ordene o estoque por nome utilizando o algoritmo Quick Sort, para alta performance em grandes volumes de dados.

---

## 🖥️ Exemplo de Execução

```text
Inicializando o Gerenciador de Estoque...
Estoque carregado e ordenado com sucesso.

--- Menu Estoque ---
1. Mostrar estoque
2. Buscar item por nome (binária)
3. Adicionar novo item
4. Mostrar itens críticos
5. Fila de reposição (itens abaixo do ideal)
6. Pilha de validade (ordem de vencimento)
7. Busca sequencial por nome
8. Ordenar estoque por nome (Merge Sort)
9. Ordenar estoque por nome (Quick Sort)
0. Sair
Escolha uma opção: 2
Digite o nome do item a ser buscado: Tubo de Ensaio de Vidro 15ml

Item encontrado:
--------------------
ID: 7
Nome: Tubo de Ensaio de Vidro 15ml
Categoria: Vidraria
Quantidade: 300
Localização: Armário F6
Data de Validade: None
Preço Unitário: R$ 0.60
Quantidade Ideal: 400

```

## Estrutura do projeto

```text
│   app.py                     -- Arquivo principal.
│   data.json                  -- Dados de exemplo do estoque em formato JSON.
│   README.md                  -- Documentação do projeto.
│
└───domain
    └───stock_manager.py       -- Classe responsável pela lógica central de gerenciamento do estoque.
```
## 👥 Integrantes

- David Murillo de Oliveira Soares (RM 559078)
- Felipe Cerboncini Cordeiro (554909)
- Lucas Serrano Rocco (RM 555170)
- Pedro Henrique Martins Alves dos Santos (558107)
- Yasmin Gonçalves Coelho (RM 559147)