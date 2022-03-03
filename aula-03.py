#Funções

# criando uma função
def nome_funcao(parametro1, parametro2):
    # corpo da função
    return parametro1 + parametro2

r = nome_funcao(2,2)
print('Resultado = ' , r)

print(r, type(r))


# função com valores padrão

def funcao1(a=3, b=2):
  print('valor de a=', a)
  print('valor de b=', b)
  print('soma= ', a + b)

# forma 1 de chamar a função
funcao1()

# forma 2 de usar a função
funcao1(a=15, b=75)

# a função também é um tipo...
print(type(funcao1))


# eu posso atribuir a função à uma variável
f = funcao1
f(12, 23)