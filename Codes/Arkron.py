from scripts import *	
from time import sleep	

						#Personagem
Poções = {"Vida":20, "Magia":20, "Stamina":20}

class hero:
    Vida = 100
    Mana= 100
    Stamina = 100

    def __init__(self):
        self.Nome = ""
        self.Raça = ""
        self.Classe = ""
        self.magia = 0
        self.força = 0
        self.inteligência = 0
        self.audacia = 0
        self.bravura = 5
        self.Arkron = False
        self.Arma = ""
        self.Dano = 0

        #Armamentos
    def atualizar_armamento(self):
        if self.Classe == "Arqueiro":
            self.Arma = "Arco Leve"
            self.Dano = 10

        elif self.Classe == "Guerreiro":
            self.Arma = "Machado Leve"
            self.Dano = 10

        elif self.Classe == "Mago":
            self.Arma = "Cajado de Chamas"
            self.Dano = 10

        elif self.Classe == "Assassino":
            self.Arma = "Punhal Serrado"
            self.Dano = 10

    def atualizar_atributos(self):
        if self.Classe == "Arqueiro":
            self.inteligência += 20

        elif self.Classe == "Guerreiro":
            self.força += 20

        elif self.Classe == "Mago":
            self.magia += 20

        elif self.Classe == "Assassino":
            self.audacia += 20

        if self.Raça == "Elfo":
            self.inteligência += 20

        elif self.Raça == "Orc":
            self.força += 20

        elif self.Raça == "Humano":
            self.audacia += 20

        elif self.Raça == "Draconiano":
            self.magia += 20

        elif self.Raça == "Espectro":
            self.magia += 10
            self.inteligência += 10


iniciar()
logo()
abertura()
hero = hero()

print("\033[33mSeja bem vindo à Heaven Hill jovem aliado")
sleep(1)
hero.Nome = str(input("Qual é o seu Nome? "))
print("\n\n\n")

print("✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠ Raças ✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠")
print("\n   ❖ Elfo\n   ❖ Orc\n   ❖ Humano\n   ❖ Draconiano\n   ❖ Espectro\n")
hero.Raça = str(input("Qual é sua Raça? ")).capitalize()
print("\n\n\n")

print("✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠ Classe ✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠")
print("\n   ❖ Arqueiro\n   ❖ Guerreiro\n   ❖ Mago\n   ❖ Assassino\n")
hero.Classe = str(input("Qual é sua Classe? ")).capitalize()
print("\n\n\n")


print("✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠ Atributos ✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠")
print("\nSão 100 pontos para dividir em \033[31m4\033[33m atributos\n")
while True:
    pontos = 100
    hero.força = int(input("\nPontos de \033[32mFORÇA\033[33m: "))
    pontos -= hero.força
    if pontos == 0:
        print("Você esgotou seus pontos...")
    else:
        hero.magia = int(input("\nPontos de \033[34mMAGIA\033[33m: "))
        pontos -= hero.magia
        if pontos == 0:
            print("Você esgotou seus pontos...")
        else:
            hero.inteligência = int(input("\nPontos de \033[36mINTELIGÊNCIA\033[33m: "))
            pontos -=hero.inteligência
            if pontos == 0:
                print("Você esgotou seus pontos...")
            else:
                hero.audacia = int(input("\nPontos de \033[31mAUDACIA\033[33m: "))
                pontos -= hero.audacia
    print(f'\nForça: {hero.força}')
    print(f'Inteligência: {hero.inteligência}')
    print(f'Magia: {hero.magia}')
    print(f'Audacia: {hero.audacia}')
    print(f"Restam {pontos} pontos")
    ask = str(input("\nDeseja alterar os atributos? ")).upper()
    if ask in "SIM":
        continue
    elif ask in "NÃO" or ask == "N" or ask == "NAO":
        break
print("\n\n\n")

hero.atualizar_armamento()
hero.atualizar_atributos()

print('\n✠✠✠✠✠✠✠✠✠✠✠✠ Dados do aliado ✠✠✠✠✠✠✠✠✠✠✠✠\n')
print(f"\nNome: {hero.Nome}")
sleep(0.5)
print(f"Raça: {hero.Raça}")
sleep(0.5)
print(f"Classe: {hero.Classe}")
sleep(0.5)
print(f"Arma: {hero.Arma}")
sleep(0.5)
print(f"Atributos: ")
sleep(0.5)
print(f"    -Força: {hero.força}")
sleep(0.2)
print(f"    -Inteligência: {hero.inteligência}")
sleep(0.2)
print(f"    -Audacia: {hero.audacia}")
sleep(0.2)
print(f"    -Bravura: {hero.bravura}")
sleep(0.2)
print(f"    -Magia: {hero.magia}")
sleep(0.2)

print('\n\n✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠✠')
sleep(5)



