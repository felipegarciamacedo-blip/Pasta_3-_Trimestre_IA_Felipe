cardapio = ["pastel", "coxinha", "suco"]

cardapio.append("lasanha")
cardapio.pop(1)
print(cardapio)

pedido = input('Qual seu pedido? ').strip().lower()

if pedido not in cardapio:
    print("Desculpe, este item não está no cardápio.")
else:
    print(f"Pedido confirmado: {pedido}!")
    print(cardapio)
