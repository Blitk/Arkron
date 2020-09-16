from scripts import *	
from time import sleep	

						#Personagem

hero = {"Nome": None,"Raça": None, "Classe": None, "Atributos": None}
atributos = {"Força": None, "Magia": None, "Inteligência": None, "Audacia": None, "Bravura": 5}
Armamento = {"Arma": None, "Dano": None }
vida = {"Vida":100, "Magia":100, "Stamina":100}
Poções = {"Vida":10, "Magia":10, "Stamina":10}


iniciar()
logo()
abertura()

print("\033[33mSeja bem vindo à Heaven Hill jovem aliado")
sleep(1)
hero["Nome"] = str(input("Qual é o seu Nome? "))
print("\n\n\n")

print("✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠ Raças ✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠")
print("\n   ❖ Elfo\n   ❖ Orc\n   ❖ Humano\n   ❖ Draconiano\n   ❖ Espectro\n")
hero["Raça"] = str(input("Qual é sua Raça? ")).capitalize()
print("\n\n\n")

print("✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠ Classe ✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠")
print("\n   ❖ Arqueiro\n   ❖ Guerreiro\n   ❖ Mago\n   ❖ Assassino\n")
hero["Classe"] = str(input("Qual é sua Classe? ")).capitalize()
print("\n\n\n")


print("✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠ Atributos ✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠")
print("\nSão 100 pontos para dividir em \033[31m4\033[33m atributos\n")
while True:
    pontos = 100
    atributos["Força"] = int(input("\nPontos de \033[32mFORÇA\033[33m: "))
    pontos -= atributos["Força"]
    if pontos == 0:
        print("Você esgotou seus pontos...")
    else:
        atributos["Magia"] = int(input("\nPontos de \033[34mMAGIA\033[33m: "))
        pontos -= atributos["Magia"]
        if pontos == 0:
            print("Você esgotou seus pontos...")
        else:
            atributos["Inteligência"] = int(input("\nPontos de \033[36mINTELIGÊNCIA\033[33m: "))
            pontos -= atributos["Inteligência"]
            if pontos == 0:
                print("Você esgotou seus pontos...")
            else:
                atributos["Audacia"] = int(input("\nPontos de \033[31mAUDACIA\033[33m: "))
                pontos -= atributos["Audacia"]
    for k, i in atributos.items():
        print(f"{k}: {i}")
    print(f"Restam {pontos} pontos")
    ask = str(input("\nDeseja alterar os atributos? ")).upper()
    if ask in "SIM":
        continue
    elif ask in "NÃO" or ask == "N" or ask == "NAO":
        break
print("\n\n\n")
#atributos
hero["Atributos"] = atributos

if hero["Raça"] == "Elfo":
    atributos["Inteligência"] += 20

elif hero["Raça"] == "Orc":
    atributos["Força"] += 20

elif hero["Raça"] == "Humano":
    atributos["Audacia"] += 20

elif hero["Raça"] == "Draconiano":
    atributos["Magia"] += 20

elif hero["Raça"] == "Espectro":
    atributos["Magia"] += 10
    atributos["Inteligência"] += 10

#classes
if hero["Classe"] == "Arqueiro":
    atributos["Inteligência"] += 20

elif hero["Classe"] == "Guerreiro":
    atributos["Força"] += 20

elif hero["Classe"] == "Mago":
    atributos["Magia"] += 20

elif hero["Classe"] == "Assassino":
    atributos["Audacia"] += 20


#Armamento
if hero["Classe"] == "Arqueiro":
    Armamento["Arma"] = "Arco Leve"
    Armamento["Dano"] = 10

elif hero["Classe"] == "Guerreiro":
    Armamento["Arma"] = "Machado Leve"
    Armamento["Dano"] = 10

elif hero["Classe"] == "Mago":
    Armamento["Arma"] = "Cajado de Chamas"
    Armamento["Dano"] = 10

elif hero["Classe"] == "Assassino":
    Armamento["Arma"] = "Punhal Serrado"
    Armamento["Dano"] = 10

print('\n✠✠✠✠✠✠✠✠✠✠✠✠ Dados do aliado ✠✠✠✠✠✠✠✠✠✠✠✠\n')
for k, i in hero.items():
    if k == "Atributos":
        print("Atributos:")
        for ke, it in hero["Atributos"].items():
            print(f" -{ke}: {it}")
    if k != "Atributos":
        print(f"{k}: {i}")
