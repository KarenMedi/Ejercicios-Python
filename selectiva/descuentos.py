import random
valor_compra=int(input("ingrese el valor de la compra"))
aleatorio = random.choice(["con la balota roja","con la balota verde","con la balota azul","con la balota amarilla","con la balota negra"])

print(aleatorio)
if aleatorio=='con la balota roja':
    balota_roja=valor_compra*0.10
    print("el descuento total a pagar seria de:",balota_roja)

elif aleatorio =='con la balota verde':
    balota_verde=valor_compra*0.15
    print("el descuento total a pagarseria de:",balota_verde)

elif aleatorio =='con la balota azul':
    balota_azul=valor_compra*0,20
    print("el descuento total a pagar seria de:",balota_azul)

elif aleatorio =='von la balota amarilla':
    balota_amarilla=valor_compra*0.50
    print("el descuento total a pagar seria de:", balota_amarilla)

elif aleatorio == 'con la balota negra':
    balota_negra=valor_compra*1.0
    print("el descuento total a pagar seria de:",balota_negra)
    
