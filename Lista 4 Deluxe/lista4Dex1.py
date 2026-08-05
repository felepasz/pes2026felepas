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

profs = {'001' : "Prof Thiago Paes",
'002' : "Prof Schalata",
'003' : "Prof Ignácio",
'004' : "Prof Ryan",
'005' : "Prof André",
'006' : "Profª Fabiana",
'007' : "Prof Alberto",
'008' : "Prof Juliano",
'009' : "Prof Thiago Waltrik",
'010' : "Prof João Eduardo"}

lab102 = ['003', '001', '004', '005'] 

lab103 = ['007']

lab104 = ['004', '008', '002', '005']

lab105 = ['003', '007' , '009', '001']

lab106 = ['002', '003', '009', '001']
  
lab107 = ['006', '002', '009' , '001', '010']


while True:
    print("Dicionario de Professores")
    print("---------------")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("4 - Alterar")
    print("5 - Teste de acesso")
    print("6 - Alterar acesso laboratório")
    print("7 - Excluir acesso")
    print("8 - Listar acessos")
    print("9 - ")
    print("0 - Sair")
    opcao = int(input("Opção: "))

    if opcao == 0:
        print("Programa encerrado!")
        break
    
    elif opcao == 1:
        novocad = str(input("Digite o código do novo cadastrado: ")).zfill(3)
        if novocad in profs:
            print("Código já existente")
        else:
            nomecad = str(input("Digite o nome do novo cadastrado: "))
            profs [novocad] = nomecad
            print("Cadastrado com sucesso!")
            
    elif opcao == 2:
        excluircod = str(input("Digite o código a ser excluido: "))
        if excluircod in profs:
            del profs[excluircod]
            print("Código excluido")
        else:
            print("Código inexistente")
            
    elif opcao == 3:
        print("Professores")

        for codigo, nome in sorted(profs.items()):
            print(codigo, "-", nome)

            print("Professor excluído.")
        else:
            print("Professor não encontrado.")
            
    

        
        
            

        
            
            
        
        
    

    
    
     
    