print('\n\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠')
sleep(5)

#história
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
exp1 = "	A Terra sempre foi um lugar de poucas guerras, mas desde a descoberta das fissuras entre os mundos, tudo se resume em caos. Criaturas, Deuses e Demônios, todos contra os humanos, mas em meio a essa guerra de mundos, houve a união de diferentes, os elfos, orcs, draconianos e os espectros, que lutam por um bem maior, a paz entre as diferentes realidades, mas claro que existem os que preferem o caos e a guerra.\n\n"
delay(exp1)
sleep(2)
exp2 = "Para entendermos cada uma dessas realidades, precisamos ir para o ínicio de tudo, e tudo começa com as divindades:\n\n    - Waq o deus da sabedoria\n\n    - Jit o deus da força\n\n    - Kay o deus da magia\n\n    - Dax o deus das sombras\n\n    - Pak o deus da bravura\n\n    - Arkron o deus dos mortos.\n\nAmbos os deuses viviam juntos em harmonia, até que Arkron começou a causar discórdia entre seus irmãos para causar um desequilibrio dos poderes, o que culminou em uma briga, e a separação de ambos, e cada um criou sua dimensão, sendo:\n\n    - Waquios a dimensão dos Elfos, seres extremamente inteligentes, pacificos e desenvolvidos.\n\n    - Jitkos a dimensão dos Orcs, seres com muita força e que vivem em constante luta entre si.\n\n    - Kayros a dimensão dos Draconianos, seres com grande poder mágico.\n\n    - Daxy a dimensão dos Espectros, são seres fantasmagoricos, inteligentes e com habilidades mágicas.\n\n    - Paksu a dimensão dos Humanos, seres com muita bravura e inteligência.\n\n    - Arkronos a dimensão dos Demônios, seres com poderes sombrios e muita força.\n\nArkron conseguiu com essa fragmentação elevar seus poderes, e com isso acabou abrindo fissuras em Paksu, o mundo dos humanos, fazendo que todos os seres ficassem juntos em um único mundo, o que culminou em diversos conflitos.\n\n"
delay(exp2)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
sleep(6)
delay("ATUALMENTE...")
sleep(5)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
his1 = f'	Eu me chamo {hero["Nome"]} e sou um {hero["Raça"]}, e luto pelo lado da paz entre os povos liderado pela princesa Marjorie. Do nosso lado em Heaven Hill, lutam os Elfos, uma parcela dos Orcs, Espectros e Draconianos, e nós lutamos contra os aliados de Arkron, que é composto por Orcs, Espectros e Draconianos que não concordam com a união dos povos, e demônios que são fiéis ao Deus dos Mortos, que esperam o caos e nada mais.\nPor mais que Heaven Hill tenha um menor número de aliados, contamos com a inteligência dos Elfos para elaborar estratégias imbativeis.\n\n'
delay(his1)
sleep(2)
his2 = "Princesa Marjorie estava explicando a estrátegia para seus aliados:\n\n - \"Os focos da luta estão no Sul de Heaven Hill, e para chegar lá teremos que passar por grandes batalhas, sendo a primeira delas contra os Orcs tomados pela aura de Arkron, que são bem mais fortes que os Orcs comuns, e vocês conseguem diferenciá-los por uma sombra azulada que envolve o corpo deles.\"\n\n - \"Fiquem juntos sempre, pois a tática dos Orcs como o General Graves disse, é sempre separar os inimigos para conquistar.\"\n\n - \"E que Pak, Jit, Dax, Waq e Kay abençoe vocês!.\"\n\n"
delay(his2)
sleep(2)
his3 = "Depois disso fomos nos encontrar com nossos superiores, que são:  General Graves o orc comandante das linhas de frente, Luda a Elfo que coordena as estratégias, Rako o Draconiano que comanda ataques mágicos, Elos o Espectro comandante de ataques sorrateiros.\n\n	Graves: \"Olá rapazes, prontos para ingressar no inferno? Hahaha\"\n\n	Luda: \"Lá é diferente de tudo que vocês já viram, as vezes até a melhor das estratégias se tornam inúteis, e é por isso que como a Princesa disse, nunca se separem!\"\n\n	Luda: \"Rako... Diga um pouco sobre como lidar com a magia dos aliados de Arkron\"\n\n	Rako: \"Primeiramente quero que vocês nunca subestimem esse tipo de magia, ela é basicamente a magia de um deus, a única forma de se proteger dela é evitando os ataques e usando um amuleto de Kay, que torna os ataques mágicos mais fracos.\"\n\nElos se materializa entre os superiores\n\n	Elos: \"Como vocês sabem, lá tem todo tipo de ataque, e um que vocês devem ter a atencão redobrada, são os ataques sorrateiros, principalmente dos espectros, pois nós temos a capacidade de ficar invisiveis para olhos de não espectros, ou seja, novamente reforçando o que a Luda e a Princesa disseram, fiquem juntos e de preferencia sempre tenham um espectro no grupo...\"\n\n	Graves: \"Agora chega de papo furado e vamos ao que interessa!\"\n\n	Graves: \"Pegue o maximo que puder de poções com o Rako, pegue o amuleto, suas armas e armaduras e reze para seus deuses!\"\n\n"
delay(his3)
sleep(2)
his4 = "Saindo do castelo, andamos pelas redondezas para caçar e estocar o máximo de comida e água possivel.Quando começou a ficar tarde, paramos para acampar e esperar o sol nascer.\n\nTodos ficaram reunidos em volta da fogueira afiando suas espadas e machados, e General Graves começou a falar:\n\n	Graves: \"Lá em Jitkos o acampamento era sempre a pior parte quando estávamos em guerra, dormir era como dar seu pescoço pro inimigo, os Orcs não são muito respeitosos com o sono do inimigo. Se fosse dormir, era melhor estar com o machado e o escudo nas mãos, e rezar pra Jit para que ninguem te ache.\"\n\n	Elos: \"Orcs são previsiveis se comparados aos Espectros, bom... Pra vocês que não são Espectros é claro.\"\n\n	Luda: \"Muito obrigado Elos, dormirei tranquilamente após saber disso.\"\n\n	Graves: \"Esquenta não Luda, com o Elos, o Rako e eu aqui, não tem porque ter medo.\"\n\n	Rako: \"Isso é verdade, já preparei um escudo mágico para o nosso acampamento. E como os Espectros não dormem, nossa segurança é quase que total.\"\n\n" 
delay(his4)
sleep(2)
his5 = "Eu estava sem sono, e saí para andar um pouco. Após andar um pouco, eu sentei em uma rocha e fiquei olhando o céu, ele estava muito estrelado naquela noite, e do nada uma voz falou comigo:\n\n	Suo: \"Ora, você procura algo nas estrelas?\"\n\nMe assustei e fiquei procurando de onde vinha essa voz, e aos poucos foi surgindo um rosto no ar\n\n	Suo: \"Eu me chamo Suo, sou um Gorji, é um prazer te conhecer. Você pretende ir para o cerco dos Dark Orcs? Se eu fosse você, certamente eu não iria. Mas, após as noites frias de um deserto, sempre há um sol brilhante...\"\n\nFiquei tentando entender o que aquilo significava, e quando fui perguntar a explicação daquela frase, a criatura simplesmente sumiu. Eu achava que os Gorjis eram apenas lendas...Voltei para o acampamento e finalmente consegui dormir.\n\n"
delay(his5)
sleep(2)
his6 = "Assim que amanheceu já retomamos nossa jornada, no caminho um elfo e um draconiano vieram conversar comigo:\n\n	Viko: \"Err, olá, eu me chamo Viko, Err, você está com medo dos Orcs?\" falou com a voz tremula\n\nRespondi que estava um pouco assustado\n\n	Zibo: \"Olá, eu sou o Zibo, porque você ta tremendo Viko?\"\n\n	Viko: \"É que já ta tão perto...\"\n\n	Zibo: \"Acho que você é o único Elfo medroso de toda Waquios\"\n\n	Viko: \"Diz ai o único Draconiano que não sabe usar magia\"\n\nZibo ficou com uma expressão séria, e deu um soco no braço de Viko\n\n	Zibo: \"Não precisava ter contado isso...\"\n\n	Viko: \"Desculpa cara, foi meu mecânismo de defesa hahaha\"\n\nDei risada e continuei andando com eles."
delay(his6)
sleep(2)
his7 = "Três horas depois chegamos no Cerco dos Dark Orcs, era um lugar terrível, por toda parte tinha sangue e corpos, já tinha acontecido várias batalhas, e pelo jeito os Dark Orcs tinham saído vitoriosos, eram poucos corpos deles no chão.\n\nViko ficou extremamente ansioso e desmaiou, caindo no chão como um saco de batatas\n\n	Graves: \"Hey! Acorda magricela, aqui não é lugar para fracotes!\"\n\n	Luda: \"Pega leve com ele Graves, é a primeira batalha dele, e são poucos os elfos que lutam na linha de frente!\"\n\n	Graves: \"Desculpa ai deusa protetora dos elfos... Mas alguem acorda logo esse molenga!\"\n\n	Zibo: \"Ei, acorda cara!\"\n\n	Rako: \"Deixa que eu resolvo isso...\"\n\nRako conjurou um feitiço que fez Viko levantar na hora\n\n	Viko: \"Desculpa gente, não foi por querer...\"\n\n	Elos: \"Tanto faz, vamos entrar agora, preparem-se\"\n\nFomos caminhando devagar, com Elos na frente vendo se há inimigos na frente\n\n	Graves: \"Isso tá quieto demais pro meu gosto...\"\n\nAssim que Graves disse isso, uma tropa surgiu do chão falso, cercando todo mundo\n\nRako lançou um feitiço para quebrar a força superior causada pelo poder de Arkron nos Orcs\n\n	Rako: \"Agora é só lutar!\"\n\n"
delay(his7)
sleep(4)
batalha(hero, Armamento, vida, Poções,"Dark Orc", 18, 100, "Clava de Guerra")
sleep(4)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
his8 = "Após derrotar os Dark Orcs, Tinham mais tropas no horizonte, mas resolveram recuar\n\n	Graves: \"Tão com medinho seus traidores? hahaha\"\n\n	Rako: \"Acho que não é medo graves... É algo bem pior\"\n\n	Luda: \"Com certeza, a única coisa que faz os Orcs recuarem é o chamado de seu superior\"\n\n	Elos: \"Exatamente isso, estou vendo o superior deles, ele se chama Voko, e não vai ser fácil derrotar ele\"\n\n	Graves: \"É o único Orc com Quatro braços, maldito Voko! Ele era o mais temido em Jitkos\"\n\n	Zibo: \"Não é pra menos, o cara é enorme e tem quatro braços!\"\n\n	Graves: \"Pois é jovem lagarto... O poder sombrio tem suas vantagens\"\n\n	Rako: \"Só tem um jeito de derrotar ele, e é combinado os atributos de todas raças, a força dos Orcs, a bravura dos Humanos, a inteligência Elfica, a magia Draconiana e a destreza dos Espectros\"\n\n	Luda: \"Teremos que distrai-lo com algo, prende-lo em uma runa mágica e atacar usando toda nossa força\"\n\n	Graves: \"É isso ai!\"\n\nVoko gritava no topo da montanha\n\n	Voko: \"Vocês acham que podem me vencer? Hahahaha seus tolos. Nem com Jit do lado de vocês seria possível!\"\n\n	Graves: \"É o que vamos ver seu imbecil!\"\n\nRako nos teleportou para a montanha, e de inicio não vimos Voko\nComeçou a subir uma poeira muito densa, e lá no fim dela vem vindo uma silhueta enorme gritando\n\n	Graves: \"Droga...\"\n\nVoko arremessou graves pro outro lado da montanha\nRako fincou o cajado no chão, e uma área circular da montanha ficou azul turquesa\n\n	Roko: \"Mantenha ele dentro do circulo Azul, vai deixar ele mais fraco!\"\n\nElos criou clones dele mesmo que cercaram Voko\nLuda arremessou flechas elficas que drenam energia nas costas de Voko\n\n	Luda: \"Está dando certo!\"\n\n	Viko: \"É isso aí!\"\n\nViko e Zibo atacaram Voko, deixando um de seus braços direitos inutilizavel\n\nAgora é a hora que entro em ação!\n\n"
delay(his8)
sleep(4)
batalha(hero, Armamento, vida, Poções, "Voko", 27, 150, "Machado de Arkron")
sleep(4)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
