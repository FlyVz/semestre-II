# numeros = (100, 50) #mais utilizado
# # numero = "100", "50"

# print( numeros[0]) #acessando o primeiro elemento da tupla
# print( numeros[1]) #acessando o segundo elemento da tupla
    
# tupla = ("r")
# print  (type(tupla)) #sem a , e uma tupa

# tupla1 = ("r",) #com a virgula no final e uma tupla
# print  (type(tupla1)) #mostrando o tipo da tupla

# t = tuple()
# print(t)

# numeros = (100, 50) #mais utilizado

# for numero in numeros:
#     print(numero)
    
# numeros = (300, 800)

# for numero in numeros:
#     print(numero)

# if (0, 1, 2) < (0, 3, 4):
#     print(True)
# else:
#     print(False)

# txt = "algoritmos e a materia mais facil do curso"
# palavras = txt.split() 
# lista = list()
# for palavra in palavras:
#     lista.append((len(palavra), palavra))
    
# print(lista)

# lista.sort(reverse=True) 
# res = list()
# for tamanho, palavra in lista:
#     res.append(palavra)
#     print(res)
#     print(tamanho)

x = 20
y = 70

x, y = y, x

print(x)
print(y)