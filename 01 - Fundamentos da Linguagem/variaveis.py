from pathlib import types

nome = "Carlos Eduardo"  # string
idade = 49  # integer
estado = "São Paulo"  # string
tem_cachorro = True  # boolean
altura = 1.78  # float

print(type(nome))
print(type(idade))
print(type(estado))
print(type(tem_cachorro))
print(type(altura))

print(
    f"Olá {nome}, você tem {idade} anos e é do estado de {estado},e tem cachorro {tem_cachorro}, e a sua altura {altura}"
)
