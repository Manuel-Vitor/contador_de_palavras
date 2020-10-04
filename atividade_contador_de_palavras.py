def contagem(file_name):  
    try:
        with open (file_name) as arquivo:
            leitor = arquivo.read()  

    except FileNotFoundError:
        print("Este arquivo '{}'nao existe".format(file_name))
    
    else:
        print("Este arquivo e '{}' e tem {} palavras".format(file_name, len(leitor.split())))

contagem("book_the_republic.txt")