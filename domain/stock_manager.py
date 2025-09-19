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


    # -------------------
    # Fila de reposição: itens que precisam ser repostos, em ordem de chegada
    # -------------------
    def fila_de_reposicao(self):
        """
        Retorna uma lista (fila) dos itens que estão abaixo do ideal, em ordem de chegada.
        """
        fila = []
        for item in self.estoque:
            if item['quantity'] < item['ideal_quantity']:
                fila.append(item)
        return fila

    # -------------------
    # Pilha de validade: itens ordenados do que vence primeiro para o que vence por último
    # -------------------
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

    # -------------------
    # Busca sequencial por nome
    # -------------------
    def busca_sequencial_nome(self, nome_item):
        """
        Busca sequencialmente um item pelo nome.
        Retorna o item ou None.
        """
        for item in self.estoque:
            if item['itemName'] == nome_item:
                return item
        return None

    # -------------------
    # Ordenação do estoque por nome usando Merge Sort
    # -------------------
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

    # -------------------
    # Ordenação do estoque por nome usando Quick Sort
    # -------------------
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
        # Retorna a posição onde o item deve ser inserido
        esquerda = 0
        direita = len(self.nomes_itens)

        while esquerda < direita:
            # Calcula o meio da lista
            meio = (esquerda + direita) // 2
            # Se o nome do item no meio é menor que o nome_item,
            # significa que o item deve ser inserido à direita
            if self.nomes_itens[meio] < nome_item:
                esquerda = meio + 1
            # senão, o item deve ser inserido à esquerda
            else:
                direita = meio
        return esquerda

    def buscar_por_nome(self, nome_item):
        # Busca um item pelo nome usando busca binária,
        # como a lista já está ordenada, a busca é eficiente
        esquerda = 0
        direita = len(self.estoque) - 1

        while esquerda <= direita:
            # Calcula o meio da lista
            meio = (esquerda + direita) // 2
            # Compara o nome do item no meio com o nome_item
            nome_meio = self.estoque[meio]['itemName']
            # Se o nome do meio é igual ao nome_item, retorna o item
            if nome_meio == nome_item:
                return self.estoque[meio]
            # Se o nome do meio é menor que o nome_item, busca à direita
            elif nome_meio < nome_item:
                esquerda = meio + 1
            # Se o nome do meio é maior que o nome_item, busca à esquerda
            else:
                direita = meio - 1

        return None  # Não encontrado

    def adicionar_item(self, novo_item):
        print(f"\nAdicionando '{novo_item['itemName']}' ao estoque...")
        # Adiciona sempre no final das listas
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
        
        # Ordena os itens críticos por maior desvio
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
                