usuarios = {
    "João": 25,
    "Maria": 17,
    "Ana": 19,
    "Carlos": 16,
    "Beatriz": 22,
    "Pedro": 15,
    "Luiza": 18
}

dict_classificacao_usuarios = {
    chave: "Adulto" if valor > 18 else "Menor"
    for chave, valor in usuarios.items()
}

print(dict_classificacao_usuarios)
