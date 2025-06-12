import json
from datetime import datetime
from domain.stock_manager import StockManager

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    
estoque = StockManager(data)


while True:
    print("\n--- Menu Estoque ---")
    print("1. Mostrar estoque")
    print("2. Buscar item por nome")
    print("3. Adicionar novo item")
    print("4. Mostrar itens críticos")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        estoque.mostrar_estoque()

    elif opcao == "2":
        nome = input("Digite o nome do item a ser buscado: ")
        item = estoque.buscar_por_nome(nome)
        if item:
            print("\nItem encontrado:")
            print(20 * "-")
            print(f"ID: {item['id']}")
            print(f"Nome: {item['itemName']}")
            print(f"Categoria: {item['category']}")
            print(f"Quantidade: {item['quantity']}")
            print(f"Localização: {item['location']}")
            print(f"Data de Validade: {item['expiryDate']}")
            print(f"Preço Unitário: R$ {item['unity_price']:.2f}")
            print(f"Quantidade Ideal: {item['ideal_quantity']}")
        else:
            print("Item não encontrado.")

    elif opcao == "3":
        try:
            novo_item = {
                "id": int(input("ID: ")),
                "itemName": input("Nome do item: "),
                "category": input("Categoria: "),
                "quantity": int(input("Quantidade: ")),
                "location": input("Localização: "),
                "expiryDate": input("Data de validade (YYYY-MM-DD): "),
                "unity_price": float(input("Preço unitário: ")),
                "ideal_quantity": int(input("Quantidade ideal: "))
            }
            # Valida a data
            datetime.strptime(novo_item["expiryDate"], "%Y-%m-%d")
            estoque.adicionar_item(novo_item)
            print("Item adicionado com sucesso.")
        except Exception as e:
            print("Erro ao adicionar item:", e)

    elif opcao == "4":
        estoque.itens_criticos()
    elif opcao == "5":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
        