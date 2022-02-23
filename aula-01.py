print("Hello Word")

# Um texto com várias linhas
print("""Um texto
com várias
linhas
""")

print(2+2)

#Tipos de Variáveis

a = 2
print(a, type(a))

a = 2.2
print(a, type(a))

a = True
print(a, type(a))

a = "palavras"
print(a, type(a))

# crinado uma lista 

lista = [1,2,3,4,5,6,7]
print(lista, type(lista))

# indice da lista 
print(lista[2])

#adicionar elemento a lista da
lista.append(10)
print(lista)

# deleta elemento da lista pelo valor do elemento
lista.remove(10)
print(lista)

# deleta elemento da lista pelo valor do indice
del lista[2]
print(lista)

# array debtro de uma lista
lista2 = [1,2.0,'3',[4,5,6]]
print(type(lista2[3]))
print(lista2)
print(lista2[3])

# Dicionario

dicionario = {
    "chava1": "valor1",
    "chave2": "valor2",
    "chave3": "valor3",
    "chave4": 20,
    10: 200
}

print(dicionario)
print(type(dicionario))

# valor do elemento pela chave
print(dicionario[10])
print(dicionario["chave4"])

# adicionar valor 
dicionario["chave5"] = "outra chave adicionada"
print(dicionario)

# alterar o valor da chave 
dicionario["chave5"] = "trocou o valor"
print(dicionario)

# exibir so as chaves
print(dicionario.keys())

# exibir so os valores das chaves
print(dicionario.values())