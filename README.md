# 🔬 Sistema de Gerenciamento de Estoque Laboratorial

Este projeto foi desenvolvido como parte da disciplina de **Programação Dinâmica** do curso de **Engenharia de Software** da **FIAP**, sendo a solução proposta para o **Challenge 2025**, em colaboração com a **DASA**.

Nosso sistema simula o **controle de estoque em hospitais e farmácias**, implementando algoritmos de **Programação Dinâmica** para otimização de reabastecimento de medicamentos, materiais hospitalares e suprimentos médicos. O sistema também utiliza estruturas de dados avançadas (pilhas, filas, busca binária) para garantir eficiência nas operações de gerenciamento.

---

#### **Definição dos Componentes:**

**Estados:**
- `dp[i][w]` = benefício máximo obtido considerando os primeiros `i` itens com orçamento `w` disponível
- Cada estado representa uma decisão acumulada sobre quais itens reabastecer

**Decisões:**
- Para cada item crítico `i`: **reabastecer** ou **não reabastecer**
- Decisão baseada na relação custo-benefício e orçamento disponível

**Função de Transição:**
```
dp[i][w] = max(
    dp[i-1][w],                           // não reabastecer item i
    dp[i-1][w - custo[i]] + beneficio[i]  // reabastecer item i
)
```
Onde:
- `custo[i]` = déficit × preço unitário
- `beneficio[i]` = déficit × preço × (1 + criticidade) × 10

**Função Objetivo:**
- **Maximizar:** Benefício total do reabastecimento
- **Restrição:** Custo total ≤ Orçamento disponível
- **Objetivo:** Selecionar o subconjunto ótimo de itens para reabastecer

**Casos Base:**
- `dp[0][w] = 0` para todo `w` (sem itens, benefício = 0)
- `dp[i][0] = 0` para todo `i` (sem orçamento, benefício = 0)

---

## 📊 Três Implementações de Programação Dinâmica

O projeto implementa **três versões** do algoritmo, todas produzindo **resultados idênticos**:

### 1️⃣ Versão Recursiva Pura
```python
def _pd_recursivo(itens, n, capacidade):
    # Caso base
    if n == 0 or capacidade == 0:
        return 0
    
    # Recursão: decidir incluir ou não incluir item
    if itens[n-1]['custo'] > capacidade:
        return _pd_recursivo(itens, n-1, capacidade)
    
    incluir = beneficio[n-1] + _pd_recursivo(itens, n-1, capacidade - custo[n-1])
    nao_incluir = _pd_recursivo(itens, n-1, capacidade)
    
    return max(incluir, nao_incluir)
```
- **Complexidade:** O(2^n) - exponencial
- **Uso:** Demonstração conceitual da recorrência
- **Limitação:** Impraticável para n grande devido a recomputações

### 2️⃣ Versão Memoization (Top-Down)
```python
def _pd_memoization(itens, n, capacidade, memo):
    # Verifica cache
    if (n, capacidade) in memo:
        return memo[(n, capacidade)]
    
    # Caso base
    if n == 0 or capacidade == 0:
        return 0
    
    # Calcula e armazena resultado
    resultado = # ... lógica de decisão
    memo[(n, capacidade)] = resultado
    return resultado
```
- **Complexidade:** O(n × W) - onde W é o orçamento
- **Uso:** Recursão otimizada com cache de subproblemas
- **Vantagem:** Calcula apenas subproblemas necessários

### 3️⃣ Versão Iterativa (Bottom-Up)
```python
def _pd_iterativo(itens, capacidade):
    n = len(itens)
    dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
    
    # Preenche tabela bottom-up
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if custo[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], 
                              dp[i-1][w - custo[i-1]] + beneficio[i-1])
    
    return dp[n][capacidade]
```
- **Complexidade:** O(n × W) - mesma da memoization
- **Uso:** Recomendado para produção
- **Vantagem:** Sem overhead de recursão, uso eficiente de memória

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
    python app.py
    ```

---

## 🛠️ Funcionalidades

### 🎯 Programação Dinâmica (Core do Projeto)
* **Otimização Recursiva**: Implementação recursiva pura com recorrência explícita
* **Otimização com Memoization**: Top-down com cache (dicionário) de subproblemas
* **Otimização Iterativa**: Bottom-up com tabela DP, O(n × W)
* **Comparação de Métodos**: Valida que as três versões produzem resultados idênticos
* **Reconstrução de Solução**: Backtracking para identificar itens selecionados
* **Análise de Benefício**: Calcula criticidade baseada em deficit/ideal

### 📦 Estruturas de Dados Auxiliares
* **Cadastro de itens**: Adicione novos medicamentos e materiais ao estoque
* **Visualização completa**: Exiba todos os itens do estoque com detalhes
* **Busca binária**: Busca eficiente O(log n) em lista ordenada
* **Busca sequencial**: Busca linear O(n) em lista não ordenada
* **Itens críticos**: Identifique produtos abaixo do estoque ideal

### 📚 Algoritmos de Ordenação
* **Fila de reposição (FIFO)**: Itens que precisam ser repostos, ordem de chegada
* **Pilha de validade (LIFO)**: Itens ordenados por vencimento (Insertion Sort)
* **Merge Sort**: Ordenação estável O(n log n)
* **Quick Sort**: Ordenação in-place O(n log n) médio

---

## 🖥️ Exemplo de Execução

```text
======================================================================
MENU GERENCIADOR DE ESTOQUE
======================================================================
1. Mostrar estoque
2. Buscar item por nome (binária)
3. Adicionar novo item
4. Mostrar itens críticos
5. Fila de reposição (itens abaixo do ideal)
6. Pilha de validade (ordem de vencimento)
7. Busca sequencial por nome
8. Ordenar estoque por nome (Merge Sort)
9. Ordenar estoque por nome (Quick Sort)
10. Otimizar reabastecimento - Método RECURSIVO
11. Otimizar reabastecimento - Método MEMOIZATION
12. Otimizar reabastecimento - Método ITERATIVO
13. Comparar todos os métodos de PD