#história
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
exp1 = "    A Terra sempre foi um lugar de poucas guerras, mas desde a descoberta das fissuras entre os mundos, tudo se resume em caos. Criaturas, Deuses e Demônios, todos contra os humanos, mas em meio a essa guerra de mundos, houve a união de diferentes, os elfos, orcs, draconianos e os espectros, que lutam por um bem maior, a paz entre as diferentes realidades, mas claro que existem os que preferem o caos e a guerra.\n\n"
delay(exp1)
sleep(2)
exp2 = "Para entendermos cada uma dessas realidades, precisamos ir para o ínicio de tudo, e tudo começa com as divindades:\n\n    - Waq o deus da sabedoria\n\n    - Jit o deus da força\n\n    - Kay o deus da magia\n\n    - Dax o deus das sombras\n\n    - Pak o deus da bravura\n\n    - Arkron o deus dos mortos.\n\nAmbos os deuses viviam juntos em harmonia, até que Arkron começou a causar discórdia entre seus irmãos para causar um desequilibrio dos poderes, o que culminou em uma briga, e a separação de ambos, e cada um criou sua dimensão, sendo:\n\n    - Waquios a dimensão dos Elfos, seres extremamente inteligentes, pacificos e desenvolvidos.\n\n    - Jitkos a dimensão dos Orcs, seres com muita força e que vivem em constante luta entre si.\n\n    - Kayros a dimensão dos Draconianos, seres com grande poder mágico.\n\n    - Daxy a dimensão dos Espectros, são seres fantasmagoricos, inteligentes e com habilidades mágicas.\n\n    - Paksu a dimensão dos Humanos, seres com muita bravura e inteligência.\n\n    - Arkronos a dimensão dos Demônios, seres com poderes sombrios e muita força.\n\nArkron conseguiu com essa fragmentação elevar seus poderes, e com isso acabou abrindo fissuras em Paksu, o mundo dos humanos, fazendo que todos os seres ficassem juntos em um único mundo, o que culminou em diversos conflitos.\n\n"
delay(exp2)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
sleep(6)
delay("ATUALMENTE...")
sleep(5)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
his1 = f'   Eu me chamo {hero.Nome} e sou um {hero.Raça}, e luto pelo lado da paz entre os povos liderado pela princesa Marjorie. Do nosso lado em Heaven Hill, lutam os Elfos, uma parcela dos Orcs, Espectros e Draconianos, e nós lutamos contra os aliados de Arkron, que é composto por Orcs, Espectros e Draconianos que não concordam com a união dos povos, e demônios que são fiéis ao Deus dos Mortos, que esperam o caos e nada mais.\nPor mais que Heaven Hill tenha um menor número de aliados, contamos com a inteligência dos Elfos para elaborar estratégias imbativeis.\n\n'
delay(his1)
sleep(2)
his2 = "Princesa Marjorie estava explicando a estrátegia para seus aliados:\n\n - \"Os focos da luta estão no Sul de Heaven Hill, e para chegar lá teremos que passar por grandes batalhas, sendo a primeira delas contra os Orcs tomados pela aura de Arkron, que são bem mais fortes que os Orcs comuns, e vocês conseguem diferenciá-los por uma sombra azulada que envolve o corpo deles.\"\n\n - \"Fiquem juntos sempre, pois a tática dos Orcs como o General Graves disse, é sempre separar os inimigos para conquistar.\"\n\n - \"E que Pak, Jit, Dax, Waq e Kay abençoe vocês!.\"\n\n"
delay(his2)
sleep(2)
his3 = "Depois disso fomos nos encontrar com nossos superiores, que são:  General Graves o orc comandante das linhas de frente, Luda a Elfo que coordena as estratégias, Rako o Draconiano que comanda ataques mágicos, Elos o Espectro comandante de ataques sorrateiros.\n\n    Graves: \"Olá rapazes, prontos para ingressar no inferno? Hahaha\"\n\n    Luda: \"Lá é diferente de tudo que vocês já viram, as vezes até a melhor das estratégias se tornam inúteis, e é por isso que como a Princesa disse, nunca se separem!\"\n\n    Luda: \"Rako... Diga um pouco sobre como lidar com a magia dos aliados de Arkron\"\n\n    Rako: \"Primeiramente quero que vocês nunca subestimem esse tipo de magia, ela é basicamente a magia de um deus, a única forma de se proteger dela é evitando os ataques e usando um amuleto de Kay, que torna os ataques mágicos mais fracos.\"\n\nElos se materializa entre os superiores\n\n    Elos: \"Como vocês sabem, lá tem todo tipo de ataque, e um que vocês devem ter a atencão redobrada, são os ataques sorrateiros, principalmente dos espectros, pois nós temos a capacidade de ficar invisiveis para olhos de não espectros, ou seja, novamente reforçando o que a Luda e a Princesa disseram, fiquem juntos e de preferencia sempre tenham um espectro no grupo...\"\n\n    Graves: \"Agora chega de papo furado e vamos ao que interessa!\"\n\n    Graves: \"Pegue o maximo que puder de poções com o Rako, pegue o amuleto, suas armas e armaduras e reze para seus deuses!\"\n\n"
delay(his3)
sleep(2)
his4 = "Saindo do castelo, andamos pelas redondezas para caçar e estocar o máximo de comida e água possivel.Quando começou a ficar tarde, paramos para acampar e esperar o sol nascer.\n\nTodos ficaram reunidos em volta da fogueira afiando suas espadas e machados, e General Graves começou a falar:\n\n    Graves: \"Lá em Jitkos o acampamento era sempre a pior parte quando estávamos em guerra, dormir era como dar seu pescoço pro inimigo, os Orcs não são muito respeitosos com o sono do inimigo. Se fosse dormir, era melhor estar com o machado e o escudo nas mãos, e rezar pra Jit para que ninguem te ache.\"\n\n    Elos: \"Orcs são previsiveis se comparados aos Espectros, bom... Pra vocês que não são Espectros é claro.\"\n\n    Luda: \"Muito obrigado Elos, dormirei tranquilamente após saber disso.\"\n\n    Graves: \"Esquenta não Luda, com o Elos, o Rako e eu aqui, não tem porque ter medo.\"\n\n    Rako: \"Isso é verdade, já preparei um escudo mágico para o nosso acampamento. E como os Espectros não dormem, nossa segurança é quase que total.\"\n\n" 
delay(his4)
sleep(2)
his5 = "Eu estava sem sono, e saí para andar um pouco. Após andar um pouco, eu sentei em uma rocha e fiquei olhando o céu, ele estava muito estrelado naquela noite, e do nada uma voz falou comigo:\n\n    Suo: \"Ora, você procura algo nas estrelas?\"\n\nMe assustei e fiquei procurando de onde vinha essa voz, e aos poucos foi surgindo um rosto no ar\n\n    Suo: \"Eu me chamo Suo, sou um Gorji, é um prazer te conhecer. Você pretende ir para o cerco dos Dark Orcs? Se eu fosse você, certamente eu não iria. Mas, após as noites frias de um deserto, sempre há um sol brilhante...\"\n\nFiquei tentando entender o que aquilo significava, e quando fui perguntar a explicação daquela frase, a criatura simplesmente sumiu. Eu achava que os Gorjis eram apenas lendas...\nVoltei para o acampamento e finalmente consegui dormir.\n\n"
delay(his5)
sleep(2)
his6 = "Assim que amanheceu já retomamos nossa jornada, no caminho um elfo e um draconiano vieram conversar comigo:\n\n    Viko: \"Err, olá, eu me chamo Viko, Err, você está com medo dos Orcs?\" falou com a voz tremula\n\nRespondi que estava um pouco assustado\n\n    Zibo: \"Olá, eu sou o Zibo, porque você ta tremendo Viko?\"\n\n    Viko: \"É que já ta tão perto...\"\n\n    Zibo: \"Acho que você é o único Elfo medroso de toda Waquios\"\n\n    Viko: \"Diz ai o único Draconiano que não sabe usar magia\"\n\nZibo ficou com uma expressão séria, e deu um soco no braço de Viko\n\n    Zibo: \"Não precisava ter contado isso...\"\n\n    Viko: \"Desculpa cara, foi meu mecânismo de defesa hahaha\"\n\nDei risada e continuei andando com eles.\n\n"
delay(his6)
sleep(2)
his7 = "Três horas depois chegamos no Cerco dos Dark Orcs, era um lugar terrível, por toda parte tinha sangue e corpos, já tinha acontecido várias batalhas, e pelo jeito os Dark Orcs tinham saído vitoriosos, eram poucos corpos deles no chão.\n\nViko ficou extremamente ansioso e desmaiou, caindo no chão como um saco de batatas\n\n    Graves: \"Hey! Acorda magricela, aqui não é lugar para fracotes!\"\n\n    Luda: \"Pega leve com ele Graves, é a primeira batalha dele, e são poucos os elfos que lutam na linha de frente!\"\n\n    Graves: \"Desculpa ai deusa protetora dos elfos... Mas alguem acorda logo esse molenga!\"\n\n    Zibo: \"Ei, acorda cara!\"\n\n    Rako: \"Deixa que eu resolvo isso...\"\n\nRako conjurou um feitiço que fez Viko levantar na hora\n\n    Viko: \"Desculpa gente, não foi por querer...\"\n\n    Elos: \"Tanto faz, vamos entrar agora, preparem-se\"\n\nFomos caminhando devagar, com Elos na frente vendo se há inimigos na frente\n\n    Graves: \"Isso tá quieto demais pro meu gosto...\"\n\nAssim que Graves disse isso, uma tropa surgiu do chão falso, cercando todo mundo\n\nRako lançou um feitiço para quebrar a força superior causada pelo poder de Arkron nos Orcs\n\n    Rako: \"Agora é só lutar!\"\n\n"
delay(his7)
sleep(4)
batalha(hero, Poções,"Dark Orc", 18, 100, "Clava de Guerra")
sleep(4)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

