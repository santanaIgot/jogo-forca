def jogar():
    palavra_secreta = "Banana"

    enforcou = False
    acertou = False
    while not enforcou and not acertou:
        
        chute = input("Qual letra ?")
        chute = chute.strip()
        # Criamos essa estrutura de repeticao para a variavel letra ir percorrendo as str e printalas depois da estrutura de condicao 
        index = 0
        for letra in palavra_secreta:
            if chute.upper() == letra.upper():
                print('Encontrei a letra {} na posião {}'.format(letra,index))
            index = index + 1

        print("Jogando...")
        break


    



jogar()