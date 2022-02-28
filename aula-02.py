#Operadores Lógicos e Matemáticos

# ==
# !=
# >
# >=
# <
# < =

a = 30
b = 20

maior = a >= b 
print (maior)

# operador in e not in

lista = [1, 2.0, '3', [4, 5, 6]]

# contem o numero 7 nesta lista ? 
contem = 7 in lista
print (contem)

contem = 7 not in lista
print (contem)

# operador lógico E
x = 10 > 5 and 20 > 3
print (x)

# operador lógico OU
x = 10 > 5 or 3 >20
print (x)


##############################################

# Operadores
# +
# -
# /
# *

a = 10
b = 20

resultado = b / a
print (resultado)

# Operador **
# expoente (power)

a = 2
b = 10

resultado = a ** b
print (resultado)

# operador mod
a = 5
b = 2
 
resultado = a % b
print (resultado)

lista2  = [2,4,5,8,10]
print (lista2)

#############################################

#Decisão

# if, else
a = 10
b = 20

if a > b:
  print("A maior que B")
else:
  print("B maior ou igual a A")


#if, elif, else

a = 10
b = 20
c = 30

if a > b:
  print('a > b')
elif b < c: # else if das outras linguagens
  print('b < c')
else:
  print('entrei no else')
  


######################################

#Laços de Repetição

# Em Java:  for ( int 1=0;i<10;i++)

# o laço for é um tiquim diferente

# o primeiro parâmetro (opcional): início da contagem 
# o segundo parâmetro (obrigatório): final da contagem
# o terceiro parâmetro (opcional): passo



# com 1 parâmetro (apenas o final)

for i in range(10):
 print(i)


# com 2 parâmetros (início e final)
for i in range(3, 10):
  print(i)


# com 3 parâmetros (início, final e passo)
for i in range(3, 10, 2):
  print(i)


# percorrendo a lista

lista3 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(lista3)

for x in lista3:
   print(x)

for x in range(len(lista3)):
  # percorrendo pelo índice da lista
  print("lista", lista3[x])