his8 = "Após derrotar os Dark Orcs, Tinham mais tropas no horizonte, mas resolveram recuar\n\n    Graves: \"Tão com medinho seus traidores? hahaha\"\n\n    Rako: \"Acho que não é medo graves... É algo bem pior\"\n\n    Luda: \"Com certeza, a única coisa que faz os Orcs recuarem é o chamado de seu superior\"\n\n    Elos: \"Exatamente isso, estou vendo o superior deles, ele se chama Voko, e não vai ser fácil derrotar ele\"\n\n    Graves: \"É o único Orc com Quatro braços, maldito Voko! Ele era o mais temido em Jitkos\"\n\n    Zibo: \"Não é pra menos, o cara é enorme e tem quatro braços!\"\n\n    Graves: \"Pois é jovem lagarto... O poder sombrio tem suas vantagens\"\n\n    Rako: \"Só tem um jeito de derrotar ele, e é combinado os atributos de todas raças, a força dos Orcs, a bravura dos Humanos, a inteligência Elfica, a magia Draconiana e a destreza dos Espectros\"\n\n    Luda: \"Teremos que distrai-lo com algo, prende-lo em uma runa mágica e atacar usando toda nossa força\"\n\n    Graves: \"É isso ai!\"\n\nVoko gritava no topo da montanha\n\n    Voko: \"Vocês acham que podem me vencer? Hahahaha seus tolos. Nem com Jit do lado de vocês seria possível!\"\n\n    Graves: \"É o que vamos ver seu imbecil!\"\n\nRako nos teleportou para a montanha, e de inicio não vimos Voko\nComeçou a subir uma poeira muito densa, e lá no fim dela vem vindo uma silhueta enorme gritando\n\n    Graves: \"Droga...\"\n\nVoko arremessou graves pro outro lado da montanha\nRako fincou o cajado no chão, e uma área circular da montanha ficou azul turquesa\n\n    Roko: \"Mantenha ele dentro do circulo Azul, vai deixar ele mais fraco!\"\n\nElos criou clones dele mesmo que cercaram Voko\nLuda arremessou flechas elficas que drenam energia nas costas de Voko\n\n    Luda: \"Está dando certo!\"\n\n    Viko: \"É isso aí!\"\n\nViko e Zibo atacaram Voko, deixando um de seus braços direitos inutilizavel\n\nAgora é a hora que entro em ação!\n\n"
delay(his8)
sleep(4)
batalha(hero, Poções, "Voko", 27, 150, "Machado de Arkron")
sleep(4)
if hero.Classe == "Orc":
    hero.Arma = "Machado de Arkron"
    hero.Dano = 50
    hero.Arkron = True
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

