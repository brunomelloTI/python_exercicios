preco = float(input("Informe o preço do produto: "))
v = (preco * 5) / 100
v1 = preco - v
print("Preço com 5% de desconto: R${:.4}" .format(v1))