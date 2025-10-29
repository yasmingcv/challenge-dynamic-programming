import json
from datetime import datetime
from domain.stock_manager import StockManager

with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    
estoque = StockManager(data)


while True:
    print("\n" + "="*70)
    print("MENU GERENCIADOR DE ESTOQUE")
    print("="*70)
    print("1. Mostrar estoque")
    print("2. Buscar item por nome (binária)")
    print("3. Adicionar novo item")
    print("4. Mostrar itens críticos")
    print("5. Fila de reposição (itens abaixo do ideal)")
    print("6. Pilha de validade (ordem de vencimento)")
    print("7. Busca sequencial por nome")
    print("8. Ordenar estoque por nome (Merge Sort)")
    print("9. Ordenar estoque por nome (Quick Sort)")
    print("10. Otimizar reabastecimento - Método RECURSIVO")
    print("11. Otimizar reabastecimento - Método MEMOIZATION")
    print("12. Otimizar reabastecimento - Método ITERATIVO")
    print("13. Comparar todos os métodos de otimização de reabastecimento")
    
    print("\n0. Sair")
    print("="*70)

    opcao = input("\nEscolha uma opção: ")

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
            print("\n--- Adicionar Novo Item ---")
            novo_item = {
                "id": int(input("ID: ")),
                "itemName": input("Nome do item: "),
                "category": input("Categoria: "),
                "quantity": int(input("Quantidade: ")),
                "location": input("Localização: "),
                "expiryDate": input("Data de validade (YYYY-MM-DD) ou deixe vazio: "),
                "unity_price": float(input("Preço unitário: ")),
                "ideal_quantity": int(input("Quantidade ideal: "))
            }
            
            # Valida a data se fornecida
            if novo_item["expiryDate"]:
                datetime.strptime(novo_item["expiryDate"], "%Y-%m-%d")
            else:
                novo_item["expiryDate"] = None
                
            estoque.adicionar_item(novo_item)
            print("✓ Item adicionado com sucesso.")
        except ValueError as e:
            print(f"✗ Erro: Valor inválido - {e}")
        except Exception as e:
            print(f"✗ Erro ao adicionar item: {e}")

    elif opcao == "4":
        estoque.itens_criticos()

    elif opcao == "5":
        fila = estoque.fila_de_reposicao()
        print("\nFila de reposição (itens abaixo do ideal):")
        if fila:
            for i, item in enumerate(fila, 1):
                print(20 * "-")
                print(f"Posição na fila: {i}")
                print(f"ID: {item['id']}")
                print(f"Nome: {item['itemName']}")
                print(f"Quantidade: {item['quantity']}")
                print(f"Ideal: {item['ideal_quantity']}")
                print(f"Déficit: {item['ideal_quantity'] - item['quantity']}")
        else:
            print("✓ Não há itens abaixo do ideal!")

    elif opcao == "6":
        pilha = estoque.pilha_de_validade()
        print("\nPilha de validade (ordem de vencimento - topo vence primeiro):")
        for i, item in enumerate(pilha, 1):
            print(20 * "-")
            print(f"Posição: {i}")
            print(f"ID: {item['id']}")
            print(f"Nome: {item['itemName']}")
            print(f"Validade: {item['expiryDate'] if item['expiryDate'] else 'Sem validade'}")

    elif opcao == "7":
        nome = input("Digite o nome do item a ser buscado (sequencial): ")
        item = estoque.busca_sequencial_nome(nome)
        if item:
            print("\nItem encontrado (busca sequencial):")
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
            print("✗ Item não encontrado.")

    elif opcao == "8":
        print("\nOrdenando estoque usando Merge Sort...")
        estoque.ordenar_estoque_merge()
        print("✓ Estoque ordenado por nome usando Merge Sort.")

    elif opcao == "9":
        print("\nOrdenando estoque usando Quick Sort...")
        estoque.ordenar_estoque_quick()
        print("✓ Estoque ordenado por nome usando Quick Sort.")

    # ============================================================================
    # NOVAS OPÇÕES - SPRINT 4
    # ============================================================================
    
    elif opcao == "10":
        try:
            print("\n" + "="*70)
            print("OTIMIZAÇÃO DE REABASTECIMENTO - MÉTODO RECURSIVO")
            print("="*70)
            orcamento = float(input("\nDigite o orçamento disponível (R$): "))
            
            if orcamento <= 0:
                print("✗ Erro: O orçamento deve ser maior que zero.")
                continue
            
            print("\nProcessando... (pode demorar para muitos itens)")
            resultado = estoque.otimizar_reabastecimento(orcamento, 'recursivo')
            estoque.exibir_otimizacao(resultado)
            
        except ValueError:
            print("✗ Erro: Digite um valor numérico válido.")
        except Exception as e:
            print(f"✗ Erro ao otimizar: {e}")

    elif opcao == "11":
        try:
            print("\n" + "="*70)
            print("OTIMIZAÇÃO DE REABASTECIMENTO - MÉTODO MEMOIZATION")
            print("="*70)
            orcamento = float(input("\nDigite o orçamento disponível (R$): "))
            
            if orcamento <= 0:
                print("✗ Erro: O orçamento deve ser maior que zero.")
                continue
            
            print("\nProcessando com memoization...")
            resultado = estoque.otimizar_reabastecimento(orcamento, 'memoization')
            estoque.exibir_otimizacao(resultado)
            
        except ValueError:
            print("✗ Erro: Digite um valor numérico válido.")
        except Exception as e:
            print(f"✗ Erro ao otimizar: {e}")

    elif opcao == "12":
        try:
            print("\n" + "="*70)
            print("OTIMIZAÇÃO DE REABASTECIMENTO - MÉTODO ITERATIVO")
            print("="*70)
            orcamento = float(input("\nDigite o orçamento disponível (R$): "))
            
            if orcamento <= 0:
                print("✗ Erro: O orçamento deve ser maior que zero.")
                continue
            
            print("\nProcessando com método iterativo...")
            resultado = estoque.otimizar_reabastecimento(orcamento, 'iterativo')
            estoque.exibir_otimizacao(resultado)
            
        except ValueError:
            print("✗ Erro: Digite um valor numérico válido.")
        except Exception as e:
            print(f"✗ Erro ao otimizar: {e}")

    elif opcao == "13":
        try:
            print("\n" + "="*70)
            print("COMPARAÇÃO DE MÉTODOS")
            print("="*70)
            orcamento = float(input("\nDigite o orçamento disponível (R$): "))
            
            if orcamento <= 0:
                print("✗ Erro: O orçamento deve ser maior que zero.")
                continue
            
            print("\nExecutando os três métodos para comparação...")
            print("(Isso pode demorar alguns segundos)")
            
            resultados = estoque.comparar_metodos_pd(orcamento)
            
            # Exibe análise adicional
            print("\n" + "="*70)
            print("ANÁLISE DETALHADA")
            print("="*70)
            
            for metodo, resultado in resultados.items():
                print(f"\n{metodo.upper()}:")
                print(f"  Benefício: {resultado['beneficio_maximo']}")
                print(f"  Custo: R$ {resultado['custo_total']:.2f}")
                print(f"  Itens selecionados: {resultado['itens_reabastecidos']}")
                print(f"  Economia: R$ {resultado['orcamento_restante']:.2f}")
                
                if resultado['itens_selecionados']:
                    print(f"  Itens: ", end="")
                    nomes = [item['item']['itemName'] for item in resultado['itens_selecionados']]
                    print(", ".join(nomes))
            
        except ValueError:
            print("✗ Erro: Digite um valor numérico válido.")
        except Exception as e:
            print(f"✗ Erro ao comparar métodos: {e}")

    elif opcao == "0":
        print("\n" + "="*70)
        print("Encerrando o Gerenciador de Estoque...")
        print("="*70)
        break

    else:
        print("\n✗ Opção inválida. Tente novamente.")
    
    # Pausa para visualização
    input("\nPressione ENTER para continuar...")