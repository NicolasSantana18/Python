#Lista Decrescente sendo adicionada ao arquivo txt
lista = []
arquivo = open("lista_decrescente", "a+", encoding = "UTF-8")
for i in range(100, 0, -1):
    arquivo.write(f"{i}\n")
    print(i)