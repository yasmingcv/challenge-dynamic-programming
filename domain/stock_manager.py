class StockManager: 
    def __init__(self, lista_de_itens):
        print("Inicializando o Gerenciador de Estoque...")
        
        self.estoque = []
        self.nomes_itens = []
        # Carrega os itens do estoque sem ordenar
        for item in lista_de_itens:
            self.estoque.append(item)
            self.nomes_itens.append(item['itemName'])

        print("Estoque carregado com sucesso.")

    def otimizar_reabastecimento(self, orcamento, metodo='recursivo'):
        """
        Otimiza o reabastecimento do estoque usando métodos de  Programação Dinâmica.
        
        ESTADOS:
        - dp[i][w] = benefício máximo usando os primeiros i itens com orçamento w
        
        DECISÕES:
        - Para cada item i: reabastecer ou não reabastecer
        
        FUNÇÃO DE TRANSIÇÃO:
        - dp[i][w] = max(
            dp[i-1][w],                                    # não reabastecer item i
            dp[i-1][w - custo[i]] + beneficio[i]          # reabastecer item i
          )
        
        FUNÇÃO OBJETIVO:
        - Maximizar o benefício total do reabastecimento respeitando o orçamento
        - Benefício = (ideal_quantity - quantity) * unity_price * fator_criticidade
        
        Args:
            orcamento: Orçamento disponível para reabastecimento (em reais)
            metodo: 'recursivo', 'memoization' ou 'iterativo'
        
        Returns:
            dict com benefício máximo, itens selecionados e custos
        """
        # Identifica itens que precisam de reabastecimento
        itens_criticos = []
        for item in self.estoque:
            if item['quantity'] < item['ideal_quantity']:
                deficit = item['ideal_quantity'] - item['quantity']
                custo = deficit * item['unity_price']
                
                # Benefício considera o deficit e a criticidade (% abaixo do ideal)
                criticidade = 1 - (item['quantity'] / item['ideal_quantity'])
                beneficio = int(deficit * item['unity_price'] * (1 + criticidade) * 10)
                
                itens_criticos.append({
                    'item': item,
                    'deficit': deficit,
                    'custo': int(custo),
                    'beneficio': beneficio
                })
        
        if not itens_criticos:
            return {
                'beneficio_maximo': 0,
                'itens_selecionados': [],
                'custo_total': 0,
                'orcamento': orcamento,
                'metodo': metodo
            }
        
        orcamento_int = int(orcamento)
        
        # Escolhe o método de solução
        if metodo == 'recursivo':
            beneficio_max = self._pd_recursivo(itens_criticos, len(itens_criticos), orcamento_int)
            itens_selecionados = self._reconstruir_solucao_recursiva(
                itens_criticos, len(itens_criticos), orcamento_int
            )
        elif metodo == 'memoization':
            memo = {}
            beneficio_max = self._pd_memoization(itens_criticos, len(itens_criticos), orcamento_int, memo)
            itens_selecionados = self._reconstruir_solucao_memo(
                itens_criticos, len(itens_criticos), orcamento_int, memo
            )
        else:  # iterativo (bottom-up)
            beneficio_max, dp_table = self._pd_iterativo(itens_criticos, orcamento_int)
            itens_selecionados = self._reconstruir_solucao_iterativa(
                itens_criticos, dp_table, orcamento_int
            )
        
        # Calcula custo total dos itens selecionados
        custo_total = sum(item['custo'] for item in itens_selecionados)
        
        return {
            'beneficio_maximo': beneficio_max,
            'itens_selecionados': itens_selecionados,
            'custo_total': custo_total,
            'orcamento': orcamento,
            'orcamento_restante': orcamento - custo_total,
            'metodo': metodo,
            'total_itens_criticos': len(itens_criticos),
            'itens_reabastecidos': len(itens_selecionados)
        }
    
    # -------------------
    # VERSÃO RECURSIVA (sem otimização)
    # -------------------
    def _pd_recursivo(self, itens, n, capacidade):
        """
        Versão recursiva pura - Problema da Mochila 0/1
        Complexidade: O(2^n)
        """
        # Caso base: sem itens ou sem capacidade
        if n == 0 or capacidade == 0:
            return 0
        
        # Se o custo do item atual excede a capacidade, não pode ser incluído
        if itens[n-1]['custo'] > capacidade:
            return self._pd_recursivo(itens, n-1, capacidade)
        
        # Retorna o máximo entre incluir ou não incluir o item atual
        incluir = itens[n-1]['beneficio'] + self._pd_recursivo(
            itens, n-1, capacidade - itens[n-1]['custo']
        )
        nao_incluir = self._pd_recursivo(itens, n-1, capacidade)
        
        return max(incluir, nao_incluir)
    
    # -------------------
    # VERSÃO COM MEMOIZATION (top-down)
    # -------------------
    def _pd_memoization(self, itens, n, capacidade, memo):
        """
        Versão recursiva com memoization (top-down)
        Complexidade: O(n * capacidade)
        """
        # Verifica se já foi calculado
        if (n, capacidade) in memo:
            return memo[(n, capacidade)]
        
        # Caso base
        if n == 0 or capacidade == 0:
            return 0
        
        # Se o custo do item atual excede a capacidade
        if itens[n-1]['custo'] > capacidade:
            resultado = self._pd_memoization(itens, n-1, capacidade, memo)
        else:
            # Calcula o máximo entre incluir ou não incluir
            incluir = itens[n-1]['beneficio'] + self._pd_memoization(
                itens, n-1, capacidade - itens[n-1]['custo'], memo
            )
            nao_incluir = self._pd_memoization(itens, n-1, capacidade, memo)
            resultado = max(incluir, nao_incluir)
        
        # Armazena no memo
        memo[(n, capacidade)] = resultado
        return resultado
    
    # -------------------
    # VERSÃO ITERATIVA (bottom-up)
    # -------------------
    def _pd_iterativo(self, itens, capacidade):
        """
        Versão iterativa bottom-up com tabela DP
        Complexidade: O(n * capacidade)
        """
        n = len(itens)
        # Cria tabela DP: dp[i][w] = benefício máximo com i itens e capacidade w
        dp = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]
        
        # Preenche a tabela de baixo para cima
        for i in range(1, n + 1):
            for w in range(1, capacidade + 1):
                custo_item = itens[i-1]['custo']
                beneficio_item = itens[i-1]['beneficio']
                
                # Se o item não cabe, mantém o valor anterior
                if custo_item > w:
                    dp[i][w] = dp[i-1][w]
                else:
                    # Escolhe o máximo entre incluir ou não incluir
                    nao_incluir = dp[i-1][w]
                    incluir = dp[i-1][w - custo_item] + beneficio_item
                    dp[i][w] = max(incluir, nao_incluir)
        
        return dp[n][capacidade], dp
    
    # -------------------
    # RECONSTRUÇÃO DA SOLUÇÃO - Recursiva
    # -------------------
    def _reconstruir_solucao_recursiva(self, itens, n, capacidade):
        """Reconstrói quais itens foram selecionados na versão recursiva"""
        if n == 0 or capacidade == 0:
            return []
        
        if itens[n-1]['custo'] > capacidade:
            return self._reconstruir_solucao_recursiva(itens, n-1, capacidade)
        
        incluir_valor = itens[n-1]['beneficio'] + self._pd_recursivo(
            itens, n-1, capacidade - itens[n-1]['custo']
        )
        nao_incluir_valor = self._pd_recursivo(itens, n-1, capacidade)
        
        if incluir_valor > nao_incluir_valor:
            return self._reconstruir_solucao_recursiva(
                itens, n-1, capacidade - itens[n-1]['custo']
            ) + [itens[n-1]]
        else:
            return self._reconstruir_solucao_recursiva(itens, n-1, capacidade)
    
    # -------------------
    # RECONSTRUÇÃO DA SOLUÇÃO - Memoization
    # -------------------
    def _reconstruir_solucao_memo(self, itens, n, capacidade, memo):
        """Reconstrói quais itens foram selecionados na versão memoization"""
        if n == 0 or capacidade == 0:
            return []
        
        if itens[n-1]['custo'] > capacidade:
            return self._reconstruir_solucao_memo(itens, n-1, capacidade, memo)
        
        incluir_valor = itens[n-1]['beneficio'] + self._pd_memoization(
            itens, n-1, capacidade - itens[n-1]['custo'], memo
        )
        nao_incluir_valor = self._pd_memoization(itens, n-1, capacidade, memo)
        
        if incluir_valor > nao_incluir_valor:
            return self._reconstruir_solucao_memo(
                itens, n-1, capacidade - itens[n-1]['custo'], memo
            ) + [itens[n-1]]
        else:
            return self._reconstruir_solucao_memo(itens, n-1, capacidade, memo)
    
    # -------------------
    # RECONSTRUÇÃO DA SOLUÇÃO - Iterativa
    # -------------------
    def _reconstruir_solucao_iterativa(self, itens, dp, capacidade):
        """Reconstrói quais itens foram selecionados na versão iterativa"""
        n = len(itens)
        w = capacidade
        selecionados = []
        
        # Percorre a tabela de trás para frente
        for i in range(n, 0, -1):
            # Se o valor mudou, o item foi incluído
            if dp[i][w] != dp[i-1][w]:
                selecionados.append(itens[i-1])
                w -= itens[i-1]['custo']
        
        return list(reversed(selecionados))
    
    # -------------------
    # MÉTODO PARA COMPARAR AS TRÊS VERSÕES
    # -------------------
    def comparar_metodos_pd(self, orcamento):
        """
        Executa os três métodos e compara os resultados para validação.
        """
        print("\n" + "="*70)
        print("COMPARAÇÃO DE MÉTODOS")
        print("="*70)
        
        resultados = {}
        
        for metodo in ['recursivo', 'memoization', 'iterativo']:
            print(f"\nExecutando método: {metodo.upper()}")
            resultado = self.otimizar_reabastecimento(orcamento, metodo)
            resultados[metodo] = resultado
            
            print(f"  Benefício Máximo: {resultado['beneficio_maximo']}")
            print(f"  Custo Total: R$ {resultado['custo_total']:.2f}")
            print(f"  Itens Reabastecidos: {resultado['itens_reabastecidos']}/{resultado['total_itens_criticos']}")
        
        # Validação: todos os métodos devem produzir o mesmo resultado
        print("\n" + "="*70)
        print("VALIDAÇÃO DOS RESULTADOS")
        print("="*70)
        
        beneficios = [r['beneficio_maximo'] for r in resultados.values()]
        custos = [r['custo_total'] for r in resultados.values()]
        qtd_itens = [r['itens_reabastecidos'] for r in resultados.values()]
        
        if len(set(beneficios)) == 1 and len(set(custos)) == 1 and len(set(qtd_itens)) == 1:
            print("✓ TODOS OS MÉTODOS PRODUZEM RESULTADOS IDÊNTICOS!")
            print(f"  Benefício: {beneficios[0]}")
            print(f"  Custo: R$ {custos[0]:.2f}")
            print(f"  Itens: {qtd_itens[0]}")
        else:
            print("✗ ATENÇÃO: Resultados diferentes entre os métodos!")
            for metodo, resultado in resultados.items():
                print(f"  {metodo}: benefício={resultado['beneficio_maximo']}, custo={resultado['custo_total']}")
        
        return resultados

    # -------------------
    # EXIBIR RESULTADO DA OTIMIZAÇÃO
    # -------------------
    def exibir_otimizacao(self, resultado):
        """Exibe os resultados da otimização de forma formatada"""
        print("\n" + "="*70)
        print(f"RESULTADO DA OTIMIZAÇÃO - Método: {resultado['metodo'].upper()}")
        print("="*70)
        print(f"Orçamento Disponível: R$ {resultado['orcamento']:.2f}")
        print(f"Benefício Máximo: {resultado['beneficio_maximo']}")
        print(f"Custo Total: R$ {resultado['custo_total']:.2f}")
        print(f"Orçamento Restante: R$ {resultado['orcamento_restante']:.2f}")
        print(f"Itens Críticos: {resultado['total_itens_criticos']}")
        print(f"Itens Selecionados para Reabastecimento: {resultado['itens_reabastecidos']}")
        
        if resultado['itens_selecionados']:
            print("\n" + "-"*70)
            print("ITENS SELECIONADOS PARA REABASTECIMENTO:")
            print("-"*70)
            for i, item_data in enumerate(resultado['itens_selecionados'], 1):
                item = item_data['item']
                print(f"\n{i}. {item['itemName']}")
                print(f"   Categoria: {item['category']}")
                print(f"   Quantidade Atual: {item['quantity']}")
                print(f"   Quantidade Ideal: {item['ideal_quantity']}")
                print(f"   Déficit: {item_data['deficit']} unidades")
                print(f"   Custo: R$ {item_data['custo']:.2f}")
                print(f"   Benefício: {item_data['beneficio']}")
                print(f"   Localização: {item['location']}")

    def fila_de_reposicao(self):
        """
        Retorna uma lista (fila) dos itens que estão abaixo do ideal, em ordem de chegada.
        """
        fila = []
        for item in self.estoque:
            if item['quantity'] < item['ideal_quantity']:
                fila.append(item)
        return fila

    def pilha_de_validade(self):
        """
        Retorna uma lista (pilha) dos itens ordenados por data de validade (topo = vence primeiro).
        """
        pilha = self.estoque[:]
        # Ordenação simples (Insertion Sort) por data de validade
        for i in range(1, len(pilha)):
            chave = pilha[i]
            j = i - 1
            while j >= 0 and (
                (pilha[j]['expiryDate'] is not None and chave['expiryDate'] is not None and pilha[j]['expiryDate'] > chave['expiryDate']) or
                (pilha[j]['expiryDate'] is not None and chave['expiryDate'] is None)
            ):
                pilha[j + 1] = pilha[j]
                j -= 1
            pilha[j + 1] = chave
        return pilha

    def busca_sequencial_nome(self, nome_item):
        """
        Busca sequencialmente um item pelo nome.
        Retorna o item ou None.
        """
        for item in self.estoque:
            if item['itemName'] == nome_item:
                return item
        return None

    def ordenar_estoque_merge(self):
        """
        Ordena o estoque por nome usando Merge Sort.
        """
        def merge_sort(lista):
            if len(lista) <= 1:
                return lista
            meio = len(lista) // 2
            esquerda = merge_sort(lista[:meio])
            direita = merge_sort(lista[meio:])
            return merge(esquerda, direita)

        def merge(esq, dir):
            resultado = []
            i = j = 0
            while i < len(esq) and j < len(dir):
                if esq[i]['itemName'] < dir[j]['itemName']:
                    resultado.append(esq[i])
                    i += 1
                else:
                    resultado.append(dir[j])
                    j += 1
            resultado.extend(esq[i:])
            resultado.extend(dir[j:])
            return resultado

        self.estoque = merge_sort(self.estoque)
        self.nomes_itens = [item['itemName'] for item in self.estoque]

    def ordenar_estoque_quick(self):
        """
        Ordena o estoque por nome usando Quick Sort.
        """
        def quick_sort(lista):
            if len(lista) <= 1:
                return lista
            pivo = lista[0]
            menores = [x for x in lista[1:] if x['itemName'] <= pivo['itemName']]
            maiores = [x for x in lista[1:] if x['itemName'] > pivo['itemName']]
            return quick_sort(menores) + [pivo] + quick_sort(maiores)

        self.estoque = quick_sort(self.estoque)
        self.nomes_itens = [item['itemName'] for item in self.estoque]

    def busca_binaria(self, nome_item):
        esquerda = 0
        direita = len(self.nomes_itens)

        while esquerda < direita:
            meio = (esquerda + direita) // 2
            if self.nomes_itens[meio] < nome_item:
                esquerda = meio + 1
            else:
                direita = meio
        return esquerda

    def buscar_por_nome(self, nome_item):
        esquerda = 0
        direita = len(self.estoque) - 1

        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            nome_meio = self.estoque[meio]['itemName']
            if nome_meio == nome_item:
                return self.estoque[meio]
            elif nome_meio < nome_item:
                esquerda = meio + 1
            else:
                direita = meio - 1

        return None

    def adicionar_item(self, novo_item):
        print(f"\nAdicionando '{novo_item['itemName']}' ao estoque...")
        self.estoque.append(novo_item)
        self.nomes_itens.append(novo_item['itemName'])
    
    def mostrar_estoque(self):
        print("\nEstoque atual:")
        for item in self.estoque:
            print(20 * "-")
            print(f"ID: {item['id']}")
            print(f"Nome: {item['itemName']}")
            print(f"Categoria: {item['category']}")
            print(f"Quantidade: {item['quantity']}")
            print(f"Localização: {item['location']}")
            print(f"Data de Validade: {item['expiryDate']}")
            print(f"Preço Unitário: R$ {item['unity_price']:.2f}")
            print(f"Quantidade Ideal: {item['ideal_quantity']}")
            
    def itens_criticos(self):
        criticos = []

        for item in self.estoque:
            atual = item['quantity']
            ideal = item['ideal_quantity']

            if atual < ideal:
                desvio = ideal - atual
                criticos.append({
                    'item': item,
                    'desvio': desvio,
                    'relacao': f"{atual}/{ideal}"
                })
        
        criticos.sort(key=lambda x: x['desvio'], reverse=True)
        print("\nItens críticos:")
        for critico in criticos:
            item = critico['item']
            print(20 * "-")
            print(f"ID: {item['id']}")
            print(f"Nome: {item['itemName']}")
            print(f"Categoria: {item['category']}")
            print(f"Quantidade Atual: {item['quantity']}")
            print(f"Quantidade Ideal: {item['ideal_quantity']}")
            print(f"Desvio: {critico['desvio']}")
            print(f"Relação: {critico['relacao']}")
            print(f"Localização: {item['location']}")