his9 = "Após derrotar Voko, todos se sentaram no chão para descansar e recuperar o folego\n\n    Luda: \"huf... Passou...\" \n\nGraves voltou mancando\n\n    Graves: \"Ainda bem que esse maldito se foi...\"\n\n    Graves: \"Culpa dele minha perna tá estragada, dá uma ajuda aqui Rako!\"\n\nRako procurou em sua bolsa de poções e deu uma Poção de fraturas para Graves\n\n    Rako: \"Em 30 minutos você estará ótimo...\"\n\n    Rako: \"Preciso fazer mais poções, não podemos prosseguir com poucas.\"\n\n    Rako: \"Vou me teletransportar para a fortaleza de Heaven Hill para pegar mais poções, até logo\"\n\nRako estendeu os braços e largou o cajado, que girou no ar e fez um clarão roxo.\n\n    Graves: \"Essas magias do Rako são fascinantes!\"\n\n    Luda: \"Os Draconianos são incriveis quando o assunto é magia, Kay deu muito de seu poder para suas criações\"\n\n    Zibo: \"Acho que Kay se esqueceu de mim...\"\n\n    Graves: \"Relaxa largatão, sua habilidade como guerreiro é muito melhor que qualquer magia\"\n\nZibo olhou surpreso pro graves\n\n    Zibo: \"Eee... Você acha mesmo?\" Disse animado\n\n    Graves: \"A luta contra Voko mostrou isso garoto\"\n\n    Elos: \"Você foi corajoso, e lutou bravamente contra ele\"\n\n    Luda: \"Pak e Jit com toda certeza abençoaram você\"\n\n    Graves: \"Hey magricela, preciso dizer que você lutou bem\"\n\n    Viko: \"Que nada, Zibo que fez tudo\"\n\n    Graves: \"Quando foi que eu elogiei um elfo?! Então acredite seu saco de batatas!\"\n\n    Graves: \"Eu não reconheci você na luta, você estava totalmente diferente\"\n\n    Elos: \"Vai ver Pak e Jit estão torcendo por você também jovem elfo\"\n\n    Viko: \"o... Obrigado gente...\" Disse com uma felicidade indescritível\n\n    Luda: \"Que eles continuem torcendo por nós... Esse foi só o ínicio da jornada\"\n\nUm portal roxo surgiu próximo deles e todos ficaram assustados, de dentro dele surge Rako\n\n    Rako: \"Olá rapazes...\"\n\nRako voltou vestido com uma longa túnica roxa cheia de runas Kayronianas\n\n    Rako: \"Tempos extremos exigem medidas extremas, não é mesmo?\"\n\n    Rako: \"Aproveitei e dei uma passada em Kayros...\"\n\n    Rako: \"Essa túnica é nada menos que uma relíquia de Kay, não preciso nem dizer que ela é extremamente poderosa\"\n\nTodos ficaram surpresos\n\n    Graves: \"Hahahahaha é por isso que eu amo esse lagarto\"\n\nRoko Riu\n\n    Graves: \"Agora estamos protegidos contra a magia de Arkron!\"\n\n    Roko: \"Bom... Ela é poderosa mas não em todos os casos\"\n\n    Elos: \"Ela é poderosa apenas contra seres não divinos\"\n\n    Rako: \"Exatamente... Contra demônios e divindades ela não é funcional...\"\n\n    Luda: \"É feita assim para que ninguém ussasse ela contra o próprio criador\"\n\n    Graves: \"Faz muito sentido pensando assim...\"\n\n    Graves: \"Mas já ajuda muito, dar um cacete naqueles aliados de Arkron!\"\n\n    Elos: \"Vocês desejam continuar agora?\"\n\n    Luda: \"Melhor esperarmos mais um pouco\"\n\n"
delay(his9)
sleep(4)
his10 = f'Ficamos descansando um pouco, pois a batalha foi muito exaustiva\n\nEu, Viko e Zibo ficamos sentados na beira do lago conversando\n\n    Viko: \"Eu nunca pensei que Graves me elogiaria\"\n\n    Zibo: \"Digo o mesmo, eu sempre achei ele um pé no saco\"\n\n    Viko: \"Eu sei lá, foi algo diferente naquela batalha...\"\n\n    Viko: \"Eu nunca me senti tão seguro e confortável\"\n\n    Zibo: \"Você lutou bem Viko, parabéns\"\n\n    Zibo: \"Hey, esqueci de perguntar uma coisa...\"\n\n    Viko: \"Pode falar\"\n\n    Zibo: \"Você usou alguma magia durante a batalha?\"\n\n    Viko: \"Não... Eu nem sei usar magia, porque?\"\n\n    Zibo: \"Você ficou com os olhos azuis\"\n\n    Viko: \"Como assim?!\" Disse assombrado\n\n    Zibo: \"Seus olhos ficaram completamente azuis\"\n\n    Viko: \"Você viu isso {hero.Nome} ?\"\n\nRepondi que pensei que ele estava usando algum tipo de magia\n\n    Viko: \"Juro pra vocês que não usei nenhuma magia\"\n\n    zibo: \"Que estranho cara, fale com o Rako depois para saber o que foi isso\"\n\nDo nada uma voz ressoou entre eles:\n\n    Ako: \"É melhor você estudar sobre isso meu querido elfo\"\n\nFicamos procurando, e novamente era o Gorji, só que em forma de água\nFormou um rosto amigável na água\n\n    Ako: \"Talvez você seja abençoado por Kay, meu amigo\"\n\n    Ako: \"E caso isso for verdade, você tem grande poder mágico escondido\"\n\n    Viko: \"Mas eu sou um Elfo... Elfos não conseguem dominar magia\"\n\n    Ako: \"Bom, seu melhor amigo é um Draconiano guerreiro\"\n\n    Zibo: \"Faz muito sentido Viko\"\n\n    Ako: \"Só busque informações sobre isso meu querido\"\n\n    Ako: \"Rako pode ser de grande ajuda nessa sua jornada\"\n\n    Ako: \"E você Zibo, continue treinando, você será lembrado por gerações\"\n\n    Zibo: \"Como assim?!\"\n\n    Ako: \"Apenas continue sendo você meu querido\"\n\n    Ako: \"Ah, quase me esqueci...\"\n\n    Ako: \"Você {hero.Nome}... Você será um grande herói\"\n\n    Ako: \"Hihihi, hora de partir... Até logo...\"\n\nE a criatura sumiu, deixando para trás diversas questões em aberto.\n\n    Zibo: \"Bom... Se ele disse ta falado\"\n\n    Viko: \"Preciso muito falar com o Rako...\"\n\nE Viko saiu correndo para falar com Rako.\nEle chegou lá ofegante e Rako ficou surpreso toda pressa de Viko\n\n    Rako: \"Hum? Por quê toda essa pressa?\"\n\n    Viko: \"Eu... Talvez eu seja um mago...\"\n\n    Rako: \"E o que te faz pensar isso?\"\n\n    Zibo: \"Os olhos dele ficaram completamente azuis na batalha\"\n\n    Zibo: \"Além dele ter ficado muito forte e sem medo\"\n\n    Rako: \"Hum...\"\n\n    Rako: \"Preciso conversar com Elos...\"\n\nRako se levantou assustado e foi se encontrar com Elos\n\n    Rako: \"Elos... Acho que Viko é um Kawaq\"\n\n    Elos: \"Mas como?\" Disse surpreso\n\n    Rako: \"Não faço a mínima idéia\"\n\n    Elos: \"Talvez ele tenha um gene perdido de Kayros\"\n\n    Rako: \"Mas como?!\"\n\n    Elos: \"Talvez algum de seus antepassados tenha cruzado as dimensões...\"\n\n    Rako: \"Mas isso é era impossível antes de Arkron tomar o poder!\"\n\n    Elos: \"Essa é a maior incognita aqui\"\n\n    Elos: \"Mas já existiram Kawaqs antes, que o poder aparecia de forma espoôntanea\"\n\n    Rako: \"Só que era algo conquistado com uma vida inteira de estudo...\"\n\n    Elos: \"Bom, independente de motivo... Você deve treinar o garoto\"\n\n    Rako: \"Exato... Com um Kawaq conosco tudo ficará mais acessivel\"\n\nRako voltou para Viko\n\n    Rako: \"Você é um Kawaq\"\n\n    Viko: \"E o que isso significa?\"\n\n    Rako: \"Você é um ser raro, basicamente...\"\n\n    Rako: \"Um Elfo que possui grande poder mágico\"\n\n    Rako: \"É como se você fosse um Elfo filho de Kay...\"\n\n    Viko: \"Mas como? Eu sou filho de elfos comuns!\"\n\n    Rako: \"É uma pergunta sem repostas por enquanto\"\n\n    Rako: \"Mas enfim garoto, vou treinar você\"\n\n    Rako: \"Com um Kawaq e um Mestre de Kayros, certamente venceremos essa guerra...\"\n\nRako disse para todos para fazerem um dia inteiro de acampamento, pois ia treinar Viko.\n\n'
delay(his10)
sleep(4)
his11 = f'Após o término desse acampamento, continuamos nossa jornada\n\nRako se teletransportou para Heaven Hill para saber como seria o próximo passo\n\n    Princesa: \"Parábens, vocês conseguiram ganhar a primeira batalha\"\n\n    Princesa: \"Os Elfos corrompídos estão juntos com Luno\"\n\n    Princesa: \"Eles estão escondidos nas Colinas do Triunfo, lá é de fácil acesso\"\n\n    Princesa: \"A única dica que preciso dar, é ter cuidado com as flechas dos Elfos\"\n\n    Princesa: \"E se possível, não mate Luno...\"\n\nRako retornou para perto de todos\n\n    Rako: \"Vamos...\"\n\nTrês dias se passaram, e chegamos na colina do triunfo, lá era muito diferente do Cerco dos Dark Orcs, era tudo muito verde e lindo\n\n    Graves: \"Chegamos? Mas cade toda a carnificina?\"\n\n    Rako: \"Vamos lutar contra um Elfo, Elfos são discretos\"\n\n    Luda: \"Só prestem atenção nas árvores\"\n\nLuda estava com uma expressão de tristeza\n\nGraves parou e ficou procurando algo\n\n    Graves: \"Vocês estão ouvindo esse barulho?\"\n\nRako ficou procurando, e rapidamente empunhou o cajado\n\n    Rako: \"Protejam-se!\"\n\n    Graves: \"São os malditos Dark Elfs!\"\n\nE flechas negras voaram sobre todos\nRako, Luda, Zibo e Elos foram feridos por elas\n\n    Rako: \"Não consigo me mexer!\"\n\n    Graves: \"Arr! Covardes!\"\n\n    Luda: \"Fiquem juntos!\"\n\n    Zibo: \"Viko! Usa o que você aprendeu!\"\n\nViko ficou furioso e seu corpo foi coberto por uma aura azul\n\n    Viko: \"Vocês vão pagar seus malditos!\"\n\nViko lançava feitiços poderosos contra os inimigos\n\n    Rako: \"Viko! Diga as palavras que te ensinei!\"\n\nViko disse palavras da língua antiga de Kayros e metade dos Dark Elfs cairam no chão petrificados\n\nA aura azul que cobria Viko se dissipou e ele caiu no chão\n\n    Zibo: \"Viko!\"\n\n    Rako: \"A magia dele se esgotou...\"\n\n    Rako: \"{hero.Nome}... Sua vez de atacar!\"\n\n'
delay(his11)
sleep(4)
batalha(hero, Poções, "Dark Elf", 25, 80, "Arco Negro")
sleep(4)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
his12 = f'Após a batalha, fomos retirar as flechas de nossos aliados\n\n    Rako: \"Muito bem {hero.nome}, você lutou bravamente\"\n\n    Luda: \"Você é um excelente aliado!\"\n\n    Elos: \"Muito bom, garoto...\"\n\n    Graves: \"Meus parabéns...\"\n\nViko acordou e nos ajudou a retirar as flechas\n\n    Luda: \"Nunca pensei que veria elfos aliados ao mal...\"\n\n    Rakos: \"Pois é...\"\n\nAssim que todos levantaram, uma flecha de fumaça é lançada no chão\n\n    Graves: \"De novo não!\"\n\nTodos ficaram sem visão com toda aquela fumaça\n\nSurge uma voz grossa no meio da fumaça\n\n    Luno: \"Acharam que acabou?\"\n\nLuno estava segurando um punhal no pescoço de Luda\n\n    Luno: \"Vocês acham mesmo que vão vencer Arkron?!\"\n\n    Luno: \"Aceitem as trevas em quanto é tempo\"\n\n    Rako: \"Luno, se afeste dela! Você está enfeitiçado por Arkron!\"\n\n    Luda: \"Não matem ele!\"\n\n    Luno: \"Seu tolo, Luno se foi!\"\n\n    Luno: \"Vocês acabaram com muitos de meus aliados, hora de vocês sentirem dor!\"\n\nLuno apunhala Luda no peito e dá começa a gargalhar\n\n    Luno: \"Hahahaha, isso é só o começo da era de Arkron!\"\n\nTodos ficam sem reação com a cena, todos tentam atacar Luno mas estão fracos demais\n\n    Graves: \"Não!\"\n\n    Rako: \"Arr! As flechas... drenaram minha energia!\"\n\n    Elos: \"Estamos... todos muito... fracos para lutar!\"\n\nViko tenta usar o poder de Kawaq mas também está esgotado\n\nA frase que Ako disse ressoava na minha cabeça:\n\n    Ako: \"Você será um grande herói\"\n\nComecei a caminhar em direção de Luno, e Rako olhou para mim\nRako fechou os olhos e começou a falar baixo em Kayroniano, e em seguida desmaiou\n\nUma aura verde cobriu meu corpo e me senti forte como nunca!\n\n'
delay(his12)
sleep(4)
batalha(hero, Poções, "Luno", 30, 100, "Arco de Arkron")
sleep(4)
if hero.Classe == "Elfo":
    hero.Arma = "Arco de Arkron"
    hero.Dano = 50
    hero.Arkron = True
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

