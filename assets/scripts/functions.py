def cadastroDeJogador(nome, email):
    arquivo = open('assets/logs/cadastroJogadores.txt','a')
    arquivo.write("\n------------------------------------------------------------------\n")
    arquivo.write(f"Nome: {nome}\n")
    arquivo.write(f"Email: {email}\n")
    arquivo.write("------------------------------------------------------------------\n")
    arquivo.close()