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
* **Busca inteligente:** Encontre qualquer item no estoque pelo nome de forma rápida e eficiente.

---

## 🖥️ Exemplo de Execução

```text
Inicializando o Gerenciador de Estoque...
Estoque carregado e ordenado com sucesso.

--- Menu Estoque ---
1. Mostrar estoque
2. Buscar item por nome
3. Adicionar novo item
4. Mostrar itens críticos
5. Sair
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