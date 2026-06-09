#4 – Solicite ao usuário um superpoder entre três opções: “força”, “velocidade” ou “voo”.
#Use estruturas de decisão para exibir uma frase que diga qual super-herói você seria com
#base na escolha:
#• Se escolher “força”: exiba “Você seria o Hulk!”;
#• Se escolher “velocidade”: exiba “Você seria o Flash!”;
#• Se escolher “voo”: exiba “Você seria o Superman!”.

poder = int(input("escolha seu poder.\nDigite 1 para força.\nDigite 2 para velocidade.\nDigite 3 para voo: "))
            
if poder == 1 :
    print("Você seria o Hulk!")

if poder == 2 :
    print("Você seria o Flash!")

if poder == 3 :
    print("Você seria o Superman!")