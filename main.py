def jogar():
    
    palavra_secreta = "Banana"
    enforcou = False
    acertou = False
    listas_acertadas = ["_", "_", "_", "_", "_", "_",]

    print(listas_acertadas)
    
    while not enforcou and not acertou:
        
        chute = input("Qual letra ?")
        chute = chute.strip()
        
        # Criamos essa estrutura de repeticao para a variavel letra ir percorrendo as str e printalas depois da estrutura de condicao 
        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                # print('Encontrei a letra {} na posião {}'.format(letra,index))
                listas_acertadas[index]  = letra
            index = index + 1
        print(listas_acertadas)
    

# O que é variável de indice ?
# Uma variavel de indice, é uma variavel que armazena a posicao de indice de elemento em uma colecao de dados 
# , como um array ou string. O indice geralmente é um numero inteiro, que representa a posicao do elemento 
# dentro da colecao. Ao utilizar uma variavel de indice , é possível acessa, atualizar e manipular elementos especificos
# de forma individual 
# index = 0
# listas_acertadas[index]
    



jogar()