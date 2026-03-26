cantidad = int(input("Cuantos numeros vamos a poner: "))

lista_num = []
while len(lista_num) != cantidad:
    num = int(input("Ingresa un num entero: "))
    lista_num.append(num)
print (f"La lista antes de arreglar es: {lista_num}")
maximo = max(lista_num)
minimo = min(lista_num)

for i in range(len(lista_num)):
    for j in range(len(lista_num) - 1):
        if lista_num[j] > lista_num[j+1]:
            lista_num[j], lista_num[j+1] = lista_num[j+1], lista_num[j]

print (f"La lista ordenada es: {lista_num}")