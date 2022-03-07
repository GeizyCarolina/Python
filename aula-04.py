#Conjuntos em python

# definição da lista
lista = [1, 2, 3, 2, 5, 2, 7, 2, 9, 2]
print(lista)

# 10 elementos
print(len(lista))
print(type(lista)) # tipo de dado

# definindo o conjunto
conjunto = {1, 2, 3, 2, 5, 2, 7, 2, 9, 2}
print(conjunto)

# 6 elementos
print(len(conjunto))

print(type(conjunto)) # tipo de dado

A = {1, 2, 3}
B = {2, 3, 4}
print(A)
print(B)

# união (junta A E B)
c= A.union(B)
print(c)

# interseção (TEM NO A E TEM NO B)
c= A.intersection(B)
print(c)

# Diferença A - B (TEM NO A MAS N TEM NO B)
print(A - B)

# Diferença B - A (TEM NO B MAS N TEM NO A)
print(B - A)




A = {1, 2, 3, 4, 5, 6, 7, 8}
B = {2, 4, 6, 8, 11}

# Sabemos que B é um subconjunto "próprio" de A

cont = 0 

for b in B:
    # se o elemento B[i] está presente no conjunto A 
    if(b in A):
       cont += 1

if(cont == len(B)):
    print("É subconjunto")
else:
    print("Nao", "quantidade de elementos = ", cont)



# B é subconjunto de A?
print(B.issubset(A))

# A é subconjunto de B?
print(A.issubset(B))


# Diferença simétrica
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# é o resultado da diferença entre União e Interseção
print(A.symmetric_difference(B))


# produto cartesiano
p = set()
for a in A:
  for b in B:
    p.add((a, b))
print(p)

# produto cartesiano utilizando
# função lambda (A MESMA COISA DA DE CIMA)
p = {(a, b) for a in A for b in B}
print(p) 



# Associatividade

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {4, 6, 8, 10}

