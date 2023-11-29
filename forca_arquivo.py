arquivo = open("palavra.txt", "w")

print(arquivo)

arquivo.write("banana")


arquivo.close()


arquivo = open("palavra.txt", "a")
arquivo.write("morango\n")
arquivo.write("manga\n")

arquivo.close()

arquivo = open("palavra.txt", "r")

arquivo.read()

linha = arquivo.read()


for linha in arquivo:
     print(linha)