his13 = "Luno cai no chão e imediatamente a aura negra que cobria seu corpo se dissipa, ele estava muito fraco\n\nEle se levanta e vê Luda no chão coberta de sangue\n\n    Luno: \"Não... Não!\"    Luno: \"O que foi que eu fiz!\"\n\nEle se agacha e segura a mão de Luda, que está muito fraca\n\n    Luno: \"Não, não, não!\"\n\n    Luno: \"Filha, me desculpe!\"\n\n    Luno: \"Arkron tinha se enraizado na minha mente, ele me fez fazer coisas terríveis...\"\n\n    Luda: \"P... Pai...\"\n\n    Luno: \"Fala comigo filha por favor!\"\n\n    Luda: \"É bom... Poder te ver novamente\"\n\n    Luda: \"Acho... Que Waq... me buscará... agora pai...\"\n\n    Luda: \"Ajude... Eles a... acabar com... a guerra...\"\n\n    Luda: \"Me desculpe... pai...\"\n\nLuda fecha os olhos...\n\n    Luno: \"Não!\"\n\n    Luno: \"Resista filha!\"\n\n    Luno: \"Seja forte!\"\n\nLuno começa a chorar abraçando sua filha, que não está mais entre nós\n\nTodos caiem de joelho e ficam de cabeça baixa\n\n    Graves: \"Que... Que Waq cuide de você Luda...\"\n\n    Elos: \"Arkron vai se arrepender disso...\"\n\nRako acorda confuso\n\n    Rako: \"Luda! Onde está a Luda?!\"\n\n    Graves: \"Ela... Não está mais entre nós...\"\n\n    Rako: \"Não!\"\n\nRako fica muito agitado\n\n    Rako: \"Eu falhei! Eu jurei proteger todos vocês!\"\n\n    Rako: \"Isso foi culpa minha!\"\n\n    Rako: \"Você!\" Disse olhando pra Luno\n\n    Rako: \"Você matou ela seu maldito!\"\n\n    Luno: \"Não... Não foi culpa minha!\" Disse chorando\n\n    Elos: \"Rako... Não culpe ele\"\n\n    Elos: \"Foi Arkron que fez isso com a Luda\"\n\n    Elos: \"Acredite, Luno está quebrado por dentro...\"\n\nRako sentou e colocou as mão na cabeça\n\n    Rako: \"Se eu não tivesse sido atingido por aquela flecha!\"\n\n    Rako: \"Luda estaria viva!\"\n\n    Graves: \"Para Rako!\"\n\n    Graves: \"Você não teve culpa nenhuma!\"\n\n    Rako: \"Eu vou acabar com a raça daquele maldito\"\n\n    Graves: \"Sim... Você vai... Mas primeiro descanse\"\n\n    Graves: \"Não foi um dia fácil...\"\n\n"
delay(his13)
sleep(4)
his14 = "No entardecer, todos se despediram de Luda\n\n    Luno: \"O por do sol sempre a parte do dia favorito dela...\"\n\n    Rako: \"Uhum... Ela merece a melhor paisagem em sua despedida\"\n\nGraves cavou uma cova na sombra de uma árvore, no exato lugar onde a sombra do sol se pondo fica\n\n    Graves: \"Não é justo...\" disse quase chorando\n\n    Graves: \"Ela era tão doce, não merecia isso...\"\n\n    Rako: \"Esse mundo estava ruim demais para ela Graves\"\n\n    Rako: \"Agora ela descansará na paz de Waq\"\n\nElos tirou seu capuz e se aproximou do caixão de Luda\n\n    Elos: \"Ela fará uma boa viagem, tenho certeza disso\"\n\n    Elos: \"O sol já está começando a se por, melhor começarmos logo\" \n\n    Rako: \"Deixe que eu carrego ela\"\n\nLuno se levantou e colocou o mão no ombro de Rako\n\n    Luno: \"Posso levar ela com você?\" disse com uma voz baixa e triste\n\nRako hesitou por um momento, mas olhou pra Luno e acenou com a cabeça\n\n    Rako: \"Tudo bem...\"\n\n    Luno: \"Obrigado\"\n\nEles se reuniram em um circulo em volta da cova\nLuno e Rako colocaram o caixão na cova, e se juntaram aos demais\n\n    Graves: \"Adeus... Deusa protetora dos Elfos...\"\n\n    Graves: \"E me perdoe por ter agido de forma idiota\"\n\nUma lágrima escorreu dos olhos de Graves\n\n    Rako: \"Me desculpa por ter falhado...\"\n\n    Rako: \"Nunca imaginei que te diria adeus...\"\n\n    Rako: \"Mas enfim... Adeus Luda...\"\n\nRako dêu um longo suspiro\n\n    Elos: \"Faça uma boa viagem, obrigado por tudo...\"\n\n    Elos: \"Gostaria de ter conversado mais contigo...\"\n\nElos ficou de cabeça baixa e de punhos cerrados\n\n    Luno: \"Filha... Eu espero que você me perdoe\"\n\n    Luno: \"E espero que você esteja em paz\"\n\n    Luno: \"Você sempre foi... uma pessoa íncrivel e adorável\"\n\n    Luno: \"Adeus... Minha filha...\"\n\nLuno começou a chorar novamente\n\n    Viko: \"Obrigado, por ser um exemplo de bravura pra mim\"\n\n    Viko: \"Adeus Luda...\"\n\n    Zibo: \"Você foi uma excelente pessoa\"\n\n    Zibo: \"Adeus... Luda\"\n\nDepois que todos se despediram, Graves enterrou o caixão e Rako fez uma Lápide usando magia, com os dizeres: \"Aqui jaz uma aliada da paz, Luda de Waquios\"\n\n"
delay(his14)
sleep(4)
his15 = "Logo após a cerimônia acabar, Rako disse para continuarmos a jornada\n\n    Rako: \"Não é seguro acamparmos hoje\"\n\n    Rako: \"Arkron sabe que Luno está com a gente, e sabe onde nós estamos\"\n\n    Rako: \"Quando mais cedo sairmos daqui melhor\"\n\n    Graves: \"Mas Rako, estamos exaustos!\"\n\n    Rako: \"Vou preparar um Elixir para todos\"\n\nRako conjurou um caldeirão e vários potes de ingredientes\n\n    Rako: \"Só um segundo...\"\n\n    Rako: \"Ai está, bebam de uma vez\"\n\nE o caldeirão e os ingredientes sumiram\n\n    Graves: \"Sendo assim, vamos então\"\n\n    Luno: \"Quando antes eu quero matar aquele desgraçado!\"\n\n    Graves: \"E nós vamos!\"\n\n    Rako: \"Claro que vamos...\"\n\nApós duas horas caminhando, o Gorji novamente aparece\n\n    Eji: \"Ei!\"\n\nE todos param assustados\n\n    Graves: \"O que foi isso?!\"\n\n    Eji: \"Olha pro chão gordão\"\n\n    Graves: \"Mas não tem nada no chão!\"\n\nE uma pedra voa na cabeça de Graves\n\n    Graves: \"Ah!\"\n\n    Graves: \"Onde você está?!\"\n\n    Eji: \"hahaha\"\n\n    Eji: \"Sou um Gorji, me chamo Eji\"\n\nE uma rocha no chão começa a ganhar rosto\n\n    Eji: \"Se eu fosse vocês, teria atenção redobrada\"\n\n    Rako: \"Porque?\"\n\n    Eji: \"Ah... Não posso dizer o porque\"\n\n    Eji: \"Mas... Olhem para todos os lados enquanto estiverem caminhando\"\n\n    Graves: \"Quem você acha que é para botar medo na gente?!\"\n\n    Eji: \"Bom, primeiramente eu ajudo vocês por livre e expontânea vontade\"\n\n    Eji: \"Segundo, eu sou um Gorji, eu sei de muiiiitas coisas\"\n\n    Eji: \"Então, se eu fosse um Orc idiota como você...\"\n\n    Eji: \"Eu certamente tomaria cuidado!\"\n\n    Eji: \"Bom, o recado já está dado\"\n\n    Eji: \"Cabe aos idiotas acreditarem ou não\"\n\n    Eji: \"Adeus...\"\n\nE a criatura desapareceu\n\n    Graves: \"... Tanto faz!\"\n\n    Rako: \"Um Gorji nunca fala nada atoa, tomem cuidado\"\n\nContinuamos a jornada normalmente, até que do topo de uma árvore saiem vultos brancos indo em nossa direção\n\n    Graves: \"Cuidado!\"\n\n    Elos: \"São Espectros!\"\n\n    Rako: \"Muito cuidado com eles!\"\n\n"
delay(his15)
sleep(4)
batalha(hero, Poções, "Espectro Assassino", 25, 100, "Punhal Sangrento")
sleep(4)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
his16 = f'Assim que os espectros foram derrotados, uma luz forte clareou toda a floresta\n\nSiko e Brako apareceram, são espectros gêmeos aterrorizantes\n\n    Siko: \"Olá, seus malditos!\"\n\n    Brako: \"Luno! Eu prefiro você morto do que do lado perdedor!\"\n\n    Siko: \"Uma pena que a Elfo morreu\"\n\n    Siko: \"Fiquei triste por não ter sido eu que finquei a Adaga no peito dela!\"\n\n    Brako: \"Essa noite será uma Carnificina!\"\n\nGraves estava furioso com o que Siko disse\n\n    Graves: \"Vocês vão implorar por misericóridia!\"\n\n    Elos: \"Seus idiotas, sempre do lado perdedor!\"\n\n    Brako: \"Ora ora, o grande Elos\"\n\n    Siko: \"Um perdedor que se julga o melhor de Daxy\"\n\n    Siko: \"Hahahaha, vai ser ótimo cortar seu pescoço!\"\n\n    Elos: \"Vocês vão pagar por tudo que fizeram em Daxy!\"\n\n    Elos: \"Vocês são um câncer, que espalha morte por onde passa!\"\n\n    Rako: \"Se acalme Elos...\"\n\n    Elos: \"Você não faz idéia do que eles já fizeram!\"\n\n    Brako: \"Só nós? hahaha\"\n\n    Siko: \"Acho que alguem esqueceu o próprio passado!\"\n\n    Graves: \"Como assim Elos?\"\n\n    Elos: \"Esqueça isso, foque na batalha!\"\n\n    Brako: \"Elos foi o maior assassino de aluguel de Daxy\"\n\n    Siko: \"Mas... Do nada decidiu virar o mocinho\"\n\n    Elos: \"Foi um grande erro!\"\n\n    Elos: \"Eu passo todo dia de minha vida pedindo perdão por isso!\"\n\n    Siko: \"Você não é diferente de nós Elos!\"\n\n    Elos: \"Eu matava somente pessoas ruins!\"\n\n    Siko: \"E o que você diz sobre a filha do imperador de Daxy?\"\n\nElos congelou por um momento\n\n    Elos: \"Eu... Eu não fazia idéia que ela era inocente...\"\n\n    Graves: \"Você matou uma inocente?!\"\n\n    Rako: \"Não importa Graves!\"\n\n    Elos: \"Depois disso, comecei a fazer apenas o que é certo!\"\n\n    Brako: \"Mas no fundo você é apenas um assassino!\"\n\n    Siko: \"Ser o herói não anula seu passado sangrento\"\n\n    Elos: \"Não quero ser herói algum!\"\n\n    Elos: \"Quero somente que essa guerra maldita acabe\"\n\n    Elos: \"E quero Arkron morto!\"\n\n    Siko: \"Bom...\"\n\n    Brako: \"Que seja!\"\n\nSiko e Brako vão para cima de Elos mas Rako conjura um protetor ancestral para Elos, que envolve seu corpo com uma aura azul que segura Siko e Brako e os joga longe\n\n    Rako: \"Afaste-se Elos!\"\n\n    Rako: \"Você não está bem para lutar!\"\n\n    Graves: \"Deixa que eu cuido disso!\"\n\nGraves começou a socar Brako até que Brako sacou um punhal e fincou em seu braço\n\n    Graves: \"Ah maldito!\"\n\n    Elos: \"Graves!\"\n\n    Elos: \"Não se mexa, esse punhal drena toda sua energia!\"\n\n    Graves: \"Rako! Dá uma ajuda aqui!\"\n\nRako retirou o punhal usando magia, para não machucar mais Graves\n\n    Rako: \"Agora fique parado Graves\"\n\n    Rako: \"Se você ficar se mexendo, toda sua energia será drenada!\"\n\n    Graves: \"Ok... Agora acaba com a raça deles!\"\n\nViko e Zibo estavam lutando contra Siko\n\n    Siko: \"Hahaha, Elos treinou vocês bem!\"\n\n    Siko: \"Ah, você é o famoso elfo Kawaq!\"\n\n    Zibo: \"Acaba com ele Viko!\"\n\nQuando Viko foi entrar no modo Kawaq, Siko fincou um Punhal de Energia em seu braço\n\n    Siko: \"Não quero um Kawaq nessa luta!\"\n\n    Zibo: \"Rako!\"\n\n    Zibo: \"Viko não conseguiu se transformar!\"\n\n    Rako: \"Tire ele daqui Zibo, e não deixe ele se mexer!\"\n\nRako retirou o protetor ancestral de Elos, e colocou nele mesmo\n\n    Rako: \"Vou tentar drenar a magia de suas lâminas!\"\n\nE os braços do Protetor ancestral envolveram os dois, e a cor do punhalde Siko e Brako ficaram normais, sem o brilho vermelho da magia que drena energia\n\nLuno atirou flechas nos pés deles\n\n    Luno: \"Agora vocês não podem se teletranportar mais!\"\n\n    Rako: \"Muito bom Luno!\"\n\n    Rako: \"{hero.Nome} acabe com eles agora!\"\n\n'
delay(his16)
sleep(4)
batalha(hero, Poções, "Siko", 35, 80, "Punhal de Arkron")
sleep(4)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
batalha(hero, Poções, "Brako", 35, 80, "Punhal de Arkron")
sleep(4)
if hero.Classe == "Espectro":
    hero.Arma = "Punhal de Arkron"
    hero.Dano = 50
    hero.Arkron = True
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


