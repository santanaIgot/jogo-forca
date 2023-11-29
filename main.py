import random 

def imprimir_msg_abertura():
    print("-------comecando jogo------")


def carrega_palavra_secreta():

    arquivo = open("palavra.txt", "r")
    palavras = []
    # cada linha representará uma palavra 
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def jogar():
 
    imprimir_msg_abertura()

    palavra_secreta = carrega_palavra_secreta()

    
    enforcou = False
    acertou = False
    listas_acertadas = inicializa_letras_acertadas(palavra_secreta)



    erros = 0 

    print(listas_acertadas)
    
    while not enforcou and not acertou:
        
        chute = input("Qual letra ?")
        chute = chute.strip().upper()
        
        # Criamos essa estrutura de repeticao para a variavel letra ir percorrendo as str e printalas depois da estrutura de condicao 
        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    # print('Encontrei a letra {} na posião {}'.format(letra,index))
                    listas_acertadas[index]  = letra
                index = index + 1
        else:
            erros = erros + 1

        enforcou = erros == 6
        acertou = "_" not in listas_acertadas
        print(listas_acertadas)
    if acertou:
        print("----------parabéns você acertou---------------")
    else:
        print("----------voce perdeu------------------")
    print("fim")
    
    

# O que é variável de indice ?
# Uma variavel de indice, é uma variavel que armazena a posicao de indice de elemento em uma colecao de dados 
# , como um array ou string. O indice geralmente é um numero inteiro, que representa a posicao do elemento 
# dentro da colecao. Ao utilizar uma variavel de indice , é possível acessa, atualizar e manipular elementos especificos
# de forma individual 
# index = 0
# listas_acertadas[index]
    
# O que são tuplas?
# para comeco, tuplas comecam com parenteses, diferentemente de listas que sao com colchetes 
# tuplas não podem ser alteradas como listas, é imutavel 



if __name__ == "__main__":
    jogar()