0. Sair

Escolha uma opção: 13

======================================================================
COMPARAÇÃO DE MÉTODOS
======================================================================

Digite o orçamento disponível (R$): 1000

Executando método: RECURSIVO
  Benefício Máximo: 15840
  Custo Total: R$ 997.00
  Itens Reabastecidos: 8/42

Executando método: MEMOIZATION
  Benefício Máximo: 15840
  Custo Total: R$ 997.00
  Itens Reabastecidos: 8/42

Executando método: ITERATIVO
  Benefício Máximo: 15840
  Custo Total: R$ 997.00
  Itens Reabastecidos: 8/42

======================================================================
VALIDAÇÃO DOS RESULTADOS
======================================================================
✓ TODOS OS MÉTODOS PRODUZEM RESULTADOS IDÊNTICOS!
  Benefício: 15840
  Custo: R$ 997.00
  Itens: 8
```

---

## 📊 Base de Dados

O arquivo `data.json` contém **50 itens** realistas de estoque hospitalar/farmácia:

### Categorias Principais:
- **Medicamentos**: Analgésicos, Antibióticos, Anti-hipertensivos, Antidiabéticos, Corticoides
- **Soluções**: Soro Fisiológico, Soro Glicosado  
- **Materiais Hospitalares**: Luvas, Máscaras, Seringas, Agulhas, Cateteres, Gazes
- **Antissépticos**: Álcool 70%, Clorexidina, Povidine
- **Controlados**: Diazepam, Morfina, Tramadol, Clonazepam
- **Equipamentos**: Termômetros, Esfigmomanômetros, Estetoscópios
- **Diagnóstico**: Testes COVID-19, Gravidez, Glicosímetro
- **Gases Medicinais**: Oxigênio

### Estrutura de um Item:
```json
{
  "id": 1,
  "itemName": "Paracetamol 500mg",
  "category": "Analgésicos",
  "quantity": 150,
  "ideal_quantity": 500,
  "unity_price": 0.35,
  "location": "Prateleira A1 - Farmácia",
  "expiryDate": "2026-03-15"
}
```

### Cenários para Teste de PD:
- **Itens com alto déficit**: Máscaras (1500/5000), Seringas (250/1500)
- **Itens caros**: Oxigênio (R$ 180,00), Insulina (R$ 45,00)
- **Diferentes faixas de orçamento**: R$ 500, R$ 1000, R$ 2000, R$ 5000
- **Múltiplas combinações ótimas**: Para análise de backtracking

---

## 📁 Estrutura do Projeto

```text
challenge-dynamic-programming/
│
├── app.py                      # Interface interativa com menu
├── data.json                   # 50 itens de estoque hospitalar
├── README.md                   # Documentação completa
│
└── domain/
    └── stock_manager.py        # Classe StockManager
                                # - Três implementações de PD
                                # - Reconstrução de solução
                                # - Validação de resultados
                                # - Estruturas auxiliares
```

---

## 🔬 Análise de Complexidade

### Programação Dinâmica

| Método | Complexidade Tempo | Complexidade Espaço |
|--------|-------------------|---------------------|
| Recursivo | O(2^n) | O(n) pilha |
| Memoization | O(n × W) | O(n × W) |
| Iterativo | O(n × W) | O(n × W) |

Onde:
- `n` = número de itens críticos (abaixo do ideal)
- `W` = orçamento disponível (convertido para centavos)

### Algoritmos Auxiliares

| Algoritmo | Complexidade | Uso no Projeto |
|-----------|-------------|----------------|
| Busca Sequencial | O(n) | Busca em lista não ordenada |
| Busca Binária | O(log n) | Busca em lista ordenada |
| Insertion Sort | O(n²) | Pilha de validade (pequeno n) |
| Merge Sort | O(n log n) | Ordenação estável |
| Quick Sort | O(n log n) | Ordenação rápida (média) |

---

## 🧪 Validação e Testes

### Método de Validação Implementado:
1. Executa os **três métodos** com o mesmo orçamento
2. Compara **benefício máximo**, **custo total** e **itens selecionados**
3. Valida que todos produzem **resultados idênticos**
4. Garante **corretude matemática** da implementação

### Execute o Teste:
- Escolha a opção **13** no menu
- Digite um orçamento (ex: 1000)
- Observe a execução e validação automática


## 👥 Integrantes

- **David Murillo de Oliveira Soares** (RM 559078)
- **Felipe Cerboncini Cordeiro** (RM 554909)
- **Lucas Serrano Rocco** (RM 555170)
- **Pedro Henrique Martins Alves dos Santos** (RM 558107)
- **Yasmin Gonçalves Coelho** (RM 559147)