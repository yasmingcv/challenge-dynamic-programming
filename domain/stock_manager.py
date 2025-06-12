class StockManager: 
    def __init__(self, lista_de_itens):
        print("Inicializando o Gerenciador de Estoque...")
        
        self.estoque = []
        self.nomes_itens = []
        # Carrega os itens do estoque e ordena por nome
        for item in lista_de_itens:
            nome = item['itemName']
            # Busca binária para encontrar a posição correta
            pos = self.busca_binaria(nome)
            self.estoque.insert(pos, item)
            self.nomes_itens.insert(pos, nome)

        print("Estoque carregado e ordenado com sucesso.")

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
        # Encontra a posição correta para inserir o novo item utilizando busca binária
        pos = self.busca_binaria(novo_item['itemName'])
        # Insere o novo item na posição correta
        self.estoque.insert(pos, novo_item)
        
    def mostrar_estoque(self):
        # "id": 9,
        # "itemName": "Atadura de Crepom 10cm",
        # "category": "Curativos",
        # "quantity": 200,
        # "location": "Prateleira B2",
        # "expiryDate": "2027-09-01",
        # "unity_price": 0.45,
        # "ideal_quantity": 300
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
            