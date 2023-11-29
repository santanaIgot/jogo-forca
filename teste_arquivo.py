arquivo = open("teste.txt", "w")


print(arquivo)

arquivo.write("hello word!!")
arquivo.close()

# Esse "a" é de append, para adicionar alguma coisa ao arquivo 
arquivo = open("teste.txt", "a")
# esta funcao "write, escreve algo no arquivo"
arquivo.write("morango\n")
arquivo.write("maca\n")
arquivo.close()

arquivo = open("teste.txt", "r")

linha = arquivo.readline()


for linha in arquivo:
    print(linha, end='\n')

