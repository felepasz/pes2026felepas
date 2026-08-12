'''1 - Nossa necessidade é utilizar o recurso de liberação de portas dos Laboratórios de
Informática utilizando os dispositivos instalados em cada porta com fechadura eletrônica.
Para tal, desenvolveremos um sistema que identifique e autorize a entrada dos
professores já cadastrados no sistema de uso dos laboratórios.
O sistema deve possuir:
• Um cadastro completo de professores (adicionar, alterar, excluir e listar) que
associe o código do professor ao seu nome, alguns professores já devem ser précadastrados, veja a lista abaixo;
• Um cadastro completo dos acessos dos professores aos laboratórios (adicionar,
alterar, excluir e listar), serão utilizados 6 laboratórios com as nomenclaturas
Lab102, Lab103, Lab104, Lab105, Lab106, Lab107 – os laboratórios são fixos no
sistema, o que pode ser alterado são os acessos, alguns professores já devem
ser pré-cadastrados nos laboratórios, veja a outra lista abaixo (para facilitar a
implementação, sugere-se que os laboratórios sejam associados ao código do
professor e não ao seu nome);
• Teste de acesso ao laboratório: deve ser possível informar o nome de um
laboratório e um código de professor para verificar se o acesso é permitido ou não
(por exemplo, nesse teste deveria ser possível escolher o Lab103 e informar o
código de professor 002, nesse caso, o sistema deve negar o acesso).
Pré-cadastro de Professores (códigos x nomes)
001 – Prof Thiago Paes
002 – Prof Schalata
003 – Prof Ignácio
004 – Prof Ryan
005 – Prof André
006 – Profª Fabiana
007 – Prof Alberto
008 – Prof Juliano
009 – Prof Thiago Waltrik
010 – Prof João Eduardo
Pré-cadastro de Acessos (laboratório x professor)
• Lab102 – Prof Ignácio, Prof Thiago Paes, Profª Ryan, Prof André, Profª
Fabiana;
• Lab103 – Prof Alberto;
• Lab104 – Prof Ryan, Prof Juliano, Prof Schalata, Prof André;
• Lab105 – Prof Ignácio, Prof Alberto, Prof Thiago Waltrik, Prof Thiago Paes;
• Lab106 – Prof Schalata, Prof Ignácio, Prof Thiago Waltrik, Prof Thiago Paes;
• Lab107 – Prof André, Prof Schalata, Prof Thiago Waltrik, Prof Thiago Paes, Prof
João Eduardo.'''

professores = {
    "001": "Prof Thiago Paes",
    "002": "Prof Schalata",
    "003": "Prof Ignácio",
    "004": "Prof Ryan",
    "005": "Prof André",
    "006": "Profª Fabiana",
    "007": "Prof Alberto",
    "008": "Prof Juliano",
    "009": "Prof Thiago Waltrik",
    "010": "Prof João Eduardo"
}

acessos = {
    "Lab102": ["003", "001", "004", "005", "006"],
    "Lab103": ["007"],
    "Lab104": ["004", "008", "002", "005"],
    "Lab105": ["003", "007", "009", "001"],
    "Lab106": ["002", "003", "009", "001"],
    "Lab107": ["005", "002", "009", "001", "010"]
}

laboratorios = ["Lab102", "Lab103", "Lab104", "Lab105", "Lab106", "Lab107"]

while True:
    print("\n========== CONTROLE DE LABORATORIOS ==========")
    print("1 - Adicionar professor")
    print("2 - Alterar professor")
    print("3 - Excluir professor")
    print("4 - Listar professores")
    print("5 - Adicionar acesso")
    print("6 - Excluir acesso")
    print("7 - Listar acessos")
    print("8 - Testar acesso")
    print("0 - Sair")

    opcao = input("Escolha uma opcao: ")

    if opcao == "1":
        codigo = input("Digite o codigo do professor: ")

        if codigo in professores:
            print("Professor ja cadastrado.")
        else:
            nome = input("Digite o nome do professor: ")
            professores[codigo] = nome
            print("Professor cadastrado.")

    elif opcao == "2":
        codigo = input("Digite o codigo do professor: ")

        if codigo in professores:
            nome = input("Digite o novo nome: ")
            professores[codigo] = nome
            print("Professor alterado.")
        else:
            print("Professor nao encontrado.")

   
    elif opcao == "3":
        codigo = input("Digite o codigo do professor: ")

        if codigo in professores:
             
            for laboratorio in laboratorios:
                if codigo in acessos[laboratorio]:
                    acessos[laboratorio].remove(codigo)

            professores.pop(codigo)
            print("Professor excluido.")
        else:
            print("Professor nao encontrado.")

    elif opcao == "4":
        print("\n--- PROFESSORES ---")

        for codigo in professores:
            print(codigo, "-", professores[codigo])

    elif opcao == "5":
        print("\n--- PROFESSORES ---")

        for codigo in professores:
            print(codigo, "-", professores[codigo])

        codigo = input("Digite o codigo do professor: ")

        if codigo in professores:
            print("\n--- LABORATORIOS ---")

            for laboratorio in laboratorios:
                print(laboratorio)

            laboratorio = input("Digite o laboratorio: ")

            if laboratorio in laboratorios:
                if codigo in acessos[laboratorio]:
                    print("Acesso ja cadastrado.")
                else:
                    acessos[laboratorio].append(codigo)
                    print("Acesso cadastrado.")
            else:
                print("Laboratorio invalido.")
        else:
            print("Professor nao cadastrado.")

    elif opcao == "6":
        print("\n--- LABORATORIOS ---")

        for laboratorio in laboratorios:
            print(laboratorio)

        laboratorio = input("Digite o laboratorio: ")

        if laboratorio in laboratorios:
            codigo = input("Digite o codigo do professor: ")

            if codigo in acessos[laboratorio]:
                acessos[laboratorio].remove(codigo)
                print("Acesso excluido.")
            else:
                print("Acesso nao encontrado.")
        else:
            print("Laboratorio invalido.")

    elif opcao == "7":
        print("\n--- ACESSOS ---")

        for laboratorio in laboratorios:
            print("\n", laboratorio)

            for codigo in acessos[laboratorio]:
                print(codigo, "-", professores[codigo])

    elif opcao == "8":
        laboratorio = input("Digite o laboratorio: ")
        codigo = input("Digite o codigo do professor: ")

        if laboratorio in laboratorios:
            if codigo in professores:
                if codigo in acessos[laboratorio]:
                    print("ACESSO PERMITIDO!")
                    print("Professor:", professores[codigo])
                else:
                    print("ACESSO NEGADO!")
            else:
                print("Professor nao cadastrado.")
        else:
            print("Laboratorio invalido.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opcao invalida.")


        
        
            

        
            
            
        
        
    

    
    
     
    